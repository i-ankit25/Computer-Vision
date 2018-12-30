import cv2
import time
def main():
    
    windowName = "Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    a=0
    #scale=1
    scale=0.1
    rows,columns,channels=frame.shape
    while True:
     ret, frame = cap.read()   
     if a==360:
      a=0
    # a=0
     if scale<2:
             scale=scale+0.1
     if scale>=2:
            scale=0.1
     r=cv2.getRotationMatrix2D((columns/2,rows/2),a,scale)
     o=cv2.warpAffine(frame,r,(columns,rows))
     cv2.imshow(windowName,o)
     a=a+1
     time.sleep(0.01)
     if cv2.waitKey(1)==27:
      break
    cv2.destroyAllWindows()
    cap.release
if __name__ == "__main__":
    main()

