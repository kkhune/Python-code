from tkinter import *
from tkinter import ttk
import sqlite3
root = Tk()
root.geometry('600x300')
root.title("Registration Form")

Fullname=StringVar()
Addresh=StringVar()
ID=StringVar()
var = StringVar()
c=StringVar()
d=IntVar()


def Add():
   conn=sqlite3.connect("Form.db")
   cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS FORM(Fullname TEXT,ID TEXT,Addresh TEXT,Gender TEXT,Department TEXT)')
   cursor.execute('INSERT INTO Form(FullName,ID,Addresh,Gender,Department) VALUES(:name1,:id1,:addresh,:gender,:dept)',
                  {
                     'name1':Fullname.get(),
                     'id1':ID.get(),
                     'addresh':Addresh.get(),
                     'dept':c.get(),
                     'gender':var.get(),
                  })
   
   conn.commit()
   conn.close()
   entry_1.delete(0, END)
   entry_2.delete(0, END)
   entry_5.delete(0, END)
   entry_6.delete(0,END)

def delete():
   conn=sqlite3.connect("Form.db")
   cursor=conn.cursor()
   cursor.execute("DELETE from FORM WHERE oid=" + entry_6.get()) 
   conn.commit()
   conn.close()
   
   
def querry():
   conn=sqlite3.connect("Form.db")
   cursor=conn.cursor()
   cursor.execute("SELECT *,oid FROM FORM")
   records=cursor.fetchall()
   print_records=" "
   for record in records:
      print_records += str(record[0])+" "+str(record[1])+" "+str(record[2])+" "+str(record[3])+" "+str(record[4])+" "+str(record[5])+ "\n"
   querry_label=Label(root,text=print_records)
   querry_label.grid(row=9,column=1,columnspan=2)
   conn.commit()
   conn.close()


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.grid(row=0,column=0)

entry_1 = Entry(root,textvar=Fullname)
entry_1.grid(row=0,column=1)

label_2 = Label(root, text="ID",width=20,font=("bold", 10))
label_2.grid(row=0,column=2)

entry_2 = Entry(root,textvar=ID)
entry_2.grid(row=0,column=3)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.grid(row=5,column=0)

entry_3=Radiobutton(root, text="Male",variable=var ,value='MALE').grid(row=5,column=1)
entry_3=Radiobutton(root, text="Female",variable=var,value='FEMALE').grid(row=5,column=2)

label_4 = Label(root, text="DEPARTMENT",width=20,font=("bold", 10))
label_4.grid(row=3,column=2)

list1 = ['IT','SALES','SUPPORT','DEVELOPERS'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your department') 
droplist.grid(row=3,column=3)
label_5 = Label(root, text="ADDRESH",width=20,font=("bold", 10))
label_5.grid(row=3,column=0)

entry_5 = Entry(root,textvar=Addresh)
entry_5.grid(row=3,column=1)


label_6=Label(root,text="Select ID")
label_6.grid(row=7,column=0)
entry_6=Entry(root,textvar=d)
entry_6.grid(row=7,column=1)


Button(root, text='ADD Record to Dataset',width=20,bg='brown',fg='white',command=Add).grid(row=6,column=0)
Button(root, text='Show Record',width=20,bg='brown',fg='white',command=querry).grid(row=8,column=1)
Button(root, text='Delete Record',width=20,bg='brown',fg='white',command=delete).grid(row=6,column=1)

root.mainloop()
