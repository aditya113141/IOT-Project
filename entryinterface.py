from tkinter import *
import random
def MemberList(filename):

    my_file = open(filename, "r")
    content = my_file.read()
    memlist = content.split(",")
    my_file.close()
    i=0
    colors = ["#1b0816","#d74650","#545275"]
    for member in memlist:  
        
        label = Label(sidebar,text=member , justify=LEFT ,bg=colors[i%3],fg="#ffffff",font=("comicsans",10,"italic"))
        label.pack(fill="x",pady="2")
        i+=1

def verify():
    print(uservalue.get())
    print(passvalue.get())
root = Tk()
root.geometry("800x600")
root.title("Home Security")
root.minsize(800,600)
root.maxsize(800,600)
sidebar = Frame(root,bg="#6c3483")
main = Frame(root)
sidebar.pack(side=LEFT, fill="y")
main.pack(fill="y")
label = Label(sidebar,text="HOME - SECURITY " , bg="gray",fg="white",font=("comicsans",16,"bold"))
label.pack()
# member-list
MemberList("member.txt")


# b1 = Button(sidebar, text="TEST", command=test)
# b1.pack()


#   USERNAME AND PASSWORD


uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(main,textvariable = uservalue)
passentry = Entry(main,textvariable = passvalue)

username = Label(main, text="Username",padx="100",pady="20" , font=("Helvetica",12,"bold"))
password = Label(main, text="Password",padx="100",pady="20",font=("Helvetica",12,"bold"))
username.pack()
userentry.pack()
password.pack()
passentry.pack()
Button(text="Submit", command=verify ).pack(pady="8")



root.mainloop()