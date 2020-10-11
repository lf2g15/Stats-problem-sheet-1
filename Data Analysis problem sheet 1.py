import numpy as np

import pylab as pl

#Q1

x = [11.45,10.91,11.6,10.59,10.32,10.34,11,10.94,11.67,11.67,11.06,10.57]

mean=sum(x)/len(x)

print(mean)

y = [a-mean for a in x]

z = np.square(y)

SD=((1/(len(x)-1))*sum(z))**(1/2)

print(SD)

SE = SD/((len(x))**(1/2))

print(SE)

# Report of error: The mean of the sensitivity of the photo diode is 11.01 with a standard error of 0.14

#Q4 

q = [45.7, 53.2, 48.4, 45.1, 51.4, 62.1, 49.3]

meanq=sum(q)/len(q)

w = [a-meanq for a in q]

e = np.square(w)

SDq=((1/(len(q)-1))*sum(e))**(1/2)

print(SDq)

def tsus(xsus):
    return (abs(xsus-meanq)/SDq)
 
#for tsus in q:
    #if tsus(q)

#Q5 
    
p = [32]

p.extend([33]*3)
p.extend([34]*5)
p.extend([35]*10)
p.extend([36]*5)
p.extend([37]*3)
p.extend([38]*1)

#print(p)

import math as mt

j = [32,33,34,35,36,37,38,39]

def gaussian(x, mu, sig):
    return (150)*(1/(sig*((2*mt.pi)**(1/2))))*(np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))))


x_values = np.linspace(10, 55, 120)

pl.plot(x_values, gaussian(x_values,35 , 35**(1/2)))

pl.hist(p,j)
pl.show()

#COMMENTS TO DO

#Q6

#Look elsewhere effect: There is a large probability that statistical outlying data will evolve if the parameter space in which one searches for results is large enough. The likelihood of a 
# 4*sigma event appearing is about 16000 to 1, but if you run a test 16000 times, statistical analysis suggest this event is likely to occur at least once during the measurements.  




