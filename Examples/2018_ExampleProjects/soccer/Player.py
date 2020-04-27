from INI import *
import pygame
class player:
    def __init__(self, window):
        self.window = window
        self.X = 200
        self.Y = 200
        self.radius = 15
        pygame.draw.circle(window, red, (self.X, self.Y), self.radius)
    def move (self,dir):
        newX = self.X + dir[0]*4
        newY = self.Y + dir[1]*4
        if (newX  < win_width and newX > 0):
            self.X = newX
        if (newY  < win_height and newY > 0):
            self.Y = newY
        pygame.draw.circle(self.window, red, (self.X, self.Y), self.radius)
        
    
        
