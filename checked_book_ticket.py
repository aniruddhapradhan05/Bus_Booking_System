from tkinter import*
root= Tk()
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))


img =PhotoImage(file=".\\Bus_for_project.png")
Label(root,image = img).grid(row = 0 , column = 0, columnspan = 3, padx = 500)

Label(root,text = "Online Bus Booking System", font = "arial 24 bold",bg = 'sky blue', fg ='Red').grid(row = 1, column = 0, pady = 20, columnspan = 3)
Label(root,text = "Check Your Booking ", font = "arial 20 bold",bg = 'light green', fg ='green').grid(row = 2, column = 0, pady = 20, columnspan = 3)

Label(root,text = "Enter Your Mobile Number: ").grid(row= 3 , column = 1,padx = 50)
Text(root, width = 20, height = 1).grid(row= 3 , column = 1, sticky = E)
Button(root, text = 'Check Booking').grid(row= 3 , column = 1, sticky = E)
 

