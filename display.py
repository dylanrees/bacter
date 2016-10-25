#this is a gui program
#here is the tutorial:	http://www.tutorialspoint.com/python/python_gui_programming.htm

import tkinter
from tkinter import *
import matplotlib.image as mpimg
import functions
import matplotlib.pyplot as plt #for plotting
import numpy as np

top = tkinter.Tk()
global data
global left_trunc #left truncation point for iv curves
global right_trunc #right truncation point for iv curves
global left_trunc_ht #left truncation point for ht curves
global right_trunc_ht #right truncation point for ht curves
left_trunc = -1000000 #initial large values prevent truncation
right_trunc = 1000000
left_trunc_ht = -1000000
right_trunc_ht = 1000000
global xpos #topo coordinates
global ypos #topo coordinates
xpos = 0
ypos = 0
data = [] # will hold the file data right when it comes out the pipe
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
left_text_ht = StringVar()
left_text_ht.set("HT Left Truncation:")
right_text_ht = StringVar()
right_text_ht.set("HT Right Truncation:")
left_label_ht = Label( top, textvariable=left_text_ht)
right_label_ht = Label( top, textvariable=right_text_ht)

def arrayProc(q):
    #this function splits the read file into a data array
    #form: input[a][b]
    # a represents the row in the list
    # b=[0,1] represents whether it's x or y
    global xpos
    global ypos
    i=0

    #pull out the I-V curve coordinates at the beginning and then pop them from the dataset
    xcoord=q[0].split('\t')
    ycoord=q[1].split('\t')
    print("x="+xcoord[0]+"um")
    print("y="+ycoord[0]+"um")
    xpos = q[0]
    q.pop(0)
    ypos = q[0]
    q.pop(0)

    while i<len(q):
        if len(q[i])==0:
            q.pop(i) #discards any dummy entry formed at the end due to the split function
        else:
            #print("q["+str(i)+"]= "+str(q[i]))
            q[i]=q[i].split('\t')
            #print("q["+str(i)+"][0]= "+str(q[i][0]))
            #print("q["+str(i)+"][1]= "+str(q[i][1]))
            q[i][0]=float(q[i][0])
            q[i][1]=float(q[i][1])
        i=i+1
    return(q)

def topoPlot():
    global xpos
    global ypos
    print("xpos = "+str(xpos))
    print("ypos = "+str(ypos))
    xpos=xpos.split('\t')
    ypos=ypos.split('\t')
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    img=mpimg.imread('Topo.png')
    ax1.axis([0, len(img), 0, len(img)]) #set the axes to match the image size
    imgplot = ax1.imshow(np.flipud(img)) #display the topo image
    xplot = len(img)*float(xpos[0])/float(xpos[1])
    yplot = len(img)*float(ypos[0])/float(ypos[1])
    ax1.plot(xplot,yplot,marker="o",color="red") #put a marker on the right part of the topo image
    plt.show()
    #Sy print("The image's extent is "+str(len(img)))

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

def integrate(q):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    i=0
    while i<len(q)-1:
        x1.append(q[i][0])
        y1.append(q[i][1])
        i = i+1
    i=0
    output = np.trapz(y1,x1)
    term.insert(INSERT, "area: "+str(output)+"nm2\n")

def truncate(q, l, r):
    #calculate data length for curve fit plotting.  only uses the "include" data from the step above
    #q is the input data
    #l is the left truncation
    #r is the right truncation
    q_include = []
    i=0
    while (i<len(q)-1):
        if (q[i][0] > l) and (q[i][0] < r):
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
        topoPlot()
        #try:
        #    topoPlot()
        #    term.insert(INSERT, "...yes!\n")
        #except:
        #    term.insert(INSERT, "...oomf\n")
    else:
        term.insert(INSERT, "Need to load topo image.\n")
topo_button = tkinter.Button(top, text ="Create Annotated Topo Image",command=topoFunc)

#iv button
def ivFunc():
    global data
    global left_trunc
    global right_trunc
    if ivload.get() == 1:
        term.insert(INSERT, "10010101001010101010\n")
        q = arrayProc(data)
        qinc = truncate(q, left_trunc, right_trunc)
        fits = functions.curveFit(qinc)
        functions.ivplot(q,qinc,fits)
    else:
        term.insert(INSERT, "Need to load IV data.\n")

iv_left_entry = Entry(top, bd =2)
iv_right_entry = Entry(top, bd =2)
ht_left_entry = Entry(top, bd =2)
ht_right_entry = Entry(top, bd =2)

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

def leftFuncHt():
    global left_trunc_ht
    leftstring=ht_left_entry.get()
    try:
        left_trunc_ht = float(leftstring)
        term.insert(INSERT, "Set the left HT truncation to "+leftstring+"\n")
    except:
        term.insert(INSERT, "Not a valid numerical value."+leftstring+"\n")

def rightFuncHt():
    global right_trunc_ht
    rightstring=ht_right_entry.get()
    try:
        right_trunc_ht = float(rightstring)
        term.insert(INSERT, "Set the right HT truncation to "+rightstring+"\n")
    except:
        term.insert(INSERT, "Not a valid numerical value."+rightstring+"\n")


iv_button = tkinter.Button(top, text ="Create I-V Curve",command=ivFunc)

iv_left_button = tkinter.Button(top, text ="Set", command=leftFunc)
iv_right_button = tkinter.Button(top, text ="Set", command=rightFunc)
ht_left_button = tkinter.Button(top, text ="Set", command=leftFuncHt)
ht_right_button = tkinter.Button(top, text ="Set", command=rightFuncHt)

#resistivity button
def resFunc():
    global data
    global left_trunc_ht
    global right_trunc_ht
    if htload.get() == 1:
        term.insert(INSERT, "10010101001010101010\n")
        q = arrayProc(data)
        qinc = truncate(q, left_trunc_ht, right_trunc_ht)
        integrate(qinc)
        s = [] #pass an empty set for curve-fitting
        functions.ivplot(q,qinc,s)
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
left_label_ht.pack()
ht_left_entry.pack()
ht_left_button.pack()
right_label_ht.pack()
ht_right_entry.pack()
ht_right_button.pack()
term.pack()

#let 'er rip
top.mainloop()
