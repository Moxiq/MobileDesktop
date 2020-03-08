import socket
from time import sleep


class NetworkConnection:

    def __init__(self):
        self.server_address = ("192.168.0.41", 10000)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = 4096

    def wait_for_connection(self):
        self.socket.bind(self.server_address)
        self.socket.listen()
        return self.socket.accept()

    def receive_data(self, connection_socket):
        data = connection_socket.recv(1024).decode("utf-8")
        return data
