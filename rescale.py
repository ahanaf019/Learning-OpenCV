import cv2 as cv

# img = cv.imread('images/img_large.jpg')

cv.imshow('Image', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    

def changeRes(width, height):
    # This method only works for live videos
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture('videos/vid.mp4')

isTrue, frame = capture.read()

while isTrue:
    frame_resized = rescaleFrame(frame, .5)
    cv.imshow('Video', frame_resized)
    isTrue, frame = capture.read()
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()