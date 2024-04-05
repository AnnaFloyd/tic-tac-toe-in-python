# Global variable to store tic-tac-toe board
board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

# Main method
def main():
    print("Main method.")
    displayBoard()
    while(not inWinningState() and not isBoardFull()):
        getXMove()
        displayBoard()

        if (not inWinningState() and not isBoardFull()):
            getOMove()
            displayBoard()


# Get the move of the X player
def getXMove():
    move = input("Enter where you want your next X" +
          " [Row Column Ex: '1 2']: ")
    [xRow, xCol] = move.split(' ')
    xRow = int(xRow)
    xCol = int(xCol)
    if(checkMoveValidity(xRow, xCol)):
        placeSymbol(xRow, xCol, 'X')
    else:
        print("Invalid move. Try again.")
        getXMove()

# Get the move of the O Player
def getOMove():
    move = input("Enter where you want your next O" +
          " [Row Column Ex: '1 2']: ")
    [oRow, oCol] = move.split(' ')
    oRow = int(oRow)
    oCol = int(oCol)
    if(checkMoveValidity(oRow, oCol)):
        placeSymbol(oRow, oCol, 'O')
    else:
        print("Invalid move. Try again.")
        getOMove()

# Check if the player can put a symbol in the specified spot    
def checkMoveValidity(row, col):
    global board
    if (board[row - 1][col - 1] != '_'):
        return False
    else:
        return True

# Put the user's symbol in their specified position    
def placeSymbol(row, col, symbol):
    global board
    board[row - 1][col - 1] = symbol

# Check if the board is in a winning state
def inWinningState():
    global board
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][0] != '_'):
        return True
    elif (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] != '_'):
        return True
    elif (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] != '_'):
        return True
    elif (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] != '_'):
        return True
    elif (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] != '_'):
        return True
    elif (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != '_'):
        return True
    elif (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] != '_'):
        return True
    elif (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] != '_'):
        return True
    else:
        return False
    
# Return true if board doesn't have any '_'    
def isBoardFull():
    global board
    for i in board:
        if i.count('_') != 0:
            return False
    return True



# Display the board to the console
def displayBoard():
    for x in range(len(board)):
        output = "|"
        for symbol in board[x]:
            output += symbol + "|"
        print(output)


if __name__ == "__main__":
    main()