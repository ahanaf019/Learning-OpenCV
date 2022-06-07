import cv2 as cv
import numpy as np

img = cv.imread('images/img_1.jpg')

cv.imshow('Image', img)
# print(img.shape[:2])

blank = np.zeros(img.shape[:3], dtype='uint8')
# cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

# blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur Image', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print((contours))

cv.drawContours(blank, contours, -1, (0, 0, 255))
cv.imshow('Contures Drawn', blank)

cv.waitKey(0)