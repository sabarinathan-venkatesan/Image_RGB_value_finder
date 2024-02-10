
import cv2
import numpy as np

def draw(event,x,y,flags,param):

    
    if event==cv2.EVENT_LBUTTONDOWN:
        xyvalues = "X=" + str(x) + ",Y=" + str(y)
        cv2.putText(img,xyvalues,(x,y),cv2.FONT_HERSHEY_PLAIN,2,(255,255,0),3)
        



    if event==cv2.EVENT_RBUTTONDOWN:
        b = img[y,x,0] #0=b
        g = img[y,x,1] #1=g
        r = img[y,x,2] #2=r
        bgr = "B="+str(b)+",G"+str(g)+",R="+str(r)
        cv2.putText(img,bgr,(x,y),cv2.FONT_HERSHEY_PLAIN,2,(0,255,255),3)




#img = np.zeros((500,500),np.uint8)
img = cv2.imread('image.jpg')
img = cv2.resize(img,(500,550))
cv2.namedWindow(winname='mywin')
cv2.setMouseCallback('mywin',draw)


while True:
    cv2.imshow('mywin',img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cv2.destroyAllWindows()