import random
xx=[]
n=int(input("enter the number :"))
def f(x):
    return(x**3)
for i in range(n+1):
    x=random.randint(0,n)
    xx.append(f(x))
print(xx,"normal cubuic of natural numbers")
for i in range(n+1):
    for j in range(n):
        if xx[i]<xx[j]:
            xx[i],xx[j]=xx[j],xx[i]

print(xx,"asscending order")

