from tkinter import*
import sqlite3
root= Tk()
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def Action():
    bus_id=e1.get()
    bustype=bus_type.get()
    capacity=e2.get()
    fare=e3.get()
    operator_id=e4.get()
    route_id=e5.get()
    conn=sqlite3.connect("company.db")
    c=conn.cursor()
    c.execute("insert into bus values (' "bus_id" ', ' "bustype" ', ' "capacity" ', ' "fare" ', ' "operator_id" ', ' "route_id" ')")
    conn.commit()
    conn.close()
img =PhotoImage(file="Bus_for_project.png")
Label(root,image = img).grid(row = 0 , column =4 ,columnspan=3)
Label(root,text = "Online Bus Booking System", font = "arial 35 bold",bg = 'sky blue', fg ='Red').grid(row = 1, column = 4, pady = 20,columnspan=4)
Label(root,text = "Add Bus Details", font = "arial 14 bold",bg = 'light green', fg ='green').grid(row = 2, column = 4, pady = 20,columnspan=3)
Label(root,text = "Bus ID").grid(row=3 , column = 0)
e1=Entry(root, width = 20)
e1.grid(row = 3 , column =1)
bus_type=StringVar()
bus_type.set("Bus Type")
d_menu=OptionMenu(root , bus_type, 'AC    ' , 'NON AC').grid(row=3,column=2)
Label(root,text = "Capacity").grid(row=3 , column = 3)
e2=Entry(root, width = 20 )
e2.grid(row = 3 , column =4)
Label(root,text = "Fare Rs").grid(row=3 , column = 5)
e3=Entry(root, width = 20 )
e3.grid(row = 3 , column =6)
Label(root,text = "Opeartor ID").grid(row=3 , column = 7)
e4=Entry(root, width = 20)
e4.grid(row = 3 , column =8)
Label(root,text = "Route ID").grid(row=3 , column = 9)
e5=Entry(root, width = 20)
e5.grid(row = 3 , column =10)
Button(root, text= 'Add Bus',fg ='black' ,bg= 'light green',command=Action).grid(row= 4 ,column = 4,pady=40)
Button(root,text='Edit Bus',fg ='black' ,bg= 'light green',).grid(row= 4 ,column = 5, padx = 6)
root.mainloop()
