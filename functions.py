import matplotlib
import matplotlib.pyplot as plt #for plotting
import numpy as np
import scipy
from scipy.optimize import curve_fit
import scipy.stats
import statistics
import matplotlib.image as mpimg
import time

#curve-fitting function
def f(x, m, b):
    y = m*x + b
    return y

def curveFit(q):
    print("Calculating curve fit...")
    i=0
    x = []
    y = []
    while i<len(q):
        x.append(q[i][0])
        y.append(q[i][1])
        i = i+1
    popt, pcov = curve_fit(f, x, y)
    print("Here are your curve fit values:")
    print(popt[0])
    print("y intercept is :")
    print(popt[1])
    resist = 1/popt[0]
    print("resistance is:")
    print(resist)
    return(popt)

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

def ivplot(q,r,s):
    #q = main data
    #r = truncated data
    #s = curve fits
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('Current (uA)')
    ax1.set_xlabel('Voltage (mV)')
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
    while i<len(r)-1:
        x2.append(r[i][0])
        y2.append(r[i][1])
        i = i+1
    #ax1.scatter(x,y,color='blue',s=5,edgecolor='none')
    #ax1.plot(x_include,y_include, color="blue")
    #ax1.plot(x_exclude_l,y_exclude_l, color="lightblue")
    #ax1.plot(x_exclude_r,y_exclude_r, color="lightblue")
    #resistance = 1/popt[0] #unit is megaohms
    #plt.legend(['slope = '+str(popt[0])+'\nintercept = '+str(popt[1])+'\nresistance = '+str(resistance)+' MegaΩ'])
    #ax1.set_aspect(1./ax1.get_data_ratio()) # make axes square
    #ax1.plot([x1,x2],[y1,y2],marker="o",color="red")
    ax1.plot(x1,y1,color="lightblue")
    ax1.plot(x2,y2,color="blue")
    if len(s)>0:#iv plot option
        line_x1 = x2[0]
        line_x2 = x2[len(x2)-1]
        line_y1 = f(x2[0],s[0],s[1])
        line_y2 = f(x2[len(x2)-1],s[0],s[1])
        ax1.plot([line_x1,line_x2],[line_y1, line_y2],marker="o",color="red")
    else: #ht plot option
        ax1.set_ylabel('Height (nm)')
        ax1.set_xlabel('Width (nm)')
    plt.show()
