import pygame
from AssetsManager import *

class BulletEnemy:
    def __init__(self, base, x, y, screen):
        self.screen = screen
        self.index = 0
        self.X = x
        self.Y = y
        self.sprites = LoadSprites(base + '/Bullet')
        self.bullet  = LoadImage(self.sprites[self.index])
        self.Valid = True
    
    def __del__(self):
        print('Enemy Bullet Expired (Out of Screen)')
    
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
            self.bullet.get_rect().left = self.X
            self.bullet.get_rect().top  = self.Y
            self.X = self.X - 25
            self.screen.blit(pygame.transform.flip(self.bullet, True, False), (self.X, self.Y))
            if self.X + self.bullet.get_size()[0] <= 0:
                self.Valid = False