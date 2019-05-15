import pygame, sys, time
from pygame.locals import *

L_WALL = pygame.image.load('Objects/left_wall.png')

class wall_left(pygame.sprite.Sprite):
    def __init__(self, coord):

        super().__init__()

        self.x = 0
        self.y = coord

        self.image = L_WALL

        self.rect = pygame.Rect(self.x, self.y, 14, 400)
