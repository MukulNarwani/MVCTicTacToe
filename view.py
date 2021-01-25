import pygame
from pygame import surface

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((height, width),0,32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    while True:
        clock.tick(10)
        screen.blit(surface)
        pygame.display.update()
