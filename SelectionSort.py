arr = [5,3,4,2,1,6,4,5,7,32,7,45,8]
print(arr)
n = len(arr)

for i in range(0,n):
    min = arr[i]
    min_index = i # 
    for j in range(i,n):
        if min > arr[j]:
            min = arr[j]
            min_index = j
    
    var = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = var

print(arr)
