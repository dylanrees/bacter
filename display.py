#this is a gui program
#here is the tutorial:	http://www.tutorialspoint.com/python/python_gui_programming.htm

import tkinter
#import tkMessageBox

top = tkinter.Tk()
# Code to add widgets will go here...

open = tkinter.Button(top, text ="Open File")
save = tkinter.Button(top, text ="Save File")

open.pack()
save.pack()
top.mainloop()