import mediapipe as mp
from mediapipe import *
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

facemesh = mp.solutions.face_mesh
face = facemesh.FaceMesh(static_image_mode=True,
                        min_detection_confidence=0.6,
                        min_tracking_confidence=0.6)
draw = mp.solutions.drawing_utils

while True:
    ret,frame = cap.read()
    # print(frame.shape)
    # break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    op = face.process(rgb)

    # print(op.multi_face_landmarks.landmark[0].x)
    # break

    # print(dir(op))
    # print(op.multi_face_landmarks)

    if op.multi_face_landmarks:
        for i in op.multi_face_landmarks:
            print(i.landmark[0].x * 680)
            print(i.landmark[0].y * 460)
            draw.draw_landmarks(frame, i, facemesh.FACEMESH_FACE_OVAL, landmark_drawing_spec = draw.DrawingSpec(color = (120, 0, 0), thickness = 1, circle_radius = 1))


    cv2.imshow("face detect", frame)

    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break