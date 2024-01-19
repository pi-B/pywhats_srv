
BASIC_MESSAGE = {
    "packet_type" : "",
    "content": None, 
    "identifier" : ""
}

class MessageHandler:

    def __init__(self, message: dict):
        self.message = message
        self.checkMessage()
        self.processMessage()

    def checkMessage(self):
        for key in BASIC_MESSAGE.keys():
            if str(key) not in self.message.keys():
                raise KeyError
            
    def processMessage(self):
        if self.message["packet_type"] == "chat":
            print(f"Received this message : {self.message['content']}")
        
    