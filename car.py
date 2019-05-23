import pygame, sys, time
from pygame.locals import *

#class for main car
CAR = pygame.image.load('Objects/car.png')

class car(pygame.sprite.Sprite):
    def __init__(self, ground):

        super().__init__()

        self.x = 40
        self.y = ground

        self.image = CAR
        self.rect = pygame.Rect(self.x, self.y, 88, 52)
#go left
    def left(self):
        self.rect.x = self.rect.x - 5
#go right
    def right(self):
        self.rect.x = self.rect.x + 5
