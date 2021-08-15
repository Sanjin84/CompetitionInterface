from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
keywords=["key1","key2","key3","key4","key5"]
title="GLOBAL WATCHTOWER SV 21 INTERFACE"
font_title="Verdana 30 bold"
font_title_s="Verdana 31 bold"
font_basic="Verdana 15 bold"
font_basic_s="Verdana 16 bold"
font_custom="Arial 20 bold"
BOX_COLOR="#4472C4"
BUTTON_COLOR="#70AD47"
TEXT_COLOR = 'FFFFFF'
score=0
answers=[]

def team_check():
    if len(tn.get()):
        switch_frame(cv1,cv2)

def check(v,b):
    
    global score
    if v.get() in keywords:
        answers.append(v.get())
        keywords.remove(v.get())
        score+=10
        print(keywords)
        b.config(text="VALIDATED",bg=green_bg)
    if len(keywords) == 2:
        switch_frame(cv2,cv3)
    #if len(keywords) == 0:
        #save_file()

def switch_frame (old,new):
    old.pack_forget()
    new.pack(fill="both", expand=True)
    
def save_file():
    tf = open('info.txt',"a")
    tf.write("\n"+tn.get()+" - ["+answers[0]+", "+answers[1]+", "+answers[2]+", "+answers[3]+", "+answers[4]+"]")
   
    tf.close()

def stroke_text(canv,x, y, text,stroke_font,text_font):
    canv.create_text(x, y, text=text, font=stroke_font, fill='black')
    canv.create_text(x, y, text=text, font=text_font, fill='white')
    

root.geometry("1000x600")
root.title("DASHBOARD")

#CREATE A START PAGE
cv1 = Canvas( root,width = 1000,height = 600)

img=ImageTk.PhotoImage(Image.open("background.png"))
cv1.create_image( 0, 0, image = img, anchor = "nw")

stroke_text(cv1,500, 100, 'GLOBAL WATCHTOWER \n    SV 21 INTERFACE',font_title_s,font_title)
stroke_text(cv1,500, 220, 'ENTER TEAM NAME',font_basic_s,font_basic)


tn = StringVar()
e1 = Entry(cv1, text = 'ENTER TEAM NAME', textvariable=tn)
cv1.create_window(500,300,window=e1,height=80, width=500)

button = Button(cv1,text="Enter",bg="gray",font = font_basic,command=team_check)
button.place(rely=0.65,relx=0.1, relwidth=0.8, relheight=0.15)
cv1.create_window(500,400,window=button,height=50, width=400)
cv1.pack(fill = "both", expand = True)


#CREATE A SECOND PAGE
cv2 = Canvas( root,width = 200,height = 200)
cv2.create_image( 0, 0, image = img, anchor = "nw")
stroke_text(cv2,500, 80, title,font_basic_s,font_basic)
stroke_text(cv2,500, 150, 'TO LOG IN YOU MUST ENTER 3 VALID KEYWORDS\nYOU CAN MAKE AS MANY ATTEMPTS AS YOU WISH',font_basic_s,font_basic)

est1 = StringVar()
est2 = StringVar()
est3 = StringVar()
es1 = Entry(cv2, text = 'WORD 1', textvariable=est1)
cv2.create_window(300,250,window=es1,height=80, width=500)
es2 = Entry(cv2, text = 'WORD 2', textvariable=est2)
cv2.create_window(300,370,window=es2,height=80, width=500)
es3 = Entry(cv2, text = 'WORD 3', textvariable=est3)
cv2.create_window(300,490,window=es3,height=80, width=500)
b21 = Button(cv2,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(est1,b21))
cv2.create_window(700,250,window=b21,height=80, width=200)
b22 = Button(cv2,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(est2,b22))
cv2.create_window(700,370,window=b22,height=80, width=200)
b23 = Button(cv2,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(est3,b23))
cv2.create_window(700,490,window=b23,height=80, width=200)

#CREATE A THIRD PAGE
cv3 = Canvas( root,width = 200,height = 200)
cv3.create_image( 0, 0, image = img, anchor = "nw")
stroke_text(cv3,500, 80, title,font_basic_s,font_basic)

cv3.create_rectangle(320, 550, 75, 260, outline = 'black',width=3)
bt1 = Button(cv3,text="Launch Virus",bg=green_bg,font = font_custom,command=lambda: switch_frame(cv3,cvl))
cv3.create_window(200,200,window=bt1,height=80, width=250)
cv3.create_text(200, 370, text="This option launches the virus directly in 3,125,673 with number of infected devices doubling every 13 hours."+
"\n\nTotal collapse in global tech infrastructure in 3 -5 days", font="Arial 15 ", fill='white', width=230)

cv3.create_rectangle(375, 550, 620, 260, outline = 'black',width=3)
bt2 = Button(cv3,text="Stall Virus",bg=green_bg,font = font_custom,command=lambda: switch_frame(cv3,cvs))
cv3.create_window(500,200,window=bt2,height=80, width=250)
cv3.create_text(500, 370, text="This option modifies the source code of the virus so that it cannot be activated for another 5 days."
+"This is to be exercised as a precaution during organizational disagreement", font="Arial 15 ", fill='white', width=230)

cv3.create_rectangle(675, 550, 920, 260, outline = 'black',width=3)
bt3 = Button(cv3,text="Destroy Virus",bg=green_bg,font = font_custom,command=lambda: switch_frame(cv3,cvd))
cv3.create_window(800,200,window=bt3,height=80, width=250)
cv3.create_text(800, 392, text="This option sends the virus source code to 39 of the most prominent Anti Virus companies. It publishes a patch for windows, Linux and Mac computers making them immune to the virus"
+"\n\nThis option requires MASTER ACCESS", font="Arial 15 ", fill='white', width=230)


#CREATE A LAUNCH PAGE
cvl = Canvas( root,width = 200,height = 200)
cvl.create_image( 0, 0, image = img, anchor = "nw")
stroke_text(cvl,500, 80, title,font_basic_s,font_basic)

#tl1 = Label(launch,text="VIRUS LAUNCHED!",font = font_basic,bg=blue_bg)
stroke_text(cvl,500, 150, 'DESTRUCTION OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS',font_basic_s,font_basic)

esl1 = StringVar()
esl2 = StringVar()

el1 = Entry(cvl, text = 'WORD 1',bg=green_bg, textvariable=esl1)
cvl.create_window(400,250,window=el1,height=80, width=500)
el2 = Entry(cvl, text = 'WORD 2',bg=green_bg, textvariable=esl2)
cvl.create_window(400,350,window=el2,height=80, width=500)

bl1 = Button(cvl,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(esl1,bl1))
cvl.create_window(800,250,window=bl1,height=80, width=200)
bl2 = Button(cvl,text="VALIDATE",bg="gray",font = font_basic,command=lambda: check(esl2,bl2))
cvl.create_window(800,350,window=bl2,height=80, width=200)


#CREATE A STALL PAGE
cvs = Canvas( root,width = 200,height = 200)
cvs.create_image( 0, 0, image = img, anchor = "nw")
stroke_text(cvs,500, 80, title,font_basic_s,font_basic)

#ts1 = Label(stall,text="VIRUS RELEASE SUSPENDED FOR 5 DAYS!",font = font_basic,bg=blue_bg)

stroke_text(cvs,500, 150, 'STALLING OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS',font_basic_s,font_basic)

es1 = Entry(cvs, text = 'WORD 1',bg=green_bg)
cvs.create_window(400,250,window=es1,height=80, width=500)
es2 = Entry(cvs, text = 'WORD 2',bg=green_bg)
cvs.create_window(400,350,window=es2,height=80, width=500)

bs1 = Button(cvs,text="VALIDATE", command="",bg="gray",font = font_basic)
cvs.create_window(800,250,window=bs1,height=80, width=200)
bs2 = Button(cvs,text="VALIDATE", command="",bg="gray",font = font_basic)
cvs.create_window(800,350,window=bs2,height=80, width=200)

#CREATE A DESTROY PAGE
cvd = Canvas( root,width = 200,height = 200)
cvd.create_image( 0, 0, image = img, anchor = "nw")
stroke_text(cvd,500, 80, title,font_basic_s,font_basic)

#td1 = Label(des,text="VIRUS DESTROYED!",font = font_title,bg=blue_bg)

stroke_text(cvd,500, 150, 'DESTRUCTION OF THE VIRUS REQUIRES THE USE OF THE FINAL TWO KEYWORDS',font_basic_s,font_basic)


ed1 = Entry(cvd, text = 'WORD 1',bg=green_bg)
cvd.create_window(400,250,window=ed1,height=80, width=500)
ed2 = Entry(cvd, text = 'WORD 2',bg=green_bg)
cvd.create_window(400,350,window=ed2,height=80, width=500)

bd1 = Button(cvd,text="VALIDATE", command="",bg="gray",font = font_basic)
cvd.create_window(800,250,window=bd1,height=80, width=200)
bd2 = Button(cvd,text="VALIDATE", command="",bg="gray",font = font_basic)
cvd.create_window(800,350,window=bd2,height=80, width=200)



mainloop()