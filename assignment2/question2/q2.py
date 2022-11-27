import numpy as np
import random
import numpy as np
data = np.genfromtxt('data.dat',
                     skip_header=1,
                     skip_footer=1,
                     names=True,
                     dtype=None,
                    )


xx=[data[i][0] for i in range(len(data))]
yy=[data[i][1] for i in range(len(data))]
def f(x):
    ss=[]
    for i in range(len(xx)):
        s=0
        m=1
        for j in range(len(xx)):
            if j!=i:
                m=m*(x-xx[j])/(xx[i]-xx[j])
        s+=m*yy[i]
        ss.append(s)
    return(np.sum(ss))

def l(x,j):
    s=0
    for i in range(len(xx)):
        if i!=j:
            M=1
            for m in range(len(xx)):
                if m!=i and m!=j:
                    M=M*(x-xx[m])/(xx[j]-xx[m])
            s+=M/(xx[j]-xx[i])
    return(s)
def deri(x):
    s1=0
    for j in range(len(xx)):
        s1+=yy[j]*l(x,j)
    return(s1)
#print(deri(2))

#xn+1=xn-f(xn)/f'(xn)  raphson.py
def NR(x):
    eps=10**(-6)
    err=1.0
    while err>=eps:
        xn=x-f(x)/deri(x)
        err=abs(xn-x)
        x=xn
    return(x)
print(NR(4),NR(0.5))


