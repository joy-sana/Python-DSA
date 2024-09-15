# list1 = [1, 3, 5, 2, 2]
# list1 = [-3,-1,-1,-1]
list1 = [-7, 2, 4, 9, -8, 1, 6]

def sum(j,listx):
    sum = 0
    for i in range(j,len(listx)):
        sum = sum + listx[i]
    return sum


leftSum = i = j = 0
finalIndex = -1
rightSum = sum(1,list1)

while( i < len(list1) and  j < len(list1)-1):
    j = i + 1
    k = i + 2
    leftSum = leftSum + list1[i]
    rightSum -= list1[j]
    
 
    # print(f"i: {i}, k: {k}, leftlist: {leftSum}, rightlist: {rightSum}, sum of list: {sumOfList}")

    if leftSum == rightSum:
        finalIndex = k
    else:
        i+=1

if finalIndex > 0:
    print("index: ",finalIndex)
else:
    print("NOT FOUND")



# 37741493026547328_1