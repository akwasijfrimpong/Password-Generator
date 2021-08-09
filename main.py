import sys
from tkinter import *
import os
import random

root = Tk()
root.geometry('600x800')
root.minsize(height=560)
root.title("Password Generator")

def save():
    wbstr = website.get()
    unstr = username.get()
    pwstr = password.get()
    formated = '{} | {} | {} \n'.format(wbstr, unstr,pwstr)
    if os.path.isfile('password_file.txt'):
        with open('password_file.txt', 'a') as f:
            f.write(formated)
    else:
        with open('password_file.txt', 'w') as f:
            f.write(formated)

def generate():
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    symbols = "!@$%^&*()_+"
    pw = ""
    for i in range(10):
        uppercase = random.randint(0,25)
        lowercase = random.randint(0,25)
        symbolschar = random.randint(0,len(symbols) -1)

        pw = pw + upper[uppercase] + lower[lowercase] + symbols[symbolschar]

    password.delete(0,END)
    password.insert(0,pw)

#Logo
picture = PhotoImage(file='lock.png')
panel = Label(root, image = picture)
panel.pack(pady=50)

canvas = Canvas(root, width=600, height=400)
canvas.pack()

#website
website = Entry(width=50)
label = Label(root, text='Website: ', padx= 10)
canvas.create_window(270, 140, window=website)
canvas.create_window(80, 140, window=label)

#Username/email
username = Entry(width=50, )
label_username = Label(root, text='Username ')
canvas.create_window(270, 180, window=username)
canvas.create_window(80, 180, window=label_username)

#Password
password = Entry(width=50)
label_password= Label(root, text='Password: ')
canvas.create_window(270, 220, window=password)
canvas.create_window(80, 220, window=label_password)

#Buttons
pwbutton = Button(text="Generate Password", command=generate)
canvas.create_window(480, 180, window = pwbutton)

add = Button(text="Add",width=50, command=save)
canvas.create_window(270,250, window=add )




root.mainloop()
