import error_handler

BASIC_MESSAGE = {
    "packet_type" : "",
    "content": None, 
    "identifier" : ""
}

class MessageHandler:

    def __init__(self, message: dict):
        self.message = message
        self.check_message()
        self.process_message()

    def process_message(self):
        if self.message["packet_type"] == "chat":
            print(f"Received this message : {self.message['content']}")
        
    def check_message(self):
        for key in BASIC_MESSAGE.keys():
            if str(key) not in self.message.keys():
                raise KeyError
    