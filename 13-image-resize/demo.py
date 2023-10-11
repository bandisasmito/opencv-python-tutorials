import cv2 as cv 
import os 
import matplotlib.pyplot as plt 

def imageResize(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    img = img[286:345,322:389,:]
    height,width,_ = img.shape
    
    scale = 1/4

    interpMethods = [
        cv.INTER_AREA,
        cv.INTER_LINEAR, 
        cv.INTER_NEAREST,
        cv.INTER_CUBIC,
        cv.INTER_LANCZOS4
    ]

    interpTitle = ['area','linear','nearest','cubic','lanczos']

    plt.figure() 
    plt.subplot(2,3,1)
    plt.imshow(img)

    for i in range(len(interpMethods)): 
        plt.subplot(2,3,i+2)
        imgResize = cv.resize(img,(int(width*scale),int(height*scale)),interpolation=interpMethods[i])
        plt.imshow(imgResize)
        plt.title(interpTitle[i])
    plt.show() 


if __name__ == '__main__': 
    imageResize() 