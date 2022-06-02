import cv2 as cv
import cvzone 

cap = cv.VideoCapture(0)

img = cv.imread('../photos/drum.png', cv.IMREAD_UNCHANGED)
img = cv.resize(img, (200,200))

_,frame1=cap.read()

hi,wi,ci=img.shape
hc,wc,cc=frame1.shape

while(True):
    _,frame1=cap.read()
    frame = cv.flip(frame1, +1)


    res_img=cvzone.overlayPNG(frame, img, pos=[wc-wi,hc-hi])
    
    cv.imshow('cam',res_img)


    key = cv.waitKey(1)
    if(key==27):
        break

cap.release()
cv.destroyAllWindows()
