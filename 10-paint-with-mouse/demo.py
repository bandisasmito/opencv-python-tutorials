import cv2 as cv 
import os 

def drawCircle(event,x,y,flags,param): 
    img = param 
    if event == cv.EVENT_LBUTTONDBLCLK: 
        cv.circle(img,(x,y),10,(0,0,255),-1)

def doubleClickDrawing(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    
    windowName = 'drawing app'
    cv.namedWindow(windowName)
    cv.setMouseCallback(windowName,drawCircle,img)

    while True: 
        cv.imshow(windowName,img)
        if cv.waitKey(1) == ord('q'):
            break

class DrawingApp: 
    def __init__(self,imagePath): 
        self.imagePath = imagePath 
        self.startX, self.startY = 0, 0 
        self.isDrawing = False 

    def drawLine(self,event,x,y,flags,param): 
        img = param 
        if event == cv.EVENT_LBUTTONDOWN: 
            self.isDrawing = True
            self.startX, self.startY = x,y 
        elif event == cv.EVENT_MOUSEMOVE and self.isDrawing:
            cv.line(img,(self.startX,self.startY),(x,y),(255,255,255),3)
        elif event == cv.EVENT_LBUTTONUP: 
            self.isDrawing = False
            cv.line(img,(self.startX,self.startY),(x,y),(255,255,255),3)

    def run(self): 
        img = cv.imread(self.imagePath)
        
        windowName = 'drawing app'
        cv.namedWindow(windowName)
        cv.setMouseCallback(windowName,self.drawLine,img)

        while True: 
            cv.imshow(windowName,img)
            if cv.waitKey(1) == ord('q'):
                break

def holdAndDragDrawing(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    app = DrawingApp(imgPath)
    app.run() 

if __name__ == '__main__': 
    # doubleClickDrawing() 
    holdAndDragDrawing()
