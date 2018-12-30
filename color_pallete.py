# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 00:29:35 2018

@author: hp
"""
def emptyfunction():
    pass
import cv2
import numpy as np
def main():
    img=np.zeros((512,512,3),np.uint8)
    windowName='OpenCv BGR Color Palette'
    cv2.namedWindow(windowName)
    cv2.createTrackbar('B',windowName,0,255,emptyfunction)
    cv2.createTrackbar('G',windowName,0,255,emptyfunction)
    cv2.createTrackbar('R',windowName,0,255,emptyfunction)
    while (True):
        cv2.imshow(windowName,img)
        if cv2.waitKey(1)==27:
            break
        blue=cv2.getTrackbarPos('B',windowName)
        green=cv2.getTrackbarPos('G',windowName)
        red=cv2.getTrackbarPos('R',windowName)
        img[:]=[blue,green,red]
        print(blue,green,red)
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()