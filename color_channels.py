import cv2 as cv
import numpy as np

img = cv.imread('images/img_1.jpg')
cv.imshow('Image', img)


cv.waitKey(0)