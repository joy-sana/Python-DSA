arr = [5, 3, 4, 2, 1, 6, 7, 32, 45, 8]
# sorded [1, 2, 3, 4, 5, 6, 7, 8, 32, 45]
n = len(arr)


print(arr)
for i in range(0,n):
    key = arr[i]
    j = i - 1
    
    while(j>=0 and arr[j] > key):
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = key
    print(i,arr)

print(arr)
    
        

