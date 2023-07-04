import mediapipe as mp
from mediapipe import *
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

facemesh = mp.solutions.face_mesh
face = facemesh.FaceMesh(static_image_mode=True,
                        max_num_faces=5,
                        refine_landmarks=False,
                        min_detection_confidence=0.6,
                        min_tracking_confidence=0.6)
draw = mp.solutions.drawing_utils

h = 460
w = 640

red = [0,0,255]

while True:
    ret,frame = cap.read()
    # print(frame.shape)
    # break

    frame = cv2.flip(frame, 1)

    image = np.zeros(frame.shape,np.uint8)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    op = face.process(rgb)

    # print(op.multi_face_landmarks.landmark[0].x)
    # break

    # print(dir(op))
    # print(op.multi_face_landmarks)

    if op.multi_face_landmarks:
        for i in op.multi_face_landmarks:
            # print(i.landmark[0].x * 680)
            # print(i.landmark[0].y * 460)
            draw.draw_landmarks(image, i, facemesh.FACEMESH_FACE_OVAL, landmark_drawing_spec = draw.DrawingSpec(color = (120, 0, 0), thickness = 1, circle_radius = 1))

    fps = cap.get(cv2.CAP_PROP_FPS)
    # print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
 
    image = cv2.putText(image, str(fps), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, (255, 255, 255), 2, cv2.LINE_AA)

    # cv2.imshow("face detect", frame)
    cv2.imshow("face detect", image)

    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break