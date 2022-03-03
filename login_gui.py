from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from MainGui import MainScreen
import sqlite3



gui = Tk()
gui.title('Payslip')
gui.geometry("500x500")







Frame(gui, width=250, height=400, bg='white').place(x=100, y=50)

# label_username
username_lbl = Label(gui, text='Username', bg='white')
l = ('consolas', 13)
username_lbl.config(font=1)
username_lbl.place(x=120, y=200)

username_entry = Entry(gui, width=20, border=0)
username_entry.config(font=1)
username_entry.place(x=120, y=230)

# label_password
password_lbl = Label(gui, text='Password', bg='white')
password_lbl.config(font=1)
password_lbl.place(x=120, y=280)

password_entry = Entry(gui, width=20, border=0, show='*')
password_entry.config(font=1)
password_entry.place(x=120, y=310)

Frame(gui, width=180, height=2, bg="#141414").place(x=125, y=250)
Frame(gui, width=180, height=2, bg="#141414").place(x=125, y=330)


def cmd():
    if username_entry.get() == 'admin' and password_entry.get() == "admin":
        messagebox.showinfo('Login Successfully', '  Welcome ')
        gui.destroy()
        MainScreen()




    else:
        messagebox.showinfo('Login Failed', '  Try Again  ')




Button(gui, width=15, height=2, fg='#999442', bg='#999442', border=0, command=cmd, text='L O G I N').place(x=130, y=375)

gui.mainloop()
