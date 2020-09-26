import pygame
import random
from screeninfo import get_monitors
from pygame.locals import *
from AssetsManager import *
from GameObjects import GameSession

def GetRandomBg(lst):
    return random.choice(lst)

def ToggleFullscreen():
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor() 
    
    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()
    
    screen = pygame.display.set_mode((w, h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(*caption)

    pygame.key.set_mods(0)

    pygame.mouse.set_cursor(*cursor)
    
    return screen

if __name__ == '__main__':
    SW, SH = 0, 0
    mX, mY = 30, 30
    backgrounds = ['background1', 'background2', 'background3']
    isGameOver = False
    pygame.init()
    FPS = 24
    fpsClock = pygame.time.Clock()
    bg = LoadImage('backgrounds/' + GetRandomBg(backgrounds))
    for m in get_monitors():
        SW,SH = m.width,m.height
        break
        
    bg = pygame.transform.scale(bg, (SW, SH))
    screen = pygame.display.set_mode((SW, SH))
    pygame.display.set_caption('Cute Plane')
    ToggleFullscreen()
    game_session = GameSession(SH, SW, screen)
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    _quit = False
    
    while not _quit:
        screen.blit(bg, (0, 0))

        game_session.DrawScore()

        for e in pygame.event.get():
            if e.type is KEYDOWN:
                if e.key == K_ESCAPE:
                    _quit = True
                elif e.key == K_n and isGameOver:
                    _quit = True
                elif e.key == K_y and isGameOver:
                    isGameOver = False
                    game_session.Restart()
                    bg = LoadImage('backgrounds/' + GetRandomBg(backgrounds))
            elif e.type == pygame.MOUSEMOTION:
                mX, mY = e.pos
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    game_session.Fire(mX, mY)

        if game_session.GameOver(SH) and isGameOver == False:
            isGameOver = True
            bg = LoadImage('gameover')
        
        if isGameOver == False:   
            game_session.UpdateGameState(mX, mY)

        pygame.display.flip()
        fpsClock.tick(FPS)