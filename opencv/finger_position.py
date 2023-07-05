import cv2
import mediapipe as mp
import time
cap = cv2.VideoCapture(0)

mp_handmesh = mp.solutions.hands
mp_hands = mp_handmesh.Hands(static_image_mode=False,
                            max_num_hands=2,
                            model_complexity=1,
                            min_detection_confidence=0.5,
                            min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, frame = cap.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = frame.shape
                cx, cy = int(lm.x *w), int(lm.y*h)
                #if id ==0:
                cv2.circle(frame, (cx,cy), 3, (255,0,255), cv2.FILLED)

            mp_drawing.draw_landmarks(frame, handLms, mp_handmesh.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(frame,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", frame)
    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break