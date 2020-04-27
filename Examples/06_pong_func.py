#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:02:36 2018

@author: hemma

2 player game of Pong controlled using:
    Player 1 : W and S keys
    Player 2 : UP and DOWN arrows
    
"""

import pygame as pg 
import sys
import random
import math
import pygame.mixer as mix
from pygame.draw import circle, rect

##### FUNCTIONS ######    
    
def update_pad_pos():
    """ Updates the paddle position """
    for pos, vel in zip(pad_pos, pad_vel):
        if ((pos[y] > 0 and pos[y] < win_height - pad_height) or
            (pos[y] >= win_height - pad_height and vel[y] < 0) or 
            (pos[y] <= 0 and vel[y] > 0)):
                pos[y] += vel[y]
                
def collision_with_pad():
    """ Ball bounces in reverse direction if it hits a paddle """
    collision = [(ball_pos[x] <= (radius + pad_width)), 
                 (ball_pos[x] >= win_width - (radius + pad_width))]

    for pos, col in zip(pad_pos, collision): 
        if (col and 
            pos[y] < ball_pos[y] < pos[y] + pad_height):
            zap.play()
            ball_vel[x] = -ball_vel[x]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
            
def set_ball(x_dir=(random.randrange(0,2) == 0)):
    """ Resets ball to centre of screen """
    global ball_vel, ball_pos
    ball_vel = [random.randrange(2,4), random.randrange(1,3)] 
    if random.randrange(0,2) == 0:
        ball_vel[y] *= -1
    if x_dir:
        ball_vel[x] *= -1
    ball_pos = [win_width//2, win_height//2] 
    
def move_pads(up, down, vel):
    """ Moves the paddles when keyboard keys are pressed """
    if pressed[ up ] & pressed[ down ]: 
        vel[y] = 0
    elif pressed[ up ]: 
        vel[y] = -8
    elif pressed[ down ]: 
        vel[y] = 8
    else: 
        vel[y] = 0
        
def update_scores():
    """ Updates a counters for each player's score """
    if ball_pos[x] < -radius: 
        r_score += 1

    elif ball_pos[x] > win_width + radius:
        l_score += 1
        
def show_scores():
    """ Displays the current score of each player """
    myfont = pg.font.SysFont("Comic Sans MS", 20)
    label_l = myfont.render("Score " + str(l_score), 1, black)
    label_r = myfont.render("Score " + str(r_score), 1, black)
    window.blit(label_l, ((win_width * 1/4 - 20), 20))
    window.blit(label_r, ((win_width * 3/4 - 20), 20))


# 1. Initailise the pg library
pg.init()
mix.init()
mix.music.load("../Sounds/moonlight.wav")
mix.music.set_volume(0.5)
mix.music.play(-1, 0.0)

# 2. Variables
x = 0
y = 1

game_over = False   


# 2.1 colours 
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# 2.2 window
win_width = 600
win_height = 400

# 2.3 ball
radius = 20 
ball_vel = []# [random.randrange(2,4), random.randrange(1,3)]
ball_pos = []#= [win_width//2, win_height//2]
#if random.randrange(0,2) == 0:
#    ball_vel[x] *= -1
#if random.randrange(0,2) == 0:
#    ball_vel[y] *= -1

print(ball_vel)
print(ball_pos)  
# 2.4 paddles
pad_width = 40
pad_height = 120
pad1_vel = [0,0]
pad2_vel = [0,0]
pad1_pos = [0,                       win_height//2 - pad_height//2]
pad2_pos = [win_width - pad_width,   win_height//2 - pad_height//2] 

pad_pos = [pad1_pos, pad2_pos]
pad_vel = [pad1_vel, pad2_vel]

# 2.5 scores
l_score = 0
r_score = 0 

# We will use this later
#collision = [(ball_pos[x] <= (radius + pad_width)), 
#             (ball_pos[x] >= win_width - (radius + pad_width))] 
   
# 3. Launch a game window
window = pg.display.set_mode((win_width, win_height))

# 3.1 Set initial position of the ball
set_ball( x_dir=(random.randrange(0,2) == 0) )

# 3.2 Import sounds
zap = mix.Sound("../Sounds/zap8a.ogg")




# 4. Set up the main game loop
while True:
    
    # 5. Event processing
    event = pg.event.poll()
    
    # 5.1 Check if the user has quit the game
    if event.type == pg.QUIT:        
        pg.quit()
        sys.exit() 
        
    # If either player reaches 5 points, exit the program        
#    if l_score >= 5 or r_score >= 5:
#        pg.quit()
#        sys.exit() 
        
    if game_over:
        pg.quit()
        sys.exit()

    if l_score >= 5 or r_score >= 5:
        game_over = True
    
    # 5.2 Check if any keys have been pressed    
    pressed = pg.key.get_pressed()
    print(pressed)

    # 5.3 Check if paddles have been moved
    # 5.3.1 Right rectangle 
    move_pads(pg.K_UP, 
              pg.K_DOWN, 
              pad2_vel)
#    if pressed[pg.K_UP] & pressed[pg.K_DOWN]: 
#        pad2_vel[y] = 0
#    elif pressed[pg.K_UP]: 
#        pad2_vel[y] = -8
#    elif pressed[pg.K_DOWN]: 
#        pad2_vel[y] = 8
#    else: 
#        pad2_vel[y] = 0
        
    # 5.3.2 Left rectangle
    move_pads(pg.K_w, 
              pg.K_s, 
              pad1_vel)
#    if pressed[pg.K_w] & pressed[pg.K_s]: 
#        pad1_vel[y] = 0
#    elif pressed[pg.K_w]: 
#        pad1_vel[y] = -8
#    elif pressed[pg.K_s]: 
#        pad1_vel[y] = 8
#    else: 
#        pad1_vel[y] = 0
        
    collision = [(ball_pos[x] <= (radius + pad_width)), 
             (ball_pos[x] >= win_width - (radius + pad_width))] 
        
    # 6. Calculations     
    # 6.1 Collisions
    # 6.1.1 Collision with left paddle
    collision_with_pad()
#    collision = [(ball_pos[x] <= (radius + pad_width)), 
#                 (ball_pos[x] >= win_width - (radius + pad_width))]
#
#    for pos, col in zip(pad_pos, collision): 
#        if (col and 
#            pos[y] < ball_pos[y] < pos[y] + pad_height):
#            ball_vel[x] = -ball_vel[x]
#            ball_vel[0] *= 1.1
#            ball_vel[1] *= 1.1
        
#    if (ball_pos[x] <= (radius + pad_width) and 
#       pad1_pos[y] < ball_pos[y] < pad1_pos[y] + pad_height):
#        ball_vel[x] = -ball_vel[x]
#        ball_vel[0] *= 1.1
#        ball_vel[1] *= 1.1
#        
#        
#    # 6.1.2 Collision with right paddle    
#    if (ball_pos[x] >= win_width - (radius + pad_width) and 
#       pad2_pos[y] < ball_pos[y] < pad2_pos[y] + pad_height):
#        ball_vel[x] = -ball_vel[x]
#        ball_vel[0] *= 1.1
#        ball_vel[1] *= 1.1
        
        
    # 6.1.3 Reverse direction of travel if edge is reached
#    if ball_pos[x] > (win_width-radius) or ball_pos[x] < radius:
#        ball_vel[x] *= -1
    if ball_pos[y] > (win_height-radius) or ball_pos[y] < radius:
        ball_vel[y] *= -1
         
    
    
    # 6.2 Reset ball position if ball goes off screen
    if (ball_pos[x] < -radius) or (ball_pos[x] > win_width + radius):
        
        # 6.2.1 Update scores
        update_scores()
#        if ball_pos[x] < -radius: 
#            r_score += 1
#
#        elif ball_pos[x] > win_width + radius:
#            l_score += 1
            
#        ball_vel = [random.randrange(2,4), random.randrange(1,3)]    
#        if random.randrange(0,2) == 0:
#            ball_vel[y] *= -1
#        # if player on left loses, ball starts by firing to the left
#        if ball_pos[x] < 0:
#            ball_vel[x] *= -1
#            
#        ball_pos = [win_width//2, win_height//2] 
        set_ball( ball_pos[x] < 0 )
        
    # 6.3 Update ball position
    ball_pos[x] += ball_vel[x]
    ball_pos[y] += ball_vel[y]
    
    
    # 6.4 Update paddle position  
    update_pad_pos()

#        if ((pos[y] > 0 and pos[y] < win_height - pad_height) or
#            (pos[y] >= win_height - pad_height and vel[y] < 0) or 
#            (pos[y] <= 0 and vel[y] > 0)):
#                pos[y] += vel[y]
            
            
#    if ((pad1_pos[y] > 0 and pad1_pos[y] < win_height - pad_height) or
#        (pad1_pos[y] >= win_height - pad_height and pad1_vel[y] < 0) or 
#        (pad1_pos[y] <= 0 and pad1_vel[y] > 0)):
#            pad1_pos[y] += pad1_vel[y]
#            
#    if ((pad2_pos[y] > 0 and pad2_pos[y] < win_height - pad_height) or
#        (pad2_pos[y] >= win_height - pad_height and pad2_vel[y] < 0) or 
#        (pad2_pos[y] <= 0 and pad2_vel[y] > 0)):
#            pad2_pos[y] += pad2_vel[y]


    # 7. Draw everything
    # 7.1 Draw Window
    window.fill(blue)
    
    
    # 7.2 Draw ball and paddles
    circle(window, red, (int(ball_pos[x]), int(ball_pos[y])), radius)
    rect(window, white, pg.Rect(int(pad1_pos[x]), int(pad1_pos[y]), pad_width, pad_height))
    rect(window, white, pg.Rect(int(pad2_pos[x]), int(pad2_pos[y]), pad_width, pad_height))
    

    # 7.3 Draw score counters
    show_scores()
#    myfont = pg.font.SysFont("Comic Sans MS", 20)
#    label_l = myfont.render("Score " + str(l_score), 1, black)
#    label_r = myfont.render("Score " + str(r_score), 1, black)
#    window.blit(label_l, ((win_width * 1/4 - 20), 20))
#    window.blit(label_r, ((win_width * 3/4 - 20), 20))


    # 8. Update display
    pg.display.update()
    
    
    # 9. Frame rate
    clock = pg.time.Clock().tick(60)

    
