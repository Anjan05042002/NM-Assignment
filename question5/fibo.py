
def fib(n):
 if n==1:
     x3=0
 else:
     x1=1
     x2=1
     x0=0
     for i in range(n-1):
         x3=(x1+x0)
         x1=x0
         x0=x3
 return x3
