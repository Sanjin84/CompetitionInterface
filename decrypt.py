from cryptography.fernet import Fernet
from tkinter import *

def go():
    name=name_var.get()
    if name=="BOSSMAN":
        check()
        button["state"] = DISABLED


def check():
    key = b'DqbtoOEMKXpTsYjm9FFRJOwOXEfUPn5vmUvlOnsx2MY='

    fernet = Fernet(key)
    try:
        with open("info.txt", 'r') as enc_file:
            encrypted = enc_file.read()
            val = encrypted.split('\n')
            val.pop()
        text_box = Text(root,height=18,width=80)
        text_box.pack(expand=True)
        
        for i in val:
            i= i.encode()
            decrypted = fernet.decrypt(i).decode()
            text_box.insert('end', decrypted)
        text_box.config(state='disabled')
            
    except:
        text_box = Text(root,height=12,width=40)
        text_box.pack(expand=True)
        text_box.insert('end', "CHOOSE CORRECT FILE")
        text_box.config(state='disabled')


root = Tk()
root.geometry("1000x600")
root.resizable(width=False, height=False)
root.title("DASHBOARD")
root.configure(bg="gray")
name_var=StringVar()


ent = Entry(root,textvariable = name_var)
ent.place(rely=0.1,relx=0.2, relwidth=0.3, relheight=0.1)
button = Button(root,text="LOGIN" ,bg="white",font = "Verdana 15 bold", command = go)
button.place(rely=0.1,relx=0.6, relwidth=0.3, relheight=0.1)


mainloop()