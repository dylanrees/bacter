#temporary program for integration
import numpy as np
import matplotlib
import matplotlib.pyplot as plt #for plotting

#http://docs.scipy.org/doc/numpy/reference/generated/numpy.trapz.html

def integrate(q,r):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    i=0
    while i<len(q):
        x1.append(q[i][0])
        y1.append(q[i][1])
        i = i+1
    i=0
    while i<len(r):
        x2.append(r[i][0])
        y2.append(r[i][1])
        i = i+1
    output = np.trapz(x1,y1)
    print("area: "+str(output)+" square picometers or whatever")
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('Current (nA)')
    ax1.set_xlabel('Voltage (uV)')
    ax1.plot(x1,y1,color="blue")
    ax1.plot(x2,y2,color="lightblue")
    plt.show()

v = [[2,4],[3,9],[4,16]]
w = [[1,1],[2,4],[3,9],[4,16]]

integrate(v,w)
