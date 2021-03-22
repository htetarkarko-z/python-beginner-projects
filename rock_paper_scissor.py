#import labires
from tkinter import *
import random


#init window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock, Paper, Scissors')
root.config(bg='#fffff0')

#title in window
Label(root, text='Rock, Paper, Scissors', font='monospace 15 bold', bg='#fffff0').pack()

#let user to type one
user_take = StringVar()
Label(root, text='Enter one of the following: rock paper scissors: ', font='ubuntu 12', bg='#fffff0').place(x = 20,y=70)
Entry(root, textvariable=user_take, font='ubuntu 12', bg='#fffff9').place(x = 90, y = 130)

#let the computer chose one
comp_pick = random.randint(1, 3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
elif comp_pick == 3:
    comp_pick = 'scissors'

#main func
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick not in ['rock', 'paper', 'scissor']:
        Result.set('invalid character')
    else:
        if user_pick == comp_pick:
            Result.set('tie')
        elif (user_pick == 'rock' and comp_pick == 'scissors') or (user_pick == 'scissor' and comp_pick == 'paper') or (user_pick == 'paper' and comp_pick == 'rock'):
            Result.set('You win')
        else:
            Result.set('You lose')

#reset func
def reset():
    Result.set('')
    user_take.set('')


#exit func
def exit():
    root.destroy()

#define buttons
Label(root, font = 'ubuntu 10', textvariable = Result, bg ='#fffff0', width = 50).place(x=25, y = 250)
Button(root, font = 'ubuntu 13', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)
Button(root, font = 'ubuntu 13', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = reset).place(x=70,y=310)
Button(root, font = 'ubuntu 13', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = exit).place(x=230,y=310)


root.mainloop()