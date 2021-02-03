import math
from numpy.core.numeric import cross
import pygame
import numpy as np
from  events import Events
import math
from itertools import cycle


class Viewer():
    Cross = pygame.transform.scale(pygame.image.load('cross.png'),(249,249))
    Circle =pygame.transform.scale(pygame.image.load('circle.png'),(249,249))
    
    def __init__(self,eventHandle,boardState):
        self.HEIGHT,self.WIDTH=770,770
        self.boardState=boardState
        self.events = eventHandle
        self.winner = None
        self.run = True
  
    def updateBoard(self, newBoard):
        self.boardState = newBoard
    
    def handleWin(self,winner):
        print(winner)
        self.winner = winner
        #self.run = False

    def convertToMatrix(self,pos):
        step = self.WIDTH/3
        i=math.floor(pos[0]/step)
        k = math.floor(pos[1]/step)
        return (i,k)
        
    def convertToScreen(self,pos):
        i = self.WIDTH/3 * pos[0]
        j = self.WIDTH/3 * pos[1]        
        return (i,j)
    
    #Draws The board by placing Crosses and Circles
    def drawBoard(self,screen):
        it = np.nditer(self.boardState, flags=['multi_index'])
        for cell in it:
            if cell == -1:
                screen.blit(self.Cross,self.convertToScreen(it.multi_index))
            if cell == 1:
                screen.blit(self.Circle,self.convertToScreen(it.multi_index))


    def drawWinner(self,screen):
        if self.winner:
            #Display Win screen
            pygame.font.init() # you have to call this at the start,            
            myfont = pygame.font.SysFont('Times New Roman', 30)
            screen.fill(pygame.Color("white"))
            if self.winner == 1 :
                textsurface = myfont.render('Circle Wins', False, pygame.Color("black"))
                screen.blit(textsurface,(self.WIDTH/2 - 40,self.HEIGHT/2-30))
            if self.winner ==-1:
                textsurface = myfont.render('Cross Wins', False, pygame.Color("black"))
                screen.blit(textsurface,(self.WIDTH/2-40 ,self.HEIGHT/2-30))

    #TODO better way to handle errors
    def exceptionHandler(self,screen):
        screen.fill(pygame.Color("black"))
        print('a')
        screen.fill(pygame.Color("black"))

        
    # Text Renderer
    def text_format(self,message, textFont, textSize, textColor):
        newFont=pygame.font.SysFont(textFont, textSize)
        newText=newFont.render(message, 0 , textColor)
        return newText

    
    
    def main(self):
        pygame.init()
        #Starts the clock 
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        self.events.onException += self.exceptionHandler

        #Menu loop
        menu=True
        selected="quit"
        LogIn = False
        options = ["start","quit","LogIn"]
        LogInOptions = cycle(['Textbox','login','back'])
        text = ''
        cycleOptions= cycle(options)
        
        
        # Main Menu UI
        def drawMenu():
            screen.fill(pygame.Color("black"))

            title=self.text_format("Tic Tac Toe", font, 90, pygame.Color('yellow'))
            if selected=="start":
                text_start=self.text_format("START", font, 75, pygame.Color('white'))
            else:
                text_start = self.text_format("START", font, 75, pygame.Color('yellow'))
            if selected=="quit":
                text_quit=self.text_format("QUIT", font, 75, pygame.Color('white'))
            else:
                text_quit = self.text_format("QUIT", font, 75, pygame.Color('yellow'))
            if selected=="LogIn":
                text_login=self.text_format("LogIn", font, 75, pygame.Color('white'))
            else:
                text_login = self.text_format("LogIn", font, 75, pygame.Color('yellow'))
            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            quit_rect=text_quit.get_rect()
            # Main Menu Text
            screen.blit(title, (self.WIDTH/2 - (title_rect[2]/2), 80))
            screen.blit(text_start, (self.WIDTH/2 - (start_rect[2]/2), 300))
            screen.blit(text_quit, (self.WIDTH/2 - (quit_rect[2]/2), 360))
            screen.blit(text_login, (self.WIDTH/2 - (quit_rect[2]/2), 420))
            pygame.display.update()
        
        
        #TODO seperate menu and login loops
        while  menu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if LogIn:   
                        if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key==pygame.K_RETURN :
                            if selected == 'login' or 'textbox':
                                print(text)
                                text=''
                            if selected == 'back':
                                LogIn=False
                            
                        elif event.key==pygame.K_DOWN:
                            selected = next(LogInOptions)
                            print(selected)

                        elif event.key==pygame.K_UP:
                            selected = next(LogInOptions)
                            print(selected)

                        else:
                            text += event.unicode                            
                    else:
                        if event.key==pygame.K_DOWN:
                            selected = next(cycleOptions)
                        if event.key==pygame.K_UP:
                            next(cycleOptions)
                            selected = next(cycleOptions)
                        
                        if event.key==pygame.K_RETURN:
                            if selected=="start":
                                menu=False
                            if selected=="quit":
                                pygame.quit()
                                quit()
                            if selected=="LogIn":
                                LogIn = True


            def drawLogIn():
                screen.fill(pygame.Color("black"))

                input_box = pygame.Rect(self.WIDTH/2 -90, 250 , 40, 32)
                FONT = pygame.font.Font(None, 32)
                color_active = pygame.Color('white')
                color_inactive = pygame.Color('yellow')
                

                if selected=="login":
                    text_login=self.text_format("LogIn", font, 75, pygame.Color('white'))
                else:
                    text_login = self.text_format("LogIn", font, 75, pygame.Color('yellow'))
                if selected=="Textbox":
                    color = color_active
                else:
                    color = color_inactive
                if selected=="back":
                    text_back=self.text_format("back", font, 75, pygame.Color('white'))
                else:
                    text_back = self.text_format("back", font, 75, pygame.Color('yellow'))

                txt_surface = FONT.render(text, True, color)
                login_rect=text_login.get_rect()
                back_rect=text_back.get_rect()
                # Render the current text.
                # Resize the box if the text is too long.
                width = max(200, txt_surface.get_width())
                input_box.w = width
                # Blit the text.
                screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                # Blit the input_box rect.
                pygame.draw.rect(screen, color, input_box, 2) 

                # Main Menu Text
                screen.blit(text_back, (self.WIDTH/2 - (back_rect[2]/2), 420))
                screen.blit(text_login, (self.WIDTH/2 - (login_rect[2]/2), 360))




                pygame.display.update()
                        
            font = "Retro.ttf"
           
            drawLogIn() if LogIn else drawMenu()

            
        

        #The Draw function
        def redrawWindow():
            screen.fill(pygame.Color("white"))
            self.drawBoard(screen)
            self.drawWinner(screen)
            pygame.display.update()

        #Main game loop
        while self.run:
            clock.tick(10)
            # screen.blit(surface)
            redrawWindow()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    pos =self.convertToMatrix(pos)
                    self.events.onMouseClick(pos)
        
        

            
