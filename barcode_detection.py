from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import cv2
import winsound

def decode(im) : 
    decodedObjects = pyzbar.decode(im)
    for obj in decodedObjects:
      winsound.Beep(7000,600)
      k=obj.data
      t=str(k)
      return ("1"+t)
def main():
    ret=True
    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)  
    cap = cv2.VideoCapture(0)
    while ret:
        ret, frame = cap.read()
        cv2.imshow(windowName,frame)
        s=decode(frame)
        if(s!=None):
          if(s[0]=='1'):
              ret=False
              id=s[1:]
              print(id)
        if (cv2.waitKey(1)==27):
            break
    cv2.destroyAllWindows()    
    cap.release()  
if __name__ == '__main__':
  main()