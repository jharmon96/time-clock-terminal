import csv
import Main
from datetime import datetime
import pprint
import schedule
import time
from shutil import copyfile

pp = pprint.PrettyPrinter(indent=4)

# Create a file that contains total hours worked for the day by employee
def createFile():
    sql = "SELECT staff_number, DATE(timestamp) AS date, "\
                "SUM(UNIX_TIMESTAMP(timestamp)*(1-2*BooleanOutput))/3600 AS hours_worked "\
            "FROM(" \
                "SELECT t.staff_number, t.timestamp, " \
                        "CASE WHEN t.direction = 'in' THEN 1 ELSE 0 END BooleanOutput " \
                "FROM timeLog t " \
                "WHERE t.timestamp >= '2019-10-02' "\
                "ORDER BY t.staff_number, t.timestamp, t.direction) AS timetoday " \
            "GROUP BY staff_number"

    Main.mycursor.execute(sql)
    rows = Main.mycursor.fetchall()

    pp.pprint(rows)

    with open('tmp/hours_worked.csv', 'w', newline= '') as f:
        a = csv.writer(f, delimiter=',')
        a.writerow(["staff_number", "date", "hours_worked"])  ## etc
        a.writerows(rows)  ## closing paren added
        print("Export created")
    copyfile('tmp/hours_worked.csv', 'tmp/hours_worked_{}.csv'.format(datetime.now()))

schedule.every().day.at("21:23").do(createFile)

while True:
    schedule.run_pending()
    time.sleep(1)
