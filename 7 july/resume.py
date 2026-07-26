import mysql.connector

def connection():
    conn = mysql.connector.connect(
    host  = "localhost",
    username = "root",
    password = "Sanskruti@22",
    database = "sms_linkcode"
)

print("db connected!")

