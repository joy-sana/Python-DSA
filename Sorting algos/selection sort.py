def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min]:
                min = j
        if arr[i] > arr[min]:
            arr[i], arr[min] = arr[min], arr[i]


list1 =  [3, -1, 4, 1, -5, 9,10,42,2,35,3,21,342,62,3,53]
selectionSort(list1)
print(list1)