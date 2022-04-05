# Hello my name is Mahdi-Abedi
# this project for save sell order in sqlite3 

import sqlite3      #import sqlite3 library
from sqlite3 import Error

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
star="*"*30



def sql_connection():       # Tese connect or created database

    try:

        con = sqlite3.connect('order.db')

        print("Connection is established")

    except Error:

        print(Error)

    finally:

        con.close()


class menu(object):
    def one(self):
        pass
    def two(self):
        return print("two")
    def three(self):
        pass
    def four(self):
        pass
    def five(self):
        pass
    def six(self):
        print("*"*10,"GoodBy","*"*10)
def chooser():
    print(star," S E L L - L I S T ",star)
    print(star," M A I N - M E N U ",star)
    print("*"*10," please choise ","*"*10)
    print(""" 
    1 . Add Order \t 2 . Show All Orders \n 
    3 . Show By Id \t 4 . Delet By Id \n
    5 . Total Sell \t 6 . Exite \n""")
    choose=input("please enter your choose : ")
    if choose == 1:
        menu().one()
    elif choose == 2:
        menu().two()
    elif choose == 3:
        menu().three()
    elif choose == 4:
        menu().four()
    elif choose == 5:
        menu().five()
    elif choose == 6:
        menu().six()
    else:
        print("your choose invalid")

loop=True
chooser()
while loop:
    endornot = input("are you want closed !!! answer By y or n : ")
    if endornot == "n" :
        chooser()
    elif endornot =="y":
        loop=False
    else :
        print("your choose invalid")


con.close()