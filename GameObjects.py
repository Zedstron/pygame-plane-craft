import random
import pygame
from Enemy import Enemy
from Bullet import Bullet
from Plane import Plane
from BulletEnemy import BulletEnemy
from Collectable import Collectable
from SoundEngine import SoundManager

class GameSession:
    def __init__(self, SH, SW, screen):
        self.enemies = []
        self.collectables = []
        self.SW = SW
        self.SH = SH
        self.screen = screen
        self.score = 0
        self.coins = 0
        self.isGameOver = False
        self.plane = Plane(screen)
        self.sound_mgr = SoundManager()
        self.snd_collectable = self.sound_mgr.LoadSound('collectable')
        self.snd_fire = self.sound_mgr.LoadSound('fire_plane')
        self.sound_mgr.PlayMusic('background')

    def CheckCollision(self, rect1, rect2):
        return rect1.colliderect(rect2)


    def SpanRandom(self):
        if random.randrange(0, 100) < 1:
            self.enemies.append(Enemy(self.SW, self.SH, self.screen, self.sound_mgr))
            
        if random.randrange(0, 100) < 1:
            self.collectables.append(Collectable(self.SW, self.SH, self.screen))
        
    def UpdateGameState(self, mX, mY):
        self.plane.Update(mX, mY, self.SW, self.SH)
        for enemy in self.enemies:
            if enemy.IsValid():
                enemy.Update()
                for bullet in self.plane.GetBullets():
                    if self.CheckCollision(bullet.GetRect(), enemy.GetRect()):
                        enemy.Die()
                        self.plane.RemoveBullet(bullet)
                   
                for bullet in enemy.GetBullets():
                    if self.CheckCollision(bullet.GetRect(), self.plane.GetRect()):
                        self.plane.Die()
                        self.sound_mgr.PlayMusic('gameover', 1)
                        enemy.RemoveBullet(bullet)
                   
                if self.CheckCollision(enemy.GetRect(), self.plane.GetRect()):
                    self.plane.Die()
                    self.sound_mgr.PlayMusic('gameover', 1)
            else:
                self.enemies.remove(enemy)
        
        for collectable in self.collectables:
            if collectable.IsValid():
                collectable.Update()
                if self.CheckCollision(collectable.GetRect(), self.plane.GetRect()):
                    self.coins = self.coins + 1
                    self.collectables.remove(collectable)
                    self.sound_mgr.PlaySound(self.snd_collectable)
            else:
                self.collectables.remove(collectable)
        
        self.SpanRandom()
    
    def Fire(self, mX, mY):
        self.mX = mX
        self.mY = mY
        self.plane.Fire(mX, mY, self.SW)
        self.sound_mgr.PlaySound(self.snd_fire)
    
    def GameOver(self, h):
        self.isGameOver = self.plane.GameOver(h)
        return self.isGameOver
    
    def Restart(self):
        self.isGameOver = False
        self.score, self.coins = 0, 0
        self.plane = Plane(self.screen)
        self.sound_mgr.PlayMusic('background')
        self.plane.Update(30, 30, self.SW, self.SH)
        
    def DrawScore(self):
        if self.isGameOver == False:
            self.score = self.score + 1
            largeFont = pygame.font.SysFont('comicsans', 40)
            text = largeFont.render('Score: ' + str(self.score), 1, (0, 0, 255))
            self.screen.blit(text, (5, 5))
            text = largeFont.render('Coins: ' + str(self.coins), 1, (255, 0, 0))
            self.screen.blit(text, (5, 40))
        else:
            largeFont = pygame.font.SysFont('comicsans', 100)
            text = largeFont.render('Score: ' + str(self.score), 1, (255, 255, 255))
            self.screen.blit(text, ((self.SW/2) - 150, (self.SH/4) - 75))
            text = largeFont.render('Coins: ' + str(self.coins), 1, (255, 255, 255))
            self.screen.blit(text, ((self.SW/2) - 150, (self.SH/4)))