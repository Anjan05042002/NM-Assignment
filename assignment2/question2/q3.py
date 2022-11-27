import numpy as np
import matplotlib.pyplot as plt
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
m=100000
xx=np.linspace(0,4,m)
H=(4-0)/m

P=f(xx)
simp=(H/3)*(P[0]+P[-1]+4*np.sum(P[1:-1:2])+2*np.sum(P[2:-2:2]))
print(simp)
plt.plot(xx,P,"-o")
plt.grid()
plt.plot(x,y)
plt.show()
#Newtons rapsons method where it will be zero







