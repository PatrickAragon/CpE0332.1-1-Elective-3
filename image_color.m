# Octave 7.1.0, Sat Jul 27 12:05:46 2024 GMT <unknown@Laurence-Morales-16>
f = imread('C:\Users\PATRICK LAURENCE\Downloads\orange.png');
figure
imshow(f)

size(f);

imwrite(f,'C:\Users\PATRICK LAURENCE\Downloads\orange.jpg');
figure
imshow(f)

g = rgb2gray(f);
size(f)
figure
imshow(g)
whos f
whos g

imfinfo('C:\Users\PATRICK LAURENCE\Downloads\orange.jpg')
img_red = f;
img_red(:,:,2)=0;
img_red(:,:,3)=0;
figure(1):imshow(img_red);

f = imread('C:\Users\PATRICK LAURENCE\Downloads\orange.png');
img_green = f;
img_green(:,:,1) = 0;
img_green(:,:,3) = 0;
figure(2);imshow(img_green);

f = imread('C:\Users\PATRICK LAURENCE\Downloads\orange.png');
img_blue = f;
img_blue(:,:,1) = 0;
img_blue(:,:,2) = 0;
figure(3);imshow(img_blue);

figure(4);imshow(g);

imwrite(img_red,'C:\Users\PATRICK LAURENCE\Downloads\img_red.png');
imwrite(img_green,'C:\Users\PATRICK LAURENCE\Downloads\img_green.png');
imwrite(img_blue,'C:\Users\PATRICK LAURENCE\Downloads\img_blue.png');
imwrite(g,'C:\Users\PATRICK LAURENCE\Downloads\gray.png');
