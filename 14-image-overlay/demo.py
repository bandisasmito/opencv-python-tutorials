import cv2 as cv 
import os 
import matplotlib.pyplot as plt 

def imageOverlay(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    teslaLogoPath = os.path.join(root,'demoImages\\teslaLogo.png')
    teslaLogo = cv.imread(teslaLogoPath)
    height,width,_ = teslaLogo.shape
    scale = 1/4
    height = int(height*scale)
    width = int(width*scale)
    teslaLogo = cv.resize(teslaLogo,(width,height),interpolation=cv.INTER_LINEAR)
    teslaMask = teslaLogo[:,:,0]

    plt.figure()
    plt.subplot(231)
    plt.imshow(teslaMask,cmap='gray')
    
    plt.subplot(232)
    plt.imshow(img)

    imgRegion = img[156:156+height,376:376+width]
    plt.subplot(233)
    plt.imshow(imgRegion)

    teslaMaskInv = cv.bitwise_not(teslaMask)
    imgRegionBlack = cv.bitwise_and(imgRegion,imgRegion,mask=teslaMaskInv)
    plt.subplot(234)
    plt.imshow(imgRegionBlack)

    imgRegionLogo = cv.add(imgRegionBlack,teslaLogo)
    plt.subplot(235)
    plt.imshow(imgRegionLogo)

    img[156:156+height,376:376+width] = imgRegionLogo
    plt.subplot(236)
    plt.imshow(img)

    plt.show() 


if __name__ == '__main__': 
    imageOverlay() 