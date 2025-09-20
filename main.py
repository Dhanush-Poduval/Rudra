import cv2 as cv
import os
import numpy as np

def readImage():
    path='images/cat.jpg'
    image=cv.imread(path)
    if image is None:
        print("Error: No image found")
    resized_image=cv.resize(image,(600,400))
    cv.imshow('Image',resized_image)
    cv.waitKey(0)

def writeImage():
    path='images/cat.jpg'
    image= cv.imread(path)
    outPath='images/output.jpg'
    cv.imwrite(outPath,image)

def videoFromWebcam():
    cap=cv.VideoCapture(3)
    if not cap.isOpened():
        exit()
    while True:
        ret,frame=cap.read()
        if ret:
            cv.imshow('Webcam',frame)
        if cv.waitKey(1)==ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

def videoFromFile():
    path='videos/vid1.mov'
    cap=cv.VideoCapture(path)
    fps = cap.get(cv.CAP_PROP_FPS)#dynamically get fps 
    delay = int(1000 / fps) if fps > 0 else 33 
    if not cap.isOpened():
        exit()
    while cap.isOpened():
        ret,frame=cap.read()
        cv.imshow('video',frame)
        if cv.waitKey(delay)==ord('q'):
            break
def writeVideoTofile():
    path='videos/vid1.mov'
    cap =cv.VideoCapture(path)
    fourcc=cv.VideoWriter_fourcc(*'mp4v')
    outpath='videos/output.mov'
    width  = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))#always try to dynamically get width height and fps 
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv.CAP_PROP_FPS)
    out=cv.VideoWriter(outpath,fourcc,fps if fps>0 else 20.0,(width, height))
    while cap.isOpened():
        ret,frame=cap.read()
        if ret:
            out.write(frame)
            cv.imshow('Webcam',frame)
        if cv.waitKey(1)==ord('q'):
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()

def singlePixel():
    path='images/cat.jpg'
    img=cv.imread(path)
    imageRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imageRGB)
    plt.show()

def readandwriteImage():
    path='images/cat.jpg'
    img=cv.imread(path)
    imgRGC=cv.cvtColor(img,cv.COLOR_BGR2RGBA)
    plt.figure()
    plt.imshow(imgRGC)
    plt.show()
    eyeRegion=imgRGC[325:400,350:460]
    dx=400-325
    dy=460-350
    startx=260
    starty=400
    imgRGC[startx:startx+dx,starty:starty+dy]=eyeRegion
    plt.figure()
    plt.imshow(imgRGC)
    plt.show()

def pureColors():
    zeroes=np.zeros((100,100))
    ones=np.ones((100,100))
    imgRGB=cv.merge((ones*255,zeroes,zeroes))
    plt.figure()
    plt.title('Red')
    plt.plot()
    plt.imshow(imgRGB)
    plt.show()

def houghCircles():
    path='images/circles2.jpg'
    image = cv.imread(path,cv.IMREAD_GRAYSCALE)
    if image is None:
        print("Photo not loaded")
    resized_image=cv.resize(image,(600,400))
    cimg=cv.cvtColor(resized_image,cv.COLOR_GRAY2BGR)
    blurred_img=cv.blur(cimg,(5,5))
    circles=cv.HoughCircles(blurred_img,cv.HOUGH_GRADIENT,1,20,param1=80,param2=50,minRadius=0,maxRadius=0)
    if circles is None:
        print("Error is found")
    circles=np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv.circle(blurred_img,(i[0],i[1]),i[2],(0,255,0),2)
        cv.circle(blurred_img,(i[0],i[1]),2,(0,0,255),3)
    cv.imshow('circle_image',blurred_img)
    cv.waitKey(0)

        

    
    


if __name__=="__main__":
    houghCircles()

