import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    while ret:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Blue Color
        low1= np.array([100, 50, 50])
        high1 = np.array([140, 255, 255])

        # Green Color
        low2= np.array([40,50,50])
        high2 = np.array([80,255,255])

        # Red Color
        low3 = np.array([0,0,30])
        high3 = np.array([80,80,255])
        
        #verify the ranges before use     
        
        image_mask1 = cv2.inRange(hsv, low1, high1)
        image_mask2 = cv2.inRange(hsv, low2, high2)
        image_mask3 = cv2.inRange(hsv, low3, high3)
        
        
        output1 = cv2.bitwise_and(frame, frame, mask = image_mask1)
        output2 = cv2.bitwise_and(frame, frame, mask = image_mask2)
        output3 = cv2.bitwise_and(frame, frame, mask = image_mask3)
        output4=output1+output2+output3
      #  cv2.imshow("Image mask", image_mask1)
        cv2.imshow("Original Webcam Feed", frame)       
        cv2.imshow("Blue Color Tracking", output1)
        cv2.imshow("Green Color Tracking", output2)
        cv2.imshow("Red Color Tracking", output3)
        cv2.imshow("Merged", output4)
        if cv2.waitKey(1) == 27: 
            break

    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()