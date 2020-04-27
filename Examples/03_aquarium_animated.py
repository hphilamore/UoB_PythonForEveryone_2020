#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:02:36 2018

@author: hemma
"""

import pygame 
import sys
import numpy as np

# 1. Initailise the pygame library
pygame.init()

# 2. Variables
x = 0
y = 1


# 2.1 colours
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# 2.2 window
win_width = 600
win_height = 400

# 2.3 Shape variables
# circle variables
#x_pos = 100
#y_pos = 50
circ_vel = [5, 1]
circ_pos = [100, 50] 
radius = 20  
circ_col = white

# rectangle variables
rect_vel = [2, 3]
rect_pos = [30, 30]  
rect_width = 60
rect_height = 80
rect_col = red

# polygon and line variables
poly_vel = [2, 3]
poly_pos = [[100, 100], [150, 150], [100, 150], [50, 125]] 
poly_col = green
line_col = black


position = [circ_pos, rect_pos] + poly_pos
velocity = [circ_vel, rect_vel] + [poly_vel] * 4
horizontal = [[radius, radius], [rect_width, 0]] + [[rect_width, 0]]*4
vertical = [[radius, radius], [rect_height, 0]]  + [[rect_height, 0]]*4

# print(position)
# print(velocity)
# print(horizontal)
# print(vertical)

# 3. Launch a game window
window = pygame.display.set_mode((win_width, win_height))

# 4. Set up the main game loop
while True:
    # 5. Event Processing
    event = pygame.event.poll()
    # 5.1 Check if the user has quit the game
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()  
        

    # 6. Calculations
    for vel, pos, vert, horiz in zip(velocity, position, vertical, horizontal):
        
        # print(pos)
        # print(vel)
        
        # Update position
        pos[0] += vel[0]  
        pos[1] += vel[1]
    
        # 6.2 Reverse direction of travel if edge is reached
        if pos[0] > (600-horiz[0]) or pos[0] < vert[1]:
            vel[0] *= -1
        if pos[1] > (400-vert[0]) or pos[1] < horiz[1]:
            vel[1] *= -1
        
    # 7. Draw
    # 7.1 Draw the window
    window.fill(blue)
    # 
    
    # 7.2 Draw Shapes
    # circle
    pygame.draw.circle(window, circ_col, (circ_pos[0], circ_pos[1]), radius)
    
    # rectangle
    #pygame.draw.rect(window, white, pygame.Rect(30, 300, 60, 80))
    pygame.draw.rect(window, rect_col, pygame.Rect(rect_pos[0], rect_pos[1], rect_width, rect_height, width=10))

    
    # ploygon
    pygame.draw.polygon(window, poly_col, poly_pos)
    
    # multiple continuous lines
    pygame.draw.lines(window, line_col, True, poly_pos, 3)
    
    
    # 8. Update display
    pygame.display.update()
    
    # 9. Frame rate
    clock = pygame.time.Clock().tick(60)