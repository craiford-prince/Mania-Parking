import pygame, sys, time
from pygame.locals import *

DISPLAYSURF = pygame.display.set_mode((650, 450), 0, 32)

BLACK = (0,0,0)

while True:
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
