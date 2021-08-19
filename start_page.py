from tkinter import *

def create_start_page(root):
    start = Frame(root,bg='#FF0000', height=600, width=1000)
    start.pack()
    fr = Label(start,text="GLOBAL WATCHTOWER \n SV 21 INTERFACE",font = "Verdana 30 bold",bg="#4472C4")
    fr.place(rely=0.1,relx=0.1, relwidth= 0.8)
    e1 = Entry(start, text = 'ENTER TEAM NAME',bg="#70AD47").place(relx=0.1,rely=0.5, relwidth=0.8, relheight=0.15)
    button = Button(start,text="GO TO FINISH" ,bg="gray",font = "Verdana 15 bold", command = lambda: switch_frame(start,finish))
    button.place(rely=0.65,relx=0.1, relwidth=0.4, relheight=0.15)