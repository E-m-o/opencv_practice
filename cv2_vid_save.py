import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(capture.isOpened()):
    _, frame = capture.read()
    if _ == True:
        # print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        
        output.write(frame)
        
        g_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
out.release()
cv2.destroyAllWindows()
