class Config:

        def __init__ (self):
                self.SERVER_PORT = None   
                # self.SRV_TOKEN = None
        
        def loadConfig(self,conf: dict):
            
            self.SERVER_PORT = conf.get("server_port", None)
            
            
            for attr in self.__dict__.keys():     
                attribute = self.__getattribute__(str(attr))  
                if attribute == None or attribute == "" :
                      raise ValueError(f"The {attr} value is missing in conf")
            
            # print(vars(self))

