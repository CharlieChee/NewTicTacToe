# Print the board
import time
import sys# Importing the required libraries
def printboard(board):
    print('----------------------------------')
    for row in board:
        print(*row, sep="\t")
# Function for AI's move        
def AIPlay(board):
    #to find the best cordinate and place the value X
    bestMove = findBestMove(board)
    board[bestMove[0]][bestMove[1]]='x'
    print("AI Played")
    printboard(board)
    # Check if AI won
    if (Checkwon(board) == 1):
        print("\nAI Won")
        sys.exit()
    # Check if opponent won    
    elif  (Checkwon(board) == -1):
        print("\nOpponent Won")
        sys.exit()
    # Check if it's a draw    
    elif  (isMovesLeft(board) == False) :
        print("\nIt's a draw !")
        sys.exit()

# Function to check if someone won        
def Checkwon(board) :
	
	# Checking for Rows for X or O victory.
	for i in range(3) :	
		if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '_':
			if (board[i][0] == 'x') :
				return 1
			else :
				return -1

	# Checking for Columns for X or O victory.
		if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '_':
		
			if (board[0][i] == 'x') :
				return 1
			else:
				return -1

	# Checking for Diagonals for X or O victory.
	if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_'):
	
		if (board[0][0] == 'x') :
			return 1
		else :
			return -1

	if (board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_') :
	
		if (board[0][2] == 'x') :
			return 1
		else:
			return -1

	# Else if none of them have won then return 0
	return 0 
# Function to check if there are still moves left   
def isMovesLeft(board) :

	for i in range(3) :
		for j in range(3) :
			if (board[i][j] == '_') :
				return True
	return False

# Function for the minimax algorithm
def minimax(board, depth, player) :
    # Check the current score
	score = Checkwon(board)
     # If the maximizing player wins, return a high score   
	if (score == 1) :
		return 10 - depth
	if (score == -1) :
                # If the minimizing player wins, return a low score
		return depth - 10
	if (isMovesLeft(board) == False) :
                # If the game ends in a tie, return a score of 0
		return 0
	#For Max player
	if (player == 'x') :	
		best = -float('inf')
		for i in range(3) :		
			for j in range(3) :
				if (board[i][j]=='_') :
					board[i][j] = player

					# Call minimax recursively 
					best = max( best, minimax(board,
											depth + 1,
											'o') )

					# Undo the move
					board[i][j] = '_'
		return best

	# If this minimizer's move
	else :
		best = float('inf')
		for i in range(3) :		
			for j in range(3) :
				if (board[i][j] == '_') :
					board[i][j] = 'o'
					best = min(best, minimax(board, depth + 1, 'x'))
					board[i][j] = '_'
		return best

# Return the best possible move for the player
def findBestMove(board):
    bestVal = -float('inf')
    bestMove = (-1, -1)
    start_time = time.time()
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'x'
                moveVal = minimax(board, 0, 'o')
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    end_time = time.time()
    print("Execution time:", end_time - start_time, "seconds")
    return bestMove
# Main code
board = [
	[ '_', '_', '_' ],
	[ '_', '_', '_' ],
	[ '_', '_', '_' ]
]


print("Hi Welcome to Unbeatable TicTacToe")
input("Press Enter to Continue !!")
#print the board
printboard(board)


while True :
    n = input("What's the position of Your Move? (1-9)\n")
    match n:
        case "1":
            if (board [0][0] != '_'):
                print("Invalid move do Again")
            else:    
                board [0][0]='o'
                AIPlay(board)
        case "2":
            if (board [0][1] != '_'):
                print("Invalid move do Again")
            else:
                board [0][1]='o'
                AIPlay(board)
                        
        case "3":
            if (board [0][2] != '_'):
                print("Invalid move do Again")
            else:
                board [0][2]='o'
                AIPlay(board)         
        case "4":
            if (board [1][0] != '_'):
                print("Invalid move do Again")
            else:
                board [1][0]='o'
                AIPlay(board)         
        case "5":
            if (board [1][1] != '_'):
                print("Invalid move do Again")
            else:
                board [1][1]='o'
                AIPlay(board)     
        case "6":
            if (board [1][2] != '_'):
                print("Invalid move do Again")
            else:
                board [1][2]='o'
                AIPlay(board)    
        case "7":
            if (board [2][0] != '_'):
                print("Invalid move do Again")
            else:
                board [2][0]='o'
                AIPlay(board)
        case "8":
            if (board [2][1] != '_'):
                print("Invalid move do Again")
            else:
                board [2][1]='o'
                AIPlay(board)     
        case "9":
            if (board [2][2] != '_'):
                print("Invalid move do Again")
            else:
                board [2][2]='o'
                AIPlay(board)     
        case _:
            print("Wrong Input")

    



