#this is a gui program
#here is the tutorial:	http://www.tutorialspoint.com/python/python_gui_programming.htm

import tkinter
from tkinter import *
import matplotlib.image as mpimg
import functions

top = tkinter.Tk()
global data
global left_trunc
global right_trunc
left_trunc = -1000000
right_trunc = 1000000
data = [] # will hold the data right when it comes out the pipe
data_iv = [] #specifically iv data
data_ht = [] #specifically height data
data_topo = [] #specifically topo map data

#filename label
var = StringVar()
var.set("Type a filename below (from the same directory) and press the button to load it.")
label = Label( top, textvariable=var)
left_text = StringVar()
left_text.set("IV Left Truncation:")
right_text = StringVar()
right_text.set("IV Right Truncation:")
left_label = Label( top, textvariable=left_text)
right_label = Label( top, textvariable=right_text)

#filename entry field
E1 = Entry(top, bd =5)

#checkmarks
topoload = tkinter.IntVar()
C1 = Checkbutton(top, text = "Topo Image Loaded", state=DISABLED, variable=topoload)

ivload = tkinter.IntVar()
C2 = Checkbutton(top, text = "I-V Coordinate Data Loaded", state=DISABLED, variable=ivload)

htload = tkinter.IntVar()
C3 = Checkbutton(top, text = "Nanowire Height Profile Loaded", state=DISABLED, variable = htload)

#terminal
term = Text(top)

def truncate(q):
    #calculate data length for curve fit plotting.  only uses the "include" data from the step above
    q_include = []
    global left_trunc
    global right_trunc
    i=0
    while (i<len(q)-1):
        if (q[i][0] > left_trunc) and (q[i][0] < right_trunc):
                q_include.append(q[i])
        i = i+1
    return(q_include)

#load button
def loadFunc(): #the function that the load button uses
    global data
    loadstring=E1.get() #load the text field text
    term.insert(INSERT, "Trying to load \""+loadstring+"\"\n")
    try:
        f=open(loadstring,'r')
        try:
            data=str(f.read())
            data=data.split('\n')
            if data[0]=="iv":
                data_iv = data
                data_iv.pop(0) #take the "iv" tag off the beginning
                print("data_iv 1: "+str(data_iv))
                print("data: "+str(data))
                C2.select() #check the IV button
                term.insert(INSERT, "...successfully loaded IV data!\n"         )
            elif data[0]=="ht":
                data_ht = data
                data_ht.pop(0)
                C3.select() #check the height button
                term.insert(INSERT, "...successfully loaded height data!\n")
                print(data_ht[0])
            else:
                term.insert(INSERT, "...not sure what type of file this is.\n")
        except:
            try:
                data_topo=mpimg.imread(loadstring)
                term.insert(INSERT, "...successfully loaded topo image!\n")
                C1.select() #check the topo button
            except:
                term.insert(INSERT, "...not sure what type of file this is.\n")
    except:
        term.insert(INSERT, "...failed.\n")
load = tkinter.Button(top, text ="Load File", command=loadFunc)

#graph button
def topoFunc():
    if topoload.get() == 1:
        term.insert(INSERT, "10010101001010101010...\n")
        try:
            functions.topoplot()
            term.insert(INSERT, "...yes!\n")
        except:
            term.insert(INSERT, "...oomf\n")
    else:
        term.insert(INSERT, "Need to load topo image.\n")
topo_button = tkinter.Button(top, text ="Create Annotated Topo Image",command=topoFunc)

#iv button
def ivFunc():
    global data
    if ivload.get() == 1:
        term.insert(INSERT, "10010101001010101010\n")
        q = functions.arrayProc(data)
        qinc = truncate(q)
        fits = functions.curveFit(qinc)
        functions.ivplot(q,qinc,fits)
    else:
        term.insert(INSERT, "Need to load IV data.\n")

iv_left_entry = Entry(top, bd =2)
iv_right_entry = Entry(top, bd =2)

def leftFunc():
    global left_trunc
    leftstring=iv_left_entry.get()
    try:
        left_trunc = float(leftstring)
        term.insert(INSERT, "Set the left IV truncation to "+leftstring+"\n")
    except:
        term.insert(INSERT, "Not a valid numerical value."+leftstring+"\n")


def rightFunc():
    global right_trunc
    rightstring=iv_right_entry.get()
    try:
        right_trunc = float(rightstring)
        term.insert(INSERT, "Set the right IV truncation to "+rightstring+"\n")
    except:
        term.insert(INSERT, "Not a valid numerical value."+rightstring+"\n")


iv_button = tkinter.Button(top, text ="Create I-V Curve",command=ivFunc)

iv_left_button = tkinter.Button(top, text ="Set", command=leftFunc)
iv_right_button = tkinter.Button(top, text ="Set", command=rightFunc)

#resistivity button
def resFunc():
    if htload.get() == 1:
        term.insert(INSERT, "10010101001010101010\n")
    else:
        term.insert(INSERT, "Need to load wire profile.\n")
res_button = tkinter.Button(top, text ="Calculate Resistivity",command=resFunc)

#pack all the interface buttons in the proper order
label.pack()
E1.pack()
load.pack()
C1.pack()
C2.pack()
C3.pack()
topo_button.pack()
iv_button.pack()
left_label.pack()
iv_left_entry.pack()
iv_left_button.pack()
right_label.pack()
iv_right_entry.pack()
iv_right_button.pack()
res_button.pack()
term.pack()

#let 'er rip
top.mainloop()
