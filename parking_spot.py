import pygame, sys, time
from pygame.locals import *
#box to park in to win
P_SPOT = pygame.image.load('Objects/parking_spot.png')

class parking_spot(pygame.sprite.Sprite):
    def __init__(self, xground3 , yground3):

        super().__init__()

        self.x = xground3
        self.y = yground3

        self.image = P_SPOT

        self.rect = pygame.Rect(self.x, self.y, 85, 50)
