import cv2
capture = cv2.VideoCapture(0)
print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

capture.set(3, 2000)#set width
capture.set(4, 1080)#set height
print(capture.get(3))
print(capture.get(4))

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()

