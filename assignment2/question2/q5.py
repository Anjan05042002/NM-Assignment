import numpy as np
import matplotlib.pyplot as plt
x,y=np.loadtxt("data.dat",unpack=True)
def f(t,x):
    n=100
    s1=0
    for k in range(n):
        L=1.0
        for h in range(n):
            if h!=k:
                L=L*(t-x[h])/(x[k]-x[h])
        s2=s1+L*y[k]
        s1=s2
    return(s2)
def diff(a,x):
    p=0
    for i in range(100):
        L=1
        k=0
        for j in range(100):
            if i!=j:
                L=((a-x[j])/(x[i]-x[j]))*L
                k=k+(1/(a-x[j]))
        l=L*k
        m=(y[i]*l)
        p=p+m
    return(p)
#print("The value at first derivstive",diff(0,x))
def dbl_diff(b,x):
    h=0.00001
    return((-diff(b+2*h,x)+8*diff(b+h,x)-8*diff(b-h,x)+diff(b-2*h,x))/(12*h))
#print("The value of double derivative at 0-",dbl_diff(0,x))
def trpl_diff(c,x):
    h=0.00001
    return((-diff(c+2*h,x)+16*diff(c+h,x)-30*diff(c,x)+16*diff(c-h,x)-diff(c-2*h,x))/(12*h**2))
#print("The value of triple derivative at 0-",trpl_diff(0,x))
#First finding the value of w
#The eqn of if y=3*f"(0)*w-3*f'(0)*w^2+w^3*f(0)-f"'(0)

err=1.0
eps=10**(-6)
w=2.0
while err>=eps:
    w1=w-((3*dbl_diff(0,x)*w-3*diff(0,x)*w**2+f(0,x)*w**3-trpl_diff(0,x))/(3*dbl_diff(0,x)-6*diff(0,x)*w+3*f(0,x)*w**2))
    err=abs(w-w1)
    w=w1
root=w1#It is the value of w
c=f(0,x)#The value of c
b=diff(0,x)-(c*root)#The value of b
a=(dbl_diff(0,x)-(2*b*root)-c*(root)**2)/2#This is the value of a
print("The value of a",a)
print("value of b",b)
print("value of c",c)
print("value of w",root)
I=((a)*x**2+b*x+c)*np.exp(root*x)
plt.plot(x,I,"-o")
plt.plot(x,y)
plt.title("Original plot and The plot of the function")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.axhline(linestyle="--")

plt.show()



