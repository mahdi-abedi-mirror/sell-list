# Hello my name is Mahdi-Abedi
# this project for save sell order in sqlite3 

import sqlite3      #import sqlite3 library
from sqlite3 import Error
from time import sleep

def sql_connection():       # Tese connect or created database

    try:

        con = sqlite3.connect('order.db')

        print("Connection is established")

    except Error:

        print(Error)

    finally:

        con.close()

sql_connection()
sleep(5)
con = sqlite3.connect('order.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
    Id INT PRIMARY KEY,
    fname TEXT,
    lname TEXT,
    date TEXT,
    total INT);
""")
con.commit()





con.close()