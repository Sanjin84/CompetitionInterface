from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
keywords=["key1","key2","key3","key4","key5"]
title="GLOBAL WATCHTOWER SV 21 INTERFACE"
font_title="Verdana 30 bold"
font_basic="Verdana 15 bold"
font_custom="Arial 20 bold"
blue_bg="#4472C4"
green_bg="#70AD47"
count=0
answers=[]

def team_check():
    if len(tn.get()):
        switch_frame(start,finish)

def check(v,b):
    
    global count
    if v.get() in keywords:
        answers.append(v.get())
        keywords.remove(v.get())
        count+=1
        print(keywords)
        b.config(text="VALIDATED",bg=green_bg)
    if len(keywords) == 2:
        switch_frame(finish,thr)
    if len(keywords) == 0:
        save_file()

def switch_frame (old,new):
    old.pack_forget()
    new.pack(fill="both", expand=True)
    
def save_file():
    tf = open('info.txt',"a")
    tf.write("\n"+tn.get()+" - ["+answers[0]+", "+answers[1]+", "+answers[2]+", "+answers[3]+", "+answers[4]+"]")
   
    tf.close()

    

root.geometry("1000x600")
root.resizable(True,True)
root.title("DASHBOARD")

#CREATE A START PAGE
start = Frame(root,bg=blue_bg, height=600, width=1000)
start.pack(fill="both", expand=True)

img=ImageTk.PhotoImage(Image.open("kali.png"))
imgl = Label(start, image=img)
imgl.place(x=0, y=0, relwidth=1, relheight=1)

fr = Label(start,text="GLOBAL WATCHTOWER \n SV 21 INTERFACE",font = font_title,bg=blue_bg)
fr.place(rely=0.1,relx=0.25,relwidth=0.55, relheight=0.3)

tn = StringVar()
e1 = Entry(start, text = 'ENTER TEAM NAME',bg=green_bg, textvariable=tn)
e1.place(relx=0.1,rely=0.5, relwidth=0.8, relheight=0.15)

button = Button(start,text="Enter",bg="gray",font = font_basic,command=team_check)
button.place(rely=0.65,relx=0.1, relwidth=0.8, relheight=0.15)


#CREATE A SECOND PAGE
finish = Frame(root,bg=blue_bg, height=600, width=1000)
imgs = Label(finish, image=img)
imgs.place(x=0, y=0, relwidth=1, relheight=1)
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
b21 = Button(finish,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(est1,b21))
b21.place(relx=0.6,rely=0.4, relwidth=0.2, relheight=0.1)
b22 = Button(finish,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(est2,b22))
b22.place(relx=0.6,rely=0.55,relwidth=0.2, relheight=0.1)
b23 = Button(finish,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(est3,b23))
b23.place(relx=0.6,rely=0.7,relwidth=0.2, relheight=0.1)

#CREATE A THIRD PAGE
thr = Frame(root,bg=blue_bg, height=600, width=1000)
imgt = Label(thr, image=img)
imgt.place(x=0, y=0, relwidth=1, relheight=1)
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
imgla = Label(launch, image=img)
imgla.place(x=0, y=0, relwidth=1, relheight=1)
tl = Label(launch,text=title,font = font_basic,bg=blue_bg)
tl.place(rely=0.05,relx=0.25,relwidth=0.55, relheight=0.1)
tl2 = Label(launch,text="DESTRUCTION OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS",font = font_basic,bg=blue_bg)
tl2.place(relx=0.0,rely=0.25,relwidth=1, relheight=0.1)

esl1 = StringVar()
esl2 = StringVar()

el1 = Entry(launch, text = 'WORD 1',bg=green_bg, textvariable=esl1)
el1.place(relx=0.1,rely=0.4, relwidth=0.45, relheight=0.1)
el2 = Entry(launch, text = 'WORD 2',bg=green_bg, textvariable=esl2)
el2.place(relx=0.1,rely=0.55, relwidth=0.45, relheight=0.1)

bl1 = Button(launch,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(esl1,bl1))
bl1.place(relx=0.6,rely=0.4, relwidth=0.2, relheight=0.1)
bl2 = Button(launch,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(esl2,bl2))
bl2.place(relx=0.6,rely=0.55,relwidth=0.2, relheight=0.1)


#CREATE A STALL PAGE
stall = Frame(root,bg=blue_bg, height=600, width=1000)
imgst = Label(stall, image=img)
imgst.place(x=0, y=0, relwidth=1, relheight=1)
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






mainloop()