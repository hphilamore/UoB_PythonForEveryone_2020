#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 22:27:47 2018

@author: sandrute12@hotmail.com
"""


# 0. Import libraries
import pygame 
import sys
import random
#import math

#Variables 
x = 0
y = 1



# 1. Initailise the pygame library
pygame.init()

# 2. Colors
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)
purple = (140, 0, 140)

# 2.1 Other variables
penguin = True
score = 0


# 2.2 Position and velocity variables 
penguin_pos =[30, 315] 
penguin_vel = [0, 0]       


# 3. Launch a game window + background
win_size = [1000, 650]
window = pygame.display.set_mode((1000, 650))
pygame.display.set_caption ('Underwater')

background_start = pygame.image.load("../background1.png").convert()
b1_size = pygame.Rect(background_start.get_rect()).size
print('b1_size=', b1_size)

background2 = pygame.image.load("../background2.png").convert()
b2_size = pygame.Rect(background2.get_rect()).size
print('b2_size=', b2_size)

background3 = pygame.image.load("../background3.png").convert()
b3_size = pygame.Rect(background3.get_rect()).size
print('b3_size=', b3_size)

background4 = pygame.image.load("../background4.png").convert()
b4_size = pygame.Rect(background4.get_rect()).size
print('b4_size=', b4_size)

game_over = pygame.image.load("../black.png").convert()
g_o_size = pygame.Rect(game_over.get_rect()).size
print('g_o_size=', g_o_size)

winner = pygame.image.load("../win.png").convert()
w_size = pygame.Rect(winner.get_rect()).size
print('w_size=', w_size)


#Penguin pictures
penguin = pygame.image.load("../peng1.png")
p_size = pygame.Rect(penguin.get_rect()).size
print('p_size=', p_size)

penguin2 = pygame.image.load("../peng2.png")
p2_size = pygame.Rect(penguin2.get_rect()).size
print('p2_size=', p2_size)

win_peng = pygame.image.load("../proudpeng.png")
p3_size = pygame.Rect(win_peng.get_rect()).size
print('p3_size=', p3_size)

###Fishes 
fishy = pygame.image.load("../arthritis.png")
f_size = pygame.Rect(fishy.get_rect()).size

blowfishy = pygame.image.load("../blowfish.png")
bf_size = pygame.Rect(blowfishy.get_rect()).size

orcy = pygame.image.load("../orca.png")
o_size = pygame.Rect(orcy.get_rect()).size

#3.1 Time
start_time = pygame.time.get_ticks()
print(start_time)

#Functions

def change_background():
    global start_time
    """ Changing the background after a certain time """    
   
    time_now = pygame.time.get_ticks()
    print(time_now - start_time)


    #change to first background    
    if time_now - start_time >= 0 and time_now - start_time < 15000:
        window.blit(background_start, [0, 0])    
    
    #change to second background
    if time_now - start_time  >= 15000 and time_now - start_time < 30000:
        window.blit(background2, [0, 0])
        print (background2) 
        
     #change to third background    
    if time_now - start_time >= 30000 and time_now - start_time < 45000:
        window.blit(background3, [0, 0])
        print (background3)
        
        # if you don't score at all you die
        if score <= 10:
            penguin == False
            the_end ()
        
     #change to fourth background
    if time_now - start_time >= 45000 and time_now - start_time < 60000:
        window.blit(background4, [0, 0])
        print (background4)
        
    if time_now - start_time > 60000:
        start_time = pygame.time.get_ticks()
        
def attack ():
    global start_time
    """ Orca attacks both after time and score """ 
    
    time_now = pygame.time.get_ticks()
    print(time_now - start_time)
 
    
    #orca attack time and speed 
    if time_now - start_time > 45000 and time_now - start_time < 60000:
        # Process each orca in the list
        for i in range(len(o_list)):
            # speed of the fish
            o_list[i][0] -= 9
            
    if time_now - start_time > 60000:
        start_time = pygame.time.get_ticks()
        
    if 60 <= score and score < 125: 
        # Process each orca in the list
        for i in range(len(o_list)):
            # speed of the fish
            o_list[i][0] -= 9
        
    if 200 <= score and score < 225: 
        # Process each orca in the list
        for i in range(len(o_list)):
            # speed of the fish
            o_list[i][0] -= 9
    
    if 300 <= score and score < 325: 
        # Process each orca in the list
        for i in range(len(o_list)):
            # speed of the fish
            o_list[i][0] -= 10
            
    if 425 <= score and score < 425: 
        # Process each orca in the list
        for i in range(len(o_list)):
            # speed of the fish
            o_list[i][0] -= 11
#            

        
        
def speed_up ():
    global start_time
    """ Speeds up fish """ 
    
 
    if 25 <= score and score < 50:
        for i in range(len(fish_list)):
            # speed of the fish
            fish_list[i][0] -= 4    
            
        for i in range(len(bf_list)):
            # speed of the fish
            bf_list[i][0] -= 5
            
    if 50 <= score and score < 75:
 
        for i in range(len(fish_list)):
            # speed of the fish
            fish_list[i][0] -= 5    
            
        for i in range(len(bf_list)):
            # speed of the fish
            bf_list[i][0] -= 6
        
    
    if 75 <= score and score < 100:
        for i in range(len(fish_list)):
            # speed of the fish
            fish_list[i][0] -= 6    
            
        for i in range(len(bf_list)):
            # speed of the fish
            bf_list[i][0] -= 7
            
    if 100 <= score and score < 125:
        for i in range(len(fish_list)):
            # speed of the fish
            fish_list[i][0] -= 9    
            
        for i in range(len(bf_list)):
            # speed of the fish
            bf_list[i][0] -= 10
        
            
    if 125 <= score and score < 150:
        for i in range(len(fish_list)):
            # speed of the fish
            fish_list[i][0] -= 10    
            
        for i in range(len(bf_list)):
            # speed of the fish
            bf_list[i][0] -= 11
            
    if 150 <= score and score < 300:
        for i in range(len(fish_list)):
            # speed of the fish
            fish_list[i][0] -= 11    
            
        for i in range(len(bf_list)):
            # speed of the fish
            bf_list[i][0] -= 12
    
    if 300 <= score:
        for i in range(len(fish_list)):
            # speed of the fish
            fish_list[i][0] -= 13   
            
        for i in range(len(bf_list)):
            # speed of the fish
            bf_list[i][0] -= 14
    
                  
                
            
def the_end ():
        
    """If you die"""
        
    window.blit(game_over, [0, 0])
        
    font = pygame.font.SysFont('helveticaneuedeskinterface', 100)   # font from list above  
    white = (255, 255, 255)
    text = font.render("GAME OVER", True, white)
    window.blit(text, (400, 325))
        
    window.blit(penguin2, [500, 425])
    

        
#        font = pygame.font.SysFont('helveticaneuedeskinterface', 100)   # font from list above  
#        white = (255, 255, 255)
#        text = font.render("Press "R" to restart", True, white)
#        window.blit(text, (500, 275))
        
    
# All the lists!!!        
# Create an empty array
fish_list = []
 
# Loop 50 times and add a fish in a random x,y position
for i in range(10):
    x1 = random.randrange(1000, 1400)
    y1 = random.randrange(0, 650)
    fish_list.append([x1, y1])

# Create an empty array
bf_list = []
 
# Loop 50 times and add a fish in a random x,y position
for i in range(3):
    x2 = random.randrange(1000, 1400)
    y2 = random.randrange(0, 650)
    bf_list.append([x2, y2])
    

# Create an empty array
o_list = []
 
# Loop 50 times and add a fish in a random x,y position
for i in range(1):
    x3 = random.randrange(1200, 1400)
    y3 = random.randrange(40, 610)
    o_list.append([x3, y3])    
    
    

# 4. Set up the main game loop
while True:
  
    event = pygame.event.poll()     
    time_now = pygame.time.get_ticks()
    
    if penguin :
        change_background()
        speed_up ()
        attack ()

    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit() 

    # 4.1 Event loop
    # 4.1.1 : Key press 
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_q]: 
            pygame.quit()
#    if pressed[pygame.K_r] and penguin == False :
#            game()
    elif pressed[pygame.K_UP] & pressed[pygame.K_DOWN]: 
            penguin_vel[y] = 0
    elif pressed[pygame.K_UP]: 
            penguin_vel[y] = -9
    elif pressed[pygame.K_DOWN]: 
            penguin_vel[y] = 9
    else: 
            penguin_vel[y] = 0
            
    if pressed[pygame.K_LEFT] & pressed[pygame.K_RIGHT]: 
            penguin_vel[x] = 0
    elif pressed[pygame.K_LEFT]: 
            penguin_vel[x] = -9
    elif pressed[pygame.K_RIGHT]: 
            penguin_vel[x] = 9
    else: 
            penguin_vel[x] = 0
            
            
#        # 4.1.2 : Mouse position
#        mouse_pos = pygame.mouse.get_pos()
#        
#        # 4.1.3 : Mouse click
#        if event.type==pygame.MOUSEBUTTONDOWN:
#            mouse_click = True
#        else:
#            mouse_click = False

    # 4.2.2 Update position
    penguin_pos[x] += penguin_vel[x]
    penguin_pos[y] += penguin_vel[y]
  
    #If penguin collide with fish     
    for i, fish in enumerate(fish_list): 
        p_a = [penguin_pos[x],penguin_pos[y]]
        p_b = [penguin_pos[x] + p_size[x],penguin_pos[y]]
        p_c = [penguin_pos[x],penguin_pos[y]+p_size[y]]
        p_d = [penguin_pos[x] + p_size[x],penguin_pos[y]+p_size[y]]
        
        f_a = [fish[x],fish[y]]
        f_c = [fish[x],fish[y]+f_size[y]]
       
           
        # 6.1.1 Collision with fish 
        if ((p_a[x] < f_a[x] < p_b[x]) and (p_b[y] < f_a[y] < p_d[y])
            or 
            (p_c[x] < f_c[x] < p_d[x]) and (p_b[y] < f_c[y] < p_d[y])):
            fish_list[i] = [random.randrange(0, 650),random.randrange(1000, 1400)]
            score += 1
                 
        
    #If penguin collide with blowfish    
    for i, blowfish in enumerate(bf_list): 
        p_a = [penguin_pos[x],penguin_pos[y]]
        p_b = [penguin_pos[x] + p_size[x],penguin_pos[y]]
        p_c = [penguin_pos[x],penguin_pos[y]+p_size[y]]
        p_d = [penguin_pos[x] + p_size[x],penguin_pos[y]+p_size[y]]
        
        b_a = [blowfish[x],blowfish[y]]
        b_c = [blowfish[x],blowfish[y]+bf_size[y]]
       
           
        # 6.1.1 Collision with fish 
        if ((p_a[x] < b_a[x] < p_b[x]) and (p_b[y] < b_a[y] < p_d[y])
            or 
            (p_c[x] < b_c[x] < p_d[x]) and (p_b[y] < b_c[y] < p_d[y])):
            penguin = False                                  
            the_end ()
            
            
     #If penguin collide with orca             
    for i, orca in enumerate(o_list): 
        p_a = [penguin_pos[x],penguin_pos[y]]
        p_b = [penguin_pos[x] + p_size[x],penguin_pos[y]]
        p_c = [penguin_pos[x],penguin_pos[y]+p_size[y]]
        p_d = [penguin_pos[x] + p_size[x],penguin_pos[y]+p_size[y]]
        
        o_a = [orca[x],orca[y]]
        o_c = [orca[x],orca[y]+o_size[y]]
       
           
        # 6.1.1 Collision with fish 
        if ((p_a[x] < o_a[x] < p_b[x]) and (p_b[y] < o_a[y] < p_d[y])
            or 
            (p_c[x] < o_c[x] < p_d[x]) and (p_b[y] < o_c[y] < p_d[y])):
            penguin = False
            the_end ()
    
        
    # Process each fish in the list
    for i in range(len(fish_list)):
 
        # Draw the fish 
        window.blit(fishy, fish_list[i])
 
 
        # If the fish has moved off the bottom of the screen
        if fish_list[i][0] < -100:
            # Reset it just above the top
            y1 = random.randrange(0, 650)
            fish_list[i][1] = y1
            # Give it a new x position
            x1 = random.randrange(1000, 1400)
            fish_list[i][0] = x1   
            
        if penguin: 
            # speed of the fish
            fish_list[i][0] -= 3
            
            
        
    # Process each blowfish in the list
    for i in range(len(bf_list)):
 
        # Draw the fish 
        window.blit(blowfishy, bf_list[i])

 
        # If the fish has moved off the bottom of the screen
        if bf_list[i][0] < -100:
            # Reset it just above the top
            y2 = random.randrange(0, 650)
            bf_list[i][1] = y2
            # Give it a new x position
            x2 = random.randrange(1000, 1400)
            bf_list[i][0] = x2   
            
        if penguin: 
            # speed of the fish
            bf_list[i][0] -= 4
            
    # Process each orca in the list
    for i in range(len(o_list)):
 
        # Draw the fish
        window.blit(orcy, o_list[i])
# 
#        # speed of the fish
#        o_list[i][0] -= 4
 
        # If the fish has moved off the bottom of the screen
        if o_list[i][0] < -700:
            # Reset it just above the top
            y3 = random.randrange(0, 650)
            o_list[i][1] = y3
            # Give it a new x position
            x3 = random.randrange(1200, 1400)
            bf_list[i][0] = x3 
             
      
    # If you win
    if 500 <= score:
        
        for i in range(len(fish_list)):
            # speed of the fish
            fish_list[i][0] -= 0    
            
        for i in range(len(bf_list)):
            # speed of the fish
            bf_list[i][0] -= 0
            
        penguin = False
        
        window.blit(winner, [0, 0])
        
        window.blit(win_peng, [200, 200])
        
        font = pygame.font.SysFont('helveticaneuedeskinterface', 100)   # font from list above  
        white = (255, 255, 255)
        text = font.render("You won", True, white)
        window.blit(text, (400, 325))
        
        font = pygame.font.SysFont('helveticaneuedeskinterface', 70)   # font from list above  
        white = (255, 255, 255)
        text = font.render("I'm proud of you!", True, white)
        window.blit(text, (400, 500))
        
        
#    # 5. Draw true penguin and score
    if penguin:       
         window.blit(penguin, penguin_pos)
    
    # Print the score
    font = pygame.font.SysFont('helveticaneuedeskinterface', 50)   # font from list above  
    white = (255, 255, 255)
    text = font.render(str(score), True, white)
    window.blit(text, (220, 30))
    
    font = pygame.font.SysFont('helveticaneuedeskinterface', 50)   # font from list above  
    white = (255, 255, 255)
    text = font.render("Score:", True, white)
    window.blit(text, (100, 30))


    # 6. Update display
    pygame.display.update()
        
    # 7. Frame rate  (60 or 30???)
    clock = pygame.time.Clock().tick(60)
