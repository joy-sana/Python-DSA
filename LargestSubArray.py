arr = [-2,1,-3,4,-1,2,1,-5,4]
n = len(arr)

maxSum = float('-inf')
currentSum = 0
left,right = 0,0
loopTerminator = 0
subArray = []
for right in range(n):
    currentSum += arr[right]
    
    if currentSum > maxSum:
        maxSum = currentSum
        l,r = left,right
    
    if currentSum < 0:
        currentSum = 0
        left = right + 1




print(maxSum,arr[l:r+1])