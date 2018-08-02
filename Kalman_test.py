import math;

def update(mean1,var1,mean2,var2):
    new_mean = float(var2*mean1+ var1*mean2)/(var1+var2)
    new_var =1./(1./var1+1./var2)
    return [new_mean,new_var]

def predict(mean1,var1,mean2,var2):
    new_mean = mean1+mean2
    new_var = var1+var2
    return[new_mean, new_var]

measurements=[5.,6.,7.,9.,10.,11.,12.,13.]
measurements_uncertainty =44.

motion = [1.,1.,2.,1.,1.,1.,1.,1.]
motion_uncertainty =2.
mu = 4.
sig = 1000.

for n in range(len(measurements)):
    [mu, sig] = update(mu,sig, measurements[n], measurements_uncertainty)
    print 'update:' , [mu, sig]
    [mu, sig] = predict(mu, sig, motion[n], motion_uncertainty)
    print 'predict:', [mu,sig]


