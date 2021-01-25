from model import GameBoard

class Controller():
    
    def __init__(self,gameBoard,boardViewer):
        self.board = gameBoard
        self.view = boardViewer
    
    #TODO: mouse Handler, convert to posn and send to model
