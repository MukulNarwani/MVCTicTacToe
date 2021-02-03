import numpy as np


class GameBoard():

    def __init__(self):
        self.board = self.initializeBoard()
        self.activeTurn=-1

    #BoardInitialization 
    def initializeBoard(self):
        return np.array([[0,0,0],[0,0,0],[0,0,0]])
    
    def view(self):
        return(self.board)
    
    #Win Logic
    def checkRows(self,board):
       
        for row in board:
            if len(set(row)) == 1:
                return row[0]
        return 0

    def checkDiagonals(self):
        board = self.board
        if len(set([board[i][i] for i in range(len(board))])) == 1:
            return board[0][0]
        if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
            return board[0][len(board)-1]
        return 0

    def checkWin(self):
        board = self.board
        #transposition to check rows, then columns
        for newBoard in [board, np.transpose(board)]:
            result = self.checkRows(newBoard)
            if result:
                return result
        diagResult = self.checkDiagonals() 
        return diagResult

    

    #Move Logic
    def makeMove(self, pos):
        if(self.board[pos[0],pos[1]] == 0):
            
            self.board[pos[0],pos[1]] = self.activeTurn
            self.activeTurn = self.activeTurn*-1
        else:
            raise ValueError('position already filled')


