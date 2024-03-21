board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

def main():
    print("Main method.")
    displayBoard()

def displayBoard():
    for x in range(len(board)):
        output = "|"
        for symbol in board[x]:
            output += symbol + "|"
        print(output)


if __name__ == "__main__":
    main()