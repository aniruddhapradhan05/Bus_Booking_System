from tkinter import*
root= Tk()
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def a():
    root.destroy()
    import Add_bus_operator_details.py
img =PhotoImage(file="Bus_for_project.png")
Label(root,image = img).grid(row = 0 , column = 6,columnspan=35)

Label(root,text = "Online Bus Booking System", font = "arial 18 bold",bg = 'sky blue', fg ='Red').grid(row = 1, column = 6, pady = 20)

Label(root,text = "Add New Details to DataBase", font = "arial 14 bold", fg ='green').grid(row = 2, column = 6, pady = 20)
Button(root, text= 'New Operator',fg ='black' ,bg= 'light green',command=a).grid(row= 3 ,column = 2)
Button(root, text= 'New Bus',fg ='black' ,bg= 'orange red').grid(row= 3 ,column = 3,padx=20)
Button(root, text= 'New Route',fg ='black' ,bg= 'steelBlue1').grid(row= 3 ,column = 4,padx=20)
Button(root, text= 'New Run',fg ='black' ,bg= 'rosy brown').grid(row= 3 ,column = 5,padx=20)

root.mainloop
