#Splitted JSON string auf
#1. An welchen soll es gehen?
#2. Methode aus passendem Controller ausführen
#3. return an main.py übergeben
import json
import controller.db_controller.mongo_controller as mongo

def manageMongo(content):

    for key, value in content:
        if key == "params":
            for subkey, subvalue in value.items():
                if subkey == "mode":

                    if subvalue == "c":
                        for transmitKey, transmitValue in value.items():
                            if transmitKey == "values":
                                #mongo.insert(transmitValue)
                                print(transmitValue)

                    if subvalue == "r":
                        for transmitKey, transmitValue in value.items():
                            if transmitKey == "values":
                                #mongo.insert(transmitValue)
                                print(transmitValue)

                    if subvalue == "u":
                        for transmitKey, transmitValue in value.items():
                            if transmitKey == "values":
                                #mongo.insert(transmitValue)
                                print(transmitValue)

                    if subvalue == "d":
                        for transmitKey, transmitValue in value.items():
                            if transmitKey == "values":
                                #mongo.insert(transmitValue)
                                print(transmitValue)



def managePG(content):
    print("Postgres")

def recieveInput(input):
    data = json.loads(input)

    for key, value in data.items():
        if key == "dbs":
            if value == "1":
                managePG(value)
            elif value == "3":
                manageMongo(data.items())