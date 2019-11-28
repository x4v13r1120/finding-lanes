"""
self driving course i found online
https://www.udemy.com/course/applied-deep-learningtm-the-complete-self-
driving-car-course/learn/lecture/11241778#content
_author_ Xavier Naranjo 11/27/2019
using anaconda 3.7 download
"""
import cv2
import numpy as np

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow('result', blur)
cv2.waitKey(0)
