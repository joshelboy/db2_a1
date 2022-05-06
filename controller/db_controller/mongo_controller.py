from http import client
from pymongo import MongoClient, InsertOne
import json

client = MongoClient("mongodb://localhost:27017")

db = client["DB2-B1"]
users = db["user"]
collection = db["employees"]

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

    return data

def updateMongoDB(content):
    newData = {}
    newDataToInsert = {} 
    oldData = {}
    valueToSearch = {}
    for key, value in updatedata.items():
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