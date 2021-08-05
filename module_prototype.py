from tkinter import *
from PIL import ImageTk, Image

root = Tk()
keywords=["key1","key2","key3","key4","key5"]
title="GLOBAL WATCHTOWER SV 21 INTERFACE"
font_title="Verdana 30 bold"
font_basic="Verdana 15 bold"
font_custom="Arial 20 bold"
blue_bg="#4472C4"
green_bg="#70AD47"
count=0

def check():
    global count
    #if est1.get() == "" or est2.get()=="":
    #    print("empty")
    if est1.get() in keywords:
        keywords.remove(est1.get())
        count+=1
        print(keywords)


root.geometry("1000x600")
root.resizable(True,True)
root.title("DASHBOARD")

#CREATE A START PAGE
start = Frame(root,bg=blue_bg, height=600, width=1000)
start.pack(fill="both", expand=True)

img=ImageTk.PhotoImage(Image.open("kali.jpg"))
imgl = Label(start, image=img)
imgl.place(x=0, y=0, relwidth=1, relheight=1)

fr = Label(start,text="GLOBAL WATCHTOWER \n SV 21 INTERFACE",font = font_title,bg=blue_bg)
fr.place(rely=0.1,relx=0.25,relwidth=0.55, relheight=0.3)

e1 = Entry(start, text = 'ENTER TEAM NAME',bg=green_bg)
e1.place(relx=0.1,rely=0.5, relwidth=0.8, relheight=0.15)

button = Button(start,text="Enter",bg="gray",font = font_basic,command=lambda: switch_frame(start,finish))
button.place(rely=0.65,relx=0.1, relwidth=0.8, relheight=0.15)

#CREATE A SECOND PAGE
finish = Frame(root,bg=blue_bg, height=600, width=1000)

ts = Label(finish,text=title,font = font_basic,bg=blue_bg)
ts.place(rely=0.05,relx=0.25,relwidth=0.55, relheight=0.1)
ts2 = Label(finish,text="TO LOG IN YOU MUST ENTER 3 VALID KEYWORDS\nYOU CAN MAKE AS MANY ATTEMPTS AS YOU WISH",font = font_basic,bg=blue_bg)
ts2.place(rely=0.25,relx=0.2,relwidth=0.6, relheight=0.1)

est1 = StringVar()
est2 = StringVar()
est3 = StringVar()
es1 = Entry(finish, text = 'WORD 1',bg=green_bg, textvariable=est1)
es1.place(relx=0.1,rely=0.4, relwidth=0.45, relheight=0.1)
es2 = Entry(finish, text = 'WORD 2',bg=green_bg, textvariable=est2)
es2.place(relx=0.1,rely=0.55, relwidth=0.45, relheight=0.1)
es3 = Entry(finish, text = 'WORD 3',bg=green_bg, textvariable=est3)
es3.place(relx=0.1,rely=0.7, relwidth=0.45, relheight=0.1)
bs1 = Button(finish,text="VALIDATE",bg="gray",font = font_basic,command=check)
bs1.place(relx=0.6,rely=0.4, relwidth=0.2, relheight=0.1)
bs2 = Button(finish,text="VALIDATE", command="",bg="gray",font = font_basic)
bs2.place(relx=0.6,rely=0.55,relwidth=0.2, relheight=0.1)
bs3 = Button(finish,text="VALIDATE",bg="gray",font = font_basic,command=lambda: switch_frame(finish,thr))
bs3.place(relx=0.6,rely=0.7,relwidth=0.2, relheight=0.1)

#CREATE A THIRD PAGE
thr = Frame(root,bg=blue_bg, height=600, width=1000)

tt = Label(thr,text=title,font = font_basic,bg=blue_bg)
tt.place(rely=0.05,relx=0.25,relwidth=0.55, relheight=0.1)

framet1 = LabelFrame(thr,bd=5,bg=blue_bg)
framet1.place(relx=0.06,rely=0.2, relwidth=0.25, relheight=0.75)

bt1 = Button(framet1,text="Launch Virus",bg=green_bg,font = font_custom,command=lambda: switch_frame(thr,launch))
bt1.place(relx=0,rely=0, relwidth=1, relheight=0.15)
#t2 = tk.Label(frame1,text="This option launches the virus directly\nin 3,125,673 with number of \ninfected devices doubling every 13 hours."+
#"\n"+"Total collapse in global tech infrastructure in 3 -5 days",font = "Verdana 9",justify=LEFT).place(relx=0.08,rely=0.4, relwidth=0.25, relheight=0.5)

framet2 = LabelFrame(thr,bd=5,bg=blue_bg)
framet2.place(relx=0.4,rely=0.2, relwidth=0.25, relheight=0.75)

bt2 = Button(framet2,text="Stall Virus",bg=green_bg,font = font_custom,command=lambda: switch_frame(thr,stall))
bt2.place(relx=0,rely=0,relwidth=1, relheight=0.15)
#t2 = tk.Label(thr,text=title,font = font_basic).place(rely=0.3,relx=0.4)

framet3 = LabelFrame(thr,bd=5,bg=blue_bg)
framet3.place(relx=0.7,rely=0.2, relwidth=0.25, relheight=0.75)

bt3 = Button(framet3,text="Destroy Virus",bg=green_bg,font = font_custom,command=lambda: switch_frame(thr,finish))
bt3.place(relx=0,rely=0,relwidth=1, relheight=0.15)
#tt = tk.Label(thr,text=title,font = font_basic).place(rely=0.06,relx=0.3)

#CREATE A LAUNCH PAGE
launch = Frame(root,bg=blue_bg, height=600, width=1000)

tl = Label(launch,text=title,font = font_basic,bg=blue_bg)
tl.place(rely=0.05,relx=0.25,relwidth=0.55, relheight=0.1)
tl2 = Label(launch,text="DESTRUCTION OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS",font = font_basic,bg=blue_bg)
tl2.place(relx=0.0,rely=0.25,relwidth=1, relheight=0.1)

el1 = Entry(launch, text = 'WORD 1',bg=green_bg).place(relx=0.1,rely=0.4, relwidth=0.45, relheight=0.1)
el2 = Entry(launch, text = 'WORD 2',bg=green_bg).place(relx=0.1,rely=0.55, relwidth=0.45, relheight=0.1)

bl1 = Button(launch,text="VALIDATE", command="",bg="gray",font = font_basic)
bl1.place(relx=0.6,rely=0.4, relwidth=0.2, relheight=0.1)
bl2 = Button(launch,text="VALIDATE", command="",bg="gray",font = font_basic)
bl2.place(relx=0.6,rely=0.55,relwidth=0.2, relheight=0.1)


#CREATE A STALL PAGE
stall = Frame(root,bg=blue_bg, height=600, width=1000)

tst = Label(stall,text=title,font = font_basic,bg=blue_bg)
tst.place(rely=0.05,relx=0.25,relwidth=0.55, relheight=0.1)
ts1 = Label(stall,text="VIRUS RELEASE SUSPENDED FOR 5 DAYS!",font = font_basic,bg=blue_bg)
ts1.place(relx=0.1,rely=0.15,relwidth=0.85, relheight=0.1)
ts2 = Label(stall,text="DESTRUCTION OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS",font = font_basic,bg=blue_bg)
ts2.place(relx=0,rely=0.25,relwidth=1, relheight=0.1)
es1 = Entry(stall, text = 'WORD 1',bg=green_bg).place(relx=0.1,rely=0.4, relwidth=0.45, relheight=0.1)
es2 = Entry(stall, text = 'WORD 2',bg=green_bg).place(relx=0.1,rely=0.55, relwidth=0.45, relheight=0.1)

bs1 = Button(stall,text="VALIDATE", command="",bg="gray",font = font_basic)
bs1.place(relx=0.6,rely=0.4, relwidth=0.2, relheight=0.1)
bs2 = Button(stall,text="VALIDATE", command="",bg="gray",font = font_basic)
bs2.place(relx=0.6,rely=0.55,relwidth=0.2, relheight=0.1)




def switch_frame (old,new):
    old.pack_forget()
    new.pack(fill="both", expand=True)




mainloop()