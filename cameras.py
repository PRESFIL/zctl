import numpy as np
import cv2
import pyfakewebcam
import os
from PIL import Image

# Initialize input devices
print("Initializing video capture device...", end="", flush=True)
try:
    camera = cv2.VideoCapture(1)

    width = int(camera.get(3))
    height = int(camera.get(4))
except Exception as e:
    print("ERROR")
    print(e)
    exit(1)
else:
    print("\033[0;32mDONE\033[0;0m")

print("Initializing video file source......", end="", flush=True)
try:
    video = cv2.VideoCapture("video.avi")
except Exception as e:
    print("ERROR")
    print(e)
    exit(1)
else:
    print("\033[0;32mDONE\033[0;0m")

print("Initializing image file source......", end="", flush=True)
try:
    image = cv2.cvtColor(cv2.resize(np.array(Image.open("image.jpg")), (width, height), interpolation=cv2.INTER_LINEAR), cv2.COLOR_BGR2RGB)
except Exception as e:
    print("ERROR")
    print(e)
    exit(1)
else:
    print("\033[0;32mDONE\033[0;0m")

# Initialize the virtual camera output
print("Initializing video output device....", end="", flush=True)
try:
    output = pyfakewebcam.FakeWebcam('/dev/video0', width, height)
except Exception as e:
    print("ERROR")
    print(e)
    exit(1)
else:
    print("\033[0;32mDONE\033[0;0m")

# Set the default
with open("status", "w") as statusfile:
    statusfile.write("PASSTHROUGH")

# Begin the main loop
while True:
    try:
        with open("status", "r") as statusfile:
            status = statusfile.read().strip()
    except Exception as e:
        print(e)
        status = "PASSTHROUGH" # Bail out to passthrough if there are issues reading the file

    if status == "EXIT":
        break

    elif status == "PASSTHROUGH":
        ret, frame = camera.read()
        output.schedule_frame(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    elif status == "VIDEO":
        ret, frame = video.read()

        if ret:
            output.schedule_frame(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        else:
           video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    elif status == "IMAGE":
        output.schedule_frame(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # cv2.imshow("Reference Monitor", cv2.flip(cv2.addWeighted(cameraFrame, 0.75, videoFrame, 0.75, 0), 1))

    cv2.waitKey(24)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture devices
camera.release()
video.release()
cv2.destroyAllWindows()
