arr = [8,10,6,2,9,7]
l = len(arr)
max = float('-inf')
count = 0

for i in range(l-1, -1,-1):
    j = None
    if arr[i] > max:
        count+=1
        max = arr[i]

print(count)
    

