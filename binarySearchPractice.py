arr = [1,2,4,6,7,9,15,88]
key = 6

low = 0
high = len(arr)
flag =False

while low<high:
    mid = (low+high)//2

    if arr[mid] == key:
        flag = True
        index = mid
        break
    elif (arr[mid] > key):
        high = mid
    else:
        low = mid + 1

if flag:
    print("found in ",index)
else:
    print("not found")