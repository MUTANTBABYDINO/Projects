def main():
    # board is organized as a list of lists
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 6, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    # list to store all of the empty spaces that have been attempted
    missing = []
    print_board(board)
    try:
        solve(board, missing)
    except:
        print('Not Solvable')
    else:
        print('Done')
        print_board(board)

def print_board(board):
    # print horizontal dividing lines
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- ' * 12)
        # print vertical dividing lines
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            # print numbers
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')

def solve(board, missing):
    # add the missing spots to a list to backtrack
    if find_empty(board) != None:
        missing.append(find_empty(board))
    else:
        return True

    # set the top coordinates of the list to the current row and col
    row, col = missing.pop()
    missing.append((row, col))

    # check if any numbers work at the position
    for i in range(1, 10):
        if check_valid(board, (row, col), i):
            board[row][col] = i
            if solve(board, missing):
                return True

            board[row][col] = 0

    # if no numbers work then backtrack to the previous position and try a new number
    if board[row][col] == 0:
        missing.pop()
        row, col = missing.pop()
        missing.append((row, col))

    return False

def check_valid(board, pos, num):
    # check vertical
    for i in range(len(board)):
        if board[i][pos[1]] == num:
            return False

    # check horizontal
    if num in board[pos[0]]:
        return False

    # check square
    box_row = pos[0] // 3
    box_col = pos[1] // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty(board):
    # return position of empty spaces
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None

main()
