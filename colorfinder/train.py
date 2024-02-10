import cv2
import numpy as np

def draw(event,x,y,flags,param):
    """print("Event=",event)
    print("x=",x)
    print("y=",y)    
    print("flags=",flags)
    print("param=",param)"""
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,(255,255,0),4)
    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img,(x,y),(x+100,y+100),(255,255,0),3)

img = np.zeros((500,500),np.uint8)
cv2.namedWindow(winname='mywin')
cv2.setMouseCallback('mywin',draw)


while True:
    cv2.imshow('mywin',img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cv2.destroyAllWindows()