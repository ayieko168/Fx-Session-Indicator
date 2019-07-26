from tkinter import *
from tkinter import font
import math

class Balloon():

    def __init__(self, master, xpos=None, ypos=None, text=None):

        global t3
        # FONT = ('Times', 20, 'bold')
        FONT = font.Font(family='Helvetica', size=40, weight='bold')
        # FONT = 12

        self.master = master
        self.text = text
        self.xpos = xpos
        self.ypos = ypos

        t3 = Toplevel(master)
        
        # Txt = Label(t3, bg="red", text=text, font=12)
        Txt = Text(t3, font=FONT, bg='#f9f5d0')
        Txt.insert(0.1, text)

        fontSize = FONT.cget("size")
        fontSizePxl = math.floor((fontSize * 1) / 0.73977124)
        # print("fontPxl = ", fontSizePxl)
        # print("fontSize = ", fontSize)
        xters = len(text)
        xlen = fontSizePxl * xters

        Txt.config(width=xters)
        Txt.pack(pady=3)

        windowHeight = Txt.cget("height")

        # print("txtxHt = ", Txt.cget("height"))
        # print("txtxWd = ", Txt.cget("width"))

        
        t3.geometry('{}x{}+{}+{}'.format(xlen, windowHeight, xpos, ypos))
        t3.overrideredirect(1)


    def destroy(self):

        t3.destroy()

