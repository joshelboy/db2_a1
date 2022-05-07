from http import client
from pymongo import MongoClient, InsertOne
import json
import config

def createMongoDB(content):

    params = config.mongo_config()
    client = MongoClient("mongodb://" + params["host"])
    db = client[params["host"]]
    
    datensatz = {}
    for key, value in content:
        if key == "table":
            collection = db[value]
        elif key == "query":
            for subkey, subvalue in value.items():
                datensatz[subkey] = subvalue
    
    collection.insert_one(datensatz)

def readMongoDB(content):

    params = config.mongo_config()
    client = MongoClient("mongodb://" + params["host"])
    db = client[params["host"]]

    dataToFind = {}
    valueToSearch = {}
    for key, value in content.items():
        if key == "table":
            collection = db[value]
        elif key == "where":
            for subkey, subvalue in value.items():
                if subvalue[0] == "=":
                    dataToFind[subkey] = subvalue[1]
                elif subvalue[0] == "<":
                    valueToSearch["$lt"] = subvalue[1]
                    dataToFind[subkey] = valueToSearch
                elif subvalue[0] == ">":
                    valueToSearch["$gt"] = subvalue[1]
                    dataToFind[subkey] = valueToSearch
    
    data = collection.find(dataToFind)

    print(data)

def updateMongoDB(content):

    params = config.mongo_config()
    client = MongoClient("mongodb://" + params["host"])
    db = client[params["host"]]

    newData = {}
    newDataToInsert = {} 
    oldData = {}
    valueToSearch = {}
    for key, value in content.items():
        if key == "table":
            collection = db[value]
        elif key == "query":
            for subkey, subvalue in value.items():
                newData[subkey] = subvalue
        elif key == "where":
            for subkey, subvalue in value.items():
                if subvalue[0] == "=":
                    oldData[subkey] = subvalue[1]
                elif subvalue[0] == "<":
                    valueToSearch["$lt"] = subvalue[1]
                    oldData[subkey] = valueToSearch
                
                elif subvalue[0] == ">":
                    valueToSearch["$gt"] = subvalue[1]
                    oldData[subkey] = valueToSearch
    
    newDataToInsert["$set"] = newData
    collection.update_many(oldData, newData)

def deleteMongoDB(content):

    params = config.mongo_config()
    client = MongoClient("mongodb://" + params["host"])
    db = client[params["host"]]

    dataToDelete = {}
    dataToSearch = {}
    for key, value in content.items():
        if key == "table":
            collection = db[value]
        elif key == "where":
            for subkey, subvalue in value.items():
                if subvalue[0] == "=":
                    dataToDelete[subkey] = subvalue[1]
                elif subvalue[0] == "<":
                    dataToSearch["$lt"] = subvalue[1]
                    dataToDelete[subkey] = dataToSearch
                elif subvalue[0] == ">":
                    dataToSearch["$gt"] = subvalue[1]
                    dataToDelete[subkey] = dataToSearch
    
    collection.delete_many(dataToDelete)