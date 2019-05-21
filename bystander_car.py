import pygame, sys, time
from pygame.locals import *

B_CAR = pygame.image.load('Objects/bystander_car.png')

class bystander_car(pygame.sprite.Sprite):
    def __init__(self, xground2 , yground2):

        super().__init__()

        self.x = xground2
        self.y = yground2

        self.image = B_CAR

        self.rect = pygame.Rect(self.x, self.y, 40, 25)
