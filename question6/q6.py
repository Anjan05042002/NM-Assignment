import math
def f(n):
    xx=[i for i in range(2,(n+1))]
    for j in xx:
        for i in range(2,math.ceil(n*1.0/j)+1):
            if (i*j) in xx:
                xx.remove(j*i)
    return(xx)
print(f(200))


