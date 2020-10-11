from scipy.integrate import quad
import numpy as np
def gaussian(x, mu, sig):
    return (150)*(1/(sig*((2*mt.pi)**(1/2))))*(np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))))


mu=35 
sig=35**(1/2)
I = quad(gaussian, -np.inf, np.inf, args=(mu,sig))

Sig= quad(gaussian, (35-(35**(1/2))), (35+(35**(1/2))), args=(mu,sig))

Sig2 = quad(gaussian, (35-(1.65*(35**(1/2)))), (35+(1.65*(35**(1/2)))), args=(mu,sig))

Sig3 = quad(gaussian, (35-(2*(35**(1/2)))), (35+(2*(35**(1/2)))), args=(mu,sig))

Sig4 = quad(gaussian, (35-(2.58*(35**(1/2)))), (35+(2.58*(35**(1/2)))), args=(mu,sig))

Sig5 = quad(gaussian, (35-(3*(35**(1/2)))), (35+(3*(35**(1/2)))), args=(mu,sig))

Sig6 = quad(gaussian, (35-(4*(35**(1/2)))), (35+(4*(35**(1/2)))), args=(mu,sig))

Sig7 = quad(gaussian, (35-(5*(35**(1/2)))), (35+(5*(35**(1/2)))), args=(mu,sig))

Sig8 = quad(gaussian, (35-(0.675*(35**(1/2)))), (35+(0.675*(35**(1/2)))), args=(mu,sig))

Sig9 = quad(gaussian, (35-(3.3*(35**(1/2)))), (35+(3.3*(35**(1/2)))), args=(mu,sig))

#Verifying Table 3.1:

print(Sig[0]/I[0], Sig2[0]/I[0], Sig3[0]/I[0], Sig4[0]/I[0], Sig5[0]/I[0] )

#Fraction outside 4 sigma:

print((1-(Sig6[0]/I[0]))*100)

#Fraction outside 5 sigma:

print((1-(Sig7[0]/I[0]))*100)

#Symmetric range within 50% of data lie, 0.675*sigma:

print(((Sig8[0]/I[0]))*100)

#Symmetric range within 50% of data lie, 3.3*sigma:

print(((Sig9[0]/I[0]))*100)




#Q6 ii) 

print(((10e5)/50)*(1-(Sig3[0]/I[0])))

print(((10e5)/100)*(1-(Sig3[0]/I[0])))

#between 455 and 910 2*sig events (above)

print(((10e5)/50)*(1-(Sig5[0]/I[0])))

print(((10e5)/100)*(1-(Sig5[0]/I[0])))

#between 27 and 54 2*sig events (above)

print(((10e5)/50)*(1-(Sig6[0]/I[0])))

print(((10e5)/100)*(1-(Sig6[0]/I[0])))

#about 1 (above)

print(((10e5)/50)*(1-(Sig7[0]/I[0])))

print(((10e5)/100)*(1-(Sig7[0]/I[0])))

#less than one 


