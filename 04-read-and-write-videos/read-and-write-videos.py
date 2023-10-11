import numpy as np
import cv2 as cv 
import os 

def videoFromWebcam(): 
    '''
        Will show how to capture video from webcam 
        note, will take about 30 sec - 1 min to start up 
    '''

    '''
        cv.VideoCapture(deviceNum) - initializes video capture 
            @param deviceNum int, number that identifies your camera 
                if you have more than one camera, can specify which one (0,1,2...etc)
            @returns cap, VideoCapture object
    '''
    cap = cv.VideoCapture(2)

    '''
        cap.isOpened() - checks if camera is opened 
            @returns bool, true if opened, false otherwise 
    '''
    if not cap.isOpened(): 
        exit() 

    while True:
        '''
            cap.read() - reads each video frame 
                @returns 
                    ret - bool, read status 
                    frame - ndarray, mxnx3 image at each frame read 
        '''
        ret, frame = cap.read()
        if ret: 
            cv.imshow("Webcam", frame)

        '''
            cv.waitKey(delay)- gets key pressed 
                NEED THIS FOR WHILE LOOP TO WORK...IDK WHY 

            @param delay delay in ms 

            @return code of the pressed key 
        '''
        if cv.waitKey(1) == ord('q'):
            break

    # Release the VideoCapture object and close all windows
    cap.release()
    cv.destroyAllWindows()

def videoFromFile(): 
    '''
        show how to playback video from a video file 
    '''
    root = os.getcwd()
    vidPath = os.path.join(root,'demoImages\\cuteVideo1.mov')
    cap = cv.VideoCapture(vidPath)

    while cap.isOpened(): 
        ret, frame = cap.read()
        cv.imshow("Video", frame)
        delay = int(1000 / 60) 
        if cv.waitKey(delay) == ord('q'):
            break

def writeVideoToFile(): 
    '''
        write video to file 

        NOTE: may need to unplug camera usb if having issues! 
    '''
    cap = cv.VideoCapture(2)

    ''' 
        cv.VideoWriter_fourcc(code)
            generates code for video compression format 
        @pram code four characters for encoding method 
            *'XVID' = 'X','V','I','D' 
            XVID is a mpeg-4 type encoding 
        @returns int, code for video compression format specified 
    '''
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    root = os.getcwd()
    outPath = os.path.join(root,'demoImages\\webcam.avi')

    '''
        cv.VideoWriter(outputFile,fourcc,fps,frameSize)
            creates video writer object for writing video to file 

            @param outputFile Str, name of video file path or name of video file 
            @param fourcc Int, compression format code 
            @param fps Float, frames per second 
            @param frameSize Tuple, (int,int) - (w,h) of each frame 
            @returns VideoWriter object 
    '''
    out = cv.VideoWriter(outPath, fourcc, 20.0, (640,  480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            '''
                out.write(frame) - writes frame to file 
                    @param frame Ndarray, mxnx3 video frame 
            '''
            out.write(frame)
            cv.imshow('Webcam', frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()

if __name__ == "__main__": 
    # videoFromWebcam() 
    # videoFromFile()
    writeVideoToFile() 

