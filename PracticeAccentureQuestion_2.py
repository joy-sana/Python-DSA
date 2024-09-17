arr = [23, 45 , 82, 71]

max_num = float('-inf')
index = -1

for i in range(0,len(arr)):
    if max_num < arr[i]:
        max_num = arr[i]
        index = i

print("maximum value: ", arr[index])
print("index: ", index)
    