# Create a connect-4 game

import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def createBoard():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

def checkForColEnd(board,col):
    return board[ROW_COUNT-1][col] == 0

def dropPiece(board, row, col, piece):
    board[row][col] = piece

def getOpenRow(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def winningMove(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def printBoard(board):
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            if board[ROW_COUNT-r-1][c] == 1:
                print(u"\U0001F7E1"+" |",end="")
            elif board[ROW_COUNT-r-1][c] == 2:
                print(u"\U0001F535"+" |",end="")
            else:
                print("   |",end="")
        print()
        if r < ROW_COUNT-1: 
            print ("-"*COLUMN_COUNT*4)

    # print(np.flip(board,0))

board = createBoard()
turn = 0
player = ""
gameover = False
while not gameover:
    if turn == 0:
        player = "Player 1 "+u"\U0001F7E1"
        piece = 1
    else:
        player = "Player 2 "+u"\U0001F535"
        piece = 2
    while True:
        try:
            while True:
                col = int(input("Select the column number "+player+" [1-6] "))
                if col in [1,2,3,4,5,6]:
                    break
                else:
                    print("Please make a selection between column 1-6 ")
            break
        except:
            print("The entered input is not a number. You can only enter a number.")
    index = col - 1
    if checkForColEnd(board,index):
        row = getOpenRow(board,index)
        dropPiece(board,row,index,piece)
        gameover = winningMove(board,piece)
        turn += 1
        turn = turn % 2
    else:
        print("\nThe column is already full\n")
    printBoard(board)
print("\n\n"+player+" won the Game\n\n")
