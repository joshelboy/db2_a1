import redis

def insertJsonToRedis(departments, employees, jobs, job_history, locations):
    r = redis.Redis(
        host = "localhost",
        port = 6379)
    

    r.set('departments', departments)
    r.set('employees', employees)
    r.set('jobs', jobs)
    r.set('job_history', job_history)
    r.set('locations', locations)

def createRedis(data):
    r = redis.Redis(
        host = "localhost",
        port = 6379)

    insertkey = ""
    datensatz = {}

    for key, value in data:
        if key == "table":
            insertkey = key
        elif key == "query":
            for subkey, subvalue in value.items():
                datensatz[subkey] = subvalue


        r.set(key, datensatz)

    print("create")

def readRedis(data):
    r = redis.Redis(
        host = "localhost",
        port = 6379)

    searchKey = ""
    datensatz = {}

    for key, value in data:
        if key == "table":
            searchKey = key
        if key == "query":
            for subkey, subvalue in value.items():
                for rediskey, redisvalue in r.scan_iter():
                    if sorted(rediskey.items()) == sorted(subkey.items()):
                        print(datensatz)

def updateRedis():
    r = redis.Redis(
        host = "localhost",
        port = 6379)
    print("update")

def deleteRedis(data):
    r = redis.Redis(
        host = "localhost",
        port = 6379)

    deleteKey = ""
    datensatz = {}

    for key, value in data:
        if key == "table":
            deleteKey = key
        if key == "query":
            for subkey, subvalue in value.items():
                for rediskey, redisvalue in r.scan_iter():
                    if sorted(rediskey.items()) == sorted(subkey.items()):
                        print(datensatz)
                        r.delete(key)