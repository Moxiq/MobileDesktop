import socket


class SendPacket:

    def send(self, soc, data):
        try:
            soc.sendAll(data)
        except socket.error as e:
            print(e)