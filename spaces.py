import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/img_1.jpg')
cv.imshow('Image', img)

# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)


# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)


# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)

# plt.imshow(img)
# plt.show()

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
plt.imshow(rgb)
plt.show()





cv.waitKey(0)
