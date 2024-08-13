import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("C:/Users/Allen/Downloads/orange.png")

# Rotate by 30 degrees
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 30, 1.0)
rotated_img = cv2.warpAffine(img, M, (w, h))

# Flip horizontally
flipped_img = cv2.flip(rotated_img, 1)

# Convert BGR to RGB for displaying using matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rotated_img_rgb = cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB)
flipped_img_rgb = cv2.cvtColor(flipped_img, cv2.COLOR_BGR2RGB)

# Display results
plt.figure(1)
plt.imshow(img_rgb)
plt.title('Original Image')

plt.figure(2)
plt.imshow(rotated_img_rgb)
plt.title('Rotated 30°')

plt.figure(3)
plt.imshow(flipped_img_rgb)
plt.title('Rotated & Flipped')

plt.show()
