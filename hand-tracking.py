import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands=mpHands.Hands(False,3) #Hands function- switch bw tracking and recognition, multiple hands
mpDraw=mp.solutions.drawing_utils

pTime=0 #previous time
cTime=0 #current time

while True:
    success, img=cap.read()
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLMS in results.multi_hand_landmarks:
            for id, lm in enumerate(handLMS.landmark):
                # print(id,lm)
                h,w,c=img.shape
                cx, cy=int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                
                # if id==4:
                #     cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)
                
            mpDraw.draw_landmarks(img, handLMS, mpHands.HAND_CONNECTIONS) #handlms attribute is given to handle multiple hands
    
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    
    cv2.putText(img, str(int(fps)), (50,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)