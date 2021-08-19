from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
keywords=["key1","key2","key3","key4","key5"]
title="GLOBAL WATCHTOWER SV 21 INTERFACE"
font_title="Verdana 30 bold"
font_basic="Verdana 15 bold"
font_custom="Arial 20 bold"
BOX_COLOR="#23838c"
BUTTON_COLOR_AFTER="#7bffb9"
TEXT_COLOR = 'white'
greenc="#7bffb9"
bluec="#23838c"
score=0
once=False
answers=[]

def team_check():
    if len(tn.get()):
        switch_frame(cv1,cv2)

def check(v,b):
    if v.get() not in keywords:
        answers.append(v.get())

    global score
    global once
    
    if v.get() in keywords:
        answers.append(v.get())
        keywords.remove(v.get())
        score+=10
        print(keywords)
        b.config(text="VALIDATED",bg=BUTTON_COLOR_AFTER)
    if len(keywords) == 2 and once == False:
        once=True
        switch_frame(cv2,cv3)
    if len(keywords) == 0:
        cvl.create_text(500, 500, text="VIRUS LAUNCHED!", font=font_title, fill=TEXT_COLOR)
        cvs.create_text(500, 500, text="VIRUS RELEASE SUSPENDED FOR 5 DAYS!", font=font_title, fill=TEXT_COLOR)
        cvd.create_text(500, 500, text="VIRUS DESTROYED!", font=font_title, fill=TEXT_COLOR)
        

def switch_frame (old,new):
    old.pack_forget()
    new.pack(fill="both", expand=True)
       

def stroke_text(canv,x, y, text,stroke_font,text_font):
    canv.create_text(x, y, text=text, font=stroke_font, fill='black')
    canv.create_text(x, y, text=text, font=text_font, fill=TEXT_COLOR)

def on_closing():
    
    tf = open('info.txt',"a")
    
    tf.write("\n"+tn.get()+" - [")
    for i in answers:
        tf.write(i+", ")
    tf.write("]")
    tf.close()
    root.destroy()

root.geometry("1000x600")
root.resizable(width=False, height=False)
root.title("DASHBOARD")

#CREATE A START PAGE
cv1 = Canvas( root,width = 1000,height = 600)

img=ImageTk.PhotoImage(Image.open(r"F:\Google Drive\GATEWAYS\Challenge\2021\InterfaceCode\CompetitionInterface\background.png"))
cv1.create_image( 0, 0, image = img, anchor = "nw")
cv1.create_rectangle(220, 40, 770, 165,fill=BOX_COLOR,outline=BOX_COLOR)
cv1.create_rectangle(380, 200, 620, 240,fill=BOX_COLOR,outline=BOX_COLOR)

cv1.create_text(500, 100, text='GLOBAL WATCHTOWER \n    SV 21 INTERFACE', font=font_title, fill=TEXT_COLOR)
cv1.create_text(500, 220, text='ENTER TEAM NAME', font=font_basic, fill=TEXT_COLOR)


tn = StringVar()
e1 = Entry(cv1, textvariable=tn,bg=BOX_COLOR)
cv1.create_window(500,300,window=e1,height=80, width=500)

button = Button(cv1,text="Enter",bg="gray",font = font_basic,command=team_check)
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
b21 = Button(cv2,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(est1,b21))
cv2.create_window(700,250,window=b21,height=80, width=200)
b22 = Button(cv2,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(est2,b22))
cv2.create_window(700,370,window=b22,height=80, width=200)
b23 = Button(cv2,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(est3,b23))
cv2.create_window(700,490,window=b23,height=80, width=200)

#CREATE A THIRD PAGE (OPTIONS TO STALL, LAUNCH OR DESTROY)
cv3 = Canvas( root,width = 200,height = 200)
cv3.create_image( 0, 0, image = img, anchor = "nw")
cv3.create_rectangle(250, 60, 750, 100,fill=BOX_COLOR,outline=BOX_COLOR)

cv3.create_text(500, 80, text=title, font=font_basic, fill=TEXT_COLOR)

cv3.create_rectangle(320, 550, 75, 260, fill = BOX_COLOR,outline = BOX_COLOR)
bt1 = Button(cv3,text="Launch Virus",bg=BUTTON_COLOR_AFTER,font = font_custom,command=lambda: switch_frame(cv3,cvl))
cv3.create_window(200,200,window=bt1,height=80, width=250)
cv3.create_text(200, 370, text="This option launches the virus directly in 3,125,673 with number of infected devices doubling every 13 hours."+
"\n\nTotal collapse in global tech infrastructure in 3 -5 days", font="Arial 15 ", fill='white', width=230)

cv3.create_rectangle(375, 550, 620, 260, fill = BOX_COLOR,outline = BOX_COLOR)
bt2 = Button(cv3,text="Stall Virus",bg=BUTTON_COLOR_AFTER,font = font_custom,command=lambda: switch_frame(cv3,cvs))
cv3.create_window(500,200,window=bt2,height=80, width=250)
cv3.create_text(500, 370, text="This option modifies the source code of the virus so that it cannot be activated for another 5 days."
+"This is to be exercised as a precaution during organizational disagreement", font="Arial 15 ", fill='white', width=230)

cv3.create_rectangle(675, 550, 920, 260, fill = BOX_COLOR,outline = BOX_COLOR)
bt3 = Button(cv3,text="Destroy Virus",bg=BUTTON_COLOR_AFTER,font = font_custom,command=lambda: switch_frame(cv3,cvd))
cv3.create_window(800,200,window=bt3,height=80, width=250)
cv3.create_text(800, 392, text="This option sends the virus source code to 39 of the most prominent Anti Virus companies. It publishes a patch for windows, Linux and Mac computers making them immune to the virus"
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

bl1 = Button(cvl,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(esl1,bl1))
cvl.create_window(800,250,window=bl1,height=80, width=200)
bl2 = Button(cvl,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(esl2,bl2))
cvl.create_window(800,350,window=bl2,height=80, width=200)


#CREATE A STALL PAGE
cvs = Canvas( root,width = 200,height = 200)
cvs.create_image( 0, 0, image = img, anchor = "nw")
cvs.create_rectangle(250, 60, 750, 100,fill=BOX_COLOR,outline=BOX_COLOR)
cvs.create_text(500, 80, text=title, font=font_basic, fill=TEXT_COLOR)

#cvs.create_text(500, 500, text="VIRUS RELEASE SUSPENDED FOR 5 DAYS!", font=font_title, fill=TEXT_COLOR)
cvs.create_rectangle(40, 130, 960, 170,fill=BOX_COLOR,outline=BOX_COLOR)
cvs.create_text(500, 150, text='STALLING OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS', font=font_basic, fill=TEXT_COLOR)

ess1 = StringVar()
ess2 = StringVar()

es1 = Entry(cvs, text = 'WORD 1',bg=BOX_COLOR, textvariable=ess1)
cvs.create_window(400,250,window=es1,height=80, width=500)
es2 = Entry(cvs, text = 'WORD 2',bg=BOX_COLOR, textvariable=ess2)
cvs.create_window(400,350,window=es2,height=80, width=500)

bs1 = Button(cvs,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(ess1,bs1))
cvs.create_window(800,250,window=bs1,height=80, width=200)
bs2 = Button(cvs,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(ess2,bs2))
cvs.create_window(800,350,window=bs2,height=80, width=200)

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

bd1 = Button(cvd,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(esd1,bd1))
cvd.create_window(800,250,window=bd1,height=80, width=200)
bd2 = Button(cvd,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(esd2,bd2))
cvd.create_window(800,350,window=bd2,height=80, width=200)


root.protocol("WM_DELETE_WINDOW", on_closing)
mainloop()