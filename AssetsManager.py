import pygame
from os import walk

def LoadImage(img):
    if img.find('.') == -1:
        return pygame.image.load(r'./assets/images/' + img + '.png')
    else:
        return pygame.image.load(r'./assets/images/' + img)
    
def LoadSprites(path):
    f = []
    for (dirpath, dirnames, filenames) in walk('./assets/images/' + path):
        f.extend(filenames)
        break
    return [path + '/' + file for file in f]