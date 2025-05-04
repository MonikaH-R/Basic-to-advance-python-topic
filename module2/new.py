import cv2
#open video file
cap=cv2.VideoCapture("video2.mp4") #0 is for web cam
while cap.isOpened():
    ret,frame=cap.read() #read frame by frame
    if not ret:
        break # break if video ends
    cv2.imshow("Video Frame",frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()