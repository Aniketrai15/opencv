import cv2 as cv
import numpy as np

def nothing(x):
    pass

cap=cv.VideoCapture(0)


cv.namedWindow("trackbars") 


cv.createTrackbar("LH","trackbars",79,255,nothing)
cv.createTrackbar("LS","trackbars",88,255,nothing)
cv.createTrackbar("LV","trackbars",121,255,nothing)
cv.createTrackbar("UH","trackbars",136,255,nothing)
cv.createTrackbar("US","trackbars",255,255,nothing)
cv.createTrackbar("UV","trackbars",255,255,nothing)

kernel = np.ones((5,5), np.uint8)

while(True):
    _,frame1=cap.read()
    frame = cv.flip(frame1, +1)

    hsv=cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h=cv.getTrackbarPos("LH","trackbars")
    l_s=cv.getTrackbarPos("LS","trackbars")
    l_v=cv.getTrackbarPos("LV","trackbars")
    u_h=cv.getTrackbarPos("UH","trackbars")
    u_s=cv.getTrackbarPos("US","trackbars")
    u_v=cv.getTrackbarPos("UV","trackbars")

    l_b=np.array([l_h,l_s,l_v])    
    u_b=np.array([u_h,u_s,u_v])
    
    mask=cv.inRange(hsv, l_b, u_b)

    mask=cv.erode(mask, kernel, iterations=1)
    mask = cv.dilate(mask, kernel, iterations=2)

    #res=cv.bitwise_and(frame,frame, mask=mask)

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv.contourArea(contour)

        if area>1000:
            x,y,w,h= cv.boundingRect(contour)
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)

    cv.imshow('frame',frame)
    #cv.imshow('mask',mask)
    #cv.imshow('res',res)

    key = cv.waitKey(1)
    if(key==27):
        break

cap.release()
cv.destroyAllWindows()
