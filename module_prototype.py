from tkinter import *


root = Tk()


root.geometry("1000x600")
root.resizable(True,True)
root.title("DASHBOARD")

#CREATE A START PAGE
start = Frame(root,bg='#4472C4', height=600, width=1000)
start.pack(fill="both", expand=True)
fr = Label(start,text="GLOBAL WATCHTOWER \n SV 21 INTERFACE",font = "Verdana 30 bold",bg="#4472C4")
fr.place(rely=0.1,relx=0.25,relwidth=0.55, relheight=0.3)

e1 = Entry(start, text = 'ENTER TEAM NAME',bg="#70AD47").place(relx=0.1,rely=0.5, relwidth=0.8, relheight=0.15)

button = Button(start,text="Enter",bg="gray",font = "Verdana 15 bold",command=lambda: switch_frame(start,finish))
button.place(rely=0.65,relx=0.1, relwidth=0.8, relheight=0.15)

#CREATE A SECOND PAGE
finish = Frame(root,bg='#4472C4', height=600, width=1000)

ts = Label(finish,text="GLOBAL WATCHTOWER SV 21 INTERFACE",font = "Verdana 15 bold",bg="#4472C4")
ts.place(rely=0.05,relx=0.25,relwidth=0.55, relheight=0.1)
ts2 = Label(finish,text="TO LOG IN YOU MUST ENTER 3 VALID KEYWORDS\nYOU CAN MAKE AS MANY ATTEMPTS AS YOU WISH",font = "Verdana 15 bold",bg="#4472C4")
ts2.place(rely=0.25,relx=0.2,relwidth=0.6, relheight=0.1)

es1 = Entry(finish, text = 'WORD 1',bg="#70AD47").place(relx=0.1,rely=0.4, relwidth=0.45, relheight=0.1)
es2 = Entry(finish, text = 'WORD 2',bg="#70AD47").place(relx=0.1,rely=0.55, relwidth=0.45, relheight=0.1)
es3 = Entry(finish, text = 'WORD 3',bg="#70AD47").place(relx=0.1,rely=0.7, relwidth=0.45, relheight=0.1)

bs1 = Button(finish,text="VALIDATE", command="",bg="gray",font = "Verdana 15 bold")
bs1.place(relx=0.6,rely=0.4, relwidth=0.2, relheight=0.1)
bs2 = Button(finish,text="VALIDATE", command="",bg="gray",font = "Verdana 15 bold")
bs2.place(relx=0.6,rely=0.55,relwidth=0.2, relheight=0.1)
bs3 = Button(finish,text="VALIDATE",bg="gray",font = "Verdana 15 bold",command=lambda: switch_frame(finish,thr))
bs3.place(relx=0.6,rely=0.7,relwidth=0.2, relheight=0.1)

#CREATE A THIRD PAGE
thr = Frame(root,bg='#4472C4', height=600, width=1000)

tt = Label(thr,text="GLOBAL WATCHTOWER SV 21 INTERFACE",font = "Verdana 15 bold",bg='#4472C4')
tt.place(rely=0.05,relx=0.25,relwidth=0.55, relheight=0.1)

framet1 = LabelFrame(thr,bd=5,bg='#4472C4')
framet1.place(relx=0.06,rely=0.2, relwidth=0.25, relheight=0.75)

bt1 = Button(framet1,text="Launch Virus",bg="#70AD47",font = "Arial 20 bold",command=lambda: switch_frame(thr,launch))
bt1.place(relx=0,rely=0, relwidth=1, relheight=0.15)
#t2 = tk.Label(frame1,text="This option launches the virus directly\nin 3,125,673 with number of \ninfected devices doubling every 13 hours."+
#"\n"+"Total collapse in global tech infrastructure in 3 -5 days",font = "Verdana 9",justify=LEFT).place(relx=0.08,rely=0.4, relwidth=0.25, relheight=0.5)

framet2 = LabelFrame(thr,bd=5,bg='#4472C4')
framet2.place(relx=0.4,rely=0.2, relwidth=0.25, relheight=0.75)

bt2 = Button(framet2,text="Stall Virus",bg="#70AD47",font = "Arial 20 bold",command=lambda: switch_frame(thr,stall))
bt2.place(relx=0,rely=0,relwidth=1, relheight=0.15)
#t2 = tk.Label(thr,text="GLOBAL WATCHTOWER SV 21 INTERFACE",font = "Verdana 15 bold").place(rely=0.3,relx=0.4)

framet3 = LabelFrame(thr,bd=5,bg='#4472C4')
framet3.place(relx=0.7,rely=0.2, relwidth=0.25, relheight=0.75)

bt3 = Button(framet3,text="Destroy Virus",bg="#70AD47",font = "Arial 20 bold",command=lambda: switch_frame(thr,finish))
bt3.place(relx=0,rely=0,relwidth=1, relheight=0.15)
#tt = tk.Label(thr,text="GLOBAL WATCHTOWER SV 21 INTERFACE",font = "Verdana 15 bold").place(rely=0.06,relx=0.3)

#CREATE A LAUNCH PAGE
launch = Frame(root,bg='#4472C4', height=600, width=1000)

tl = Label(launch,text="GLOBAL WATCHTOWER SV 21 INTERFACE",font = "Verdana 15 bold",bg="#4472C4")
tl.place(rely=0.05,relx=0.25,relwidth=0.55, relheight=0.1)
tl2 = Label(launch,text="DESTRUCTION OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS",font = "Verdana 15 bold",bg="#4472C4")
tl2.place(relx=0.0,rely=0.25,relwidth=1, relheight=0.1)

el1 = Entry(launch, text = 'WORD 1',bg="#70AD47").place(relx=0.1,rely=0.4, relwidth=0.45, relheight=0.1)
el2 = Entry(launch, text = 'WORD 2',bg="#70AD47").place(relx=0.1,rely=0.55, relwidth=0.45, relheight=0.1)

bl1 = Button(launch,text="VALIDATE", command="",bg="gray",font = "Verdana 15 bold")
bl1.place(relx=0.6,rely=0.4, relwidth=0.2, relheight=0.1)
bl2 = Button(launch,text="VALIDATE", command="",bg="gray",font = "Verdana 15 bold")
bl2.place(relx=0.6,rely=0.55,relwidth=0.2, relheight=0.1)


#CREATE A STALL PAGE
stall = Frame(root,bg='#4472C4', height=600, width=1000)

tst = Label(stall,text="GLOBAL WATCHTOWER SV 21 INTERFACE",font = "Verdana 15 bold",bg="#4472C4")
tst.place(rely=0.05,relx=0.25,relwidth=0.55, relheight=0.1)
ts1 = Label(stall,text="VIRUS RELEASE SUSPENDED FOR 5 DAYS!",font = "Verdana 15 bold",bg="#4472C4")
ts1.place(relx=0.1,rely=0.15,relwidth=0.85, relheight=0.1)
ts2 = Label(stall,text="DESTRUCTION OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS",font = "Verdana 15 bold",bg="#4472C4")
ts2.place(relx=0,rely=0.25,relwidth=1, relheight=0.1)
es1 = Entry(stall, text = 'WORD 1',bg="#70AD47").place(relx=0.1,rely=0.4, relwidth=0.45, relheight=0.1)
es2 = Entry(stall, text = 'WORD 2',bg="#70AD47").place(relx=0.1,rely=0.55, relwidth=0.45, relheight=0.1)

bs1 = Button(stall,text="VALIDATE", command="",bg="gray",font = "Verdana 15 bold")
bs1.place(relx=0.6,rely=0.4, relwidth=0.2, relheight=0.1)
bs2 = Button(stall,text="VALIDATE", command="",bg="gray",font = "Verdana 15 bold")
bs2.place(relx=0.6,rely=0.55,relwidth=0.2, relheight=0.1)


def switch_frame (old,new):
    old.pack_forget()
    new.pack(fill="both", expand=True)

mainloop()