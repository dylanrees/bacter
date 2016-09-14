#this is a gui program
#here is the tutorial:	http://www.tutorialspoint.com/python/python_gui_programming.htm

import tkinter
from tkinter import *
import matplotlib.image as mpimg
import functions

top = tkinter.Tk()
data = [] # will hold the data right when it comes out the pipe
data_iv = [] #specifically iv data
data_ht = [] #specifically height data
data_topo = [] #specifically topo map data

#filename label
var = StringVar()
var.set("Type a filename below (from the same directory) and press the button to load it.")
label = Label( top, textvariable=var)

#filename entry field
E1 = Entry(top, bd =5)

#checkmarks
C1 = Checkbutton(top, text = "Topo Image Loaded", state=DISABLED)
C2 = Checkbutton(top, text = "I-V Coordinate Data Loaded", state=DISABLED)
C3 = Checkbutton(top, text = "Nanowire Topo Profile Loaded", state=DISABLED)

#terminal
term = Text(top)

#load button
def loadFunc(): #the function that the load button uses

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
                C1.select() #check the IV button
                term.insert(INSERT, "...successfully loaded IV data!\n")
            elif data[0]=="ht":
                data_ht = data
                data_ht.pop(0)
                C2.select() #check the height button
                term.insert(INSERT, "...successfully loaded height data!\n")
                print(data_ht[0])
            else:
                term.insert(INSERT, "...not sure what type of file this is.\n")
        except:
            try:
                data_topo=mpimg.imread(loadstring)
                term.insert(INSERT, "...successfully loaded topo image!\n")
                C3.select() #check the topo button
            except:
                term.insert(INSERT, "...not sure what type of file this is.\n")
    except:
        term.insert(INSERT, "...failed.\n")
load = tkinter.Button(top, text ="Load File", command=loadFunc)

#graph button
def topoFunc():
    term.insert(INSERT, "Need to load topo image.\n")
topo_button = tkinter.Button(top, text ="Create Annotated Topo Image",command=topoFunc)

#iv button
def ivFunc():
    term.insert(INSERT, "Need to load IV data.\n")
iv_button = tkinter.Button(top, text ="Create I-V Curve",command=ivFunc)

#resistivity button
def resFunc():
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
res_button.pack()
term.pack()

#let 'er rip
top.mainloop()
