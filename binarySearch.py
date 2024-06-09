def binarySearch(arr,start,end,key):
    if start >= end:
        return -1
    mid = (start + end)//2

    if key == arr[mid]:
        # print("element found in index number" , mid)
        return mid
    elif key > arr[mid]:
        # binarySearch(arr,mid+1,end,key)
        start = mid+1
    else:
        # binarySearch(arr,start,mid,key)
        end = mid
    
    return binarySearch(arr,start,end,key)
        

list = [2, 3, 3, 10, 21, 35, 42, 53, 62, 342]
print(list)
while True:

    n = int(input("Enter the data you want to search: "))
    print("element found in index number" , binarySearch(list,0,len(list),n))