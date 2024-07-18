
# list1 = [1, 3, 5, 2, 2]
# list1 = [-7, 2, 4, 9, -8, 1, 6]
list1 = [-3,-1,-1,-1]

def sum(j,listx):
    sum = 0
    for i in range(j,len(listx)):
        sum = sum + listx[i]
    return sum
sumOfList = sum(0,list1)



leftSum = i = 0
finalIndex = -1
while( i < len(list1)):
    k = 2 + i
    leftSum = leftSum + list1[i]
    rightSum = sum(k,list1)
 
    # print(f"i: {i}, k: {k}, newlist: {leftSum}, rightlist: {rightSum}")
    if leftSum == rightSum:
        finalIndex = k
    else:
        i+=1

if finalIndex > 0:
    print("index: ",finalIndex)
else:
    print("NOT FOUND")



