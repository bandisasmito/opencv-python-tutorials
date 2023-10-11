import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
import os 

# use pyenv36 created in SURF ex 

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

    # print in bytes - 32 bytes
    print(descriptors[0])

    # print in bits (1 byte = 8 bits)
    # 32 x 8 = 256 bits 
    # so 256 pairs 
    print(' '.join([format(val, '08b') for val in descriptors[0]]))

if __name__ == '__main__': 
    BRIEF()