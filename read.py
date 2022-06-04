import cv2 as cv

# img = cv.imread('images/img (1).jpg')
# cv.imshow('Image', img)


capture = cv.VideoCapture('videos/vid.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)