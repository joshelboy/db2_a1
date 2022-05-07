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

def createRedis():
    r = redis.Redis(
        host = "localhost",
        port = 6379)

    r.set()

    print("create")

def readRedis():
    r = redis.Redis(
        host = "localhost",
        port = 6379)
    print("read")

def updateRedis():
    r = redis.Redis(
        host = "localhost",
        port = 6379)
    print("update")

def deleteRedis():
    r = redis.Redis(
        host = "localhost",
        port = 6379)
    print("delete")