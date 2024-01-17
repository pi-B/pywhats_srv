import socket
import logging
import datetime
import threading

class ClientHandler(threading.Thread):

    def __init__(self, connection: socket.socket, addr):
        super().__init__()
        self.connection = connection
        self.add = addr
        self.endConnection = False

    def run(self):
        logging.critical(f"New client connected at {datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%Sl')}")
        
        while not self.endConnection :
            self.read_request()

        logging.critical("fin de la conversation")

    def read_request(self):
        payload = self.connection.recv(8096)
        command = payload.decode("utf-8")
        print(command)
        if command == "exit":
            self.endConnection = True