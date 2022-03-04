import cv2
import numpy as np

def openCamera():
    cap=cv2.VideoCapture(0)
    classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    while True:
        ret,frame=cap.read()
        if ret:
        
            faces=classifier.detectMultiScale(frame)
            for face in faces:
                x,y,w,h=face
                faces=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
            cv2.imshow("Webcam",frame)
                
            key=cv2.waitKey(1)
    
            if key==ord("q"):
                break
    cap.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    openCamera()