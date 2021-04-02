from tkinter import *
import datetime
import time
import winsound
from sys import exit


#alarm function take user pass input and check if the it's now
def alarm(set_alarm_time):
    while True:
        time.sleep(1)
        now = datetime.datetime.now().strftime('%H:%M:%S')
        date = datetime.datetime.now().strftime('%d:%m:%Y')
        print("The set date is: ", date)
        print(now)
        if now == set_alarm_time:
            print('Time to wakeup')
            winsound.PlaySound('recycle.wav', winsound.SND_ASYNC)
            notification()


def set_alarm():
    set_alarm_time = f"{hour.get()}:{minutes.get()}:{seconds.get()}"
    alarm(set_alarm_time)

def notification():
    noti = Tk()
    noti.after(2000, exit)
    Button(noti, text = 'exit', font = ("Verdana", 12), bg = "yellow", command = exit).pack()
    noti.geometry('400x50+700+500')
    noti.mainloop()


#initialize window
root = Tk()
root.title('Alarm Clock')
root.geometry('400x200')
root.resizable(0, 0)
root.attributes('-alpha',0.95)
#adding label
Label(root, text = 'Enter time in 24 hour format').place(x = 120, y = 160)
Label(root, text = 'When to wake\n you up').place(x = 10, y = 80)
Label(root, text = 'Hour    Minutes    Seconds').place(x = 120, y = 10)

#get user input
hour = StringVar()
minutes = StringVar()
seconds = StringVar()

Entry(root, textvariable = hour, width = 5).place(x = 120, y = 35)
Entry(root, textvariable = minutes, width = 5).place(x = 170, y = 35)
Entry(root, textvariable = seconds, width = 5).place(x = 220, y = 35)

#summit user input
Button(root, text = 'Set Alarm Clock', command = set_alarm).place(x = 140, y = 80)

root.mainloop()
