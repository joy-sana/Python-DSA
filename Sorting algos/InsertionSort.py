arr=[1,2,3,4,5,6,7,8,9]
n = len(arr)

swapCount=0
for j in range(1,n):
    current = arr[j]
    print("current",current)
    i = j-1

    while (i>=0 and arr[i]>current ):
        arr[i+1] = arr[i]
        i-=1
        swapCount+=1
    arr[i+1] = current
    swapCount+=1

print(arr,swapCount)
