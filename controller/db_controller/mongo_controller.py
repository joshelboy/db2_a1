from http import client
from pymongo import MongoClient, InsertOne
import json

client = MongoClient("mongodb://localhost:27017")

db = client["DB2-B1"]
users = db["user"]
collection = db[""]

def createMongoDB(content):
    
    datensatz = {}
    for key, value in content:
        if key == "table":
            collection = db[value]
        elif key == "query":
            for subkey, subvalue in value.items():
                datensatz[subkey] = subvalue
    
    collection.insert_one(datensatz)

def readMongoDB(content):
    dataToDelete = {}
    dataToSearch = {}
    for key, value in content:
        if key == "table":
            collection = db[value]
        elif key == "query":
            for subkey, subvalue in value.items():
                for subsubkey, subsubvalue in value.items():
                    if(subsubkey) == "=":
                        dataToDelete[subkey] = subsubvalue
                    elif(subsubkey) == "<":
                        dataToSearch["$lt"] = subsubvalue
                        dataToDelete[subkey] = dataToSearch
                    elif(subsubkey) == ">":
                        dataToSearch["$gt"] = subsubvalue
                        dataToDelete[subkey] = dataToSearch
    
    data = collection.find(dataToDelete)

    return data

def updateMongoDB(content):
    newData = {}
    oldData = {}
    for key, value in content:
        if key == "table":
            collection = db[value]
        elif key == "query":
            for subkey, subvalue in value.items():
                newData["$set"][subkey] = subvalue
        elif key == "where":
            for subkey, subvalue in value.items():
                oldData[subkey] = subvalue
  
    collection.update_one(oldData, newData)

def deleteMongoDB(content):
    dataToDelete = {}
    dataToSearch = {}
    for key, value in content:
        if key == "table":
            collection = db[value]
        elif key == "query":
            for subkey, subvalue in value.items():
                for subsubkey, subsubvalue in value.items():
                    if(subsubkey) == "=":
                        dataToDelete[subkey] = subsubvalue
                    elif(subsubkey) == "<":
                        dataToSearch["$lt"] = subsubvalue
                        dataToDelete[subkey] = dataToSearch
                    elif(subsubkey) == ">":
                        dataToSearch["$gt"] = subsubvalue
                        dataToDelete[subkey] = dataToSearch
    
    collection.delete_many(dataToDelete)