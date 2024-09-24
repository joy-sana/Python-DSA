arr = [5, 3, 4, 2, 1, 6, 7, 32, 45, 8]
# sorded [1, 2, 3, 4, 5, 6, 7, 8, 32, 45]
n = len(arr)
print(arr)
for i in range(n):
    for j in range(0,n-1-i):
        if arr[j] > arr[j+1]:
            arr[j] = arr[j] + arr[j+1]
            arr[j+1] = arr[j] - arr[j+1]
            arr[j] = arr[j] - arr[j+1]
    print(arr)
print(arr)