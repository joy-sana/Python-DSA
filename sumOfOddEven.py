n = [3,9,5,6,5,4,7,9,7,1,0,2,44,1,5,1,4,45,]
OddSum = 0
EvenSum = 0

for i in n:
    if i%2 == 0:
        EvenSum += i
    else:
        OddSum += i

print((EvenSum,OddSum))