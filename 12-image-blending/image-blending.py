import cv2 as cv 
import os 

def callback(input): 
    pass 

def imageBlending():
    root = os.getcwd()
    img1Path = os.path.join(root,'demoImages\\cutepic1.jpg')
    img1 = cv.imread(img1Path)
    height,width,_ = img1.shape

    img2Path = os.path.join(root,'demoImages\\joshuaTree.png')
    img2 = cv.imread(img2Path)

    x0 = 400
    y0 = 0
    
    # make img2 same size as img1 
    img2 = img2[y0:y0+height,x0:x0+width]

    windowName = 'image blending'
    cv.namedWindow(windowName)

    '''
        alpha is between 0 and 1 
        BUT trackbar can't do 0-1 so we do 0-100
        and divide by 100 later to get 0 to 1! 
    '''
    scale = 100
    cv.createTrackbar('alpha',windowName,0,1*scale,callback)
    cv.createTrackbar('gamma',windowName,0,255,callback)

    while True: 
        '''
            cv.addWeighted(img1,alpha,img2,beta,gamma)
                @param img1 Ndarray
                @param alpha Float 
                @param img2 Ndarray 
                @param beta Float
                @param gamma Float 

                Blend image based on the equation 
                    dst=α⋅img1+β⋅img2+γ

                    beta = 1-alpha 

        '''
        if cv.waitKey(1) == ord('q'): 
            break 

        alpha = cv.getTrackbarPos('alpha',windowName)/scale
        beta = 1-alpha
        gamma = cv.getTrackbarPos('gamma',windowName)

        imgBlend = cv.addWeighted(img1,alpha,img2,beta,gamma)

        cv.imshow(windowName,imgBlend)
        
    
    cv.destroyAllWindows()

if __name__ == '__main__': 
    imageBlending()