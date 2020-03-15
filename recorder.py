import numpy as np
import cv2

cap = cv2.VideoCapture(1)
width = int(camera.get(3))
height = int(camera.get(4))
out = cv2.VideoWriter("video.avi",cv2.VideoWriter_fourcc(*'XVID'), 20.0, (width, height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow("Recorder",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
