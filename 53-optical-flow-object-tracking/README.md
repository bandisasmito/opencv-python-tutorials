#### calcOpticalFlowPyrLK
`cv.calcOpticalFlowPyrLK(prevImg,nextImg,prevPts,nextPts,winSize,maxLevel,criteria) -> nextPts,status,err` - calculates optical flow for a sparse feature set using Lucas-Kanade with pyramids

Input: 
- `prevImg`: _mxnx3 numpy array_, prev image 
- `nextImg`: _mxnx3 numpy array_, next image
- `prevPts`: _mx1x2 numpy array_, previous feature points
- `nextPts`: _mx1x2 numpy array_, input/output, can set as None
- `winSize`: _2x1 tuple of ints_, window dimension for search window
- `criteria`: _3x1 tuple_, iteration termination criteria
  - `type`：_enum_, stopping method 
    - `cv.TERM_CRITERIA_EPS`: stop if min error reached 
    - `cv.TERM_CRITERIA_COUNT`: stop if max iter reached 
  - `max_iter`：_int_, max iterations
  - `eps`：_float_, min error 

Output: 
- `nextPts`: _mx1x2 numpy array_, current feature points 
- `status`: _nx1 numpy array_, 1 if feature match found between two images, 0 otherwise
- `err`: _nx1 numpy array_, error array 

#### calcOpticalFlowFarneback
`cvcalcOpticalFlowFarneback(prev,next,flow,pyr_scale, levels,winsize,iterations,poly_n,poly_sigma,flags) -> flow` - computes a dense optical flow using the Gunnar Farneback's algorithm

Inputs: 
- `prev`: _mxnx3 numpy array_, previous image 
- `next`: _mxnx3 numpy array_, current image 
- `flow`: _mxnx3 numpy array_, input/output, can set as None
- `pyr_scale`: _float_, how much the image size is reduced at each image pyramid level
- `levels`: _int_, the number of pyramid levels including the initial image
- `winsize`: _int_, the averaging window size; larger values result in more blurring
- `iterations`: _int_, the number of iterations at each pyramid level
- `poly_n`: _int_, the size of the pixel neighborhood (typically 5 or 7)
- `poly_sigma`: _float_, standard deviation for Gaussian smoothing 
  - poly_n=5 with poly_sigma=1.1 
  - poly_n=7 with poly_sigma=1.5
- `flags`:
  - `cv.OPTFLOW_USE_INITIAL_FLOW`: use input as initial flow approximation
  - `cv.OPTFLOW_FARNEBACK_GAUSSIAN`: use a Gaussian window instead of a box filter of the same size for optical flow estimation

Output: 
- `flow`: _mxnx3 numpy array_, flow image 

#### Reference
https://docs.opencv.org/3.4/dc/d6b/group__video__track.html#ga473e4b886d0bcc6b65831eb88ed93323


#### Markdown Shortcut
Generate Preview: `ctrl+k, v`