import cv2 as cv 
import os 

windowName = 'trackbar'
'''
    cv.createTrackbar(trackbarName, winName, initValue, maxValue, callbackFunc)
        @param trackbarName Str name of trackbar 
        @param windowName Str name of window 
        @param initValue Int initial value of trackbar 
        @param maxVaue Int max value of trackbar 
        @param callbackFunc Func function called when trackbar updates 
'''

def trackbarCallback(input): 
    pass 

def trackbarDemo(): 
    windowName = 'trackbar demo'
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    cv.namedWindow(windowName)
    cv.createTrackbar('B',windowName,0,255,trackbarCallback)
    cv.createTrackbar('G',windowName,0,255,trackbarCallback)
    cv.createTrackbar('R',windowName,0,255,trackbarCallback)
    
    while True: 
        cv.imshow(windowName,img)

        if cv.waitKey(1) == ord('q'):
            break

        b = cv.getTrackbarPos('B',windowName)
        g = cv.getTrackbarPos('G',windowName)
        r = cv.getTrackbarPos('R',windowName)

        cv.circle(img,(496,325), 10, (b,g,r), -1)
        cv.circle(img,(353,315), 10, (b,g,r), -1)

    cv.destroyAllWindows() 

if __name__ == '__main__': 
    trackbarDemo() 


