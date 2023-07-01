import cv2
from pyzbar.pyzbar import decode
import numpy as np

cap = cv2.VideoCapture(0)



while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decoded = decode(gray)
    for obj in decoded:
        print("Data: ", obj.data)
        pts = np.array([obj.polygon], np.int32,)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 0, 255), 2)
    cv2.imshow("QR", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()