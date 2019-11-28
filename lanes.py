"""
self driving course i found online
https://www.udemy.com/course/applied-deep-learningtm-the-complete-self-
driving-car-course/learn/lecture/11241778#content
_author_ Xavier Naranjo 11/27/2019
using anaconda 3.7 download
"""
import cv2
import numpy as np


def canny(image):
    """
    :param image: regular picture
    :return: canny image
    """
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


def region_of_interest(image):
    """
    :param image: creates triangle within image
    had to change to polygon because of an exception where fill poly fills an
    area of polygons instead of an array to one polygon
    """
    height = image.shape[0]
    polygons = np.array([
        [(200, height), (1100, height), (550, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    return mask


image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny = canny(lane_image)
cv2.imshow('result', region_of_interest(canny))
cv2.waitKey(0)
