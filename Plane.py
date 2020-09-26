import pygame
from AssetsManager import *
from Bullet import Bullet

class Plane:
    def __init__(self, screen):
        self.screen = screen
        self.Shoot = False
        self.sprites_plane  = LoadSprites('Plane/Alive')
        self.bullets = []
        self.X = 0
        self.Y = 0
        self.isAlive = True
        self.index_sprite_plane  = -1
        self.plane = LoadImage(self.sprites_plane[self.index_sprite_plane])
        self.plane.get_rect(topleft=(30, 30))
    
    def GameOver(self, height):
        return self.Y - 10 >= height + self.plane.get_size()[1]
    
    def GetRect(self):
        return self.plane.get_rect(topleft = (self.X, self.Y))
    
    def GetBullets(self):
        return self.bullets
    
    def RemoveBullet(self, bullet):
        self.bullets.remove(bullet)
    
    def Die(self):
        print('Pilot is no more . .')
        self.isAlive = False
        self.sprites_plane = LoadSprites('Plane/Dead')
        self.index_sprite_plane = -1

    def Update(self, x, y, w, h):
        self.index_sprite_plane = self.index_sprite_plane + 1
        if self.index_sprite_plane >= len(self.sprites_plane):
            if self.isAlive == False:
                self.index_sprite_plane = len(self.sprites_plane) - 1
            elif self.Shoot == False:
                self.index_sprite_plane = 0
            else:
                self.sprites_plane = LoadSprites('Plane/Alive')
                self.index_sprite_plane = 0
                self.Shoot = False
            
        self.plane = LoadImage(self.sprites_plane[self.index_sprite_plane])
        self.plane = pygame.transform.scale(self.plane, (100, 75))
        
        if self.isAlive:
            self.X, self.Y = x, y
        else:
            self.Y = self.Y + 25
        
        self.screen.blit(self.plane, (self.X, self.Y))
        for bullet in self.bullets:
            if bullet.IsValid():
                bullet.Update()
            else:
                del bullet
            
    def Fire(self, x, y, width):
        if self.isAlive:
            self.Shoot = True
            self.sprites_plane  = LoadSprites('Plane/Shoot')
            self.bullets.append(Bullet(x + (self.plane.get_size()[0] - 55), y + (self.plane.get_size()[1] - 55), width, self.screen))
    
    def __del__(self):
        print('Plane Garbage Collected')