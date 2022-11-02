import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'/home/anjan/Desktop/assignment1/question5')
import fibo
k=int(input("enter the number-"))
l=fibo.fib(k+1)/fibo.fib(k)
def f(l):
    return(l)
print(f(l))
xx=[]
n=np.linspace(2,99,98)
for j in range(2,100):
    x=fibo.fib(j+1)/fibo.fib(j)
    xx.append(x)

plt.plot(n,xx,'-o')
plt.xlabel("n axis")
plt.ylabel(" f(n)(The ratio of two consecutive fibonacci)")
plt.grid()
plt.show()

