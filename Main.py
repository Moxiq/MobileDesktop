from NetworkConfig import NetworkConnection
from time import sleep

# input("Press any key to start")


tcp = NetworkConnection()

print("Waiting for Connection...")
tcp_socket, client_addr = tcp.wait_for_connection()
client_ip = client_addr[0]
# client_name = socket.gethostbyaddr(client_ip)[0]
print("Connected to: ")
while 1:
    sleep(1)
# print("Message received: " + tcp.recieve_data())

