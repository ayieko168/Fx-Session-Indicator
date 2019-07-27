from tkinter import *
import threading
from time import sleep
import datetime

SIZE = "630x270+100+200"

root = Tk()
root.geometry(SIZE)
root.title("FOREX TRADING SESSIONS WORLDWIDE")
# root.resizable(0,0)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# The Top Time Showing Canvas
fm1 = Frame(root)
topTimeCanvas = Canvas(fm1, bg="green", height=30)

# Draw gard lines
for x in range(1, 24):

    x1 = 0 + (x*26.25)
    y1 = 30
    x2 = 0 + (x*26.25)
    y2 = 20
    
    # Draw the graduation lines
    topTimeCanvas.create_line(x1, y1, x2, y2) # Hour Marks
    # topTimeCanvas.create_line((x*13.125), y1, (x*13.125), y2+5, fill="red") # Half Hour Marks

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
body = Canvas(fm2, bg="black", height=200)

_DISABLED = "#f2f3f5"
_ACTIVE = "#00c020"
x1L = 26.25
x2L = 26.25
y1L = 0
y2L = 270
mousex = 0
mousey = 0

time = datetime.datetime.now().time()
Hr = time.hour
Min = time.minute
Sec = time.second        
TimeInSeconds = (Hr*3600)+(Min*60)+(Sec)

localSydneyTime = TimeInSeconds 

sydneyBar = body.create_rectangle(0, 10, 236.25, 40, fill=_DISABLED)
tokyoBar = body.create_rectangle(78.75, 50, 315, 80, fill=_DISABLED)
londonBar = body.create_rectangle(262.5, 90, 498.75, 120, fill=_DISABLED)
newYorkBar = body.create_rectangle(393.75, 130, 630, 160, fill=_DISABLED)

body.create_text(90, 25, text="Sydney  {} local time".format(""))
body.create_text(168.75, 65, text="Tokyo  {} local time".format("55 am"))
body.create_text(352.5, 105, text="London  {} local time".format("55 am"))
body.create_text(483.75, 145, text="NewYork  {} local time".format("55 am"))

CurrentTimeLine = body.create_line(x1L, y1L, x2L, y2L, fill=_ACTIVE)

def convertToStd(TSec):

    hrs = int(TSec / 3600)
    mins = int(float(".".join(["0", str(TSec / 3600).split(".")[1]])) * 60)
    sec = 60 - (datetime.datetime.now().time().second)

    return (hrs, mins, sec)


# Returns the Begins In or The Ends In value
def calcEndStart(session):

    global TimeInSeconds
    
    if session.lower() == "sydney":
        if body.itemcget(sydneyBar, "fill") == _DISABLED:
            startsTime = (86400 - TimeInSeconds) + (0 * 3600)
            return convertToStd(startsTime)
        else:
            endTime= (9*3600) - TimeInSeconds
            return convertToStd(endTime)          
    elif session.lower() == "tokyo":
        if body.itemcget(tokyoBar, "fill") == _DISABLED:
            startsTime = (86400 - TimeInSeconds) + (3 * 3600)
            return convertToStd(startsTime)
        else:
            endTime= (12*3600) - TimeInSeconds
            return convertToStd(endTime)
    elif session.lower() == "london":
        if body.itemcget(londonBar, "fill") == _DISABLED:
            startsTime = (86400 - TimeInSeconds) + (10 * 3600)
            return convertToStd(startsTime)
        else:
            endTime= (19*3600) - TimeInSeconds
            return convertToStd(endTime)
    elif session.lower() == "newyork":
        if body.itemcget(newYorkBar, "fill") == _DISABLED:
            startsTime = (86400 - TimeInSeconds) + (15 * 3600)
            return convertToStd(startsTime)
        else:
            endTime= (24*3600) - TimeInSeconds
            return convertToStd(endTime)
    

# Mouse position capture
def motion(event):
    global mousex, mousey
    mousex, mousey = event.x, event.y
    # print('{}, {}'.format(mousex, mousey))

def animate():
    
    global x1L, x2L, TimeInSeconds
    x1Ll, _, x2Ll, _ = body.coords(CurrentTimeLine)
    while 1:
        sleep(0.25)

        time = datetime.datetime.now().time()
        Hr = time.hour
        Min = time.minute
        Sec = time.second        
        TimeInSeconds = (Hr*3600)+(Min*60)+(Sec)

        # move the crrent time line
            # if x2Ll < 630:
            #     x1Ll = x1Ll + 26.25
            #     x2Ll = x2Ll + 26.25
            #     body.coords(CurrentTimeLine, x1Ll, 0.0, x2Ll, 270)
            # else:
            #     x1Ll = 0
            #     x2Ll = 0
        x1Ll = (TimeInSeconds * 26.25) / 3600
        x2Ll = (TimeInSeconds * 26.25) / 3600
        body.coords(CurrentTimeLine, x1Ll, 0.0, x2Ll, 270)

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
            
        # Status Bar Widget Update
        # print('{}, {}'.format(mousex, mousey))
        if ((mousex >= 0) and (mousex <= 236.25)) and ((mousey >= 10) and (mousey <= 30)):
            # print("Sydney")
            RemTime = calcEndStart("sydney")
            if body.itemcget(sydneyBar, "fill") == _DISABLED:
                label1.config(text="Sydney Session; Begins in {}Hrs {}Mins {}Sec ()".format(RemTime[0], RemTime[1], RemTime[2]))
            else:
                label1.config(text="Sydney Session; Ends in {}Hrs {}Mins {}Sec ()".format(RemTime[0], RemTime[1], RemTime[2]))
            
        if ((mousex >= 78.75) and (mousex <= 315)) and ((mousey >= 50) and (mousey <= 80)):
            # print("Tokyo")
            RemTime = calcEndStart("tokyo")
            if body.itemcget(tokyoBar, "fill") == _DISABLED:
                label1.config(text="Tokyo Session; Begins in {}Hrs {}Mins {}Sec ()".format(RemTime[0], RemTime[1], RemTime[2]))
            else:
                label1.config(text="Tokyo Session; Ends in {}Hrs {}Mins {}Sec ()".format(RemTime[0], RemTime[1], RemTime[2]))

        if ((mousex >= 262.5) and (mousex <= 498.75)) and ((mousey >= 90) and (mousey <= 120)):
            # print("London")
            RemTime = calcEndStart("London")
            if body.itemcget(londonBar, "fill") == _DISABLED:
                label1.config(text="London Session; Begins in {}Hrs {}Mins {}Sec ()".format(RemTime[0], RemTime[1], RemTime[2]))
            else:
                label1.config(text="London Session; Ends in {}Hrs {}Mins {}Sec ()".format(RemTime[0], RemTime[1], RemTime[2]))

        if ((mousex >= 393.75) and (mousex <= 630)) and ((mousey >= 130) and (mousey <= 160)):
            # print("NewYork")
            RemTime = calcEndStart("NewYork")
            if body.itemcget(newYorkBar, "fill") == _DISABLED:
                label1.config(text="NewYork Session; Begins in {}Hrs {}Mins {}Sec ()".format(RemTime[0], RemTime[1], RemTime[2]))
            else:
                label1.config(text="NewYork Session; Ends in {}Hrs {}Mins {}Sec ()".format(RemTime[0], RemTime[1], RemTime[2]))

        

th1 = threading.Thread(target=animate)
th1.start()


body.pack(fill=X)
fm2.pack(fill=X)

fm3 = Frame(root)
statusBar = Canvas(fm3, bg="grey", relief=GROOVE, bd=3)

status = "Welcome"
label1 = Label(statusBar, text=status, anchor=W, font="Purisa 12", bg="grey")
label1.pack(anchor="w", padx=10, pady=5)
root.after(5000, lambda:label1.config(text=""))

statusBar.pack(fill=X)
fm3.pack(fill=X)

root.bind('<Motion>', motion)
root.mainloop()

