import pygame as pg 
import sys
import random
import math

import cfg
from cfg import x, y
from cfg import black, white, red, green, blue, win_width, win_height, radius, pad_width, pad_height

import pygame.mixer as mix
mix.init()

##### FUNCTIONS ######    
    
def update_pad_pos():
    """ Updates the paddle position """
    for pos, vel in zip(cfg.pad_pos, cfg.pad_vel):
        if ((pos[y] > 0 and pos[y] < win_height - pad_height) or
            (pos[y] >= win_height - pad_height and vel[y] < 0) or 
            (pos[y] <= 0 and vel[y] > 0)):
                pos[y] += vel[y]
                
def collision_with_pad():
    """ Ball bounces in reverse direction if it hits a paddle """
    zap = mix.Sound("../../Sounds/zap8a.ogg")
    
    collision = [(cfg.ball_pos[x] <= (radius + pad_width)), 
                 (cfg.ball_pos[x] >= win_width - (radius + pad_width))]

    for pos, col in zip(cfg.pad_pos, collision): 
        if (col and 
            pos[y] < cfg.ball_pos[y] < pos[y] + pad_height):
            zap.play()
            cfg.ball_vel[x] = -cfg.ball_vel[x]
            cfg.ball_vel[0] *= 1.1
            cfg.ball_vel[1] *= 1.1
            
def set_ball(x_dir=(random.randrange(0,2) == 0)):
    """ Resets ball to centre of screen """
    #global ball_vel, ball_pos
    cfg.ball_vel = [random.randrange(5,10), random.randrange(5,10)] 
    if random.randrange(0,2) == 0:
        cfg.ball_vel[y] *= -1
    if x_dir:
        cfg.ball_vel[x] *= -1
    cfg.ball_pos = [win_width//2, win_height//2] 
    
def move_pads(up, down, vel):
    """ Moves the paddles when keyboard keys are pressed """
    if cfg.pressed[ up ] & cfg.pressed[ down ]: 
        vel[y] = 0
    elif cfg.pressed[ up ]: 
        vel[y] = -8
    elif cfg.pressed[ down ]: 
        vel[y] = 8
    else: 
        vel[y] = 0
        
def update_scores():
    """ Updates a counters for each player's score """
    if cfg.ball_pos[x] < -radius: 
        cfg.r_score += 1

    elif cfg.ball_pos[x] > win_width + radius:
        cfg.l_score += 1
        
def show_scores():
    """ Displays the current score of each player """
    myfont = pg.font.SysFont("Comic Sans MS", 20)
    label_l = myfont.render("Score " + str(cfg.l_score), 1, black)
    label_r = myfont.render("Score " + str(cfg.r_score), 1, black)
    cfg.window.blit(label_l, ((win_width * 1/4 - 20), 20))
    cfg.window.blit(label_r, ((win_width * 3/4 - 20), 20))
    

def check_high_score():
    """ Ends the game and checks past scores for a new high score """
    #cfg.game_over = True
        
    # store scores
    with open("scores.txt" , "a" ) as file :  
        file.write(f"{cfg.l_score} {cfg.r_score}\n")
        
    # read all previous scores
    with open("scores.txt" , "r" ) as file :  
        scores = file.read().split()
    
    # convert scores to integer values           
    scores = [int(s) for s in scores]
#    for s in range(len(scores)):
#        scores[s] = int(scores[s]) 
        
    # Check if l_score or r_score are a) highest recorded score b) unique 
    if cfg.l_score == max(scores) and scores.count(cfg.l_score) == 1:
        cfg.new_high_score = cfg.l_score
    elif cfg.r_score == max(scores) and scores.count(cfg.r_score) == 1:
        cfg.new_high_score = cfg.r_score
            
def show_new_high_score():
    """ If a new high score is achieved, the score and winning player is displayed """ 
    print("new_high_score")
    myfont = pg.font.SysFont("Comic Sans MS", 30)
    winner = "left" if cfg.l_score > cfg.r_score else "right"
    score = str(cfg.new_high_score)
    print(score)
    text = myfont.render(f"{winner} player, new highest score! {score} points!!!", 1, white)
    cfg.window.blit(text, (win_width/9, win_height/2))