import pygame, sys, time
from pygame.locals import *

D_WALL = pygame.image.load('Objects/down_wall.png')

class wall_down(pygame.sprite.Sprite):
    def __init__(self, coord_y):

        super().__init__()

        self.x = 0
        self.y = coord_y

        self.image = D_WALL

        self.rect = pygame.Rect(self.x, self.y, 700, 15)
