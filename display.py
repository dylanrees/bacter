#this is a gui program
#here is the tutorial:	http://www.tutorialspoint.com/python/python_gui_programming.htm

import tkinter
from tkinter import *

top = tkinter.Tk()

#filename entry field
var = StringVar()
label = Label( top, textvariable=var)

#filename label
var.set("Type a filename below (from the same directory) and press the button to load it.")
label.pack()
E1 = Entry(top, bd =5)
E1.pack()

#load button
load = tkinter.Button(top, text ="Load File")
load.pack()

#Terminal
var = StringVar()
label = Message( top, textvariable=var)
var.set("[ ] Topographic Image Loaded \n [ ] I-V and Coordinate Data Loaded \n [ ] Nanowire Profile Loaded")
label.pack()

#graph button
topo_button = tkinter.Button(top, text ="Create Annotated Topo Image")
topo_button.pack()

#iv button
iv_button = tkinter.Button(top, text ="Create I-V Curve")
iv_button.pack()

#resistivity button
res_button = tkinter.Button(top, text ="Calculate Resistivity")
res_button.pack()

top.mainloop()
