board = [['-' for x in range(3)] for y in range(3)]
test_board = [['o', '-', 'o'], ['o', 'o', 'o'], ['o', '-', 'o']]

tracker = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def three_across(board):
    for x in range(len(board)):
        win = True
        spot_check = board[x][x]
        for y in range(len(board)):
            if board[x][y] != spot_check:
                win = False

        if win == True:
            print('three across')
            return

# three_across(test_board)

def diag_up(board):
    for x in range(len(board)):
        counter = 0
        win = True
        spot_check = board[0][2]
        if board[x][(-1) - counter] != spot_check:
            win = False
            return

        counter += 1

    if win == True:
        print('diag up')
        return

# diag_up(test_board)
            
def diag_down(board):
    for x in range(len(board)):
        win = True
        spot_check = board[0][0]
        if board[x][x] != spot_check:
            win = False
            return
    
    if win == True:
        print('diag down')

# diag_down(test_board)


def left_down(board):
    for x in range(len(board)):
        win = True
        spot_check = board[x][0]
        if board[x][0] != spot_check:
            win = False
            return
        
        if win == True:
            print('left down')
            return

# left_down(test_board)

def mid_down(board):
    for x in range(len(board)):
        win = True
        spot_check = board[x][1]
        if board[x][1] != spot_check:
            win = False
            return

        if win == True:
            print("mid down")
            return

# mid_down(test_board)

def right_down(board):
    for x in range(len(board)):
        win = True
        spot_check = board[x][2]
        if board[x][2] != spot_check:
            win = False
            return

        if win == True:
            print('right down')
            return

# right_down(test_board)


# added a counter to get a draw for now.
# i need to find a more efficient way
# to get the draw.

def draw(board):
    counter = 0 
    for x in range(3):
        for y in range(3):
            if '-' != board[x][y]:
                counter += 1

    if counter == 9:
        print("DRAW!")

