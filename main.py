import cv2 as cv
import os
import numpy as np
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

