from tkinter import *
import random
import time
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
def clear():
    list = main.pack_slaves()
    for sl in list:
        sl.destroy()

def verify():
    # print(uservalue.get())
    # print(passvalue.get())
    exec(open('./first.py').read())

def login():
    clear()
    animate()
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
    Button(main,text="Submit", command=verify ).pack(pady="8")
    Button(main,text="guest", command=guest ).pack(pady="8")

def guest():
    clear()
    animate()
    Button(main,text="back", command=login ).pack(pady="8")

def animate():
    canvas = Canvas(main, width=400, height = 400)
    canvas.pack()
    alien1 = canvas.create_oval(20, 260, 80, 320, outline='white',fill='#581845') 
    alien2 = canvas.create_oval(90, 260, 130, 300, outline='white',fill='#ff5733') 
    canvas.pack()
    track = 0
    starttime = int(round(time.time() * 1000))
    while int(round(time.time() * 1000))-starttime < 800:
        x = 5
        y = 0
        if track == 0:
            for i in range(0,51):
                time.sleep(0.008)
                canvas.move(alien1, x, y)
                canvas.move(alien2, x, y)
                canvas.update()
            track = 1
            

        else:
            for i in range(0,51):
                time.sleep(0.008)
                canvas.move(alien1, -x, y)
                canvas.move(alien2, -x, y)
                canvas.update()
            track = 0
    
    clear()
                
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

login()



root.mainloop()