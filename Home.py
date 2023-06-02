from tkinter import *
root=Tk()
def a():
    root.destroy()
    import seat_booking
def c():
    root.destroy()
    import add_new_details_to_database
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
img =PhotoImage(file="Bus_for_project.png")
Label(root,image = img).grid(row = 0 , column = 5,pady=10,padx=400)
Label(root,text = "Online Bus Booking System", font = "arial 40 bold", bg = 'sky blue', fg ='Red').grid(row = 1, column =5,pady=50)
Button(root, text = 'Seat Booking', bg = 'green',height='3',command=a).grid(row = 2, column = 4,padx=30)
Button(root, text = 'Checked Booked Seat',height='3', font = 'arial 14', bg = 'green').grid(row = 2, column = 5,padx=30)
Button(root, text = 'Add Bus Details', height='3',font = 'arial 14', bg = 'green',command=c).grid(row = 2, column = 6)

root.mainloop()
