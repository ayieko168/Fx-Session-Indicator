from tkinter import *
import threading
from time import sleep
import Balloon

SIZE = "630x270+100+200"

root = Tk()
root.geometry(SIZE)
root.title("FOREX TRADING SESSIONS WORLDWIDE")
root.resizable(0,0)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# The Top Time Showing Canvas
fm1 = Frame(root)
topTimeCanvas = Canvas(fm1, bg="green", height=30)


for x in range(1, 24):

    x1 = 0 + (x*26.25)
    y1 = 30
    x2 = 0 + (x*26.25)
    y2 = 20
    
    # Draw the graduation lines
    topTimeCanvas.create_line(x1, y1, x2, y2)

    # format the graduation text and digits to show 12hr system
    if x < 12:
        if x%2 == 1:
            topTimeCanvas.create_text(x1, y2-5, text = "{}am".format(x))
        else:
            pass
    else:
        if x%2 == 1:
            topTimeCanvas.create_text(x1, y2-5, text = "{}pm".format(x%12))
        else:
            pass
    
    # # uncomment to show 24hr System
    # if x%2 == 1:
    #     topTimeCanvas.create_text(x1, y2-5, text = "{:02}:00".format(x))

topTimeCanvas.pack(fill=X)
fm1.pack(fill=X)

# The Body 
fm2 = Frame(root)
body = Canvas(fm2, bg="black")

_DISABLED = "#f2f3f5"
_ACTIVE = "#00c020"
x1L = 26.25
x2L = 26.25
y1L = 0
y2L = 270
mousex = 0
mousey = 0


sydneyBar = body.create_rectangle(0, 10, 236.25, 40, fill=_DISABLED)
tokyoBar = body.create_rectangle(78.75, 50, 315, 80, fill=_DISABLED)
londonBar = body.create_rectangle(262.5, 90, 498.75, 120, fill=_DISABLED)
newYorkBar = body.create_rectangle(393.75, 130, 630, 160, fill=_DISABLED)

body.create_text(90, 25, text="Sydney  {} local time".format("55 am"))
body.create_text(168.75, 65, text="Tokyo  {} local time".format("55 am"))
body.create_text(352.5, 105, text="London  {} local time".format("55 am"))
body.create_text(483.75, 145, text="NewYork  {} local time".format("55 am"))

CurrentTimeLine = body.create_line(x1L, y1L, x2L, y2L, fill=_ACTIVE)

# Mouse position capture
def motion(event):
    global mousex, mousey

    mousex, mousey = event.x, event.y
    # print('{}, {}'.format(mousex, mousey))

def animate():
    
    global x1L, x2L
    x1Ll, _, x2Ll, _ = body.coords(CurrentTimeLine)
    while 1:
        sleep(0.1)

        # move the crrent time line
        if x2Ll < 630:
            x1Ll = x1Ll + 21
            x2Ll = x2Ll + 21
            body.coords(CurrentTimeLine, x1Ll, 0.0, x2Ll, 270)
        else:
            x1Ll = 0
            x2Ll = 0

        # light up active sessions
        # Sydney
        if (x2Ll >= 0) and (x2Ll<=236.25):
            body.itemconfig(sydneyBar, fill=_ACTIVE)
        else:
            body.itemconfig(sydneyBar, fill=_DISABLED)
        # Tokyo
        if (x2Ll >= 78.75) and (x2Ll<=315):
            body.itemconfig(tokyoBar, fill=_ACTIVE)
        else:
            body.itemconfig(tokyoBar, fill=_DISABLED)
        # London
        if (x2Ll >= 262.5) and (x2Ll<=498.75):
            body.itemconfig(londonBar, fill=_ACTIVE)
        else:
            body.itemconfig(londonBar, fill=_DISABLED)
        # NewYork
        if (x2Ll >= 393.75) and (x2Ll<=630):
            body.itemconfig(newYorkBar, fill=_ACTIVE)
        else:
            body.itemconfig(newYorkBar, fill=_DISABLED)
            
        # Balloon Widget
        # print('{}, {}'.format(mousex, mousey))
        if ((mousex >= 0) and (mousex <= 236.25)) and ((mousey >= 10) and (mousey <= 30)):
            print("Sydney")
        if ((mousex >= 78.75) and (mousex <= 315)) and ((mousey >= 50) and (mousey <= 80)):
            print("Tokyo")
        if ((mousex >= 262.5) and (mousex <= 498.75)) and ((mousey >= 90) and (mousey <= 120)):
            print("London")
        if ((mousex >= 393.75) and (mousex <= 630)) and ((mousey >= 130) and (mousey <= 160)):
            print("NewYork")
        



th1 = threading.Thread(target=animate)
th1.start()


body.pack(fill=X)
fm2.pack(fill=X)

root.bind('<Motion>', motion)
root.mainloop()

