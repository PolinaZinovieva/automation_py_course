import psycopg2

connection = psycopg2.connect(user ='postgres', host='localhost', password ='1',port ='5432',database='postgres')
cursor = connection.cursor()
cursor.execute('SELECT * FROM users;')
# print(cursor.fetchone())
for row in cursor.fetchall():
    print(row)
cursor.close()
if connection:
    connection.close()
