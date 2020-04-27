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
from pygame.draw import circle, rect

import pygame.mixer as mix

import cfg
from cfg import x, y
from cfg import black, white, red, green, blue, win_width, win_height, radius, pad_width, pad_height

from pong_funcs import *


# 1. Initailise the pg library
pg.init()
mix.init()
mix.music.load("../../Sounds/moonlight.wav")
mix.music.set_volume(0.2)
mix.music.play(-1, 0.0)

new_high_score = None
game_over = False


## We will use this later
#collision = [(cfg.ball_pos[x] <= (radius + pad_width)), 
#             (cfg.ball_pos[x] >= win_width - (radius + pad_width))] 
   
# 3. Launch a game window
cfg.window = pg.display.set_mode((win_width, win_height))

# 3.1 Set initial position of the ball
set_ball( x_dir=(random.randrange(0,2) == 0) )

# 4. Set up the main game loop
while True:
    
    # 5. Event processing
    event = pg.event.poll()
    
    # 5.1 Check if the user has quit the game
    if event.type == pg.QUIT:        
        pg.quit()
        sys.exit()
        
    # If time exceeds 2 mins, exit the program
    if cfg.game_over:# 2 * 60000:
        pg.time.delay(3000)
        pg.quit()
        sys.exit()
        
    # If time exceeds 2 mins, exit the program
    if pg.time.get_ticks() >= 20000:# 2 * 60000: 
        cfg.game_over = True
        check_high_score()

    
    # 5.2 Check if any keys have been pressed    
    cfg.pressed = pg.key.get_pressed()

    # 5.3 Check if paddles have been moved
    
    # 5.3.1 Right rectangle 
    move_pads(pg.K_UP,
              pg.K_DOWN, 
              cfg.pad2_vel)
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
              cfg.pad1_vel)
#    if pressed[pg.K_w] & pressed[pg.K_s]: 
#        pad1_vel[y] = 0
#    elif pressed[pg.K_w]: 
#        pad1_vel[y] = -8
#    elif pressed[pg.K_s]: 
#        pad1_vel[y] = 8
#    else: 
#        pad1_vel[y] = 0
        

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
    if cfg.ball_pos[y] > (win_height-radius) or cfg.ball_pos[y] < radius:
        cfg.ball_vel[y] *= -1
         
    
    
    # 6.2 Reset ball position if ball goes off screen
    if (cfg.ball_pos[x] < -radius) or (cfg.ball_pos[x] > win_width + radius):
        
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
        set_ball( cfg.ball_pos[x] < 0 )
        
    # 6.3 Update ball position
    cfg.ball_pos[x] += cfg.ball_vel[x]
    cfg.ball_pos[y] += cfg.ball_vel[y]
    
    
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
    cfg.window.fill(blue)
    
    
    # 7.2 Draw ball and paddles
    circle(cfg.window, red, (int(cfg.ball_pos[x]), int(cfg.ball_pos[y])), radius)
    rect(cfg.window, white, pg.Rect(int(cfg.pad1_pos[x]), int(cfg.pad1_pos[y]), pad_width, pad_height))
    rect(cfg.window, white, pg.Rect(int(cfg.pad2_pos[x]), int(cfg.pad2_pos[y]), pad_width, pad_height))
    

    # 7.3 Draw score counters
    show_scores()
#    myfont = pg.font.SysFont("Comic Sans MS", 20)
#    label_l = myfont.render("Score " + str(l_score), 1, black)
#    label_r = myfont.render("Score " + str(r_score), 1, black)
#    window.blit(label_l, ((win_width * 1/4 - 20), 20))
#    window.blit(label_r, ((win_width * 3/4 - 20), 20))
    
    if cfg.new_high_score:
        show_new_high_score()
#        print("new_high_score")
#        myfont = pg.font.SysFont("Comic Sans MS", 40)
#        winner = "left" if cfg.l_score > cfg.r_score else "right"
#        text = myfont.render(f"{winner} player \n new highest score! \n {new_high_score} points!!!", 1, white)
#        cfg.window.blit(text, (win_width/4, win_height/2))
        
    
     
    


    # 8. Update display
    pg.display.update()
    
    
    # 9. Frame rate
    clock = pg.time.Clock().tick(60)

    
