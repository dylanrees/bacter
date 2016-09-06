import matplotlib
import matplotlib.pyplot as plt #for plotting
import numpy as np
import scipy
from scipy.optimize import curve_fit
import scipy.stats
import statistics
import matplotlib.image as mpimg


# confidence interval info
# http://stackoverflow.com/questions/15033511/compute-a-confidence-interval-from-sample-data

print("Loading the file....")

#loading the file
f=open('data.txt','r')
data=str(f.read())
data=data.split('\n')

#this loop splits the read file into a data array
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

#test data
#x = np.random.uniform(0., 100., 100)
#y = 3. * x + 2. + np.random.normal(0., 10., 100)

#engage in curve-fitting
def f(x, m, b):
    y = m*x + b
    return y

# this might help: http://www2.mpia-hd.mpg.de/~robitaille/PY4SCI_SS_2014/_static/15.%20Fitting%20models%20to%20data.html
print("Calculating curve fit...")
popt, pcov = curve_fit(f, x, y)
print("Here are your curve fit values:")
print(popt[0])
print(popt[1])

#calculate data length.  this will be truncated if some of your values aren't good
print("Here are the endpoint values of x:")
print((min(x)))
x1 = min(x)
print(f(min(x),popt[0],popt[1]))
y1 = f(min(x),popt[0],popt[1])
print((max(x)))
x2 = max(x)
print(f(max(x),popt[0],popt[1]))
y2 = f(max(x),popt[0],popt[1])

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

#initialize plot and plot for the first time

fig = plt.figure()
ax1 = fig.add_subplot(121)

# plot data

#ax1.scatter(x,y,color='blue',s=5,edgecolor='none')

ax1.plot(x,y, color="blue")
resistance = 1/popt[0] #unit is megaohms
plt.legend(['slope = '+str(popt[0])+'\nintercept = '+str(popt[1])+'\nresistance = '+str(resistance)+' MegaΩ'])
ax1.set_aspect(1./ax1.get_data_ratio()) # make axes square
#plt.plot(x, f(x,popt[0],popt[1]), color="red")
ax1.plot([x1,x2],[y1,y2],marker="o",color="red")

#add an image
ax2 = fig.add_subplot(122)
img=mpimg.imread('GoodTopo3.tiff')
ax2.axis([0, len(img), 0, len(img)]) #set the axes to match the image size
imgplot = ax2.imshow(img) #display the topo image
xplot = len(img)*float(xcoord[0])/float(xcoord[1])
yplot = 256 - len(img)*float(ycoord[0])/float(ycoord[1])
print("xplot = "+str(xplot))
print("yplot = "+str(yplot))
ax2.plot(xplot,yplot,marker="o") #put a marker on the right part of the topo image
print("The image's extent is "+str(len(img)))

# show the plot
plt.show()
