import time
from pynput.keyboard import Key, Controller
from tkinter import *
from tkinter import ttk
import winsound

local_time = time.ctime()
keyboard = Controller()

def worktimer(*args):
    try:
        set_time = float(time_entry.get())*60
        set_task = task_entry.get()
        time.sleep(set_time)
        keyboard.press(Key.ctrl)
        keyboard.press("s")
        keyboard.release(Key.ctrl)
        keyboard.release("s")
        winsound.PlaySound('SystemExclamation',winsound.SND_ALIAS)
        print(set_task, " completed.")
        ttk.Label(mainframe, text=(set_task+" completed!")).grid(column=3 , row=4, sticky=W)
    except ValueError as error:
        ttk.Label(mainframe, text=error).grid(column=3 , row=4, sticky=W)

root = Tk()
root.title("Work Timer")

mainframe = ttk.Frame(root, padding="15 10 50 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

timeVar = StringVar()
textVar = StringVar()
time_entry =ttk.Entry(mainframe, width=7, textvariable=timeVar)
time_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="time length(minutes)").grid(column=3 , row=1, sticky=W)
task_entry = ttk.Entry(mainframe, width=7, textvariable=textVar)
task_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Task").grid(column=3, row=2, sticky=W)

ttk.Button(mainframe, text="start timer", command= worktimer).grid(column=3, row=3, sticky=W)

root.mainloop()