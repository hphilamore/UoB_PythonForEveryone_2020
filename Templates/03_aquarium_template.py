"""
Created on Thu May 10 21:53:55 2018

@author: Hemma Philamore

Aquarium Template
A pygame window containing animated moving shapes.
The shapes bounce off the sides of the window when they collide with it.

"""

import pygame
import sys


# 1. Initailise the pygame library
pygame.init()

# 2. Variables
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)
purple = (100, 0, 100)
#x_pos = 100
#y_pos = 100

# circle variables
circ_vel = [5, 1]
circ_pos = [100, 50]  
radius = 20  

# rectangle variables
rect_vel = [-2, -3]
rect_pos = [30, 300]  
rect_height = 80
rect_width = 60

position = [circ_pos, rect_pos]
velocity = [circ_vel, rect_vel]  
horizontal = [[radius, radius], [rect_width, 0]]
vertical = [[radius, radius], [rect_height, 0]]


# 3. Launch a game window
window = pygame.display.set_mode((600, 400))


# 4. Set up the main game loop
while True:
    # 5. Event Processing
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit() 
        
    # 6. Calculations
    
    # 6.1 Reverse direction of travel if edge is reached
#    if circ_pos[0] > (600-radius) or circ_pos[0] < radius:
#        circ_vel[0] *= -1
#    if circ_pos[1] > (400-radius) or circ_pos[1] < radius:
#        circ_vel[1] *= -1
#        
#    if rect_pos[0] > (600-rect_width) or rect_pos[0] < 0:
#        rect_vel[0] *= -1
#    if rect_pos[1] > (400-rect_height) or rect_pos[1] < 0:
#        rect_vel[1] *= -1
#    
#    # 6.2 Update shape position
#    circ_pos[0] += circ_vel[0]  
#    circ_pos[1] += circ_vel[1] 
#    
#    rect_pos[0] += rect_vel[0]  
#    rect_pos[1] += rect_vel[1]
    
    for vel, pos, vert, horiz in zip(velocity, position, vertical, horizontal):

        # 6.1 Reverse direction of travel if edge is reached
        if pos[0] > (600-horiz[0]) or pos[0] < vert[1]:
            vel[0] *= -1
        if pos[1] > (400-vert[0]) or pos[1] < horiz[1]:
            vel[1] *= -1
    
        # 6.2 Update shape position
        pos[0] += vel[0]  
        pos[1] += vel[1]
        
    
    # 7. Draw
    # window.fill((255, 255, 255))
    window.fill(purple)
    
    # 7.1 Draw circle
    # pygame.draw.circle(window, black, (100, 50), 20)# 7.1 Draw Shapes
    pygame.draw.circle(window, black, (circ_pos[0], circ_pos[1]), radius)
    pygame.draw.rect(window, white, pygame.Rect(rect_pos[0], rect_pos[1], rect_width, rect_height))
 

    # 8. Update display
    pygame.display.update()
    
    # 9. Frame rate
    clock = pygame.time.Clock().tick(60)