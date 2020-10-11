
from scipy.special import erfc

f = [45.7, 53.2, 48.4, 45.1, 51.4, 62.1, 49.3]

fmean = sum(f)/len(f)
stdf = np.std(f)

def four_i():
 
    o = 62.1
    d = ((abs(o-fmean))/stdf)
    probability_outlier = erfc(d)
    n_out=len(f)*probability_outlier
    if(n_out<0.5):
        comment = 'REJECT'
    else:
        comment ='ACCEPT'
    return(probability_outlier,n_out,comment)
    
    
print(four_i())

