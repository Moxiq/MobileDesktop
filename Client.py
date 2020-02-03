import socket
import numpy as np
import cv2
from mss import mss
from time import sleep
import pickle

# https://gist.github.com/benaisc/b89a8e6f1b3e74218ba8ceeb3240a508 to read mjpeg

def show_local_stream(arr):
    cv2.imshow('screen', data)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


HOST = "127.0.0.1"
PORT = 10000

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))

while 1:
    data = None
    # Crashes after a while since socket is filled?
    data = pickle.loads(soc.recv(829440))
    show_local_stream(data)
'''
received_bytes = ''.encode()
while 1:
    raw_data = tcp_socket.recv(1024)
    
    print(raw_data)
    if raw_data == 'img_end'.encode():
        print("Packet received!")
        break
    received_bytes += raw_data
np_array_from_bytes = np.frombuffer(received_bytes, dtype=np.uint64).reshape((8192,))
print(np_array_from_bytes)

'''
