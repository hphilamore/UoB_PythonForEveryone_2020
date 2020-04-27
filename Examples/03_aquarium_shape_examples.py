#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:02:36 2018

@author: hemma

Examples of drawing shapes using pygame

"""

import pygame 
import sys
import numpy as np

# 1. Initailise the pygame library
pygame.init()

# 2. Variables
win_width = 600
win_height = 400

black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# circle variables
#x_pos = 100
#y_pos = 50
circ_vel = [5, 1]
circ_pos = [100, 50] 
radius = 20  

# rectangle variables
rect_vel = [2, 3]
rect_pos = [30, 30]  
rect_width = 60
rect_height = 80


position = [circ_pos, rect_pos]
velocity = [circ_vel, rect_vel]  
horizontal = [[radius, radius], [rect_width, 0]]
vertical = [[radius, radius], [rect_height, 0]]

# 3. Launch a game window
window = pygame.display.set_mode((win_width, win_height))

# 4. Set up the main game loop
while True:
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()  
        
#    elif event.type == pygame.MOUSEBUTTONDOWN:
#        print("User pressed a mouse button")
        
    # 5. Draw
    window.fill(blue)
    # 
    
    # 5.1 Draw Shapes
    # circle
    pygame.draw.circle(window, black, (circ_pos[0], circ_pos[1]), radius)
    
    # rectangle
    #pygame.draw.rect(window, white, pygame.Rect(30, 300, 60, 80))
    pygame.draw.rect(window, white, pygame.Rect(rect_pos[0], rect_pos[1], rect_width, rect_height, width=10))
    
    # ploygon
    pygame.draw.polygon(window, red, [  (100, 100),
                                        (150, 150),
                                        (100, 150),
                                        (50, 125)])
    
    
    # arc
    # pygame.draw.arc(screen, color, (x,y,width,height), start_angle, stop_angle, thickness)
    # rect = (x_center, y_center, height, width) = coordinates of a rectangle that the arc would fit inside if it were drawn all the way around
    # if height and width are equal, then the rectangle is a square, and the arc will be a portion of a circle
    # start_angle and stop_angle are the angle on the unit circle in radians (not degrees) where the arc stops and starts
    arc_centre = (100, 100)
    (x, y) = arc_centre
    radius = 50
    startDeg = 0
    endDeg = 90
    thickness = 5
    rect = (x-radius,y-radius,radius*4,radius*2)
    startRad = np.radians(startDeg)
    endRad = np.radians(endDeg)

    pygame.draw.arc(window, 
                    red, 
                    rect,
                    startRad,
                    endRad,
                    thickness)

    
    # ellipse
    pygame.draw.ellipse(window, green, rect, 1)
#                                        ,
#                                        ,
#   # line
    pygame.draw.line(window, white, (0, win_height/2), (win_width, win_height/2), 3)                                    
#    
    
    # multiple continuous lines
    pygame.draw.lines(window, black, True, [(100, 100),
                                            (150, 150),
                                            (100, 150),
                                            (50, 125)], 3)
    
    # anti-aliased line
    # aaline(Surface, color, startpos, endpos, blend=1)
    pygame.draw.aaline(window, red, (400, 400), (500, 500), True)
    

    
    # 6. Update display
    pygame.display.update()
    
    # 7. Frame rate
    clock = pygame.time.Clock().tick(60)