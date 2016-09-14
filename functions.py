import matplotlib
import matplotlib.pyplot as plt #for plotting
import numpy as np
import scipy
from scipy.optimize import curve_fit
import scipy.stats
import statistics
import matplotlib.image as mpimg
import time

def arrayProc(data):
    #this function splits the read file into a data array
    #form: input[a][b]
    # a represents the row in the list
    # b=[0,1] represents whether it's x or y
    i=0
    x = []
    y = []

    #pull out the I-V curve coordinates at the beginning and then pop them from the dataset
    xcoord=data[0].split('\t')
    ycoord=data[1].split('\t')
    print(xcoord[0])
    print(ycoord[0])
    data.pop(0)
    data.pop(0)

    while i<len(data):
        #gprint(data[i])
        data[i]=data[i].split('\t')
        #data[i][0]=float(data[i][0])
        x.append(float(data[i][0]))
        #data[i][1]=float(data[i][1])
        y.append(float(data[i][1]))
        i=i+1
    return(data)

#curve-fitting function
def f(x, m, b):
    y = m*x + b
    return y

def curveFit(x):
    # split the data into two arrays, one of which is discarded from fitting but still plotted
    left = -300 #data clip area on the left
    right = 100 #data clip area on the right
    i = 0 #loop index
    #data to be included in curve fitting:
    x_include = []
    y_include = []
    #data excluded on the left:
    x_exclude_l = []
    y_exclude_l = []
    #data excluded on the right:
    x_exclude_r = []
    y_exclude_r = []
    while (i<len(x)-1):
        if (x[i] < left):
            x_exclude_l.append(x[i])
            y_exclude_l.append(y[i])
        elif (x[i] > right):
            x_exclude_r.append(x[i])
            y_exclude_r.append(y[i])
        else:
            x_include.append(x[i])
            y_include.append(y[i])
            i = i+1

    # curve fit calculation (using only "include" data from above)
    print("Calculating curve fit...")
    popt, pcov = curve_fit(f, x_include, y_include)
    print("Here are your curve fit values:")
    print(popt[0])
    print(popt[1])
    return(x)

def endpoints():
    #calculate data length for curve fit plotting.  only uses the "include" data from the step above
    print("Here are the endpoint values of x_include:")
    print((min(x_include)))
    x1 = min(x_include)
    print(f(min(x_include),popt[0],popt[1]))
    y1 = f(min(x_include),popt[0],popt[1])
    print((max(x_include)))
    x2 = max(x_include)
    print(f(max(x_include),popt[0],popt[1]))
    y2 = f(max(x_include),popt[0],popt[1])
    return(x1)

def deviation():
    #calculate standard deviation from the curve fit
    print("Calculating deviation...")
    deviat = [] #deviation between curve fit and
    i=0
    while i<len(x):
        deev = y[i]-f(x[i],popt[0],popt[1])
        #print(deev)
        deviat.append(deev)
        i=i+1
        standard_deviation = statistics.stdev(deviat)
    print("Standard deviation is "+str(standard_deviation))
    return(standard_deviation)

def ivplot():
    #ax1.scatter(x,y,color='blue',s=5,edgecolor='none')
    ax1.plot(x_include,y_include, color="blue")
    ax1.plot(x_exclude_l,y_exclude_l, color="lightblue")
    ax1.plot(x_exclude_r,y_exclude_r, color="lightblue")
    resistance = 1/popt[0] #unit is megaohms
    plt.legend(['slope = '+str(popt[0])+'\nintercept = '+str(popt[1])+'\nresistance = '+str(resistance)+' MegaΩ'])
    ax1.set_aspect(1./ax1.get_data_ratio()) # make axes square
    ax1.plot([x1,x2],[y1,y2],marker="o",color="red")

def topoplot():
    #add an image
    ax2 = fig.add_subplot(122)
    img=mpimg.imread('GoodTopo3.tiff')
    ax2.axis([0, len(img), 0, len(img)]) #set the axes to match the image size
    imgplot = ax2.imshow(np.flipud(img)) #display the topo image
    xplot = len(img)*float(xcoord[0])/float(xcoord[1])
    yplot = 256 - len(img)*float(ycoord[0])/float(ycoord[1])
    print("xplot = "+str(xplot))
    print("yplot = "+str(yplot))
    ax2.plot(xplot,yplot,marker="o") #put a marker on the right part of the topo image
    print("The image's extent is "+str(len(img)))
