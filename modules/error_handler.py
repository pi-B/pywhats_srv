import socket
import json
import logging
import datetime

ERROR_TEMPLATE = {  
    "packet_type" : "error", 
    "content" : [{"error_description":""}],
    "identifier" : ""
}

def sendError(connection: socket.socket, addr: int, errorType : str):
    
    errorFormat = dict(ERROR_TEMPLATE)
    logging.debug("sending error")
    
    if errorType == "WRONG_FORMAT":
        errorFormat["content"][0]["error_description"] = "Received a packet that wasn't in the desired format" # Need to provide more information once structure defined
        stringizedMessage = json.dumps(errorFormat)+"\n"
        
    if errorType == "WRONG_USER":
        errorFormat["content"][0]["error_description"]  = "This is not a valid username" 
        stringizedMessage = json.dumps(errorFormat)+"\n"
    
    if errorType == "NOT_AUTHENTIFIED":
        errorFormat["content"][0]["error_description"]  = "User not authentified" 
        stringizedMessage = json.dumps(errorFormat)+"\n"

    if errorType == "SERVER_MALFUNCTION":
        errorFormat["content"][0]["error_description"]  = "Something wrong happened in the treatment of your requests " 
        stringizedMessage = json.dumps(errorFormat)+"\n"

    connection.send(stringizedMessage.encode("utf-8"))

