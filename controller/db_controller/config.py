import os.path
from configparser import ConfigParser

def config(filename='./conf/config.ini', section='postgres'):

    parser = ConfigParser()
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]

    else:
        print("Problem mit der config.ini")

    return db

def mongo_config(filename='config.ini', section='mongo'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]

    else:
        print("Problem mit der config.ini")
        
    return db