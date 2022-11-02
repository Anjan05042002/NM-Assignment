# Sum of cubes of natural numbers upto 15
n=int(input('Enter the number- '))
import numpy as np
x1=0
def f(x):
    return(x**3)
y=sum([f(x) for x in range(11,41)])
for i in range(1,(n+1)):
    x2=i**3+x1
    x1=x2
print("Sum of cubes from 11 to 41-",y)
print("sum upto n th integer-",x2)
