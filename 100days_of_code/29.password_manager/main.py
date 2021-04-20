from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
# ---------------------------- PASSWORD GENERATOR --------------------------- #
def generate():
    password_entry.delete(0, END)
    letter = string.ascii_letters
    symbol = string.punctuation
    number = string.digits
    password_list = [random.choice(letter) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbol) for char in range(random.randint(2, 4))]
    password_list += [random.choice(number) for char in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(web) < 1 or len(password) < 1:
        messagebox.showerror(title='Oops', message='Please don\'t leave any \
        field empty')
    else:
        confirmation = messagebox.askokcancel(title=web, message=f'These are'
            f' the detailed entered: \nEmail: {username}\nPassword: {password}'
                f' \nIs it ok to save? ')

        if confirmation:
            with open('data.txt', 'a') as file:
                file.write(f"{web_entry.get()} | {username_entry.get()} | \
                    {password_entry.get()} \n ")
                web_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# logo field
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# website
web_label = Label(text='Website:')
web_label.grid(row=1, column=0)
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

# username_email
username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, 'spotifyhakk88@gmail.com')

# password
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# generate pwd button
generate_button = Button(text='Generate Password', command=generate)
generate_button.grid(row=3, column=2)

# add
add_button = Button(text='Add', width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
