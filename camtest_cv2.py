import cv2
import time
import sys

print("Capturing images from the camera")
print("Press CTRL+C to terminate the program")
counter = 0
try:
	while True:
		cam = cv2.VideoCapture(0)
		if cam.isOpened():
			print("open")
		else:
			sys.exit("No such camera")
		w = cam.get(3)
		h = cam.get(4)
		print(w,h)
		cam.set(3,630)
		cam.set(4,470)
		s, img = cam.read()
		cam.release()
		imgtime = time.localtime()
		cv2.imwrite("%s%s%s_%s%s%s.bmp" %  imgtime[0:6],img)
		time.sleep(0.5)
	
except KeyboardInterrupt:
	print("OK, done")
	sys.exit(0)