import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened():
    status, frame = cap.read()
    cv2.imshow("frame", frame)
    cv2.imwrite("frame.jpg",frame)
    if cv2.waitKey(27) &  0xff ==  ord('q') :
        break
    
cv2.destroyAllWindows()
cap.release()
