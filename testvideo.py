# this code does show webcam video

import cv2
import sys



video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    cv2.imshow('Press a to exit', frame)

    if cv2.waitKey(100) == ord("a"): # the waitKey thing returns the code of pressed key 
        print("Pressed a")
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()