from tkinter import *

root = Tk()
mylabel1 = Label(root,text="Hello World!")
mylabel2 = Label(root,text="My name is Aditya Kumar Sinha")
mylabel3 = Label(root,text="a")
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=0)
mylabel3.grid(row=1,column=5)
root.mainloop()