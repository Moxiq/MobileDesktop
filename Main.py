from NetworkConfig import NetworkConnection
from SendPacket import SendPacket
from CaptureScreen import Capture
import socket
from time import sleep
import pickle
import numpy as np
import cv2
import pickle


# input("Press any key to start")


tcp = NetworkConnection()

print("Waiting for Connection...")
tcp_socket, client_addr = tcp.wait_for_connection()
client_ip = client_addr[0]
client_name = socket.gethostbyaddr(client_ip)[0]
print("Connected to: " + client_name)

while 1:
    data = Capture().get_screen_image()
    print(data)
    # Other option is JSON (over pickle)
    tcp_socket.send(pickle.dumps(data))
