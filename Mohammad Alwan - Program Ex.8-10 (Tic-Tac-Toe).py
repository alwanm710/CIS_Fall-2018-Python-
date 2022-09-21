#tic tac toe
#function print board
def printBoard(board):
    print("   |   |   ")
    print(" "+board[0][0]+" | "+board[0][1]+" | "+board[0][2]+" ")
    print("---|---|---")
    print(" "+board[1][0]+" | "+board[1][1]+" | "+board[1][2]+" ")
    print("---|---|---")
    print(" "+board[2][0]+" | "+board[2][1]+" | "+board[2][2]+" ")
    print("   |   |   ")

def getMove(b, p):
    validPick = False
    while not (validPick):
        userPick = input("Player "+p+" enter an umark square 1-9:")
        if userPick >= "1" and userPick <= "9":
            row = (int(userPick) - 1) // 3
            col = (int(userPick) - 1) % 3
            if board[row][col] == "X" or board[row][col] == "O":
                print("Sorry this square is taken try again")
            else:
                b[row][col] = p
                validPick = True
        else:
            print("Must enter a square 1-9 - please try again")

def checkWinner(p, b):
    if (b[0][0] == p and b[0][1] == p and b[0][2] == p)or \
       (b[1][0] == p and b[1][1] == p and b[1][2] == p)or \
       (b[2][0] == p and b[2][1] == p and b[2][2] == p)or \
       (b[0][0] == p and b[1][0] == p and b[2][0] == p)or \
       (b[0][1] == p and b[1][1] == p and b[2][1] == p)or \
       (b[0][2] == p and b[1][2] == p and b[2][2] == p)or \
       (b[0][0] == p and b[1][1] == p and b[2][2] == p)or \
       (b[2][0] == p and b[1][1] == p and b[0][2] == p):
            return True
    else:
            return False
        



#initialize board array
board = [ ["1","2","3"], ["4","5","6"], ["7","8","9"]]
count = 1
Player = "X"
while count <= 9:
    printBoard(board)
    getMove(board, Player)
    if count >= 5:
        win = checkWinner(Player, board)
        if win:
            printBoard(board)
            print("Congratulation player",Player,"you win")
            break
    if Player == "X":
        Player = "O"
    else:
        Player = "X"
    count = count + 1
print("That's all folks")
