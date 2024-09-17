arr = [4,2,1,3]

for i in range(0,len(arr)):
    for j in range(i, len(arr)):
        if arr[j] > arr[i]:
            arr[i], arr[j] = arr[j], arr[i]

sum = 0 
for i in range(0,len(arr)):
    j = i+1
    if j != len(arr):
        sum += abs(arr[i] - arr[j])

print(arr)
print(sum)
