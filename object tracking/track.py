import cv2
import math
g1 = 520
g2 = 270
video = cv2.VideoCapture("bb3.mp4")
tracker = cv2.TrackerCSRT_create()
ret,image = video.read()
boundrie = cv2.selectROI('tracking',image,False)
tracker.init(image,boundrie)
xs = []
ys = []
goal=False
#print(boundrie)
def move_boundrie(image,boundrie):
    x,y,w,h = int(boundrie[0]),int(boundrie[1]),int(boundrie[2]),int(boundrie[3])
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3,1)
def trackObject(image,boundrie):
    global goal
    x,y,w,h = int(boundrie[0]),int(boundrie[1]),(boundrie[2]),int(boundrie[3])
    c1 = x+int(w/2)
    c2=y+int(h/2)
    cv2.circle(image,(c1,c2),2,(0,0,255),3)
    cv2.circle(image,(g1,g2),2,(0,255,0),3)
    distance = math.sqrt((c1-g1)**2+(c2-g2)**2)
    if(distance<=20):
        goal=True
    xs.append(c1)
    ys.append(c2)
    for a in range(0,len(xs)):
        cv2.circle(image,(xs[a],ys[a]),2,(255,0,0),5)

while True:
    ret,image = video.read()
    succes,boundrie = tracker.update(image)
    if(succes==True):
        move_boundrie(image,boundrie)
    else:
        cv2.putText(image,'object is not moving',(75,90),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)
    trackObject(image,boundrie)
    if(goal==True):
        cv2.putText(image,'GOAL',(300,90),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),2)
    cv2.imshow('ball attaction',image)
    if(cv2.waitKey(1)==32):
        break
video.release()
cv2.destroyAllWindows()