import cv2 as cv
from cv2 import erode

img = cv.imread('images/img_1.jpg')

cv.imshow('Image', img)


# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

blur2 = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
# cv.imshow('Blur2', blur2)


# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

canny_b = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges Blur', canny_b)


# Dialating the image
dialated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dialated', dialated)

# Eroding
eroded = cv.erode(dialated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)


# Resizing
resized = cv.resize(img, (800, 800), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Cubic', resized)

resized = cv.resize(img, (800, 800), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized Linear', resized)

resized = cv.resize(img, (800, 800), interpolation=cv.INTER_AREA)
cv.imshow('Resized Area', resized)


# Cropping
cropped = resized[50:200, 200:500]
cv.imshow('cropped', cropped)



cv.waitKey(0)