matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
x = 5
def Matrixx(matrix,x):
    print(len(matrix[0]))

    rows = len(matrix)

    for i in range(0,rows):
        col = len(matrix[i])
        
        if matrix[i][col-1] >= x:
            for j in range(0,col):
                if matrix[i][j] == x:
                    return True
    return False

v= Matrixx(matrix,x)
print(v)