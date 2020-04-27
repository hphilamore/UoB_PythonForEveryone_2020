import sys
import random

black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)
purple = (100, 0, 100)
soccer_green = (1, 166, 17)
win_width = 612
win_height = 405
radius = 10
x = 0
y = 1
points = [0,0]
ball_pos = [1+win_width/2.0, win_height/2.0]
ball_vel = [random.randrange(2,4)*[1,-1][random.randrange(0,2)], random.randrange(1,3)*[1,-1][random.randrange(0,2)]]

# 2.4 paddles

pad_width = 20
pad_height = 120
pad1_vel = [0,0]
pad2_vel = [0,0]
pad1_pos = [0,win_height//2 - pad_height//2]
pad2_pos = [win_width - pad_width,   win_height//2 - pad_height//2] 
pad_pos = [pad1_pos, pad2_pos]
pad_vel = [pad1_vel, pad2_vel] 
