clc
clear all
close all
warning off

% Ensure the Deep Learning Toolbox Model for AlexNet Network is installed
if ~exist('alexnet', 'file')
    error('AlexNet support package is not installed. Please install it from the Add-Ons menu.');
end

g = alexnet;
layers = g.Layers;
layers(23) = fullyConnectedLayer(4);
layers(25) = classificationLayer;
allImages = imageDatastore('datastorage', 'IncludeSubfolders', true, 'LabelSource', 'foldernames');
opts = trainingOptions('sgdm', 'InitialLearnRate', 0.001, 'MaxEpochs', 20, 'MiniBatchSize', 64);
myNet1 = trainNetwork(allImages, layers, opts);
save myNet1;
