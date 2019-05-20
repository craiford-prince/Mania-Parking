import pygame, sys, time
from pygame.locals import *

R_WALL = pygame.image.load('Objects/right_wall.png')

class wall_right(pygame.sprite.Sprite):
    def __init__(self, coord2):

        super().__init__()

        self.x = coord2
        self.y = 0

        self.image = R_WALL

        self.rect = pygame.Rect(self.x, self.y, 14, 400)
