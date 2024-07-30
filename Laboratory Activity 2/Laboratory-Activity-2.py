import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image
img = cv2.imread("C:/Users/Elitebook 840 G7/Documents/3rd Year - 3rd Sem/Elective (Laboratory)/orange.png")

# Display the image
plt.figure(1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

# Get image dimensions (rows, columns, color channels)
rows, cols, channels = img.shape
print(f'Image size: {rows} x {cols} x {channels}')

# Check color model (grayscale or RGB)
if channels == 1:
    print('Color Model: Grayscale')
else:
    print('Color Model: RGB')

# Access individual pixels (example: center pixel)
center_row = rows // 2
center_col = cols // 2
center_pixel = img[center_row, center_col]
print(f'Center pixel value: {center_pixel}')

# Basic arithmetic operations (add constant value to all pixels)
brightened_img = cv2.add(img, 50)
plt.figure(2)
plt.imshow(cv2.cvtColor(brightened_img, cv2.COLOR_BGR2RGB))
plt.title('Image Brightened')

# Basic geometric operation (flipping image horizontally)
flipped_img = cv2.flip(img, 1)
plt.figure(3)
plt.imshow(cv2.cvtColor(flipped_img, cv2.COLOR_BGR2RGB))
plt.title('Image Flipped Horizontally')

plt.show()
