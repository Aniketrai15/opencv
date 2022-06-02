import cv2 as cv
import cvzone 
from playsound import playsound

cap = cv.VideoCapture(0)

img = cv.imread('../photos/drum.png', cv.IMREAD_UNCHANGED)
img = cv.resize(img, (200,200))

_,frame1=cap.read()

hi,wi,ci=img.shape
hc,wc,cc=frame1.shape

def mouse_click(event, x, y, flags, params):
    if(event==cv.EVENT_LBUTTONDOWN and x>=wc-wi and y>=hc-hi):
        playsound('drum.mp3')
        

while(True):
    _,frame1=cap.read()
    frame = cv.flip(frame1, +1)


    res_img=cvzone.overlayPNG(frame, img, pos=[wc-wi,hc-hi])
    
    cv.imshow('cam',res_img)
    cv.setMouseCallback('cam', mouse_click)

    key = cv.waitKey(1)
    if(key==27):
        break

cap.release()
cv.destroyAllWindows()
