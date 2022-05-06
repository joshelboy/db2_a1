from http import client
from pymongo import MongoClient, InsertOne
import json

client = MongoClient("mongodb://localhost:27017")

db = client["DB2-B1"]
users = db["user"]

def createMongoCollections(data):
    createEmployeeTableMongoDB(data)
    createLocationsTableMongoDB(data)
    createJobsTableMongoDB(data)
    createDepartmentsTableMongoDB(data)
    createjobHistoryTableMongoDB(data)

def createEmployeeTableMongoDB(data):
    jsonFile = open('Schema/MongoDB/employee.json')
    db.createCollection( "employees", jsonFile )
    collection = db["employees"]
    collection.bulk_write(data)

def createLocationsTableMongoDB(data):
    jsonFile = open('Schema/MongoDB/locations.json')
    db.createCollection( "locations", jsonFile )
    collection = db["locations"]
    collection.bulk_write(data)

def createJobsTableMongoDB(data):
    jsonFile = open('Schema/MongoDB/jobs.json')
    db.createCollection( "jobs", jsonFile )
    collection = db["jobs"]
    collection.bulk_write(data)

def createDepartmentsTableMongoDB(data):
    jsonFile = open('Schema/MongoDB/departments.json')
    db.createCollection( "departments", jsonFile )
    collection = db["departments"]
    collection.bulk_write(data)

def createjobHistoryTableMongoDB(data):
    jsonFile = open('Schema/MongoDB/job_history.json')
    db.createCollection( "job_history", jsonFile )
    collection = db["job_history"]
    collection.bulk_write(data)

