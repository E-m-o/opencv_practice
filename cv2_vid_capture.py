import cv2

capture = cv2.VideoCapture(0)

while(True):
    _, frame = capture.read()

    g_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
