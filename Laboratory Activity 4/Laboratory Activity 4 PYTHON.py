# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:44:55 2024

@author: daryll banal, joseph nathaniel alambra, patrick lawrence aragon, david bryan sentasas, allen christopher tutanes
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('flower.jpg')  # Replace with the path to your image file

# Display the original image
cv2.imshow('Original Image', img)

# Convert to grayscale if the image is RGB
if img.shape[2] == 3:
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
else:
    img_gray = img

cv2.imshow('Grayscale Image', img_gray)

# Edge detection using Canny
edges_canny = cv2.Canny(img_gray, 100, 200)
cv2.imshow('Canny Edge Detection', edges_canny)

# Edge detection using Sobel
sobelx = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=5)  # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=5)  # Sobel Edge Detection on the Y axis
sobel_combined = cv2.sqrt(sobelx**2 + sobely**2)  # Combine X and Y axis
cv2.imshow('Sobel Edge Detection', sobel_combined)

# Motion blur
len = 21
theta = 11
psf = cv2.getGaussianKernel(len, sigma=0) @ cv2.getGaussianKernel(len, sigma=0).T  # Approximating fspecial('motion', len, theta)
img_blur = cv2.filter2D(img_gray, -1, psf)
cv2.imshow('Motion Blurred Image', img_blur)

# Gaussian filtering
img_gaussian_filtered = cv2.GaussianBlur(img_blur, (5, 5), 1)
cv2.imshow('Filtered Image (Gaussian)', img_gaussian_filtered)

# Sharpening using unsharp masking
img_sharpened = cv2.addWeighted(img_blur, 1.5, img_gaussian_filtered, -0.5, 0)
cv2.imshow('Sharpened Image', img_sharpened)

# Add Gaussian noise and remove it using median filter
img_noisy = cv2.randn(np.zeros_like(img_gray), 128, 20)  # Gaussian noise, mean 128, stddev 20
img_noisy_removed = cv2.medianBlur(img_noisy.astype(np.uint8), 5)
cv2.imshow('Noisy', img_noisy)
cv2.imshow('Noise Removed', img_noisy_removed)

# Deblurring
estimated_nsr = 0.01
img_deblurred = cv2.filter2D(img_blur, -1, psf / estimated_nsr)
cv2.imshow('Deblurred Image', img_deblurred)

# Experiment with different Gaussian filtering values
img_gaussian_filtered_exp = cv2.GaussianBlur(img_gray, (5, 5), 10)
cv2.imshow('Filtered Image with Experimented Value (Gaussian)', img_gaussian_filtered_exp)

# Experiment with different noise levels
img_noisy_exp1 = cv2.randn(np.zeros_like(img_gray), 128, 50)
img_noisy_exp2 = cv2.randn(np.zeros_like(img_gray), 128, 10)
cv2.imshow('Noisy Using Experimented Value (Gaussian is 0.5)', img_noisy_exp1)
cv2.imshow('Noisy Using Experimented Value (Gaussian is 0.1)', img_noisy_exp2)

# Display histograms
def plot_histogram(image, title):
    plt.figure()
    plt.title(title)
    plt.hist(image.ravel(), bins=256, color='black', histtype='step')
    plt.show()

plot_histogram(img_gray, 'Histogram of Grayscale')
plot_histogram(img_gaussian_filtered, 'Histogram of Gaussian Filtered Image')
plot_histogram(img_noisy_exp1, 'Histogram of Noisy Image Experimented Value 1')
plot_histogram(img_noisy_exp2, 'Histogram of Noisy Image Experimented Value 2')

cv2.waitKey(0)
cv2.destroyAllWindows()