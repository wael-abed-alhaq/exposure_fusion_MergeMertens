# exposure_fusion_MergeMertens
# Overview

This project implements an exposure fusion technique using OpenCV's MergeMertens method. The algorithm aligns multiple exposure images, merges them using weighted exposure fusion, and enhances the final output through sharpening and brightness adjustment.

Features

Reads multiple images from a specified folder.

Aligns images using OpenCV's AlignMTB.

Merges images using the MergeMertens exposure fusion technique.

Sharpens the final image using a convolution kernel.

Adjusts brightness and applies a threshold.

Displays the final processed image.

Requirements

Python 3.x

OpenCV (cv2)

NumPy

Matplotlib

SciPy

Installation

To install the required dependencies, run:

pip install opencv-python numpy matplotlib scipy

Usage

Place multi-exposure images in a folder.

Update the path variable in the script to point to the folder.

Run the script:

python exposure_fusion_MergeMertens.py

The merged and enhanced image will be displayed.

Code Explanation

1. Image Reading

The script reads all .jpg images from the specified folder and loads them in color mode.

2. Image Alignment

The AlignMTB method aligns images to compensate for camera movement.

3. Exposure Fusion

The MergeMertens function blends images to enhance details and dynamic range.

4. Sharpening

A sharpening kernel is applied to enhance details in the final image.

5. Brightness Adjustment and Thresholding

Brightness is increased using convertScaleAbs, and thresholding is applied to highlight features.

Example

path = r'C:\Users\Admin\Desktop\test3'
images = readImages(path)

Output

The final processed image is displayed with improved details and contrast.

Author

Wael

License

This project is licensed under the MIT License.

