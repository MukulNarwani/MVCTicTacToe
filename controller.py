from model import GameBoard
from view import Viewer
from events import Events

class Controller():
    
    def __init__(self):
        self.board = GameBoard()
        self.events = Events()
        self.view = Viewer(self.events,self.board.view())
        self.events.onMouseClick += self.MouseHandler

    def MouseHandler(self,pos):
        try:
            self.board.makeMove(pos)
        except ValueError as e:
            self.events.onException(e)

        self.view.updateBoard(self.board.view())

    def start(self):
        self.view.main()
    

if __name__ == "__main__":
    game = Controller()
    game.start()
