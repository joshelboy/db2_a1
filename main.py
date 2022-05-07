# main -> controller -> db_controller
import json
from controller import controller
from controller.db_controller import config
from controller import json_writer

ask_for_dbs = True
crud_choice = ""
dbs_choice = ""

json_writer.connect()

def getOverview():
    jsonFile = open('Schema/main/main.json')
    data = json.load(jsonFile)

    return data.items()


def getTable(tablename):
    returnOverview = getOverview()
    for key, value in returnOverview:
        if (tablename == key):
            return value.items()

while (True):
    if(ask_for_dbs):
        print("Zur Auswahl stehen:")
        print("1: Relationales Datenbanksystem (PostgreSQL)")
        print("2: Key-Value-System (Redis)")
        print("3: Dokumentenspeicher (MongoDB)")

        dbs_choice = input("Gewähltes DBS: ")
        ask_for_dbs = False

    print("Zur Auswahl stehen:")
    print("1: Create")
    print("2: Read")
    print("3: Update")
    print("4: Delete")
    print("5: Anderes DBS")

    crud_choice = input("Auswahl: ")

    if crud_choice == "1":
        returnOverview = getOverview()

        for key, value in returnOverview:
            print(key)

        c_table = input("Welche Tabelle (name): ")
        returnTable = getTable(c_table)

        print("Welche Werte sollen hinzugefügt werden?: ")

        values = []

        for key, value in returnTable:

            id = False

            for subkey, subvalue in value.items():
                if subkey == "key" and subvalue == "id":
                    id = True

            if not id:
                value = input("Für " + key + ": ")
                values.append({ key: value })

        valueStack = {
            "table": c_table,
            "query": values
        }

        string = {
            "mode": "c",
            "values": valueStack
        }
        dbs = {
            "dbs": dbs_choice,
            "params": string
        }
        controller.recieveInput(json.dumps(dbs))

    elif crud_choice == "2":

        returnOverview = getOverview()

        print("+++++++++++++++++++")
        print("Alle Tabellen:")
        print()

        for key, value in returnOverview:
            print(key)

        print()

        r_table = input("Welche Tabelle (name): ")
        returnTable = getTable(r_table)

        print("Alle Spalten in " + r_table + ": ")
        print()

        for key, value in returnTable:
            print(key)

        print()

        print("[Bitte mit ',' trennen. z.B job, titel, name oder *]")
        values = input("Was soll selektiert werden?: ")

        print()
        print("Sollen Filter hinzugefügt werden?")
        print()

        where = []

        for key, value in returnTable:

            choice = input("Soll nach " + key + " gefiltert werden? [j/n]")

            if choice == "j" or choice == "y":

                operator = input("Welcher Operator soll genutzt werden? (<,>,=...): ")
                filter = input("Mit was soll " + key + " verglichen werden?: ")
                where.append({ key: [operator, filter] })

        print()

        valueStack = {
            "table": r_table,
            "query": values,
            "where": where
        }

        string = {
            "mode": "r",
            "values": valueStack
        }
        dbs = {
            "dbs": dbs_choice,
            "params": string
        }
        controller.recieveInput(json.dumps(dbs))

    elif crud_choice == "3":
        returnOverview = getOverview()

        print("+++++++++++++++++++")
        print("Alle Tabellen:")
        print()

        for key, value in returnOverview:
            print(key)

        print()

        u_table = input("Welche Tabelle (name): ")
        returnTable = getTable(u_table)

        print("Welche Spalten in " + u_table + " sollen geändert werden? ")
        print()

        values = []

        for key, value in returnTable:

            choice = input("Soll " + key + " geändert werden? [j/n]")

            if choice == "j" or choice == "y":

                change = input("Zu was soll " + key + " geändert werden?: ")
                values.append({ key: change })

        print()

        print()
        print("Sollen Filter hinzugefügt werden?")
        print()

        where = []

        for key, value in returnTable:

            choice = input("Soll nach " + key + " gefiltert werden? [j/n]")

            if choice == "j" or choice == "y":

                operator = input("Welcher Operator soll genutzt werden? (<,>,=...): ")
                filter = input("Mit was soll " + key + " verglichen werden?: ")
                where.append({ key: [operator, filter] })

        print()

        valueStack = {
            "table": u_table,
            "query": values,
            "where": where
        }

        string = {
            "mode": "u",
            "values": valueStack
        }
        dbs = {
            "dbs": dbs_choice,
            "params": string
        }
        controller.recieveInput(json.dumps(dbs))

    elif crud_choice == "4":
        returnOverview = getOverview()

        print("+++++++++++++++++++")
        print("Alle Tabellen:")
        print()

        for key, value in returnOverview:
            print(key)

        print()

        d_table = input("Welche Tabelle (name): ")
        returnTable = getTable(d_table)

        print()
        print("Sollen Filter hinzugefügt werden?")
        print()

        where = []

        for key, value in returnTable:

            choice = input("Soll nach " + key + " gefiltert werden? [j/n]")

            if choice == "j" or choice == "y":

                operator = input("Welcher Operator soll genutzt werden? (<,>,=...): ")
                filter = input("Mit was soll " + key + " verglichen werden?: ")
                where.append({ key: [operator, filter] })

        print()


        valueStack = {
            "table": d_table,
            "where": where
        }

        string = {
            "mode": "d",
            "values": valueStack
        }
        dbs = {
            "dbs": dbs_choice,
            "params": string
        }
        controller.recieveInput(json.dumps(dbs))

    elif crud_choice == "5":
        ask_for_dbs = True