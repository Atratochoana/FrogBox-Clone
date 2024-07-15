# import required libraries
from vidgear.gears import CamGear
from vidgear.gears import WriteGear
import cv2

# Open live webcam video stream on first index(i.e. 0) device
stream = CamGear(source=0, logging=True).start()

# define required FFmpeg optimizing parameters for your writer
output_params = {
    "-preset:v": "veryfast",
    "-g": 60,
    "-keyint_min": 60,
    "-sc_threshold": 0,
    "-bufsize": "2500k",
    "-f": "flv",
}

# [WARNING] Change your Twitch Stream Key here:
TWITCH_KEY = "live_218704501_RiSz6LSq8JB0jLmu34R8nGnmrUdRyI"

# Define writer with defined parameters and
writer = WriteGear(
    output="rtmp://live.twitch.tv/app/{}".format(TWITCH_KEY),
    logging=True,
    **output_params
)

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # write frame to writer
    writer.write(frame)

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

# safely close writer
writer.close()