import math
from numpy.core.numeric import cross
import pygame
import numpy as np
from  events import Events
import math
class Viewer():
    Cross = pygame.transform.scale(pygame.image.load('cross.png'),(249,249))
    Circle =pygame.transform.scale(pygame.image.load('circle.png'),(249,249))
    
    def __init__(self,eventHandle,boardState):
        self.HEIGHT,self.WIDTH=770,770
        self.boardState=boardState
        self.events = eventHandle
  
    def updateBoard(self, newBoard):
        self.boardState = newBoard
    
    def convertToMatrix(self,pos):
        step = self.WIDTH/3
        i=math.floor(pos[0]/step)
        k = math.floor(pos[1]/step)
        return (i,k)
        
    def convertToScreen(self,pos):
        i = self.WIDTH/3 * pos[0]
        j = self.WIDTH/3 * pos[1]        
        return (i,j)

    def main(self):
        pygame.init()
        #Starts the clock 
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH))

        #TODO better way to handle errors
        def exceptionHandler(e):
            screen.fill(pygame.Color("black"))
            screen.fill(pygame.Color("black"))
        self.events.onException += exceptionHandler

        #The Draw function
        def redrawWindow():
            it = np.nditer(self.boardState, flags=['multi_index'])
            for cell in it:
                if cell == -1:
                    screen.blit(self.Cross,self.convertToScreen(it.multi_index))
                if cell == 1:
                    screen.blit(self.Circle,self.convertToScreen(it.multi_index))
            pygame.display.update()
        
        #Main game loop
        run = True
        while run:
            clock.tick(10)
            # screen.blit(surface)
            redrawWindow()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    pos =self.convertToMatrix(pos)
                    self.events.onMouseClick(pos)
                
