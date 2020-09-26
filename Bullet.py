import pygame
from Enemy import Enemy
from AssetsManager import *

class Bullet:
    def __init__(self, x, y, w, screen):
        self.screen = screen
        self.index = 0
        self.X = x
        self.Y = y
        self.W = w
        self.sprites = LoadSprites('Plane/Bullet')
        self.bullet  = LoadImage(self.sprites[self.index])
        self.Valid = True
    
    def __del__(self):
        print('Bullet Expired (Out of Screen)')
    
    def IsValid(self):
        return self.Valid
    
    def GetRect(self):
        return self.bullet.get_rect(topleft = (self.X, self.Y))
    
    def Update(self):
        if self.Valid:
            self.index = self.index + 1
            if self.index == len(self.sprites):
                self.index = 0
            
            self.bullet  = LoadImage(self.sprites[self.index])
            self.bullet = pygame.transform.scale(self.bullet, (32, 32))
            self.bullet.get_rect().left = self.X
            self.bullet.get_rect().top  = self.Y
            self.X = self.X + 25
            self.screen.blit(self.bullet, (self.X, self.Y))
            if self.X > self.W:
                self.Valid = False