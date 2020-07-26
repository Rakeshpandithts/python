import daemon
import time
import psycopg2

def do_something():
    conn = psycopg2.connect(database = "medilenzcrmdb", user = "postgres", password = "rakesh", host = "127.0.0.1", port = "5432")
    # conn = psycopg2.connect(database = "medilenz", user = "medilenz123", password = "medilenz#321", host = "127.0.0.1", port = "5432")
    case_id = 'M_345'
    case_name = 'rakesh_pandith'
    email = 'rakesh.pandith.ts@gmail.com'
    phone = '9481476752'
    attorney_name = 'mbridge'
    contact_person = 'pandith'
    firm_name = 'mbridge_firm'
    # status = 'uploaded'
    with open("C:/Users/rakes/current_time.test", "w") as f:
            f.write( time.ctime()+str(conn)+"The time is now \n" )
            f.close()

    while True:
        with open("C:/Users/rakes/current_test.txt", "w") as f:
            f.write( time.ctime()+str(conn)+"The time is now while1 \n" )
            f.close()
        cur = conn.cursor()
        result = cur.execute('''INSERT INTO case_tracker.case_main(case_id, case_name, email, phone, attorney_name,contact_person,firm_name) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');'''.format(case_id, case_name, email, phone, attorney_name, contact_person, firm_name))
        conn.commit()   
        time.sleep(5)
        with open("C:/Users/rakes/current_test.txt", "w") as f:
            f.write( time.ctime()+str(result) +"The time is now \n")
            f.close()

def run():
    with daemon.DaemonContext():
        do_something()

if __name__ == "__main__":
    run()
