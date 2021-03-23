#import labries
from tkinter import *
from PIL import Image, ImageTk
import random


#inatinalize window
root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Dice Rolling Simulator')

#blank label line
Label(root, text='').pack()

#title for our game
Label(root, text = 'Welcome To Dice Rolling Simulator', font = 'CenturyGothic 15').pack()

#make image into a list
dice = ['dice_rolling_simulator//die1.png', 'dice_rolling_simulator//die2.png', 'dice_rolling_simulator//die3.png', 'dice_rolling_simulator//die4.png', 'dice_rolling_simulator//die5.png', 'dice_rolling_simulator//die6.png']
dice_image = ImageTk.PhotoImage(Image.open(random.choice(dice)))

#label for dice
image_label = Label(root, image = dice_image)
image_label.image = dice_image
image_label.pack(expand = True)

#func to roll the dice
def roll_dice():
    dice_image = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    image_label.config(image = dice_image)
    image_label.image = dice_image

#button to roll the dice
Button(root, text = 'Click me to roll the dice', font = 'monospace 10', fg = 'blue', command = roll_dice).pack()

#add a blank line
Label(root, text = '').pack()


#looping the main window
root.mainloop()