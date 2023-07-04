import mediapipe as mp
from mediapipe import *
import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

mp_facemesh = mp.solutions.face_mesh
mp_face = mp_facemesh.FaceMesh(static_image_mode=True,
                        max_num_faces=5,
                        refine_landmarks=False,
                        min_detection_confidence=0.6,
                        min_tracking_confidence=0.6)

mp_handmesh = mp.solutions.hands
mp_hands = mp_handmesh.Hands(static_image_mode=False,
                            max_num_hands=2,
                            model_complexity=1,
                            min_detection_confidence=0.5,
                            min_tracking_confidence=0.5)

mp_drawing_styles = mp.solutions.drawing_styles

mp_drawing = mp.solutions.drawing_utils

h = 460
w = 640

red = [0,0,255]

pTime = 0
cTime = 0

while True:
    success,frame = cap.read()
    # print(frame.shape)
    # break

    frame = cv2.flip(frame, 1)

    image = np.zeros(frame.shape,np.uint8)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face = mp_face.process(rgb)

    # print(face.multi_face_landmarks.landmark[0].x)
    # break

    # print(dir(face))
    # print(face.multi_face_landmarks)

    if face.multi_face_landmarks:
        for i in face.multi_face_landmarks:
            # print(i.landmark[0].x * 680)
            # print(i.landmark[0].y * 460)
            mp_drawing.draw_landmarks(image, i, mp_facemesh.FACEMESH_FACE_OVAL, landmark_drawing_spec = mp_drawing.DrawingSpec(color = (120, 0, 0), thickness = 1, circle_radius = 1))

    hand = mp_hands.process(rgb)

    # print(hand)
    # print(dir(hand))
    # print(hand.multi_hand_landmarks)
    # break

    if hand.multi_hand_landmarks:
        for handLms in hand.multi_hand_landmarks:
            # for id, lm in enumerate(handLms.landmark):
            #     #print(id,lm)
            #     h, w, c = frame.shape
            #     cx, cy = int(lm.x *w), int(lm.y*h)
            #     #if id ==0:
            #     cv2.circle(image, (cx,cy), 3, (255,0,255), cv2.FILLED)

            mp_drawing.draw_landmarks(image, handLms, mp_handmesh.HAND_CONNECTIONS)


    # fps = cap.get(cv2.CAP_PROP_FPS)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    image = cv2.putText(image, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_PLAIN,
                        2, (255, 255, 255), 2, cv2.LINE_AA)

    # image = cv2.putText(image, str(fps), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
    #                     1, (255, 255, 255), 2, cv2.LINE_AA)

    # cv2.imshow("face detect", frame)
    cv2.imshow("face detect", image)

    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break