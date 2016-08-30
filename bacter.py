import matplotlib
import matplotlib.pyplot as plt #for plotting
import numpy as np
import scipy
from scipy.optimize import curve_fit

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

popt, pcov = curve_fit(f, x, y)
print popt[0]
print popt[1]

#initialize plot and plot for the first time

fig = plt.figure()
ax1 = fig.add_subplot(111)

# plot data
ax1.scatter(x,y,color='blue',s=5,edgecolor='none')
ax1.set_aspect(1./ax1.get_data_ratio()) # make axes square

plt.plot(x,y, color="blue")
plt.plot(x, f(x,popt[0],popt[1]), color="red")

# show the plot
plt.show()
