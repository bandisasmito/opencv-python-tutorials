import os 
import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def featureMatachingHomography(): 
    root = os.getcwd()
    img1path = os.path.join(root, 'demoImages//tesla.jpg')
    img2path = os.path.join(root, 'demoImages//tesla2.jpg')
    img1 = cv.imread(img1path, cv.IMREAD_GRAYSCALE)
    img2 = cv.imread(img2path, cv.IMREAD_GRAYSCALE)
    sift = cv.SIFT_create()
    keypoints1, descriptor1 = sift.detectAndCompute(img1, None)
    keypoints2, descriptor2 = sift.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 1
    indexParams = dict(algorithm = FLANN_INDEX_KDTREE, trees=5)
    searchParams = dict(checks = 50)
    flann = cv.FlannBasedMatcher(indexParams, searchParams)
    nNeighbors = 2
    matches = flann.knnMatch(descriptor1,descriptor2,k=nNeighbors)

    goodMatches = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            goodMatches.append(m)

    minGoodMatches = 10 

    if len(goodMatches) > minGoodMatches:
        # reshape(-1,1,2) -> reshapes to (nKeypoints, 1, 2)
        srcPts = np.float32([ keypoints1[m.queryIdx].pt for m in goodMatches ]).reshape(-1,1,2) 
        dstPts = np.float32([ keypoints2[m.trainIdx].pt for m in goodMatches ]).reshape(-1,1,2)
        errorThreshold = 5
        M, mask = cv.findHomography(srcPts,dstPts,cv.RANSAC,errorThreshold)
        matchesMask = mask.ravel().tolist()
        h,w = img1.shape
        imgBorder = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        warpedImgBorder = cv.perspectiveTransform(imgBorder,M)
        img2 = cv.polylines(img2,[np.int32(warpedImgBorder)],True,255,3, cv.LINE_AA)
    else:
        print("Not enough matches")
        matchesMask = None

    green = (0,255,0)
    drawParams = dict(matchColor=green,singlePointColor=None,matchesMask=matchesMask,flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
    img3 = cv.drawMatches(img1,keypoints1,img2,keypoints2,goodMatches,None,**drawParams)
    
    plt.figure() 
    plt.imshow(img3,'gray')
    plt.show()


if __name__ == '__main__': 
    featureMatachingHomography() 