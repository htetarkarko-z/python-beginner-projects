from tkinter import *
import random
import string


#initalize window
root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title("Password Generator")

#label within window
Label(root, text = 'Password Generator Application', font = '12').pack()
Label(root, text = 'by me', font = '8').pack(side = BOTTOM)

#get password lenght form user
Label(root, text = 'Password Length', font = '10').pack()
pass_len = IntVar()
Spinbox(root, from_ = 8, to_ = 32, textvariable = pass_len, width = 15).pack()

#generate a random password
pass_str = StringVar()
def generate():
    password = ''

    for i in range (0, 3):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits)
        for j in range (pass_len.get() - 3):
            password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    pass_str.set(password)

#button to generate
Button(root, text = 'click me to generate', font = '10', command = generate).pack(pady=5)
Entry(root, textvariable = pass_str).pack()

#end of the program
root.mainloop()