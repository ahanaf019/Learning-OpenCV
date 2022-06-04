import cv2 as cv
import numpy as np


img = cv.imread('images/img_3.jpg')

cv.imshow('Image', img)


# Translation (Shifting)
# -x  --> Left 
# +x  --> Right 
# -y  --> Up 
# +y  --> Down 
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    # img.shape[1] => width, 
    # img.shape[0] => height
    dimensions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, transMat, dimensions)

# Shift image down by 100px 
# and to the right by 100px
translated = translate(img, 100, 100)
cv.imshow("Shifted", translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    # Rotate around the center if rotPoint is
    # not given.
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    # cv.getRotationMatrix2D(rotPoint, angle, scaling)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)


# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized', resized)


# Flipping 
# 0 --> flip image vertically 
# 1 --> flip image horizontally 
# -1 --> both vertically and horizontally
flip = cv.flip(img, 1)
cv.imshow('Flipped', flip)


# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)