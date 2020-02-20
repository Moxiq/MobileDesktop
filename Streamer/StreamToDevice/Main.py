from NetworkConfig import NetworkConnection
from time import sleep
from CommandClicker import CommandClicker
import ctypes

# input("Press any key to start")

tcp = NetworkConnection()

print("Waiting for Connection...")
tcp_socket, client_addr = tcp.wait_for_connection()
client_ip = client_addr[0]
# client_name = socket.gethostbyaddr(client_ip)[0]
print("Connected to: ")
while 1:
    xy_pos = tcp.receive_data(tcp_socket)
    x = int(xy_pos.split(",")[0])
    y = int(xy_pos.split(",")[1])
    CommandClicker.click_xy(x, y)


