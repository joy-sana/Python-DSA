def isPrime(num):
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    return True


arr = [-1,-2,-3,3,4,-7]
arr = [10,20,30,40,50,60,70,80,90,100]
arr = []
sum = 0
n = len(arr)

for i in range(2,n):
    if isPrime(i):
        sum += arr[i]


print(sum)
