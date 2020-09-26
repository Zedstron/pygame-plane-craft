import pygame
import random
from BulletEnemy import BulletEnemy
from AssetsManager import *

class Collectable:
    def __init__(self, w, h, screen):
        self.base = random.choice(['Coin'])
        systemRandom = random.SystemRandom()
        self.screen = screen
        self.index = 0
        self.X = w + 10
        self.Y = systemRandom.randint(10, h - 200)
        self.sprites = LoadSprites('Collectables/' + self.base)
        self.collectable  = LoadImage(self.sprites[self.index])
        self.Valid = True
    
    def __del__(self):
        print('collectable possibly Disposed')
    
    def IsValid(self):
        return self.Valid
    
    def GetRect(self):
        return self.collectable.get_rect(topleft = (self.X, self.Y))

    def Update(self):
        if self.Valid:
            self.index = self.index + 1
            if self.index == len(self.sprites):
                self.index = 0
            
            self.collectable  = LoadImage(self.sprites[self.index])
            self.collectable.get_rect().left = self.X
            self.collectable.get_rect().top  = self.Y
            self.X = self.X - 5
            self.screen.blit(self.collectable, (self.X, self.Y))

            if self.X + self.collectable.get_size()[0] <= 0:
                self.Valid = False