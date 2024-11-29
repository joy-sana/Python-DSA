n = int(input("Enter numebr: "))

def fibo(n):

    return fibo(n-1) + fibo(n-2)    




print(fibo)

if n == 1:
    print(0)
if print == 2:
    print(0, 1)
else:
    print(0,1, end= " ")
f = 0
s = 1

for i in range(2, n):
    
    num = f + s
    f = s
    s = num
    print(num, end = " ")
