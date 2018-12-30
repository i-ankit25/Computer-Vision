import cv2
def emptyFunction():
    pass
def main():
    #check for the path and images
    path = "C:\\Users\\hp\\Desktop\\misc\\"
    
    imgpath1 =  path + "4.2.03.tiff"
    imgpath2 =  path + "4.2.07.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    print(img1)
    o=cv2.addWeighted(img1,0.5,img2,0.5,0) 
    windowName="transition"
    cv2.namedWindow(windowName)
    cv2.createTrackbar('ALPHA',windowName,0,1000,emptyFunction)
    cv2.createTrackbar('BETA',windowName,0,1000,emptyFunction)
    while(True):
        cv2.imshow(windowName,o)
        if cv2.waitKey(1)==27:
            break
        alpha=cv2.getTrackbarPos('ALPHA',windowName)/1000
        beta=cv2.getTrackbarPos('BETA',windowName)/1000
        o=cv2.addWeighted(img1,alpha,img2,beta,0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()