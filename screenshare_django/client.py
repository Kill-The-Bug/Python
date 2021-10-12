from vidstream import CameraClient
from vidstream import VideoClient
from vidstream import ScreenShareClient
import threading

# Choose One
# client3 = CameraClient('127.0.0.1', 9998)
# client2 = VideoClient('127.0.0.1', 9999, 'video.mp4')
client3 = ScreenShareClient('127.0.0.1', 9999)

t= threading.Thread(target=client3.start_stream)
t.start()

# Other Code
while input("") != 'STOP':
    continue

# client1.start_stream()
# client2.start_stream()
client3.stop_stream