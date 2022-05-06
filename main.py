# main -> controller -> db_controller
import json
from controller import controller

ask_for_dbs = True
crud_choice = ""
dbs_choice = ""

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

        string = {
            "mode": "c",
            "table": c_table,
            "values": values
        }
        dbs = {
            "dbs": dbs_choice,
            "operation": string
        }
        controller.recieveInput(dbs)

    elif crud_choice == "2":
        print("")

    elif crud_choice == "3":
        print("")

    elif crud_choice == "4":
        print("")

    elif crud_choice == "5":
        ask_for_dbs = True