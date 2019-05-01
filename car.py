import pygame, sys, time
from pygame.locals import *

class car(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.x = 40
        self.y = 25

        self.rect = pygame.Rect(self.x, self.y, 40, 25)

    def left(self):
        self.rect.x = self.rect.x - 5
    def right(self):
        self.rect.x = self.rect.x + 5
