from tkinter import *


root = Tk()


root.geometry("1000x600")
root.resizable(True,True)
root.title("DASHBOARD")

#CREATE A START PAGE
start = Frame(root,bg='#539bf9', height=600, width=1000)
start.pack()
start_heading = Label(start,text="GLOBAL WATCHTOWER \n SV 21 INTERFACE",font = "Verdana 30 bold",bg="#539bf9")
start_heading.place(rely=0.1,relx=0.1, relwidth= 0.8)
team_name_label = Label(start,text="ENTER YOUR TEAM NAME",font = "Verdana 30 bold",bg="#539bf9")
team_name_label.place(rely=0.4, relx = 0.1, relwidth = 0.8)
team_name_entry = Entry(start, text = 'ENTER TEAM NAME',bg="#f0f0f0").place(relx=0.1,rely=0.5, relwidth=0.8, relheight=0.15)
button = Button(start,text="GO TO FINISH" ,bg="gray",font = "Verdana 15 bold", command = lambda: switch_frame(start,finish))
button.place(rely=0.65,relx=0.1, relwidth=0.4, relheight=0.15)

#CREATE A FINISH PAGE
finish = Frame(root,bg='#FF0000', height=600, width=1000)
fr = Label(finish,text="VIRUS HAS BEEN STOPPED",font = "Verdana 30 bold",bg="#4472C4")
fr.place(rely=0.1,relx=0.1, relwidth= 0.8)
button2 = Button(finish,text="GO TO START" ,bg="gray",font = "Verdana 15 bold", command = lambda: switch_frame(finish,start))
button2.place(rely=0.65,relx=0.5, relwidth=0.4, relheight=0.15)

def switch_frame (old,new):
    old.pack_forget()
    new.pack()

mainloop()