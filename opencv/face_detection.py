import mediapipe as mp
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

facemesh = mp.solutions.face_mesh
face = facemesh.FaceMesh()
draw = mp.solutions.drawing_utils

while True:
    ret,frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    op = face.process(rgb)
    # print(dir(op))
    print(op.multi_face_landmarks)

    if op.multi_face_landmarks:
        for i in op.multi_face_landmarks:
            draw.draw_landmarks(frame, i)


    cv2.imshow("face detect", frame)

    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break