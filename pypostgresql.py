import psycopg2

conn = psycopg2.connect(database = "medilenz", user = "medilenz123", password = "medilenz#321", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")

print(conn)

cur = conn.cursor()
cur.execute('''SELECT * FROM case_main;''')

fetch_data = cur.fetchall()
print(fetch_data)


# cur.execute('''CREATE TABLE company (ID INT, NAME TEXT, AGE INT, ADDRESS char(50));''')
# conn.commit()
# print('table created')
# sql = ''
last_read_mail = 7715
# result = cur.execute('''INSERT INTO case_tracker.code_config(last_read_mail_id) VALUES ({});'''.format(last_read_mail))

# SELECT * FROM table ORDER BY datetime DESC LIMIT 10
# cursor.execute('''SELECT * FROM case_tracker.code_config WHERE ROWID IN ( SELECT max( ROWID ) FROM case_tracker.case_main )'''.format(table_name, table_name))
# cur.execute('''SELECT last_read_mail_id FROM case_tracker.code_config ORDER BY last_read_mail_id DESC LIMIT 1;''')

# last_read_mail = cur.fetchall()
# # print(result)
# print('table value')
# print(last_read_mail)
# print(type(last_read_mail[0]))
# print(last_read_mail[0][0])
# print(type(last_read_mail[0][0]))



# cur.execute("SELECT ID, NAME, AGE, ADDRESS from company")

# rows = cur.fetchall()
# print(rows)

# cur.execute('SELECT LASTVAL()')
# lastid = cur.fetchone()['name']

# print(lastid)
case_id = 'M_345'
case_name = 'rakesh_pandith'
email = 'rakesh.pandith.ts@gmail.com'
phone = '9481476752'
attorney_name = 'mbridge'
contact_person = 'pandith'
firm_name = 'mbridge_firm'
status = 'uploaded'

# result = cur.execute('''INSERT INTO case_tracker.case_main(case_id, case_name, email, phone, attorney_name,contact_person,firm_name) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');'''.format(case_id, case_name, email, phone, attorney_name, contact_person, firm_name))
# conn.commit()

# result1 = cur.execute('''INSERT INTO case_tracker.code_config(last_read_mail_id) VALUES ({});'''.format(last_read_mail))
# conn.commit()


result1 = cur.execute('''INSERT INTO case_tracker.case_status(status, case_id) VALUES ('{}', '{}') returning *;'''.format(status, case_id))
conn.commit()


# print(result)
print(result1)


conn.close()