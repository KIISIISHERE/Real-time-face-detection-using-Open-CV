import cv2
#load the haar cascade
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
#start the video
cap=cv2.VideoCapture(0)
#if cam is opened
if not cap.isOpened():
    print("Couldn't access webcam")
    exit()
while True:
    #capture frame by frame
    success,frame=cap.read()
    if not success:
        #failed to capture the drame
        print("Cannot read the image")
        break
    #convert the frames to grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #detect the faceson the grayscale frames
    faces=face_cascade.detectMultiScale(gray,1.1,minNeighbors=5,minSize=(30,30))
    #draw rectangle around the detected faces
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),5)
    #display the result
    cv2.imshow("Face Detection",frame)
    #q-quit the application
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
#release the webcam
cap.release()
cv2.destroyAllWindows()