#Examples of simpsons(1/3)rd method
import numpy as np
n1=101#for simpsons
n2=100#for trapizoidal rule
x1=np.linspace(1,3,n1)
x2=np.linspace(1,3,n2)
h1=x1[2]-x1[1]
h2=x2[2]-x2[1]

y1=(x1*np.log(x1)-x1)#for simpsons rule the function
y2=(x2*np.log(x2)-x2)#for trapizoidal rule the function

G=(h1/3)*(y1[0]+y1[-1]+4*np.sum(y1[1:-1:2])+2*np.sum(y1[2:-2:2]))
F=(h2/2)*(y2[0]+y2[-1]+2*np.sum(y2[1:-1:1]))

print("Simpsons Rule-", G)
print("Trapizoidal Rule-", F)

