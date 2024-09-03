import cv2 
import winsound
face_cascade = cv2.CascadeClassifier('E:\Python_Programming\Python\haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture('E:\Python_Programming\Python\ironman.mp4')
while cam.isOpened():
    ret,frame1= cam.read()
    ret,frame2= cam.read() 
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w,h) in faces:
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (255, 0, 0),2)
    cv2.imshow('img',frame1)
    if cv2.waitKey(10) == ord('q'):
        break
cam.release()