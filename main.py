# Hello my name is Mahdi-Abedi
# this project for save sell order in sqlite3 

import sqlite3      #import sqlite3 library
from sqlite3 import Error
from os import system, name

def osclear():
   # for windows
   if name == 'nt':
        system('cls')

   # for mac and linux
   else:
        system('clear')

con = sqlite3.connect('order.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY UNIQUE,
    fname TEXT,
    lname TEXT ,
    date TEXT,
    total INT);
""")
con.commit()

class menu(object):

    def one(self):

        cur.execute("SELECT id FROM orders")
        last_id=cur.fetchall()
        print(" Last registered ID = ",last_id[-1])
        Id=input("Please Enter Id for new order : ")
        fname=input("Please Enter First Name Customer : ")
        lname=input("Please Enter Last Name Customer : ")
        date_sell=input("Please Enter Date Ordered : ")
        total=input("Please Enter Total Order Amount : ")
        data_for_db=(Id,fname,lname,date_sell,total)
        cur.execute("INSERT INTO orders VALUES(?,?,?,?,?)",data_for_db)
        con.commit()

    def two(self):
        
        cur.execute("SELECT * FROM orders")
        rows = cur.fetchall()
        print("id | fname | lname | date-order | order-Amont |")
        for row in rows:
            print(row,"\n")

    def three(self):
        
        sh_id=int(input("Please Enter Id : "))
        cur.execute("SELECT * FROM orders WHERE id = %i"%sh_id)
        print(cur.fetchall())

    def four(self):
        
        del_id=int(input("Please Enter Id For Delete : "))
        cur.execute("DELETE FROM orders WHERE id = %i"%del_id)
        con.commit()
        print("Deleted!!!")

    def five(self):
        total_list=[]
        total_answer=0
        cur.execute("SELECT total FROM orders")
        rows = cur.fetchall()
        for row in rows:
            total_list.append(row[0])
        for i in range(len(total_list)):
            total_answer += total_list[i]
        print("your total sell = %i"%total_answer)

    def six(self):
        print("*"*10,"GoodBy","*"*10)


def chooser():
    print("*"*30," S E L L - L I S T ","*"*30)
    print("*"*30," M A I N - M E N U ","*"*30)
    print("*"*10," please choose ","*"*10)
    print(""" 
    1 . Add Order \t 2 . Show All Orders \n 
    3 . Show By Id \t 4 . Delet By Id \n
    5 . Total Sell \t 6 . Exite \n""")
    choose=input("please enter your choose : ")
    if choose == "1":
        menu().one()
    elif choose == "2":
        menu().two()
    elif choose == "3":
        menu().three()
    elif choose == "4":
        menu().four()
    elif choose == "5":
        menu().five()
    elif choose == "6":
        menu().six()
    else:
        print("your choose invalid")

loop=True
osclear()
chooser()
while loop:
    endornot = input("are you want closed !!! answer By y or n : ")
    if endornot == "n" :
        osclear()
        chooser()
    elif endornot =="y":
        print("*"*10,"GoodBy","*"*10)
        loop=False
    else :
        print("your choose invalid")


con.close()