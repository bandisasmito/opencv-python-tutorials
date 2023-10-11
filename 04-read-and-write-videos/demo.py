import numpy as np 
import cv2 as cv 
import os 

def videoFromWebcam(): 
    cap = cv.VideoCapture(1)

    if not cap.isOpened(): 
        exit() 

    while True: 
        ret, frame = cap.read() 
        if ret: 
            cv.imshow('Webcam',frame)

        if cv.waitKey(1) == ord('q'):
            break

    cap.release() 
    cv.destroyAllWindows() 

def videoFromFile(): 
    root = os.getcwd()
    vidPath = os.path.join(root,'demoImages\\cuteVideo1.mov')
    cap = cv.VideoCapture(vidPath)

    while cap.isOpened(): 
        ret, frame = cap.read() 
        cv.imshow('video',frame)
        delay = int(1000/60)
        if cv.waitKey(delay) == ord('q'):
            break

def writeVideoToFile(): 
    cap = cv.VideoCapture(1)

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    root = os.getcwd() 
    outPath = os.path.join(root,'demoImages\\webcam.avi')

    out = cv.VideoWriter(outPath,fourcc,20.0,(640,480))

    while cap.isOpened(): 
        ret, frame = cap.read() 
        if ret: 
            out.write(frame)
            cv.imshow('Webcam',frame)

        if cv.waitKey(1) == ord('q'):
            break

    cap.release() 
    out.release()
    cv.destroyAllWindows() 



if __name__ == '__main__': 
    # videoFromWebcam() 
    # videoFromFile()
    writeVideoToFile() 