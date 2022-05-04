# main -> controller -> db_controller

ask_for_dbs = True
crud_choice = ""
dbs_choice = ""

while (True):
    if(ask_for_dbs):
        print("Zur Auswahl stehen:")
        print("1: Relationales Datenbanksystem (PostgreSQL)")
        print("2: Key-Value-System (Redis)")
        print("3: Dokumentenspeicher (MongoDB)")

        dbs_choice = input("Gewähltes DBS: ")
        ask_for_dbs = False

    print("Gewähltes DBS: ")
    print("Zur Auswahl stehen:")
    print("1: Create")
    print("2: Read")
    print("3: Update")
    print("4: Delete")
    print("5: Anderes DBS")

    crud_choice = input("Auswahl: ")