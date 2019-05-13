import pygame, sys, time
from pygame.locals import *

CAR = pygame.image.load('Objects/car.png')

class car(pygame.sprite.Sprite):
    def __init__(self, ground):

        super().__init__()

        self.x = 40
        self.y = ground
        self.ground = ground

        self.image = CAR
        self.rect = pygame.Rect(self.x, self.y, 92, 52)

    def left(self):
        self.rect.x = self.rect.x - 5
    def right(self):
        self.rect.x = self.rect.x + 5
