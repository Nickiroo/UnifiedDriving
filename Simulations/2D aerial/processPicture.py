""" 
    I'm going to importing an image that is a 2d image of a road from above.
    I'm going to use this image and separate it into its different parts based on the color.

    Image Dimensions: 2000 x 2000
    Color guide(RGB):
        - 255, 255, 255: Road
        - 0, 0, 0: Lane Markings
        - 255, 0, 0: Starting Point
        - 0, 0, 255: Ending Point
        - 0, 255, 0: Other Cars
        - 0, 255, 255: Miscellaneous Obstacles
    
    I'm going to be using the following libraries:
        - OpenCV
        - Numpy
        - Matplotlib
        - Pandas
"""
    
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

def importPicture(path):
    return cv2.imread(path)

#function that separates the picture into its different parts based on color
def separatePicture(picture):
    pic = importPicture("Assets\Photoshop\Test-Road.png")
    
    for i in range(0, 2000):


#Debug Functions
def showPicture(picture):
    cv2.imshow("Picture", picture)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def getPictureDimensions(picture):
    return picture.shape
def getPictureSize(picture):
    return picture.size
def getPictureType(picture):
    return picture.dtype
