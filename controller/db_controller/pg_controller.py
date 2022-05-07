import json

import psycopg2
import controller.db_controller.config as config

def connect(query):
    conn = None
    try:
        params = config.pg_config()
        #Connect to PGSQL
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute(query)
        result = cur.fetchall()

        cur.close
    except ValueError:
        return "Error"
    finally:
        if conn is not None:
            conn.close()
            return result
            #DB closed

def create(json_string):
    #json_string = json.load(json_string)
    table = ""
    query = []
    for key, value in json_string.items():
        if key == "table":
            table = value
        elif key == "query":
            query = value

    query = ", ".join( repr(e) for e in query )

    query_request = "INSERT INTO hr." + table + " VALUES ('" + query + "');"
    #print(query_request)

    connect(query_request)

def read(json_string):
    table = ""
    query = []
    where = []

    for key, value in json_string.items():
        if key == "table":
            table = value
        elif key == "query":
            query = value
        elif key == "where":
            where = value

    #query = ", ".join( repr(e) for e in query )
    #where = ", ".join( repr(e) for e in where )

    #print(where)

    #operator = where[0]
    #filter = where[1]

    if where:

        query_request = "SELECT " + query + " FROM hr." + table + " WHERE "

        multipleRows = False

        for row in where:
            for key, value in row.items():
                #job_title
                #print(key)

                #['>', '2']
                #print(value)

                if not multipleRows:
                    query_request = query_request + key + " " + value[0] + " " + value[1]
                    multipleRows = True
                else:
                    query_request = query_request + " AND " + key + " " + value[0] + " " + value[1]

    else:
        query_request = "SELECT " + query + " FROM hr." + table

    return connect(query_request)

def update(json_string):
    table = ""
    query = []
    where = []

    for key, value in json_string.items():
        if key == "table":
            table = value
        elif key == "query":
            query = value
        elif key == "where":
            where = value

    #@TODO: query irgendwie richtig machen
    query = ", ".join( repr(e) for e in query )
    #where = ", ".join( repr(e) for e in where )

    #print(where)

    #operator = where[0]
    #filter = where[1]

    if where:

        query_request = "UPDATE hr." + table + " SET (" + query + "') WHERE "

        multipleRows = False

        for row in where:
            for key, value in row.items():
                #job_title
                #print(key)

                #['>', '2']
                #print(value)

                if not multipleRows:
                    query_request = query_request + key + " " + value[0] + " " + value[1]
                    multipleRows = True
                else:
                    query_request = query_request + " AND " + key + " " + value[0] + " " + value[1]

    else:
        query_request = "UPDATE hr." + table + " SET ('" + query + "');"

    return connect(query_request)

def delete(json_string):
    table = ""
    where = []

    for key, value in json_string.items():
        if key == "table":
            table = value
        elif key == "where":
            where = value

    if where:

        query_request = "DELETE FROM hr." + table + " WHERE "

        multipleRows = False

        for row in where:
            for key, value in row.items():
                #job_title
                #print(key)

                #['>', '2']
                #print(value)

                if not multipleRows:
                    query_request = query_request + key + " " + value[0] + " " + value[1]
                    multipleRows = True
                else:
                    query_request = query_request + " AND " + key + " " + value[0] + " " + value[1]

    else:
        query_request = "DELETE FROM hr." + table + ";"

    return connect(query_request)