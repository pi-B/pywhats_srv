import json
import logging
from modules.misc.pywhats_exceptions import PyWhatsException  

class User:

    def __init__(self, username: str, password: str):
        self.username = username
        self.userInfos = None

        try:
            with open("user_base.json","r") as users:
                dict_users = json.load(users)
                if username not in dict_users.keys():
                    raise PyWhatsException("WRONG_USER")
                    
                self.userInfos = dict_users[f"{username}"]
                
        except OSError:
            logging.critical("Could not load users database")
            raise PyWhatsException("SERVER_MALFUNCTION")

    