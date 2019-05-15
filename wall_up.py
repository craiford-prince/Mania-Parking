import pygame, sys, time
from pygame.locals import *

U_WALL = pygame.image.load('Objects/top_wall.png')

class wall_up(pygame.sprite.Sprite):
    def __init__(self, coord):

        super().__init__()

        self.x = 0
        self.y = coord

        self.image = U_WALL

        self.rect = pygame.Rect(self.x, self.y, 700, 14)
