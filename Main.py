import mysql.connector

cnx = mysql.connector.connect(user='jack', password='welcome',
                              host='127.0.0.1',
                              database='time')
print("Connected..")

mycursor = cnx.cursor()

def createTable():

    sql_command = "CREATE TABLE timeLog (key INTEGER PRIMARY KEY, staff_number INTEGER," \
    " timestamp DATETIME, direction CHAR(10))"

    mycursor.execute(sql_command)

    print("Updated")

def createTable2():
    sql_command = "CREATE TABLE timeLog (" \
    "id INTEGER," \
    "staff_number INTEGER," \
    "INDEX par_ind (staff_number)," \
    "FOREIGN KEY (staff_number)" \
    "REFERENCES employee(staff_number)" \
    "ON DELETE CASCADE)"

    mycursor.execute(sql_command)

    print("Updated")

# employee
def insertRowE(table, staff_number, fname, lname, timestamp, direction):

    sql = "INSERT INTO {} (staff_number, fname, lname, timestamp, direction) VALUES (%s, %s, %s, %s, %s)"
    val = (staff_number, fname, lname, timestamp, direction)
    mycursor.execute(sql.format(table), val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")

# timeLog
def insertRowT(table, staff_number, timestamp, direction):

    sql = "INSERT INTO {} (staff_number, timestamp, direction) VALUES (%s, %s, %s)"
    val = (staff_number, timestamp, direction)
    mycursor.execute(sql.format(table), val)
    cnx.commit()
    # print(mycursor.rowcount, "record inserted.")


def quit():
    cnx.close()

#createTable2()
#insertRow("employee", "26", "Jack", "Harmon", "2019-10-02 18:03:30", "in")
#insertRowT("timeLog", "25", "2019-10-02 18:10:30", "out")
#quit()
