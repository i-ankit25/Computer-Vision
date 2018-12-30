import cv2
import numpy as np
def emptyFunction():
    pass
windowName='drawing'
cv2.namedWindow(windowName)
img=np.zeros((1024,1024,3),np.uint8)
cv2.createTrackbar('input',windowName,0,200,emptyFunction)
drawing = False
mode =1 
(ix, iy) = (-1, -1)
def sh(event,x,y,flag,para):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        (ix, iy) = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            input=cv2.getTrackbarPos('input',windowName)
            if mode == 1:
                cv2.rectangle(img, (ix, iy), (x,y), (0, 255, 0),1)
            elif mode==2:
                cv2.circle(img, (x, y),input, (0, 0, 255), 1)
            elif mode ==3:
                cv2.line(img, (ix,iy), (x,y), (255, 0, 0), 1)
            elif mode==4:
                 cv2.ellipse(img, (x,y), (x-20,y-20), 0, 0,360, (127, 127, 127), 1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        input=cv2.getTrackbarPos('input',windowName)  
        if mode ==1:
         cv2.rectangle(img, (ix, iy),(x,y), (0, 255, 0), 1)
        elif mode==2:
           cv2.circle(img, (x, y),input , (0, 0, 255), 1)
        elif mode ==3:
                cv2.line(img, (ix,iy),(x,y), (255, 0, 0),1)
        elif mode==4:
                 cv2.ellipse(img, (x,y),(x-20,y-20), 0, 0,360, (127, 127, 127), 1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        (ix, iy) = x, y
    elif event == cv2.EVENT_RBUTTONUP:
        drawing = False
        input=cv2.getTrackbarPos('input',windowName)
        if mode ==1:
          cv2.rectangle(img, (ix, iy),(ix+input,iy+(2*input)) ,(0, 255, 0), 1)
        elif mode==2:
           cv2.circle(img, (x, y),input, (0, 0, 255), 1)
        elif mode ==3:
                cv2.line(img, (ix,iy),(ix+input,iy+input), (255, 0, 0),1)
        elif mode==4:
                 cv2.ellipse(img, (x,y),(x-input,y-input), 0, 0,360, (127, 127, 127), 1)

cv2.setMouseCallback(windowName,sh)

def main():
   global mode
    
   while(True):
        cv2.imshow(windowName, img)
        
        k = cv2.waitKey(1)
        if k == ord('r') or k == ord('R'):
            mode = 1
        if k == ord('c') or k == ord('C'):
            mode = 2
        if k == ord('l') or k == ord('L'):
            mode = 3
        if k == ord('e') or k == ord('E'):
            mode = 4
        elif k == 27:
                break
if __name__ == "__main__":
    main()
    cv2.destroyAllWindows()