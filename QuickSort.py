# def QuickSort(first,last,arr):
#     n = len(arr)

#     pivot = arr[n-1] 

#     devide(first,last,arr)  

def devide(f,l,arr):
    pivot = arr[l]
    q = None
    for i in range(f,l):
        if  pivot < arr[i]:
            arr[i], arr[l] = arr[l], arr[i]
            q = i
            devide(f,q-1,arr)
            devide(q+1,l,arr)








arr = [5, 3, 4, 2, 1, 6, 7, 32, 45, 8]
# sorded [1, 2, 3, 4, 5, 6, 7, 8, 32, 45]
n = len(arr)

devide(0,n-1,arr)
print(arr)
