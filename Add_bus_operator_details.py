from tkinter import*
import sqlite3
import tkinter.messagebox
root= Tk()
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def action():
    id1=e1.get()
    name=e2.get()
    address=e3.get()
    phone=e4.get()
    email=e5.get()

    conn=sqlite3.connect("company.db")
    c= conn.cursor()
    c.execute("INSERT INTO operator VALUES (' "+id1+" ', ' "+name+" ', ' "+address+" ', ' "+phone+" ', ' "+email+" ')")
    tkinter.messagebox.showinfo("Information" , "Your Data is Successfully Recorded")
    conn.commit()
    conn.close()
    
img =PhotoImage(file="Bus_for_project.png")
Label(root,image = img).grid(row = 0 , column = 6,columnspan=2)
Label(root,text = "Online Bus Booking System", font = "arial 18 bold",bg = 'sky blue', fg ='Red').grid(row = 1, column = 6, pady = 20,columnspan=2)
Label(root,text = "Add Bus Operator Details", font = "arial 14 bold",bg = 'light green', fg ='green').grid(row = 2, column = 6, pady = 20,columnspan=2)
Label(root,text = "Operator Id").grid(row=3 , column = 2)
e1=Entry(root, width = 20)
e1.grid(row = 3 , column =3)
Label(root,text = "Name").grid(row=3 , column = 4)
e2=Entry(root, width = 20)
e2.grid(row = 3 , column =5,)
Label(root,text = "Address").grid(row=3 , column = 6)
e3=Entry(root, width = 20)
e3.grid(row = 3 , column =7)
Label(root,text = "Phone").grid(row=3 , column = 8)
e4=Entry(root, width = 20)
e4.grid(row = 3 , column =9)
Label(root,text = "Email").grid(row=3 , column = 10)
e5=Entry(root, width = 20)
e5.grid(row = 3 , column =11)
Button(root, text= 'Add',fg ='black' ,bg= 'light green',command=action).grid(row= 3 ,column = 13)
Button(root, text= 'Edit',fg ='black' ,bg= 'light green').grid(row= 3 ,column = 15)
#Button(root,fg ='black' ,bg= 'light green',image = img1).grid(row= 3 ,column = 10, padx = 10)
root.mainloop()
