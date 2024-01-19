from client_handler import ClientHandler
from misc.pywhats_exceptions import PyWhatsException  
import socket
import unittest

class TestAuth(unittest.TestCase):
    def setUp(self) :
        self.ch = ClientHandler(socket.socket(), None)
        self.hello_world  = {"packet_type" : "chat","content": "Hello World", "identifier" : "toto","token" : "token"}

    def testMessageNotAuthentified(self):
        with self.assertRaises(PyWhatsException):
            self.ch.authentication(self.hello_world)
    

if __name__ == "__main__":
    unittest.main()