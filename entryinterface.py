from tkinter import *
import random
import time

otp_timer = 0
def MemberList(filename):

    mem_id = []
    with open(filename) as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.split(',')
        mem_id.append([line[0],line[1]])

    label = Label(sidebar,text=("ID  -  resident"), justify=LEFT ,bg="#1b0816",fg="#ffffff",font=("comicsans",10,"italic"))
    label.pack(fill="x",pady="2")

    for member in mem_id:  
        
        label = Label(sidebar,text=(member[0]+" -> "+member[1]), justify=LEFT ,bg="#d74650",fg="#000000",font=("comicsans",10,"bold"))
        label.pack(fill="x",pady="2")
        

def clear():
    list = main.pack_slaves()
    for sl in list:
        sl.destroy()

def verify():
    # print(uservalue.get())
    # print(passvalue.get())
    pass


def check_guest():
    print(time.time()-otp_timer)
    if time.time() -otp_timer >120:
        clear()
        alert = Label(main, text="TIMEOUT! please try again later",padx="100",pady="20" , fg="#ff0000" ,font=("Helvetica",12,"italic"))
        alert.pack()
        Button(main,text="retry", command=login ).pack(pady="30")
    else:

        clear()
        alert = Label(main, text="Success - gate opening",padx="100",pady="20" , fg="#ff0000" ,font=("Helvetica",12,"italic"))
        alert.pack()
        Button(main,text="back", command=login , ).pack(pady="200")
        
    

def send_otp():
    #------WRITE YOUR BACKEND HERE----- and here only!!!!!!
    clear()
    global otp_timer
    otp_timer = time.time()
    otp = StringVar()
    alert = Label(main, text="You have 2 mins to type the 6 digit OTP",padx="100",pady="20" , fg="#ff0000" ,font=("Helvetica",12,"italic"))
    alert.pack()
    otp_sec = Entry(main,textvariable = otp)
    otp_sec.pack()
    Button(main,text="Verify", command=check_guest ).pack(pady="30")
    Button(main,text="back", command=login , ).pack(pady="200")


    

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
    memvalue = StringVar()
    mem_id = Label(main, text="Enter the member ID",padx="100",pady="20" , font=("Helvetica",12,"bold"))
    mem_id.pack()
    mem_id_entry = Entry(main,textvariable = memvalue)
    mem_id_entry.pack()
    Button(main,text="GET OTP", command=send_otp ).pack(pady="30")
    Button(main,text="back", command=login , ).pack(pady="200")

def animate():
    canvas = Canvas(main, width=600, height = 800)
    canvas.pack()
    alien1 = canvas.create_oval(270, 260, 330, 320, outline='white',fill='#581845') 
    canvas.pack()
    track = 0
    starttime = int(round(time.time() * 1000))
    while int(round(time.time() * 1000))-starttime < 700:
        x = 5
        y = 0
        sx=3
        sy=3
        if track == 0:
            for i in range(0,51):
                time.sleep(0.005)
                canvas.scale(alien1, sx, sy,1.01,1.01)
                canvas.move(alien1,-sx,-sy)
                canvas.update()
            track = 1
            

        else:
            for i in range(0,51):
                time.sleep(0.005)
                canvas.scale(alien1, -sx, sy,1/(1.01),1/(1.01))
                canvas.move(alien1,sx,sy)
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