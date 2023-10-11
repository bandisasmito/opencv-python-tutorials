### Contents 
- [findChessboardCorners](#findchessboardcorners)
- [cornerSubPix](#cornersubpix)
- [calibrateCamera](#calibratecamera)
- [drawChessboardCorners](#drawchessboardcorners)
- [getOptimalNewCameraMatrix](#getoptimalnewcameramatrix)
- [undistort](#undistort)

#### findChessboardCorners
`cv.findChessboardCorners(image,patternSize,flags) -> retval,corners` - finds the corners on a chessboard pattern

Input: 
- `image`: _mxnx3 numpy array_, previous image 
- `patternSize`: _2-tuple of ints_, (nRows,nCols)
- `flags`: _int_, None, 1, or sum of 2 or more  
    - `CALIB_CB_ADAPTIVE_THRESHOLD` - apply adaptive thresholding 
    - `CALIB_CB_NORMALIZE_IMAGE` - equalize histogram before adaptive thresholding 
    - `CALIB_CB_FILTER_QUADS` - filter out bad quads 
    - `CALIB_CB_FAST_CHECK` - quick check to see if there are chessboard corners

Output: 
- `retval`: _bool_, true if corners found, false otherwise
- `corners`: _nx1x2 numpy array_, (x,y) coordinates of the corners 


Important: 
1. Make sure to count the number of corners correctly or will return false! 
2. Need at least 10 images for good results. 
3. Images should be taken in different planes to avoid degenerate case (can't be all in the same plane). 
4. Entire chessboard should be inside the image. 

#### cornerSubPix
`cv.cornerSubPix(image,corners,winSize,zeroZone,criteria) -> corners` - finds a more accurate location of the corners 

Input: 
- `image`: _mxnx2 numpy array_, previous grayscale image 
- `corners`: _nx1x2 numpy array_, (x,y) coordinates of the original corners 
- `winSize`: _2-tuple_, search window size
- `zeroZone`: _2-tuple_, region in the search area that's not used to avoid singularities; (-1,-1) means none
- `criteria`: _3-tuple_, iteration termination criteria
  - `type`：_enum_, stopping method 
    - `cv.TERM_CRITERIA_EPS`: stop if min error reached 
    - `cv.TERM_CRITERIA_COUNT`: stop if max iter reached 
  - `max_iter`：_int_, max iterations
  - `eps`：_float_, min error 

Output:
- `corners`: _nx1x2 numpy array_, (x,y) coordinates of the modified corners 

#### calibrateCamera
`cv.calibrateCamera(objectPoints,imagePoints,imageSize,cameraMatrix,distCoeffs) -> retval,cameraMatrix,distCoeffs,rvecs,tvecs` - finds the camera instrinsics and extrinsics 

Define: 
- `nPics` - number of pics with corners found  

Input: 
- `objectPoints`: _nPics-list of nx3 numpy array_, points in 3d (0,0,0), (1,0,0), (2,0,0) ....,(nRows,nCols,0)   
- `imagePoints`: _nPics-list of nx1x2 numpy array_, points in 2d on the image 
- `imageSize`: _2-tuple of ints_, (width,height) of image 
- `cameraMatrix`: Input not used, None
- `distCoeffs`: Input not used, None  

Output: 
- `repError`: _float_, overal RMS reprojection error   
- `cameraMatrix`: _3x3 numpy array_, camera matrix   
- `distCoeffs`: _1x5 numpy array_, distortion coefficients   
- `rvecs`: _nPics-tuple of 3x1 numpy array_, rotation vector for each picture  
- `tvecs`: _nPics-tuple of 3x1 numpy array_, translation vector for each picture 

#### drawChessboardCorners
`cv.drawChessboardCorners(image,patternSize,corners,patternWasFound) -> image` - draws chessboard corners 

Input: 
- `image`: _mxnx3 numpy array_, chessboard image 
- `patternSize`: _2-tuple of ints_, (nRows,nCols)
- `corners`: _nx1x2 numpy array_, (x,y) coordinates of the corners
- `patternWasFound`: _bool_, true if corners found, false otherwise (return value from cv.findChessboardCorners)

Output: 
- `image`: _mxnx3 numpy array_, chessboard image (not used if modifying original image) 

#### getOptimalNewCameraMatrix
`cv.getOptimalNewCameraMatrix(cameraMatrix,distCoeffs,imageSize,alpha,newImgSize) -> newCamMatrix,validPixROI` - compute new camera matrix to account for distortion 

Input: 
- `cameraMatrix`: _3x3 numpy array_, camera matrix 
- `distCoeffs`: _1x5 numpy array_, distortion coefficients   
- `imageSize`: _2-tuple of ints_, (width,height)
- `alpha`: _float_, scaling factor between 0 and 1 
  - `alpha=0`: rectified image zoomed and shifted so only valid pixels are visible
  - `alpha=1`: all the pixels from the original image are retained in the rectified images 
- `newImgSize`: _2-tuple of ints_, (width,height)

Output: 
- `newCamMatrix`:  _3x3 numpy array_, camera matrix  
- `validPixROI`: _4-tuple of ints_, (x, y, width, height)

#### undistort
`cv.undistort(src,cameraMatrix,distCoeffs,dst,newCameraMatrix) -> dst` - removes distortion from an image 

Input: 
- `src`: _mxnx3 numpy array_, input image 
- `cameraMatrix`: _3x3 numpy array_, camera matrix   
- `distCoeffs`: _1x5 numpy array_, distortion coefficients   
- `dst`:  Input not used, None

Output: 
- `dst`:  _mxnx3 numpy array_, undistorted image


#### Reference
https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html#ga93efa9b0aa890de240ca32b11253dd4a


#### Markdown Shortcut
Generate Preview: `ctrl+k, v`