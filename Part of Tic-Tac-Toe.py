def getMove(p,b):
    validMove = False
    while not validMove:
        move = input("player "+p+" enter valid untaken square (1-9) on board : ")
        if (move >= "1" and move <= "9") and len(move) == 1:     #  missed this and len(move)== 1: 
            row = (int(move)-1)//3
            col = (int(move)-1)%3
            if board[row][col]=="X" or board[row][col]=="O":
                print("square on board taken try again")
            else:
                validMove=True
                board[row][col] = p
        else:
             print("not valid square on board try again")

#main
player= "X"
board = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
getMove(player,board)
