# import py_serv
import json
import pathlib
import config
import py_serv
import logging

conf = config.Config()

try:

    with open("./parameters.json","r") as conf_file:
        dict_conf = json.load(conf_file)
        conf.load_config(dict_conf)

except ValueError as e:
    logging.critical(e)
    print("Server shutting down")
    exit(0)

if __name__== "__main__" :
    print("Hello world")
    PyWhatSrv = py_serv.PyServ(conf.SERVER_PORT)
    PyWhatSrv.start_server()    

    