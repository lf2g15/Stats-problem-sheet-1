

import numpy as np
import matplotlib.pyplot as plt
low =1 
high = 11
lenght = 20
itlgt = 10000

import math as mt

def counter(array, length):
    j = []
    x = np.linspace(0,10,length)
    for k in range(length):
        j.append(array.count(x[k]))
    return x , j


gaus2 = []

for k in range(itlgt):
    ss = mean(low,high,lenght)
    sss = format(ss,'.2f')
    ssss = float(sss)
    gaus2.append(ssss)




p = counter(gaus2 , 1001)
plt.plot(p[0],p[1])
plt.show()

x = sum(p[0])/itlgt

print(x)

z = np.square([a-x for a in p[0]])

SD=((1/(itlgt-1))*sum(z))**(1/2)

print(SD)

from scipy.integrate import quad

#def G(x):
   # return ((1/(SD*(2*((mt.pi)*(1/2)))))*mt.exp(-((p[0]-x)**2)/(2*(SD)**2))
            


