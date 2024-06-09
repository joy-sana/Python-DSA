def bubleSort(arr):
    len_llist = len(arr)

    for i in range(len_llist):
        for j in range(0,len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

list1 =  [3, -1, 4, 1, -5, 9,10,42,2,35,3,21,342,62,3,53]

bubleSort(list1)
print(list1)
