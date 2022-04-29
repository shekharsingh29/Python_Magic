import tkinter
from tkinter import messagebox
import clipboard
import json
import random


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHAR_LIST = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_-()+='


# ---------------------------- SEARCH PASSWORD ------------------------------#

def search():
    if web_text.get() != '':
        website = web_text.get()
        with open('credentials.json', mode='r') as jsonfile:
            json_data = json.load(jsonfile)
            if website in json_data.keys():
                email = json_data[website]['email']
                password = json_data[website]['password']
                messagebox.showinfo(message=f'email: {email} and password: {password}')
            
    else:
        messagebox.showinfo(message="Provide a website to search for")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password =''
    password_text.focus()
    password_text.delete(0,tkinter.END)
    for _ in range(0,11):
        password += random.choice(CHAR_LIST)
    password_text.insert(0,password)
    clipboard.copy(password)
        
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_cred():
    if web_text.get() !='' and email_text.get() != '' and password_text.get() != '':
        data = {
                    web_text.get(): {
                        "email" : email_text.get(),
                        "password" : password_text.get()
                    }
                }
        try:
            with open('credentials.json', mode="r") as jsonfile:
                json_data = json.load(jsonfile)              

        except FileNotFoundError:
            with open('credentials.json',mode='w') as jsonfile:
                json.dump(data, jsonfile, indent = 4)
            
        else:
            json_data.update(data)
            with open('credentials.json', mode='w') as jsonfile:
                json.dump(json_data,jsonfile, indent=4)

        finally:
            web_text.delete(0,tkinter.END)
            email_text.delete(0,tkinter.END)    
        
    else:
        print("Need to fill all the details")
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.config(width=800,height=600,padx=30,pady=30,background=YELLOW)
window.title("KEY-PASS")


# lock image
canvas = tkinter.Canvas(width=600,height=400,highlightthickness=0, background=YELLOW)
lock_image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(300,200,image=lock_image)
canvas.grid(column=1,row=0,rowspan=2)



web_label = tkinter.Label(background=GREEN,borderwidth=2,width=30,text="WEBSITE",font=(FONT_NAME,15,"bold"))
web_label.grid(row=3,column=0)

web_text = tkinter.Entry(borderwidth=1,width=95)
web_text.focus()
web_text.grid(row=3,column=1)

web_search_button = tkinter.Button(command=search,borderwidth=3,width=30,background=PINK,text="SEARCH",font=(FONT_NAME,15,"bold"))
web_search_button.grid(row=3,column=2)


email_label = tkinter.Label(background=GREEN,borderwidth=2,width=30,text="EMAIL/USERNAME",font=(FONT_NAME,15,"bold"))
email_label.grid(row=4,column=0)

email_text = tkinter.Entry(borderwidth=1, width=160)
email_text.grid(row=4,column=1,columnspan=2)


password_text = tkinter.Entry(borderwidth=1,width=160)
password_text.grid(row=5,column=0,columnspan=2)

pass_button = tkinter.Button(command=generate_pass,borderwidth=3,width=30,background=PINK,text="Generate",font=(FONT_NAME,15,"bold"))
pass_button.grid(row=5,column=2)


pass_button = tkinter.Button(command=save_cred,borderwidth=3,width=100,background=PINK,text="SAVE",font=(FONT_NAME,15,"bold"))
pass_button.grid(row=6,column=0,columnspan=3)

window.mainloop()