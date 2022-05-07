import psycopg2
import config

def connect(query):
    conn = None
    try:
        params = config.config()
        #Connect to PGSQL
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        try:
            cur.execute('CREATE SCHEMA hr')
        except:
            print("Schema may already exists")

        fileCreate = open("./schema/hr_create.sql", "r")
        filePopulate = open("./schema/hr_populate.sql", "r")
        fileComment = open("./schema/hr_comment.sql", "r")

        try:
            cur.execute(fileCreate)
        except:
            print("File may already exists")

        try:
            cur.execute(filePopulate)
        except:
            print("File may already filled")

        try:
            cur.execute(fileComment)
        except:
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

            locations_file = open('../Schema/PostgreSQL/locations.json')
            locations_file.write(locations)
            locations_file.close()

            departments_file = open('../Schema/PostgreSQL/departments.json')
            departments_file.write(departments)
            departments_file.close()

            countries_file = open('../Schema/PostgreSQL/countries.json')
            countries_file.write(departments)
            countries_file.close()

            regions_file = open('../Schema/PostgreSQL/regions.json')
            regions_file.write(departments)
            regions_file.close()

            job_history_file = open('../Schema/PostgreSQL/job_history.json')
            job_history_file.write(departments)
            job_history_file.close()

            job_file = open('../Schema/PostgreSQL/job.json')
            job_file.write(departments)
            job_file.close()

            employees_file = open('../Schema/PostgreSQL/employees.json')
            employees_file.write(departments)
            employees_file.close()

        except:
            print("JSON fetch failed")

        cur.close
    except:
        return "Error"
    finally:
        if conn is not None:
            conn.close()
            #DB closed