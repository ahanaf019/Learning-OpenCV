import cv2 as cv

img = cv.imread('images/img (1).jpg')

cv.imshow('Image', img)


# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, ())



cv.waitKey(0)