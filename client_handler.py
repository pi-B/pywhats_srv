import socket
import logging
import datetime
import threading
import json
import error_handler
import message_handler

class ClientHandler(threading.Thread):

    def __init__(self, connection: socket.socket, addr):
        super().__init__()
        self.connection = connection
        self.addr = addr
        self.endConnection = False

    def run(self):
        logging.info(f"New client connected at {datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%Sl')}")
        
        while not self.endConnection :
            self.read_request()

        logging.debug("fin de la conversation")

    def read_request(self):
        
        payload = self.connection.recv(8096)
        message = payload.decode("utf-8")

        if message == "":
            self.endConnection = True

        try:
            # Transform the received message to a dict
            message_dict = json.loads(message)    
    
        except json.JSONDecodeError as e:
            error_handler.send_error(self.connection,self.addr,"WRONG_FORMAT")
        
        if "exit" in message_dict["packet_type"] : # Change this by using a dict has payload that has a "command" key and another for text or else
            self.endConnection = True

        try:
            message_handler.MessageHandler(message_dict)
        except ValueError as e:
            error_handler.send_error(self.connection,self.addr,"WRONG_FORMAT")
