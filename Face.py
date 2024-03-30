import cv2 as cv
face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv.VideoCapture(0)

while True:
    ret,frame =cap.read()
    detect_face = face_cascade.detectMultiScale(frame,1.1,5)
    for (x,y,w,h) in detect_face:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cv.release()
cv.destroyAllWindows()
