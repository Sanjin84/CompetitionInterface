import tkinter as tk
from tkinter import *


root = Tk()
root.geometry("1000x600")
root.resizable(True,True)
root.title("DASHBOARD")
start = Frame(root,bg='#4472C4').place(relx=0, rely=0, relwidth=1, relheight=1)

fr = tk.Label(start,text="GLOBAL WATCHTOWER \n SV 21 INTERFACE",font = "Verdana 30 bold",bg="#4472C4").place(rely=0.1,relx=0.25)

e1 = Entry(start, text = 'ENTER TEAM NAME',bg="#70AD47").place(relx=0.1,rely=0.5, relwidth=0.8, relheight=0.15)

def second():
    
    sec= Frame(root,bg='#4472C4').place(relx=0, rely=0, relwidth=1, relheight=1)
    tt = tk.Label(sec,text="GLOBAL WATCHTOWER SV 21 INTERFACE",font = "Verdana 15 bold",bg="#4472C4").place(rely=0.06,relx=0.3)
    t2 = tk.Label(sec,text="TO LOG IN YOU MUST ENTER 3 VALID KEYWORDS\nYOU CAN MAKE AS MANY ATTEMPTS AS YOU WISH",font = "Verdana 15 bold",bg="#4472C4").place(rely=0.25,relx=0.25)
    e1 = Entry(sec, text = 'WORD 1',bg="#70AD47").place(relx=0.1,rely=0.4, relwidth=0.45, relheight=0.1)
    e2 = Entry(sec, text = 'WORD 2',bg="#70AD47").place(relx=0.1,rely=0.55, relwidth=0.45, relheight=0.1)
    e3 = Entry(sec, text = 'WORD 3',bg="#70AD47").place(relx=0.1,rely=0.7, relwidth=0.45, relheight=0.1)

    b1 = Button(sec,text="VALIDATE", command="",bg="gray",font = "Verdana 15 bold").place(relx=0.6,rely=0.4, relwidth=0.2, relheight=0.1)
    b2 = Button(sec,text="VALIDATE", command="",bg="gray",font = "Verdana 15 bold").place(relx=0.6,rely=0.55,relwidth=0.2, relheight=0.1)
    b3 = Button(sec,text="VALIDATE", command=third,bg="gray",font = "Verdana 15 bold").place(relx=0.6,rely=0.7,relwidth=0.2, relheight=0.1)
    
def third():
    
    thr= Frame(root,bg='#4472C4').place(relx=0, rely=0, relwidth=1, relheight=1)
    tt = tk.Label(thr,text="GLOBAL WATCHTOWER SV 21 INTERFACE",font = "Verdana 15 bold",bg='#4472C4').place(relx=0.3,rely=0.06)

    frame1 = tk.LabelFrame(thr,bd=5,bg='#4472C4').place(relx=0.06,rely=0.35, relwidth=0.25, relheight=0.6)
    b1 = Button(frame1,text="Launch Virus", command=launch,bg="#70AD47",font = "Arial 20 bold").place(relx=0.06,rely=0.2, relwidth=0.25, relheight=0.1)
    #t2 = tk.Label(frame1,text="This option launches the virus directly\nin 3,125,673 with number of \ninfected devices doubling every 13 hours."+
    #"\n"+"Total collapse in global tech infrastructure in 3 -5 days",font = "Verdana 9",justify=LEFT).place(relx=0.08,rely=0.4, relwidth=0.25, relheight=0.5)
    
    frame2 = tk.LabelFrame(thr,bd=5,bg='#4472C4').place(relx=0.4,rely=0.35, relwidth=0.25, relheight=0.6)
    b2 = Button(frame2,text="Stall Virus", command=stall,bg="#70AD47",font = "Arial 20 bold").place(relx=0.4,rely=0.2,relwidth=0.25, relheight=0.1)
    #t2 = tk.Label(thr,text="GLOBAL WATCHTOWER SV 21 INTERFACE",font = "Verdana 15 bold").place(rely=0.3,relx=0.4)
    
    frame3 = tk.LabelFrame(thr,bd=5,bg='#4472C4').place(relx=0.7,rely=0.35, relwidth=0.25, relheight=0.6)
    b3 = Button(frame3,text="Destroy Virus", command="",bg="#70AD47",font = "Arial 20 bold").place(relx=0.7,rely=0.2,relwidth=0.25, relheight=0.1)
    #tt = tk.Label(thr,text="GLOBAL WATCHTOWER SV 21 INTERFACE",font = "Verdana 15 bold").place(rely=0.06,relx=0.3)

def launch():
    sec= Frame(root,bg='#4472C4').place(relx=0, rely=0, relwidth=1, relheight=1)
    tt = tk.Label(sec,text="GLOBAL WATCHTOWER SV 21 INTERFACE",font = "Verdana 15 bold",bg="#4472C4").place(rely=0.06,relx=0.3)
    t2 = tk.Label(sec,text="DESTRUCTION OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS",font = "Verdana 15 bold",bg="#4472C4").place(relx=0.05,rely=0.25)
    e1 = Entry(sec, text = 'WORD 1',bg="#70AD47").place(relx=0.1,rely=0.4, relwidth=0.45, relheight=0.1)
    e2 = Entry(sec, text = 'WORD 2',bg="#70AD47").place(relx=0.1,rely=0.55, relwidth=0.45, relheight=0.1)

    b1 = Button(sec,text="VALIDATE", command="",bg="gray",font = "Verdana 15 bold").place(relx=0.6,rely=0.4, relwidth=0.2, relheight=0.1)
    b2 = Button(sec,text="VALIDATE", command="",bg="gray",font = "Verdana 15 bold").place(relx=0.6,rely=0.55,relwidth=0.2, relheight=0.1)

def stall():
    sec= Frame(root,bg='#4472C4').place(relx=0, rely=0, relwidth=1, relheight=1)
    tt = tk.Label(sec,text="GLOBAL WATCHTOWER SV 21 INTERFACE",font = "Verdana 15 bold",bg="#4472C4").place(rely=0.06,relx=0.3)
    t1 = tk.Label(sec,text="VIRUS RELEASE SUSPENDED FOR 5 DAYS!",font = "Verdana 15 bold",bg="#4472C4").place(relx=0.25,rely=0.15)
    t2 = tk.Label(sec,text="DESTRUCTION OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS",font = "Verdana 15 bold",bg="#4472C4").place(relx=0.05,rely=0.25)
    e1 = Entry(sec, text = 'WORD 1',bg="#70AD47").place(relx=0.1,rely=0.4, relwidth=0.45, relheight=0.1)
    e2 = Entry(sec, text = 'WORD 2',bg="#70AD47").place(relx=0.1,rely=0.55, relwidth=0.45, relheight=0.1)

    b1 = Button(sec,text="VALIDATE", command="",bg="gray",font = "Verdana 15 bold").place(relx=0.6,rely=0.4, relwidth=0.2, relheight=0.1)
    b2 = Button(sec,text="VALIDATE", command="",bg="gray",font = "Verdana 15 bold").place(relx=0.6,rely=0.55,relwidth=0.2, relheight=0.1)

    
    



button = Button(start,text="Enter", command=second,bg="gray",font = "Verdana 15 bold")
button.place(rely=0.65,relx=0.1, relwidth=0.8, relheight=0.15)



mainloop()