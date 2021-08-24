from cryptography.fernet import Fernet
from tkinter import *
from tkinter.filedialog import askopenfilename

def check():
    filename = askopenfilename()
    key = b'DqbtoOEMKXpTsYjm9FFRJOwOXEfUPn5vmUvlOnsx2MY='

    fernet = Fernet(key)
    try:
        with open(filename, 'rb') as enc_file:
            encrypted = enc_file.read()
        
        decrypted = fernet.decrypt(encrypted)
        
        text_box = Text(root,height=12,width=40)
        text_box.pack(expand=True)
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


button = Button(root,text="CHOOSE FILE" ,bg="white",font = "Verdana 15 bold", command = check)
button.place(rely=0.1,relx=0.35, relwidth=0.3, relheight=0.15)

mainloop()