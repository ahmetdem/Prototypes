
gameboard = [["-","-","-"],["-","-","-"],["-","-","-"]]
turn = 2

def showBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print()

def change(turn, board):
    while True:
        try:
            if turn % 2 == 0:
                row = int(input("Player 1, enter the row: "))
                column = int(input("Player 1, enter the column: "))
                
                if board[row][column] == "-":
                    board[row][column] = "X"
                else: raise ValueError
            else: 
                row = int(input("Player 2, enter the row: "))
                column = int(input("Player 2, enter the column: "))
                
                if board[row][column] == "-":
                    board[row][column] = "O"
                else: raise ValueError
            return board
        
        except:
            print("Enter valid Numbers!!!")
        
def gameover(board):
    #horizantally
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "X":
            return True
        elif board[i][0] == board[i][1] == board[i][2] == "O":
            return True
        
    #vertically
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == "X":
            return True
        if board[0][j] == board[1][j] == board[2][j] == "O":
            return True
    
    #diagnoally
    if board[0][0] == board[1][1] == board[2][2] == "X":
        return True
    if board[0][0] == board[1][1] == board[2][2] == "O":
        return True
            
while True:
    
    change(turn, gameboard)
    print()
    showBoard(gameboard)
    print()
    
    if gameover(gameboard):
        if turn % 2 == 0:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        break
    
    turn += 1
    
    
