from INI import *
import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def drawSoccer(window):
    window.fill(soccer_green)
    pygame.draw.circle(window, white, (300, 200), 50, 2)
    pygame.draw.lines(window, white, False, [(300, 0),(300, 400)])
    pygame.draw.rect(window, white, (-10, 100, 90, 200), 3)
    pygame.draw.rect(window, white, (520, 100, 90, 200), 3)
    pygame.draw.circle(window, white, (300, 200), 3)
    return
