import cv2
import numpy as np

img = np.zeros((612,712,3), np.uint8)
#print(img)
cv2.line(img, (0,0), (300,300), (0,255,0),3)
cv2.rectangle(img,(100,100), (300,300), (0,255,255),1)
cv2.circle(img,(400,400),20,(255,0,0),2)
cv2.putText(img,"The Great Hansil Chapadiya",(0,500),cv2.FONT_HERSHEY_COMPLEX,1,(255,50,240),2)
cv2.imshow("Image",img)
cv2.waitKey(0)