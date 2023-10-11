import cv2 as cv 
import os 
import matplotlib.pyplot as plt 
import numpy as np 

def pureColors(): 
    '''
        pure colors, rgb, white, black 
    '''
    # Set green and blue channels to zero
    zeros = np.zeros((100,100))
    ones = np.ones((100,100))
    bImg = cv.merge((255*ones, zeros, zeros))
    gImg = cv.merge((zeros, 255*ones, zeros))
    rImg = cv.merge((zeros, zeros, 255*ones))
    blackImg = cv.merge((zeros, zeros, zeros))
    whiteImg = cv.merge((255*ones,255*ones,255*ones))

    plt.figure(figsize=(10, 6))
    plt.subplot(231)
    plt.imshow(bImg)
    plt.title('blue')
    plt.subplot(232)
    plt.imshow(gImg)
    plt.title('green')
    plt.subplot(233)
    plt.imshow(rImg)
    plt.title('red')
    plt.subplot(234)
    plt.imshow(blackImg)
    plt.title('black')
    plt.subplot(235)
    plt.imshow(whiteImg)
    plt.title('white')
    plt.tight_layout()
    plt.show() 

def bgrChannelGrayScale(): 
    '''
        Plotting individual channels will just show the 
        relative intensities in Gray scale 
    '''
    root = os.getcwd()

    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    b, g, r = cv.split(img)

    plt.figure(figsize=(10, 6))
    plt.subplot(131)
    plt.imshow(b, cmap='gray')
    plt.title('Blue Channel')
    plt.subplot(132)
    plt.imshow(g, cmap='gray')
    plt.title('Green Channel')
    plt.subplot(133)
    plt.imshow(r, cmap='gray')
    plt.title('Red Channel')
    plt.tight_layout()
    plt.show()

def bgrChannelColor(): 
    '''
        To see the actual colors, need to zero out the other 
        channels and only show the corresponding bgr channel 
    '''
    root = os.getcwd()

    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    b, g, r = cv.split(img)

    # Set green and blue channels to zero
    zeros = np.zeros_like(b)
    bImg = cv.merge((b, zeros, zeros))
    gImg = cv.merge((zeros, g, zeros))
    rImg = cv.merge((zeros, zeros, r))

    plt.figure(figsize=(10, 6))
    plt.subplot(131)
    plt.imshow(bImg)
    plt.title('Blue Img')
    plt.subplot(132)
    plt.imshow(gImg)
    plt.title('Green Img')
    plt.subplot(133)
    plt.imshow(rImg)
    plt.title('Red Img')
    plt.tight_layout()
    plt.show() 


if __name__ == '__main__': 
    pureColors() 
    bgrChannelGrayScale()
    bgrChannelColor() 
