import imp
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Admin\\OneDrive\\Pictures\\Saved Pictures\\Picasa\\My Bestie\\Hansil_The_Billionaire\\MyBeautyQueen's\\62.JPG")
img_resize = cv2.resize(img,(0,0),fx=0.4,fy=0.3)
width,height = 400,400
pts1 = np.float32(([290,686],[290,1225],[890,1225],[890,686]))
pts2 = np.float32(([0,0],[width,0],[0,height],[width,height]))
matrix = cv2.getPerspectiveTransform(pts1,pts2)
img_output = cv2.warpPerspective(img_resize,matrix,(width,height))

cv2.imshow("img_Cropped",img_output)
cv2.imshow("ImageOriginal", img_resize)
cv2.waitKey(0)