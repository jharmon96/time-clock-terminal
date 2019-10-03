import mysql.connector

cnx = mysql.connector.connect(user='jack', password='welcome',
                              host='127.0.0.1',
                              database='time')
print("Connected..")

mycursor = cnx.cursor()

# employee
def insertRowE(table, staff_number, fname, lname):

    sql = "INSERT INTO {} (staff_number, fname, lname) VALUES (%s, %s, %s)"
    val = (staff_number, fname, lname)
    mycursor.execute(sql.format(table), val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")

# timeLog
def insertRowT(table, staff_number, timestamp, direction):

    sql = "INSERT INTO {} (staff_number, timestamp, direction) VALUES (%s, %s, %s)"
    val = (staff_number, timestamp, direction)
    mycursor.execute(sql.format(table), val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")


def quit():
    cnx.close()
