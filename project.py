from tkinter import *
root=Tk()
root.configure(bg  = 'white')
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def close():
    root.destroy()
    import Home
img =PhotoImage(file=".\\Bus_for_project.png")
Label(root,image = img).grid(row = 0 , column = 0)
Label(root,text = "Online Bus Booking System", font = "arial 40 bold", bg = 'sky blue', fg ='Red').grid(row = 1, column =0,padx=450)
Label(root,text="Name:Aniruddha Pradhan", font = "arial 25 bold" ,bg= 'white', fg = 'blue').grid(row = 2 , column = 0, pady = 30)
Label(root,text="Er : 211B048", font = "arial 25 bold" ,bg= 'white', fg = 'blue').grid(row = 3 , column = 0, pady = 30)
Label(root,text="Mobile:7693012426", font = "arial 25 bold" ,bg= 'white', fg = 'blue').grid(row = 4 , column = 0, pady = 30)

Label(root,text="Submitted to :Dr. Mahesh Kumar", font = "arial 35 bold" , bg = 'sky blue' ,fg = 'red').grid(row = 5 , column = 0, pady = 30)
Label(root,text="Project Based Learning", font = "arial 25 bold" ,bg= 'white', fg = 'red').grid(row = 6 , column = 0)
root.after(3000,close)
root.mainloop()
