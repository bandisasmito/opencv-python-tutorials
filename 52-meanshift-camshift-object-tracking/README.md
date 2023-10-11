#### meanShift/CamShift (same input/output)
`cv.meanShift(probImage,window,criteria)->retval,window` - computes the meanShift tracking window 
`cv.CamShift(probImage,window,criteria)->retval,window` - computes the CamShift tracking window 

Input: 
- `probImage`: _mxn array_, back projection image
- `window`: _4-tuple of ints_, initial tracking window (xTopLeft,yTopLeft,w,h)
- `criteria`: _3-tuple_, iteration termination criteria
  - `type`：_enum_, stopping method 
    - `cv.TERM_CRITERIA_EPS`: stop if min error reached 
    - `cv.TERM_CRITERIA_COUNT`: stop if max iter reached 
  - `max_iter`：_int_, max iterations
  - `eps`：_float_, min error 

Output:
- `retval`: _bool_, true if successful, false otherwise
- `window`: _4-tuple of ints_, new tracking window (xTopLeft,yTopLeft,w,h)



#### Reference
https://docs.opencv.org/3.4/dc/d6b/group__video__track.html#ga432a563c94eaf179533ff1e83dbb65ea

#### Markdown Shortcut
Generate Preview: `ctrl+k, v`
