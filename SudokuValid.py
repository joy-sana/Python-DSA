# https://leetcode.com/problems/valid-sudoku/

# In a valid Sudoku:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 3x3 subgrids must contain the digits 1-9 without repetition.

# Only the filled cells need to be validated according to the mentioned rules.

def isValidSudoku(board) -> bool:
    arr=[]
    arr2=[]

    for i in range(len(board)):
        for j in range(len(board)):
            # Checks for Unique Rows
            if board[i][j] != '.':
                if board[i][j] not in arr:
                    arr.append(board[i][j])
                else:
                    # print("wrong sudoku r" ,board[i][j],i,j)
                    return False
            
            # Checks for Unique Column
            if board[j][i] != '.':
                if board[j][i] not in arr2:
                    arr2.append(board[j][i])
                else:
                    # print("wrong sudoku c")
                    return False

        # print()
        arr.clear()
        arr2.clear()

    # Checks for Unique Boxes
    for i in range(0,7,3):
        for j in range(0,7,3):
            for k in range(j,3+j):
                for l in range(i,3+i):
                    if board[k][l] != '.':
                        if board[k][l] not in arr2:
                            arr2.append(board[k][l])
                        else:
                            print("wrong sudoku c")
                            return False
        
            arr2.clear()
        
    return True
        



board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# [[".",".",".",".","5",".",".","1","."],
#  [".","4",".","3",".",".",".",".","."],
#  [".",".",".",".",".","3",".",".","1"],
#  ["8",".",".",".",".",".",".","2","."],
#  [".",".","2",".","7",".",".",".","."],
#  [".","1","5",".",".",".",".",".","."],
#  [".",".",".",".",".","2",".",".","."],
#  [".","2",".","9",".",".",".",".","."],
#  [".",".","4",".",".",".",".",".","."]]


print(isValidSudoku(board))
