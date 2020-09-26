import pygame
import random
from BulletEnemy import BulletEnemy
from AssetsManager import *

class Enemy:
    def __init__(self, w, h, screen, sound_mgr):
        self.base = random.choice(['Dragon', 'Gargoyle'])
        systemRandom = random.SystemRandom()
        self.screen = screen
        self.sound_mgr = sound_mgr
        self.snd_fire = self.sound_mgr.LoadSound('fire_enemy')
        self.index = -1
        self.X = w + 10
        self.bullets = []
        self.doFire = False
        self.isAlive = True
        self.Y = systemRandom.randint(10, h - 200)
        self.sprites = LoadSprites(self.base + '/Fly')
        self.enemy  = LoadImage(self.sprites[self.index])
        self.Valid = True
        self.h = h
    
    def __del__(self):
        print('Eneymy Garbage Collected')
    
    def GetRect(self):
        return self.enemy.get_rect(topleft = (self.X, self.Y))
    
    def IsValid(self):
        return self.Valid
    
    def RemoveBullet(self, bullet):
        self.bullets.remove(bullet)
    
    def GetBullets(self):
        return self.bullets
        
    def Die(self):
        if self.isAlive:
            print('Enemy encountered bullet')
            self.sprites = LoadSprites(self.base + '/Dead')
            self.index = -1
            self.isAlive = False
        
    
    def __Fire(self):
        if self.isAlive:
            self.doFire = True
            self.index = -1
            self.sprites = LoadSprites(self.base + '/Attack')
            self.bullets.append(BulletEnemy(self.base, self.X, self.Y, self.screen))
            self.sound_mgr.PlaySound(self.snd_fire)
    
    def Update(self):
        if self.Valid:
            self.index = self.index + 1
            if self.index == len(self.sprites):
                if self.isAlive == False:
                    self.index = len(self.sprites) - 1
                elif self.doFire == False:
                    self.index = -1
                else:
                    self.index = 0
                    self.sprites = LoadSprites(self.base + '/Fly')
                    self.doFire = False
            
            self.enemy  = LoadImage(self.sprites[self.index])
            self.enemy.get_rect().left = self.X
            self.enemy.get_rect().top  = self.Y
            
            if self.isAlive:
                self.X = self.X - 5
            else:
                self.Y = self.Y + 15
                
            self.screen.blit(pygame.transform.flip(self.enemy, True, False), (self.X, self.Y))
            
            if random.randrange(0, 100) < 1:
                self.__Fire()
            
            for bullet in self.bullets:
                if bullet.IsValid():
                    bullet.Update()
                else:
                    del bullet
                
            if self.X + self.enemy.get_size()[0] <= 0:
                self.Valid = False
            elif self.Y + self.enemy.get_size()[1] >= self.h:
                self.Valid = False