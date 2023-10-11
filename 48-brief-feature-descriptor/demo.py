import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
import os 


def BRIEF():
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    imgGray = cv.imread(imgPath,cv.IMREAD_GRAYSCALE)

    fast = cv.FastFeatureDetector_create()
    minIntensityDiff = 100 
    brief = cv.xfeatures2d.BriefDescriptorExtractor_create()
    keypoints = fast.detect(imgGray,None)
    keypoints, descriptors = brief.compute(imgGray,keypoints)

    print(brief.descriptorSize())
    print(descriptors[0])
    print(' '.join([format(val,'08b') for val in descriptors[0]]))


if __name__ == '__main__': 
    BRIEF() 