import cv2 as cv 
import os 
import matplotlib.pyplot as plt 
import numpy as np 

def drawingFunctions(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show() 

    '''
        cv.line(img,start,end,color,lineThickness)
        cv.rectangle(img,start,end,color,lineThickness)
            @param img Ndarray - mxnx3, or just one channel 
            @param start Tuple, (x,y) pixel location
            @param end Tuple, (x,y) pixel location
            @param color Tuple, (b,g,r) 
            @param lineThickness Int, line thickness 
    '''
    cv.line(img,(366,402),(197,507),(255,255,255),2)

    r,c,d = img.shape
    offset = 10
    cv.rectangle(img,(offset,offset),(c-offset,r-offset),(255,255,255),4)

    '''
        cv.circle(img,start,end,color,lineThickness)
            @param img Ndarray - mxnx3, or just one channel 
            @param start Tuple, (x,y) pixel location
            @param radius Int 
            @param color Tuple, (b,g,r) 
            @param Int, line thickness  
                positive mean outline 
                negative means filled 

    '''
    cv.circle(img,(496,325), 10, (255,255,255), -1)

    '''
        cv.ellipse(img,start,axes,angle,startAngle,endAngle,color,lineThickness)
            @param img Ndarray - mxnx3, or just one channel 
            @param start Tuple (x,y) pixel location
            @param axes Tuple (major,minor)
            @param angle Float angle of rotation of ellipse in deg 
            @param startAngle Float starting angle of ellipse in deg 
            @param endAngle Float ending angle of ellipse in deg 
            @param color Tuple (b,g,r) 
            @param lineThickness Int, line thickness 
                    positive mean outline 
                    negative means filled 
    '''
    cv.ellipse(img,(415,439),(30,20),0,0,180,(255,255,255),-1)


    pts = np.array([[234,211],
                    [214,71],
                    [322,125]])
    '''
        cv.polylines(img,pts,isClosed,color,lineThickness)
            @param img Ndarray mxnx3, or just one channel 
            @param pts List of np.array nx2 pixel locations
            @param isClosed Bool if contour is closed or not 
            @param color Tuple (b,g,r) 
            @param lineThickness Int, line thickness 
                    positive mean outline 
                    negative means filled 
    '''
    cv.polylines(img,[pts],True,(255,255,255),3)


    '''
        cv.putTest(img,text,org,fontFace,fontScale,color,thickness,lineType)
            @param img Ndarry mxnx3
            @param text Str text content 
            @param org Tuple (x,y) location of text from bottom 
            @param fontFace CV.enumeration font type 
            @param fontScale Int font scale factor 
            @param color Tuple (b,g,r) 
            @param thickness Int line thickness 
            @lineType CV.enumeration type of line 
    '''
    cv.putText(img,'TIGER',(650,278), cv.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),4,cv.LINE_AA)

    cv.imshow("img",img)
    cv.waitKey(0)

if __name__ == '__main__': 
    drawingFunctions() 