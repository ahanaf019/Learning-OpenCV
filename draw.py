import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')


# img = cv.imread('images/img (1).png')


blank[ : ] = 0, 255, 0

blank[100:200, 300:400, :] = 0, 0, 255

# cv.rectangle(blank, (0,0), (250, 250), (255, 0, 0), thickness=cv.FILLED)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 0), thickness=cv.FILLED)


#  draw circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)

# draw line
cv.line(blank, (blank.shape[0]//2, blank.shape[1]//2), (500, 500), (0,255,255), thickness=5)


#  write text
cv.putText(blank, 'Ahanaf019', (200, 400), cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 0), thickness=3)


cv.imshow('Blank', blank)
cv.waitKey(0)