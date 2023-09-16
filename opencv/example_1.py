import cv2

img = cv2.VideoCapture(0)
effect = False

while True:
    ret, frame = img.read()

    if cv2.waitKey(1) == ord('a'):
        effect = not effect

    if effect:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if cv2.waitKey(1) == ord('p'):
        cv2.imwrite("F:\image proccing\capture.png", frame)

    cv2.imshow("cam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()