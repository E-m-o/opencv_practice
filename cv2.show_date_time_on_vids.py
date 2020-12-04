import cv2
import datetime
capture = cv2.VideoCapture(0)
print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(capture.get(3)) + 'Height: ' + str(capture.get(4))
        date_now = str(datetime.datetime.now())
        frame = cv2.putText(frame, date_now, (10,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()

