import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
import os 

def fourierTransform(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    img = cv.imread(imgPath,cv.IMREAD_GRAYSCALE)

    plt.figure() 
    plt.subplot(231)
    plt.imshow(img,cmap='gray')

    imgDFT = cv.dft(np.float32(img),flags=cv.DFT_COMPLEX_OUTPUT)
    imgDFT_DB = 20*np.log(cv.magnitude(imgDFT[:,:,0],imgDFT[:,:,1]))
    plt.subplot(232)
    plt.imshow(imgDFT_DB,cmap='gray')

    imgDFTshift = np.fft.fftshift(imgDFT)
    imgDFTshift_DB = 20*np.log(cv.magnitude(imgDFTshift[:,:,0],imgDFTshift[:,:,1]))
    plt.subplot(233)
    plt.imshow(imgDFTshift_DB,cmap='gray')

    r,c = img.shape
    mask = np.zeros((r,c,2),np.uint8)
    offset = 50 
    mask[int(r/2)-offset:int(r/2)+offset,int(c/2)-offset:int(c/2)+offset] = 1 
    plt.subplot(234)
    plt.imshow(mask[:,:,0])

    imgDFTshift_LP = imgDFTshift*mask 
    imgDFshift_LP_DB = 20*np.log(cv.magnitude(imgDFTshift_LP[:,:,0],imgDFTshift_LP[:,:,1]))
    plt.subplot(235)
    plt.imshow(imgDFshift_LP_DB,cmap='gray')

    imgInvDFT_LP = np.fft.ifftshift(imgDFTshift_LP)
    imgDFT_LP = cv.idft(imgInvDFT_LP)
    img_LP = cv.magnitude(imgDFT_LP[:,:,0],imgDFT_LP[:,:,1])
    plt.subplot(236)
    plt.imshow(img_LP,cmap='gray')

    coef = cv.getGaussianKernel(7,5)
    gaussianKernel = coef@coef.T 
    laplacianKernel = np.array([[0,1,0],
                                [1,-4,1],
                                [0,1,0]])
    
    plt.figure() 
    plt.subplot(121)
    gausFFT = np.fft.fft2(gaussianKernel)
    gausFFTshift = np.fft.fftshift(gausFFT)
    gausMag = np.log(np.abs(gausFFTshift)+1)
    plt.imshow(gausMag,cmap='gray')
    plt.subplot(122)
    lapFFT = np.fft.fft2(laplacianKernel)
    lapFFTshift = np.fft.fftshift(lapFFT)
    lapMag = np.log(np.abs(lapFFTshift)+1)
    plt.imshow(lapMag,cmap='gray')
    plt.show() 


if __name__ == '__main__': 
    fourierTransform() 