
arr = [1,2,0,4,3,0,5,0]
l = len(arr)
arr2 =[0]*l
j = 0
for i in range(0,l):
    if arr[i] != 0:
        arr2[j] = arr[i]
        j+=1

print(arr)
print(arr2)
