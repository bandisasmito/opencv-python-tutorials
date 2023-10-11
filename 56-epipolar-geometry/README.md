#### findFundamentalMat
`cv.findFundamentalMat(points1, points2, method=cv.FM_RANSAC, ransacReprojThreshold=3.0, confidence=0.99, maxIters=2000) -> F, mask` - calculates the fundamental matrix from the corresponding points in two images

Inputs:
- `points1`: _nx1x2 numpy array_, points from the first image
- `points2`: _nx1x2 numpy array_, corresponding points from the second image
- `method`: _int_, method to compute the fundamental matrix
    - `cv.FM_7POINT`: for 7-point algorithm
    - `cv.FM_8POINT`: for 8-point algorithm
    - `cv.FM_RANSAC`: for RANSAC algorithm (DEFAULT)
    - `cv.FM_LMEDS`: for LMedS algorithm
- `ransacReprojThreshold`: _double_, maximum distance from the epipolar line in pixels, above which the point is considered an outlier (default is 3.0)
- `confidence`: _double_, confidence level, between 0 and 1 (default is 0.99)
- `maxIters`: _int_, maximum number of RANSAC iterations (default is 2000)

Outputs:
- `F`: _3x3 numpy array_, computed fundamental matrix
- `mask`: _nx1 numpy array_, output array of N elements, every element of which is set to 0 for outliers and to 1 for other points

#### computeCorrespondEpilines
`cv.computeCorrespondEpilines(points, whichImage, F) -> lines` - computes the epilines for points in one image to the other image

Inputs:
- `points`: _list or nx1 or 1xn numpy array_, the points for which epilines are computed
- `whichImage`: _int_, specifies for which image epilines need to be drawn (1 for the first and 2 for the second image)
- `F`: _3x3 numpy array_, fundamental matrix

Outputs:
- `lines`: _nx3 numpy array_, the output epilines. Each line `ax + by + c=0` is encoded by 3 numbers `(a,b,c)`


#### Stereo Images Dataset
https://vision.middlebury.edu/stereo/data/scenes2014/

