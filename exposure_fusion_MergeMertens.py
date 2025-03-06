"""
Created on Mon Nov 14 14:47:32 2022
@author: wael
"""
import os
import cv2  # OpenCV library
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec
import glob
import scipy
from scipy.signal import convolve2d


# # Function to read all images and return them as a list in grayscale
def readImages(path):
    images = []
    for filename in sorted(glob.glob(os.path.join(path, '*.jpg'))):
        im = cv2.imread(filename, cv2.IMREAD_COLOR)
        images.append(im)
    return images

# Function to display images in a subplot
def auto_subplot(imgs, n_row, n_col):
    _, axs = plt.subplots(n_row, n_col)
    axs = axs.flatten()
    for img, ax in zip(imgs, axs):
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert from BGR to RGB for correct color display
    axs[0].set_title('underexposed <--------', fontsize=15)
    ax.set_title('--------> overexposed', fontsize=15)
    plt.show()

# Path to your images (replace this with your own folder path (multi-exposure images))
path = r'C:\Users\Admin\Desktop\test3'
# Read images from the specified folder
images = readImages(path)

# Ensure all images are the same size without resizing
target_size = images[0].shape[:2]  # Get the size of the first image (height and width)
for img in images:
    if img.shape[:2] != target_size:
        print(f"Error: Image {img} is not the same size as the first image.")
        break
else:
    print("All images are the same size.")

# Align images using AlignMTB
alignMTB = cv2.createAlignMTB()  # Create an alignment object
aligned_images_rgb = images.copy()
alignMTB.process(aligned_images_rgb, aligned_images_rgb)
aligned_images = aligned_images_rgb.copy()

# Merge images with the weight settings
mergeMertens = cv2.createMergeMertens()
mergeMertens.setExposureWeight(1)  # Exposure weight
mergeMertens.setContrastWeight(1.7)  # Contrast weight

# Perform the exposure fusion on the aligned images
exposureFusion = mergeMertens.process(aligned_images)

# Sharpen the merged image
kernel = np.array([[-1, -1, 0],
                   [-1, 9, -1],
                   [-1, -1, -0.1]])
sharpened_image = cv2.filter2D(exposureFusion, -1, kernel)

# Adjust brightness and threshold the image
bright_image = cv2.convertScaleAbs(sharpened_image, alpha=1.5, beta=20)
_, thresh_image = cv2.threshold(bright_image, 120, 255, cv2.THRESH_BINARY)

# Display the sharpened and merged image
plt.figure()
plt.imshow(sharpened_image, cmap='gray')
plt.title("Sharpened and Merged Image", fontsize=15)
plt.show()







