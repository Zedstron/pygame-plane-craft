import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
    
    def __del__(self):
        print('Sound Handler disposed')
    
    def PlayMusic(self, music, repeat = -1):
        pygame.mixer.music.load('./assets/sounds/' + music + '.mp3')
        pygame.mixer.music.play(repeat)
    
    def LoadSound(self, snd):
        return pygame.mixer.Sound('./assets/sounds/' + snd + '.wav')

    def PlaySound(self, snd):
        pygame.mixer.Sound.play(snd)