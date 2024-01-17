import socket
import json
import datetime

ERROR_TEMPLATE = {  
    "packet_type" : "error", 
    "content" : [{"error_description":""}],
    "identifier" : ""
}

def send_error(connection: socket.socket, addr: int, errorType : str):
    print(errorType)
    if errorType == "WRONG_FORMAT":
        print("sending error")
        errorFormat = dict(ERROR_TEMPLATE)
        errorFormat["error_descrption"] = "Received a packet that wasn't in the desired format" # Need to provide more information once structure defined
        stringizedMessage = json.dumps(errorFormat)+"\n"
        connection.send(stringizedMessage.encode("utf-8"))