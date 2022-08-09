board = [[0,0,1,3,2,5,9,7,8],
         [0,0,0,0,0,8,5,3,1],
         [0,0,8,0,0,0,4,2,0],
         [7,0,4,0,5,0,8,0,0],
         [0,0,3,0,0,0,1,6,0],
         [8,5,0,0,3,0,7,0,0],
         [0,6,5,0,0,0,2,0,0],
         [4,8,7,1,0,2,3,0,0],
         [0,9,2,0,0,3,6,8,0]]
def print_board():
    #print first line
    print('----' * len(board) + '-')
    #print details
    for row in range(len(board)):
        row_str = ''
        for col in range(len(board)):
            row_str += '| ' + str(board[row][col]) + ' '
        print(row_str + '|')
        print('----' * len(board) + '-')

#check if the number is valid in row, col, box condition
def is_valid(board, row, col, num):
    #row
    for i in range(9):
        if board[row][i] == num:
            return False

    #col
    for i in range(9):
        if board[i][col] == num:
            return False

    #box
    boxRow = row - row % 3
    boxCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + boxRow][j + boxCol] == num:
                return False

    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1,10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        #recursion
                        if solve(board):
                            return True
                        else:
                            board[row][col] = 0
                return False
    return True                    

print('Before')    
print_board()

print('After')
solve(board)
print_board()
