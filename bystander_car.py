import pygame, sys, time
from pygame.locals import *

class bystander_car(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.x = 40
        self.y = 25

        self.rect = pygame.Rect(self.x, self.y, 40, 25)
