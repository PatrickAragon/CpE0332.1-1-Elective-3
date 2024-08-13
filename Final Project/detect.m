clc; close all; clear;
warning('off','all');

c = webcam;
load myNet1;
faceDetector = vision.CascadeObjectDetector;

% Get the class names from the trained network
classNames = myNet1.Layers(end).Classes;

% Set a confidence threshold
confidenceThreshold = 0.7; % Adjust this value as needed

% Create a log file name
logFileName = 'db.txt';

% Create a map to keep track of logged faces (both from previous sessions and current session)
loggedFaces = containers.Map('KeyType', 'char', 'ValueType', 'logical');

% Initialize all known faces as not logged
for i = 1:length(classNames)
    loggedFaces(char(classNames(i))) = false;
end

% Check the log file for any existing entries for today
currentDate = datestr(now, 'yyyy-mm-dd');
if exist(logFileName, 'file')
    fid = fopen(logFileName, 'r');
    while ~feof(fid)
        line = fgetl(fid);
        if ischar(line)
            for i = 1:length(classNames)
                if contains(line, [currentDate, ' - ', char(classNames(i)), ': Present'])
                    loggedFaces(char(classNames(i))) = true;
                elseif contains(line, [currentDate, ' - ', char(classNames(i)), ': Absent'])
                    loggedFaces(char(classNames(i))) = true;
                end
            end
        end
    end
    fclose(fid);
end

% Create figure for display
fig = figure('Name', 'HariBantay', 'NumberTitle', 'off');

while ishandle(fig)
    e = snapshot(c);
    bboxes = step(faceDetector, e);
    
    if(~isempty(bboxes))
        labels = cell(size(bboxes, 1), 1);
        for i = 1:size(bboxes, 1)
            es = imcrop(e, bboxes(i,:));
            es = imresize(es, [227 227]);
            [label, scores] = classify(myNet1, es);
            
            % Get the highest score and its index
            [maxScore, ~] = max(scores);
            
            % Check if the highest score is above the threshold
            if maxScore >= confidenceThreshold
                recognizedName = char(label);
                labels{i} = recognizedName;
                
                % Log attendance if this face hasn't been logged today (including previous sessions)
                if ~loggedFaces(recognizedName)
                    currentTime = datestr(now, 'HH:MM:SS');
                    logMessage = sprintf('%s %s - %s: Present\n', currentDate, currentTime, recognizedName);
                    
                    % Write to log file
                    fid = fopen(logFileName, 'a');
                    fprintf(fid, logMessage);
                    fclose(fid);
                    
                    % Mark this face as logged
                    loggedFaces(recognizedName) = true;
                    
                    % Display logging message on command window
                    fprintf(logMessage);
                else
                    fprintf('%s has already been marked present today.\n', recognizedName);
                end
            else
                labels{i} = 'Unknown Face';
            end
        end
        % Draw bounding boxes and labels on the image
        e = insertObjectAnnotation(e, 'rectangle', bboxes, labels, 'FontSize', 18);
    end
    
    % Display the image
    imshow(e);
    title('Face Recognition Attendance System', 'FontSize', 16);
    drawnow;
    
    % Check for 'q' key press to quit the program
    if strcmp(get(fig, 'CurrentCharacter'), 'q')
        close(fig);
        break;
    end
end

% Log absent people at the end of the session
absentPeople = keys(loggedFaces);
for i = 1:length(absentPeople)
    if ~loggedFaces(absentPeople{i})
        % Check if "Absent" was already logged for this person
        if ~loggedFaces(absentPeople{i})
            logMessage = sprintf('%s - %s: Absent\n', currentDate, absentPeople{i});
        
            % Write to log file
            fid = fopen(logFileName, 'a');
            fprintf(fid, logMessage);
            fclose(fid);
        
            % Mark this person as logged
            loggedFaces(absentPeople{i}) = true;
            
            % Display logging message on command window
            fprintf(logMessage);
        end
    end
end

% Clean up
clear c;
