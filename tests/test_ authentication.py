import module.client_handler as client_handler
import socket

ch = client_handler.ClientHandler(socket.socket(), None)
hello_world = {"packet_type" : "chat","content": "Hello World", "identifier" : "toto","token" : "token"}

def testMessageNotAuthentified(ch):
    ch.authentication()
    if ch.user is not None:
        print("test message not authentified failed")
