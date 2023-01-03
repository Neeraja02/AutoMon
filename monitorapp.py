import tkinter as tk
from tkinter import ttk
import time
import random
import tkinter.font as tkFont
import sim as CTS

class Monitor(tk.Tk):

    def __init__(self):

        super().__init__()

        # configure the root window
        self.title('MONITORING APPLICATION')

        #setting window size
        width=400
        height=200

        # getting screen's width in pixels
        screenwidth = self.winfo_screenwidth()

        # getting screen's height in pixels
        screenheight = self.winfo_screenheight()

        alignstr = '%dx%d+%d+%d' % (width, height, 830, 100)
        self.geometry(alignstr)
        self.resizable(True, True)
        self.geometry('400x200')
        #self['bg'] = 'yellow'

        #start button
        global startButton
        startButton=tk.Button(self)
        startButton["activebackground"] = "#5fb878"
        startButton["activeforeground"] = "#5fb878"
        startButton["anchor"] = "center"
        startButton["bg"] = "#5fb878"
        startButton["disabledforeground"] = "#999999"
        ft = tkFont.Font(family='Times',size=17)
        startButton["font"] = ft
        startButton["fg"] = "#fdfbee"
        startButton["justify"] = "center"
        startButton["text"] = "START"
        startButton["relief"] = "raised"
        startButton.place(x=100,y=70,width=90,height=40)
        startButton["command"] = self.startButton_command

        #stop button
        global stopButton
        stopButton=tk.Button(self)
        stopButton["activebackground"] = "#5fb878"
        stopButton["activeforeground"] = "#5fb878"
        stopButton["anchor"] = "center"
        stopButton["bg"] = "#ff0000"
        stopButton["disabledforeground"] = "#999999"
        ft = tkFont.Font(family='Times',size=17)
        stopButton["font"] = ft
        stopButton["fg"] = "#fdfbee"
        stopButton["justify"] = "center"
        stopButton["text"] = "STOP"
        stopButton["relief"] = "raised"
        stopButton.place(x=240,y=70,width=90,height=40)
        stopButton["command"] = self.stopButton_command
        
    #function that is called when start button is pressed
    def startButton_command(self):
        global load
        load = CTS.WheelLoader()
        load.mainloop()
        #CTS.storeButton["state"] = "disabled"        
        return

    def stopButton_command(self):
        #CTS.storeButton["state"] = "normal"
        load.destroy()
        return
        
if __name__ == "__main__":
    obj = Monitor()
    obj.mainloop()
