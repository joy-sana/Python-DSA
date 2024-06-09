
def meargeTwoArray(arr1,arr2):
    array =[]
    i = j = k = 0
    while(len(arr1) > i and len(arr2) > j):
        if arr1[i] <= arr2[j]:
            array.append(arr1[i])  
            i+=1
        else:
            array.append(arr2[j])  
            j+=1

    while len(arr1) > i:
        array.append(arr1[i])  
        i+=1
    while len(arr2) > j:
        array.append(arr2[j])  
        j+=1
    return array

def meargeTwoSortedArray(arr1,arr2,array):
    i = j = k = 0
    while(len(arr1) > i and len(arr2) > j):
        if arr1[i] <= arr2[j]:
            array[k] = arr1[i]
            i+=1
        else:
            array[k] = arr2[j]
            j+=1
        k+=1
    while len(arr1) > i:
        array[k] = arr1[i]
        i+=1
        k+=1
    while len(arr2) > j:
        array[k] = arr2[j]
        j+=1
        k+=1
def mergeSort(arr):
    if len(arr) <= 1:
        return 
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    meargeTwoSortedArray(left,right,arr)

    

# list1 = [9,5,6,2,6,3,1,3]
# list2 = [1,3,5,6,8,9]
# list3 = [2,4,7,12]




# # print(listX)
# mergeSort(list1)
list1 = [3, -1, 4, 1, -5, 9]
list2 = [10,42,2,35,3,21,342,62,3,53]

mergeSort(list2)
mergeSort(list1)
list3 = meargeTwoArray(list1,list2)
print(list3)
