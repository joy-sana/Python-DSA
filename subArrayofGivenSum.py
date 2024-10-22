arr = [2,4,20,3,10,5]
n = len(arr)
givenSum = 15


currentSum = 0

left = 0
right = 0
subArr = []

while right <= n:

    if(currentSum < givenSum):
        currentSum += arr[right]
        right+=1
    elif(currentSum > givenSum):
        currentSum -= arr[left]
        left +=1
    if(givenSum == currentSum):
        subArr = arr[left:right]
        break
        
print(subArr)



