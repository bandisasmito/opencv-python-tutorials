import cv2 as cv 
import os 
import matplotlib.pyplot as plt 
import numpy as np 

def drawingFunctions(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    # plt.figure()
    # plt.imshow(imgRGB)
    # plt.show() 

    white = (255,255,255)
    cv.line(img,(366,402),(197,507),white,2)

    r,c,d = img.shape
    offset = 10 
    cv.rectangle(img,(offset,offset),(c-offset,r-offset),white,8)

    cv.circle(img,(496,325),10,white,-1)

    cv.ellipse(img,(415,439),(30,20),0,0,180,white,-1)

    pts = np.array([[234,211],
                    [214,71],
                    [322,125]])
    
    cv.polylines(img,[pts],True,white,3)

    cv.putText(img,'TIGER',(650,278),cv.FONT_HERSHEY_SIMPLEX,4,white,4,cv.LINE_AA)

    cv.imshow('img',img)
    cv.waitKey(0)

if __name__ == '__main__': 
    drawingFunctions() 