#!/usr/bin/env python
import time
from datetime import datetime
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import Main

reader = SimpleMFRC522()

signInTxt = ''

# While reading card
while True:
    try:
        id, text = reader.read()
        # print(id)

        # Return the last time this user scanned in or out
        sql = "SELECT a.direction FROM timeLog a LEFT OUTER JOIN timeLog b " \
        "ON a.staff_number = b.staff_number AND a.id < b.id " \
        "WHERE b.staff_number IS NULL AND a.staff_number = {};"
        try:
            Main.mycursor.execute(sql.format(text.strip()))
            myresult = list(Main.mycursor.fetchall())
        except:
            print("Could not find entry for {}".format(text.strip()))
            time.sleep(1)
            continue

        # Determin whether they signed in or out last and update current direction
        # accordingly.
        for i in myresult:
            if i[0] == "in":
                signInTxt = 'out'
            else:
                signInTxt = 'in'

        clockin = str(datetime.now())
        print("Welcome {}, you have signed {} at {}".format(text.strip(), signInTxt, clockin))
        Main.insertRowT('timeLog', text.strip(), clockin, signInTxt)
        time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
        Main.quit()
    finally:
        pass
GPIO.cleanup()
