import cv2

cap = cv2.VideoCapture(0)
while True:
	ret,frame = cap.read()
	cv2.imshow('image',frame)
	code = cv2.waitKey(10)
	if code == ord('q'):
		break