#this is a gui program
#here is the tutorial:	http://www.tutorialspoint.com/python/python_gui_programming.htm

import tkinter
from tkinter import *

top = tkinter.Tk()

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
    C1.select() #check the button
    term.insert(INSERT, "Hello.....\n")
load = tkinter.Button(top, text ="Load File", command=loadFunc)

#graph button
topo_button = tkinter.Button(top, text ="Create Annotated Topo Image")

#iv button
iv_button = tkinter.Button(top, text ="Create I-V Curve")

#resistivity button
res_button = tkinter.Button(top, text ="Calculate Resistivity")



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
