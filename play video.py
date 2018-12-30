import cv2
def main():
    windowName="LIVE VIDEO"
    cv2.namedWindow(windowName)
    fl='C:\\Users\\hp\\Desktop\\output\\ab.avi'
    cap = cv2.VideoCapture(fl)
    
 
    while (cap.isOpened()):
     ret, frame = cap.read()
     if  ret:
        cv2.imshow(windowName,frame)
        if cv2.waitKey(33)==27:
            break
     else:
         break
    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()

