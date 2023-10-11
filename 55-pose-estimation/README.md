#### projectPoints
`cv.projectPoints(objectPoints,rvec,tvec,cameraMatrix,distCoeffs) -> imagePoints,jacobian` - projects world points to image points 

Inputs: 
- `objectPoints`: _nx3 numpy array_, points in 3d 
- `rvecs`: _3x1 numpy array_, rotation vector 
- `tvecs`: _3x1 numpy array_, translation vector 
- `cameraMatrix`: _3x3 numpy array_, camera matrix   
- `distCoeffs`: _1x5 numpy array_, distortion coefficients   

Outputs: 
- `imagePoints`: _mxn numpy array_, image points
- `jacobian`: _3x1x2 numpy array_, jacobian matrix 

#### solvePnP
`cv.solvePnP(objectPoints,imagePoints,cameraMatrix,distCoeffs) -> retval,rvec,tvec` - finds the rotation and translation vectors that minimizes reprojection error

Inputs:
- `objectPoints`: _nx3 numpy array_, points in 3d 
- `imagePoints`: _mxn numpy array_, image points
- `cameraMatrix`: _3x3 numpy array_, camera matrix  
- `distCoeffs`: _1x5 numpy array_, distortion coefficients
- `useExtrinsicGuess`: _bool_, false by default 
- `flags`: _enum_, solver options
    - `cv.SOLVEPNP_AP3P`
    - `cv.SOLVEPNP_DLS`
    - `cv.SOLVEPNP_EPNP`
    - `cv.SOLVEPNP_IPPE`
    - `cv.SOLVEPNP_IPPE_SQUARE`
    - `cv.SOLVEPNP_ITERATIVE` (DEFAULT)
    - `cv.SOLVEPNP_MAX_COUNT`
    - `cv.SOLVEPNP_P3P`
    - `cv.SOLVEPNP_SQPNP`
    - `cv.SOLVEPNP_UPNP`
    
Outputs:
- `retval`: _bool_, true if successful, false otherwise
- `rvecs`: _3x1 numpy array_, rotation vector 
- `tvecs`: _3x1 numpy array_, translation vector 

#### Reference
https://docs.opencv.org/3.4/d9/d0c/group__calib3d.html#ga549c2075fac14829ff4a58bc931c033d

#### Markdown Shortcut
Generate Preview: `ctrl+k, v`