import redis

def insertJsonToRedis():
    r = redis.Redis(
        host = "localhost",
        port = 6379)
    print("insert")

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