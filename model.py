import numpy as np


class GameBoard():

    def __init__(self):
        self.board = self.initializeBoard()
        self.activeTurn=-1

    #TODO: BoardInitialization 
    def initializeBoard(self):
        return np.array([[0,0,0],[0,0,0],[0,0,0]])
    
    def view(self):
        print(self.board)
    
    #TODO: Win Logic
    

    #TODO: Move Logic
    def makeMove(self, pos):
        if(self.board[pos[0],pos[1]] == 0):
            
            self.board[pos[0],pos[1]] = self.activeTurn
            self.activeTurn = self.activeTurn*-1
        else:
            raise ValueError('position already filled')

a = GameBoard()
a.view()
a.makeMove((0,0))
a.view()
a.makeMove((1,1))
a.view()
a.makeMove((0,0))
