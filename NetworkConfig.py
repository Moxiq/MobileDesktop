import socket
from time import sleep


class NetworkConnection:

    def __init__(self):
        self.server_address = ("localhost", 10000)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def wait_for_connection(self):
        self.socket.bind(self.server_address)
        self.socket.listen()
        return self.socket.accept()
