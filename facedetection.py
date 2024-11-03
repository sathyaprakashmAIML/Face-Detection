import cv2
haarcascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
vs=cv2.VideoCapture(0)
while True:
    a,img=vs.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haarcascade.detectMultiScale(gray,1.3,3)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
    cv2.imshow('face',img)
    key=cv2.waitKey(10)
    if key == 27:
        break
vs.release()
cv2.destroyAllWindows()
                    
