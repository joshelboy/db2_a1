import psycopg2
import controller.db_controller.config as config
import controller.db_controller.converter as mongo

def connect():
    conn = None
    try:
        params = config.config()
        #Connect to PGSQL
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        #try:
        #    cur.execute('CREATE SCHEMA hr')
        #except:
        #    print("Schema may already exists")

        fileCreate = open("./Schema/main/hr_create.sql", "r")
        filePopulate = open("./Schema/main/hr_populate.sql", "r")
        fileComment = open("./Schema/main/hr_comment.sql", "r")

        try:
            cur.execute(fileCreate.read())
        except:
            conn.rollback()
            print("File may already exists")

        try:
            cur.execute(filePopulate.read())
        except:
            conn.rollback()
            print("File may already filled")

        try:
            cur.execute(fileComment.read())
        except:
            conn.rollback()
            print("File couldnt be commented")
        #db_version = cur.fetchone()

        try:
            cur.execute('SELECT json_agg(e) FROM(SELECT * FROM hr.locations) e;')
            locations = cur.fetchall()

            cur.execute('SELECT json_agg(e) FROM(SELECT * FROM hr.departments) e;')
            departments = cur.fetchall()

            cur.execute('SELECT json_agg(e) FROM(SELECT * FROM hr.employees) e;')
            employees = cur.fetchall()

            cur.execute('SELECT json_agg(e) FROM(SELECT * FROM hr.job_history) e;')
            job_history = cur.fetchall()

            cur.execute('SELECT json_agg(e) FROM(SELECT * FROM hr.jobs) e;')
            jobs = cur.fetchall()

            cur.execute('SELECT json_agg(e) FROM(SELECT * FROM hr.countries) e;')
            countries = cur.fetchall()

            cur.execute('SELECT json_agg(e) FROM(SELECT * FROM hr.regions) e;')
            regions = cur.fetchall()

            mongo.createDepartmentsTableMongoDB(str(departments[0]))
            mongo.createEmployeeTableMongoDB(str(employees[0]))
            mongo.createJobsTableMongoDB(str(jobs[0]))
            mongo.createjobHistoryTableMongoDB(str(job_history[0]))
            mongo.createLocationsTableMongoDB(str(locations[0]))



        except:
            print("JSON fetch failed")

        try:
            cur.execute("ALTER ROLE postgres SET search_path TO hr;")
        except:
            print("Search path was not set")

        cur.close
    except ValueError:
        return "Error"
    finally:
        if conn is not None:
            conn.close()
            #DB closed