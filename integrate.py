#temporary program for integration
import numpy as np

#http://docs.scipy.org/doc/numpy/reference/generated/numpy.trapz.html

data = []
data2 = [1,2,3]
data = data2
output = np.trapz(data)

print("area: "+str(output)+" square picometers or whatever")
