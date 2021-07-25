import tkinter as tk
from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("1000x600")
root.pack_propagate(False)
root.resizable(True,True)
root.title("DASHBOARD")
root.configure(background='black')

fr = tk.Label(root,text="NAME")
fr.place(rely=0.3,relx=0.5)

e1 = Entry(root,width=50).place(relx=0.35,rely=0.4)

fr = tk.Label(root,text="ADDRESS")
fr.place(rely=0.5,relx=0.5)

e2 = Entry(root,width=50).place(relx=0.35,rely=0.6)





button = Button(root,text="Enter", command="search")
button.place(rely=0.5,relx=0.8)


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

mainloop()