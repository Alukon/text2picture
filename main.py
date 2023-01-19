# pip install opencv-python
# pip install numpy
import numpy as np
import cv2

img = cv2.imread('image.jpg')
font = cv2.FONT_HERSHEY_COMPLEX

cv2.putText(img, 'fffffFFFFGGGGOOO PPP BBB', (160, 350), font, 1, color=(0, 0, 255), thickness=2)

cv2.imshow('Resalt', img)
cv2.imwrite('image_2.png', img)
cv2.waitKey()
