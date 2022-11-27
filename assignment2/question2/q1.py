import numpy as np

x,y=np.loadtxt("data.dat",unpack=True)
n=len(x)

def f(t):
    s1=0
    for k in range(n):
        
        L=1.0
        for h in range(n):
            if h!=k:
                L=L*(t-x[h])/(x[k]-x[h])
        s2=s1+L*y[k]
        s1=s2
    return(s2)
print("The value at x=2.5 is ",f(2.5))