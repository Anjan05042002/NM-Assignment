import numpy as np
x,y=np.loadtxt("data.dat",unpack=True)
def f(a,x):
    n=len(x)
    s1=0
    for k in range(n):
        L=1.0
        for h in range(n):
            if h!=k:
                L=L*(a-x[h])/(x[k]-x[h])
        s2=s1+L*y[k]
        s1=s2
    return(s2)
def simp(y,x):
    xx=np.linspace(0,y,10000)
    j=f(xx,x)
    H=(y-0)/10000
    P=(H/3)*(j[0]+j[-1]+4*np.sum(j[1:-1:2])+2*np.sum(j[2:-2:2]))
    return(P)
err=1.0
eps=10**(-6)
q=2.0
while err>=eps:
    x1=q-(simp(q,x)/f(q,x))
    err=abs(x1-q)
    q=x1
print("The value where it will be zero",x1)








