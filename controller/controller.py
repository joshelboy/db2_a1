#Splitted JSON string auf
#1. An welchen soll es gehen?
#2. Methode aus passendem Controller ausführen
#3. return an main.py übergeben
import json
#import controller.db_controller.mongo_controller as mongo
import controller.db_controller.pg_controller as pg
import controller.db_controller.mongo_controller as mg

def manageMongo(content):

    print(content)
    for key, value in content:
        if key == "params":
            for subkey, subvalue in value.items():
                if subkey == "mode":

                    if subvalue == "c":
                        for transmitKey, transmitValue in value.items():
                            if transmitKey == "values":
                                mg.createMongoDB(transmitValue)
                                # print(transmitValue)

                    if subvalue == "r":
                        for transmitKey, transmitValue in value.items():
                            if transmitKey == "values":
                                mg.readMongoDB(transmitValue)
                                # print(transmitValue)

                    if subvalue == "u":
                        for transmitKey, transmitValue in value.items():
                            if transmitKey == "values":
                                mg.updateMongoDB(transmitValue)
                                # print(transmitValue)

                    if subvalue == "d":
                        for transmitKey, transmitValue in value.items():
                            if transmitKey == "values":
                                mg.deleteMongoDB(transmitValue)
                                # print(transmitValue)



def managePG(content):
    for key, value in content:
        if key == "params":
            for subkey, subvalue in value.items():
                if subkey == "mode":

                    if subvalue == "c":
                        for transmitKey, transmitValue in value.items():
                            if transmitKey == "values":
                                pg.create(transmitValue)
                                #print(transmitValue)

                    if subvalue == "r":
                        for transmitKey, transmitValue in value.items():
                            if transmitKey == "values":
                                pg.read(transmitValue)
                                #print(transmitValue)

                    if subvalue == "u":
                        for transmitKey, transmitValue in value.items():
                            if transmitKey == "values":
                                pg.update(transmitValue)
                                #print(transmitValue)

                    if subvalue == "d":
                        for transmitKey, transmitValue in value.items():
                            if transmitKey == "values":
                                pg.delete(transmitValue)
                                #print(transmitValue)

def recieveInput(input):
    data = json.loads(input)

    for key, value in data.items():
        if key == "dbs":
            if value == "1":
                managePG(data.items())
            elif value == "3":
                manageMongo(data.items())