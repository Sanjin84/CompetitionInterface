from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from cryptography.fernet import Fernet

root = Tk()
keywords=["key1","key2","key3","key4","key5"]
title="GLOBAL WATCHTOWER SV 21 INTERFACE"
font_title="Verdana 30 bold"
font_basic="Verdana 15 bold"
font_custom="Arial 20 bold"
BOX_COLOR="#23838c"
BUTTON_COLOR="gray"
BUTTON_COLOR_AFTER="#7bffb9"
TEXT_COLOR = 'white'
score=0
once=False
answers=[]

def team_check():
    if len(tn.get()):
        switch_frame(cv1,cv2)

def score_check(value):
    print("")

def check(v,b):
    if v.get() not in keywords:
        answers.append(v.get())

    global score
    global once
    
    if v.get() in keywords:
        answers.append(v.get())
        keywords.remove(v.get())
        score+=10
        b.config(text="VALIDATED",bg=BUTTON_COLOR_AFTER)
    if len(keywords) == 2 and once == False:
        once=True
        switch_frame(cv2,cvm)
    if len(keywords) == 0:
        cvl.create_text(500, 500, text="VIRUS LAUNCHED!", font=font_title, fill=TEXT_COLOR)
        cvs.create_text(500, 500, text="VIRUS RELEASE SUSPENDED FOR 5 DAYS!", font=font_title, fill=TEXT_COLOR)
        cvd.create_text(500, 500, text="VIRUS DESTROYED!", font=font_title, fill=TEXT_COLOR)
        blb["state"] = DISABLED
        bsb["state"] = DISABLED
        bdb["state"] = DISABLED
        
def back(current,menu):
    switch_frame(current,menu)
    if len(keywords) <=1:
        bl1.config(text="VALIDATED",bg=BUTTON_COLOR_AFTER)
        bs1.config(text="VALIDATED",bg=BUTTON_COLOR_AFTER)
        bd1.config(text="VALIDATED",bg=BUTTON_COLOR_AFTER)


def switch_frame (old,new):
    old.pack_forget()
    new.pack(fill="both", expand=True)
       

def on_closing():
    vv = "\n"+tn.get()+" - ["
    v1=""
    for i in answers:
        v1 += i+", "
    v2 = "]"
    vf = vv + v1+ v2
    
    with open('score.txt', 'a+') as tf2:
        tf2.write("\n"+tn.get()+"-"+str(score))
        tf2.close()
    key = b'DqbtoOEMKXpTsYjm9FFRJOwOXEfUPn5vmUvlOnsx2MY='
    fernet = Fernet(key)

    encrypted = fernet.encrypt(vf.encode())

    with open('info.txt', 'a+') as encrypted_file:
        encrypted_file.write(encrypted.decode()+"\n")
    

    root.destroy()

root.geometry("1000x600")
root.resizable(width=False, height=False)
root.title("DASHBOARD")

#CREATE A START PAGE
cv1 = Canvas( root,width = 1000,height = 600)

img=ImageTk.PhotoImage(Image.open("background.png"))
cv1.create_image( 0, 0, image = img, anchor = "nw")
cv1.create_rectangle(220, 40, 770, 165,fill=BOX_COLOR,outline=BOX_COLOR)
cv1.create_rectangle(380, 200, 620, 240,fill=BOX_COLOR,outline=BOX_COLOR)

cv1.create_text(500, 100, text='GLOBAL WATCHTOWER \n    SV 21 INTERFACE', font=font_title, fill=TEXT_COLOR)
cv1.create_text(500, 220, text='ENTER TEAM NAME', font=font_basic, fill=TEXT_COLOR)


tn = StringVar()
e1 = Entry(cv1, textvariable=tn,bg=BOX_COLOR)
cv1.create_window(500,300,window=e1,height=80, width=500)

button = Button(cv1,text="Enter",bg=BUTTON_COLOR,font = font_basic,command=team_check)
button.place(rely=0.65,relx=0.1, relwidth=0.8, relheight=0.15)
cv1.create_window(500,400,window=button,height=50, width=400)
cv1.pack(fill = "both", expand = True)


#CREATE A SECOND PAGE (ENTER 3 KEYWORDS)
cv2 = Canvas( root,width = 200,height = 200)
cv2.create_image( 0, 0, image = img, anchor = "nw")
cv2.create_rectangle(250, 60, 750, 100,fill=BOX_COLOR,outline=BOX_COLOR)
cv2.create_rectangle(200, 120, 800, 180,fill=BOX_COLOR,outline=BOX_COLOR)

cv2.create_text(500, 80, text=title, font=font_basic, fill=TEXT_COLOR)
cv2.create_text(500, 150, text='TO LOG IN YOU MUST ENTER 3 VALID KEYWORDS\nYOU CAN MAKE AS MANY ATTEMPTS AS YOU WISH', font=font_basic, fill=TEXT_COLOR)

est1 = StringVar()
est2 = StringVar()
est3 = StringVar()
es1 = Entry(cv2, text = 'WORD 1',bg=BOX_COLOR, textvariable=est1)
cv2.create_window(300,250,window=es1,height=80, width=500)
es2 = Entry(cv2, text = 'WORD 2',bg=BOX_COLOR, textvariable=est2)
cv2.create_window(300,370,window=es2,height=80, width=500)
es3 = Entry(cv2, text = 'WORD 3',bg=BOX_COLOR, textvariable=est3)
cv2.create_window(300,490,window=es3,height=80, width=500)
b21 = Button(cv2,text="VALIDATE",bg=BUTTON_COLOR,font = font_basic,command=lambda: check(est1,b21))
cv2.create_window(700,250,window=b21,height=80, width=200)
b22 = Button(cv2,text="VALIDATE",bg=BUTTON_COLOR,font = font_basic,command=lambda: check(est2,b22))
cv2.create_window(700,370,window=b22,height=80, width=200)
b23 = Button(cv2,text="VALIDATE",bg=BUTTON_COLOR,font = font_basic,command=lambda: check(est3,b23))
cv2.create_window(700,490,window=b23,height=80, width=200)

#CREATE A MENU PAGE
cvm = Canvas( root,width = 200,height = 200)
cvm.create_image( 0, 0, image = img, anchor = "nw")
cvm.create_rectangle(250, 60, 750, 100,fill=BOX_COLOR,outline=BOX_COLOR)

cvm.create_text(500, 80, text=title, font=font_basic, fill=TEXT_COLOR)

cvm.create_rectangle(320, 550, 75, 260, fill = BOX_COLOR,outline = BOX_COLOR)
bt1 = Button(cvm,text="Launch Virus",bg=BUTTON_COLOR_AFTER,font = font_custom,command=lambda: switch_frame(cvm,cvl))
cvm.create_window(200,200,window=bt1,height=80, width=250)
cvm.create_text(200, 370, text="This option launches the virus directly in 3,125,673 with number of infected devices doubling every 13 hours."+
"\n\nTotal collapse in global tech infrastructure in 3 -5 days", font="Arial 15 ", fill='white', width=230)

cvm.create_rectangle(375, 550, 620, 260, fill = BOX_COLOR,outline = BOX_COLOR)
bt2 = Button(cvm,text="Stall Virus",bg=BUTTON_COLOR_AFTER,font = font_custom,command=lambda: switch_frame(cvm,cvs))
cvm.create_window(500,200,window=bt2,height=80, width=250)
cvm.create_text(500, 370, text="This option modifies the source code of the virus so that it cannot be activated for another 5 days."
+"This is to be exercised as a precaution during organizational disagreement", font="Arial 15 ", fill='white', width=230)

cvm.create_rectangle(675, 550, 920, 260, fill = BOX_COLOR,outline = BOX_COLOR)
bt3 = Button(cvm,text="Destroy Virus",bg=BUTTON_COLOR_AFTER,font = font_custom,command=lambda: switch_frame(cvm,cvd))
cvm.create_window(800,200,window=bt3,height=80, width=250)
cvm.create_text(800, 392, text="This option sends the virus source code to 39 of the most prominent Anti Virus companies. It publishes a patch for windows, Linux and Mac computers making them immune to the virus"
+"\n\nThis option requires MASTER ACCESS", font="Arial 15 ", fill='white', width=230)


#CREATE A LAUNCH PAGE
cvl = Canvas( root,width = 200,height = 200)
cvl.create_image( 0, 0, image = img, anchor = "nw")
cvl.create_rectangle(250, 60, 750, 100,fill=BOX_COLOR,outline=BOX_COLOR)
cvl.create_text(500, 80, text=title, font=font_basic, fill=TEXT_COLOR)

#cvl.create_text(500, 500, text="VIRUS LAUNCHED!", font=font_title, fill=TEXT_COLOR)
cvl.create_rectangle(20, 130, 980, 170,fill=BOX_COLOR,outline=BOX_COLOR)
cvl.create_text(500, 150, text='DESTRUCTION OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS', font=font_basic, fill=TEXT_COLOR)


esl1 = StringVar()
esl2 = StringVar()

el1 = Entry(cvl, text = 'WORD 1',bg=BOX_COLOR, textvariable=esl1)
cvl.create_window(400,250,window=el1,height=80, width=500)
el2 = Entry(cvl, text = 'WORD 2',bg=BOX_COLOR, textvariable=esl2)
cvl.create_window(400,350,window=el2,height=80, width=500)

bl1 = Button(cvl,text="VALIDATE",bg=BUTTON_COLOR,font = font_basic,command=lambda: check(esl1,bl1))
cvl.create_window(800,250,window=bl1,height=80, width=200)
bl2 = Button(cvl,text="VALIDATE",bg=BUTTON_COLOR,font = font_basic,command=lambda: check(esl2,bl2))
cvl.create_window(800,350,window=bl2,height=80, width=200)

blb = Button(cvl,text="<BACK",bg=BUTTON_COLOR,font = font_basic,command=lambda: back(cvl,cvm))
cvl.create_window(70,50,window=blb,height=40, width=90)


#CREATE A STALL PAGE
cvs = Canvas( root,width = 200,height = 200)
cvs.create_image( 0, 0, image = img, anchor = "nw")
cvs.create_rectangle(250, 60, 750, 100,fill=BOX_COLOR,outline=BOX_COLOR)
cvs.create_text(500, 80, text=title, font=font_basic, fill=TEXT_COLOR)

#cvs.create_text(500, 500, text="VIRUS RELEASE SUSPENDED FOR 5 DAYS!", font=font_title, fill=TEXT_COLOR)
cvs.create_rectangle(300, 130, 700, 170,fill=BOX_COLOR,outline=BOX_COLOR)
cvs.create_rectangle(120, 180, 880, 220,fill=BOX_COLOR,outline=BOX_COLOR)
cvs.create_text(500, 150, text='VIRUS STALLED FOR 5 DAYS', font=font_basic, fill=TEXT_COLOR)
cvs.create_text(500, 200, text='ENTER TWO REMAINING KEYWORDS TO DESTROY THE VIRUS', font=font_basic, fill=TEXT_COLOR)

ess1 = StringVar()
ess2 = StringVar()

es1 = Entry(cvs, text = 'WORD 1',bg=BOX_COLOR, textvariable=ess1)
cvs.create_window(400,300,window=es1,height=80, width=500)
es2 = Entry(cvs, text = 'WORD 2',bg=BOX_COLOR, textvariable=ess2)
cvs.create_window(400,400,window=es2,height=80, width=500)

bs1 = Button(cvs,text="VALIDATE",bg=BUTTON_COLOR,font = font_basic,command=lambda: check(ess1,bs1))
cvs.create_window(800,300,window=bs1,height=80, width=200)
bs2 = Button(cvs,text="VALIDATE",bg=BUTTON_COLOR,font = font_basic,command=lambda: check(ess2,bs2))
cvs.create_window(800,400,window=bs2,height=80, width=200)

bsb = Button(cvs,text="<BACK",bg=BUTTON_COLOR,font = font_basic,command=lambda: back(cvs,cvm))
cvs.create_window(70,50,window=bsb,height=40, width=90)

#CREATE A DESTROY PAGE
cvd = Canvas( root,width = 200,height = 200)
cvd.create_image( 0, 0, image = img, anchor = "nw")
cvd.create_rectangle(250, 60, 750, 100,fill=BOX_COLOR,outline=BOX_COLOR)
cvd.create_text(500, 80, text=title, font=font_basic, fill=TEXT_COLOR)

#cvd.create_text(500, 500, text="VIRUS DESTROYED!", font=font_title, fill=TEXT_COLOR)
cvd.create_rectangle(30, 130, 970, 170,fill=BOX_COLOR,outline=BOX_COLOR)
cvd.create_text(500, 150, text='DESTRUCTION OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS', font=font_basic, fill=TEXT_COLOR)

esd1 = StringVar()
esd2 = StringVar()

ed1 = Entry(cvd, text = 'WORD 1',bg=BOX_COLOR, textvariable=esd1)
cvd.create_window(400,250,window=ed1,height=80, width=500)
ed2 = Entry(cvd, text = 'WORD 2',bg=BOX_COLOR, textvariable=esd2)
cvd.create_window(400,350,window=ed2,height=80, width=500)

bd1 = Button(cvd,text="VALIDATE",bg=BUTTON_COLOR,font = font_basic,command=lambda: check(esd1,bd1))
cvd.create_window(800,250,window=bd1,height=80, width=200)
bd2 = Button(cvd,text="VALIDATE",bg=BUTTON_COLOR,font = font_basic,command=lambda: check(esd2,bd2))
cvd.create_window(800,350,window=bd2,height=80, width=200)

bdb = Button(cvd,text="<BACK",bg=BUTTON_COLOR,font = font_basic,command=lambda: back(cvd,cvm))
cvd.create_window(70,50,window=bdb,height=40, width=90)

root.protocol("WM_DELETE_WINDOW", on_closing)
mainloop()