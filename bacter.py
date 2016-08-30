import matplotlib
import matplotlib.pyplot as plt #for plotting
import time
import numpy as np
import matplotlib.pyplot as plt

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
    #print(data[i])
    data[i]=data[i].split('\t')
    #data[i][0]=float(data[i][0])
    x.append(float(data[i][0]))
    #data[i][1]=float(data[i][1])
    y.append(float(data[i][1]))
    i=i+1

#initialize plot and plot for the first time

fig = plt.figure()
ax1 = fig.add_subplot(111)

## left panel
ax1.scatter(x,y,color='blue',s=5,edgecolor='none')
ax1.set_aspect(1./ax1.get_data_ratio()) # make axes square

plt.show()
