from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR --------------------------- #


def generate():
    password_entry.delete(0, END)
    letter = string.ascii_letters
    symbol = string.punctuation
    number = string.digits
    password_list = [random.choice(letter)
                     for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbol)
                      for char in range(random.randint(2, 4))]
    password_list += [random.choice(number)
                      for char in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    data_dic = {web: {
        'username': username,
        'password': password,
    }}

    if len(web) < 1 or len(password) < 1:
        messagebox.showerror(title='Oops', message='Please don\'t leave any \
        field empty')
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(data_dic, file, indent=4)
        else:
            data.update(data_dic)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# --------------------------- SEARCH PASSWORD ------------------------------ #
def search():
    web = web_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            search_file = data[web]
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found')
    except KeyError:
        messagebox.showerror(
            title='Error', message=f'No details for the {web} exists')
    else:
        messagebox.showinfo(
            title=web, message=f"Email: {search_file['username']} \nPassword:"
            f" {search_file['password']}")


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
web_entry = Entry(width=21)
web_entry.grid(row=1, column=1)
web_entry.focus()

# search
search_button = Button(text='Search', command=search, width=10)
search_button.grid(row=1, column=2)

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
generate_button = Button(text='Generate \nPassword',
                         command=generate, width=10)
generate_button.grid(row=3, column=2)

# add
add_button = Button(text='Add', width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
