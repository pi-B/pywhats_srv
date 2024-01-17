import socket
import logging
import client_handler as ch

logging.getLogger().setLevel(logging.DEBUG)

class PyServ:
    
    def __init__(self, port: str):
        self.port = port
        self.listen_socket = None

    def start_server(self):
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # dev option to kill the process will ctrl + c and still relaunch without errno 98 
        self.listen_socket.bind(("",55000))

        while True:
            logging.debug("Waiting for a new client to handle")
            self.listen_socket.listen()
            connection, addr = self.listen_socket.accept()
            newClient = ch.ClientHandler(connection,addr)
            newClient.start()
            