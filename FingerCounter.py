import cv2 as cv
import os
import time
import Handtrackingmodule as htm
cap=cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

ptime=0
ctime=0

folderpath="fingerimage"
mylist=os.listdir(folderpath)
overlaylist=[]

for impath in mylist:
    image=cv.imread(f"{folderpath}/{impath}")
    #print(f"Image: {folderpath}/{impath}")
    reszied=cv.resize(image,(200,200))
    overlaylist.append(reszied)
print(len(overlaylist))
print(mylist)

detector=htm.handDetector(detectionCon=0.75)
lmList=[]
tipsid=[4,8,12,16,20]
while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmlist=detector.findPosition(img,draw=False)
    #print(lmlist)
    
    if lmlist!=[]:
        fingers=[]
        #Thumb
        if lmlist[tipsid[0]][1] > lmlist[tipsid[0]-1][1]:
            fingers.append(1)
            print("Thumb is up")
        else:
            fingers.append(0)
            print("Thumb is down")
        #Other 4 fingers
        for id in range(1,5):    
            if lmlist[tipsid[id]][2]< lmlist[tipsid[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        totalfingers=fingers.count(1)
        print(totalfingers)
                
        print(fingers)
        img[0:200,0:200]=overlaylist[totalfingers-1]

        cv.rectangle(img,(20,225),(170,425),(255,0,255),cv.FILLED)
        cv.putText(img,str(totalfingers),(45,375),cv.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv.putText(img,f"FPS: {int(fps)}",(400,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv.imshow("Image",img)
    cv.waitKey(1)