import sqlite3
from collections import namedtuple

Student = namedtuple("Student", ["name", "enroll", "fac", "number", "email"])

def generateStudent():
    detail = tuple(input("Enter the details in the Following order:\nname enrolment_number faculty_number mobile_number email_address\n").split(" "))
    newStudent = Student(*detail)
    return newStudent




print("Connecting to the RoboClub Database")
conn = sqlite3.connect("roboclub.db")

cursor = conn.cursor()
try:
    cursor.execute('''CREATE TABLE student
                   (name text, enrollment text, faculty text, number text, email text)
                   ''')
except:
    pass
test = Student("div", "gh00", "dsiv", "number", "gmail")
#print("{},{},{},{},{}".format(*test))
s = "INSERT INTO student VALUES({},{},{},{},{})".format(*test)
cursor.execute(s)