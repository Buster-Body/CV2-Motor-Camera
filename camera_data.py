import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while (True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face.detectMultiScale(gray, 1.3, 3)

	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 1)
	
	cv2.imshow('Frame', frame)
	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()