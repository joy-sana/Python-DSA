board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# for i in board:
#     for j in i:
#         print(j, end=" ")
#         if j != '.':
#             if j not in arr:
#                 arr.append(j)
#             else:
#                 print("wrong sudoku ")
#                 break
#     print()
#     arr.clear()



arr=[]
arr2=[]

for i in range(len(board)):

    for j in range(len(board)):
        print(board[i][j], end=" ")
        
        if board[i][j] != '.':
            if board[i][j] not in arr:
                arr.append(board[i][j])
            else:
                print("wrong sudoku r")
                break


        if board[j][i] != '.':
            if board[j][i] not in arr2:
                arr.append(board[j][i])
            else:
                print("wrong sudoku c")
                break 

            

    print()
    arr.clear()
    arr2.clear()
