import socket
import logging
import datetime
import threading
import json
import error_handler
import message_handler
import user
from pywhats_exceptions import PyWhatException  


class ClientHandler(threading.Thread):

    def __init__(self, connection: socket.socket, addr):
        super().__init__()
        self.connection = connection
        self.addr = addr
        self.endConnection = False

        # identity management
        self.user = None

    def run(self):
        logging.info(f"New client connected at {datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%Sl')}")
        
        while not self.endConnection :
            self.readRequest()

        logging.debug("fin de la conversation")

    def readRequest(self):
        
        payload = self.connection.recv(8096)
        message = payload.decode("utf-8")

        if message == "":
            self.endConnection = True

        try:
            # Transform the received message to a dict
            message_dict = json.loads(message)    

            if "exit" in message_dict["packet_type"] : # Change this by using a dict has payload that has a "command" key and another for text or else
                self.endConnection = True

            self.authentication(message_dict)
    
            message_handler.MessageHandler(message_dict)

        except json.JSONDecodeError:
            logging.critical("Packet was not structured as a dict")
            error_handler.sendError(self.connection,self.addr,"WRONG_FORMAT")
            return 0
        
        except KeyError as e:
            logging.critical(f"Did not find expected {e.args[0]}")
            error_handler.sendError(self.connection,self.addr,"WRONG_FORMAT")
            return 0
        
        except PyWhatException as e:
            error_handler.sendError(self.connection,self.addr,e.format)
  
        except ValueError as e:
            logging.critical("Packet did not fit the format")
            error_handler.sendError(self.connection,self.addr,"WRONG_FORMAT")

    def createAuthToken(self):
        if self.user == None:
            logging.critical("User has not been authentified")
            error_handler.sendError(self.connection,self.addr,"NOT_AUTHENTIFIED")

        self.token = "token"

        return "token"

    # Need to define how tokens are created and then refactore its check
    def checkAuthToken(self, token: str):
        if token == "token":
            return True
        else:
            logging.critical("Using an invalid token")
            error_handler.sendError(self.connection,self.addr,"NOT_AUTHENTIFIED")
            return False

    def authentication(self,message_dict: dict):
        if self.user == None:
            if message_dict["packet_type"] != "authentication":
                raise PyWhatException("NOT_AUTHENTIFIED")
            
            connection_info = message_dict["content"]
            self.user = user.User(username=connection_info["username"], password=connection_info["password"])

        else:
            self.checkAuthToken(message_dict["token"])
            # Vérifier token