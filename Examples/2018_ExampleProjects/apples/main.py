#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:02:36 2018

@author: hemma
"""
# 0. Import libraries
import pygame 
import sys
#sys.path.append('../')
import random

#variables
x = 0
y = 1
   
# 1. Initailise the pygame library
pygame.init()

# 2. Variables
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

win_size = [650, 600]
window = pygame.display.set_mode((650, 600))

monster = True

flag1 = False
flag2 = False
#score
HP = 3
score = 0
font = pygame.font.Font(None, 60)
font2 = pygame.font.Font(None, 42)
font3 = pygame.font.Font(None, 120)
font4 = pygame.font.Font(None, 38)
#place
placelist = [80, 250, 420]
#Monsters
monster_pos = [random.choice(placelist), 0]
monster_vel = [0,6]
monster1_pos = [random.choice(placelist), 0]
monster1_vel = [0,6]
monster2_pos = [random.choice(placelist), 0]
monster2_vel = [0,6]  
monster = pygame.image.load("img/mushi_tentoumushi2.png")
state0 = 2 #1:apple 2:monster
m_size = pygame.Rect(monster.get_rect()).size
monster.set_colorkey(white)
print('m_size=', m_size)
#background
background = pygame.image.load("img/background.big.jpg").convert()
b_size = pygame.Rect(background.get_rect()).size
print('win_size=', win_size)
#gorilla
gorilla = True
gorilla_pos = [170, 390]
gorilla = pygame.image.load("img/gorilla2.png")
g_size = pygame.Rect(gorilla.get_rect()).size
gorilla.set_colorkey(white)
print('g_size=', g_size)
#start
start1 = True
start2 = False
#game
game = False
#end
end1 = False
end2 = False
#background2
background2 = pygame.image.load("img/bg_hospital3.jpg").convert()
b2_size = pygame.Rect(background2.get_rect()).size
#ambulance
ambulance = pygame.image.load("img/tsuuhou_119_kyukyu2.png")
a_size = pygame.Rect(monster.get_rect()).size
ambulance.set_colorkey(white)
print('a.size', a_size)
a_pos = [700, 400]
a_ver = [-10, 0]
#background3
background3 = pygame.image.load("img/bg_sougen2.jpg").convert()
b3_size = pygame.Rect(background3.get_rect()).size
#background4
background4 = pygame.image.load("img/bg_yamamichi.jpg").convert()
b3_size = pygame.Rect(background4.get_rect()).size
#background5
background5 = pygame.image.load("img/ohanabatake.jpg").convert()
b3_size = pygame.Rect(background5.get_rect()).size
#gorilla2
g2_pos = [700, 400]
g2_ver = [-9, 3]
gorilla2 = pygame.image.load("img/gorilla3.png")
g2_size = pygame.Rect(gorilla2.get_rect()).size
gorilla2.set_colorkey(white)
print('g2_size', g2_size)
#kanban
k_pos = [70, 320]
kanban = pygame.image.load("img/kanban2.png")
k_size = pygame.Rect(kanban.get_rect()).size
kanban.set_colorkey(white)
print('k_size', k_size)
#animals
a2_pos =[30, 180]
animals = pygame.image.load("img/animals2.png")
a_size = pygame.Rect(animals.get_rect()).size
animals.set_colorkey(white)
print('a_size', a_size)
#tree_animals
ta_pos =[80, 75]
tree_animals = pygame.image.load("img/tree_animals.png")
ta_size = pygame.Rect(tree_animals.get_rect()).size
tree_animals.set_colorkey(white)
print('ta_size', ta_size)
#con
c_pos =[130, 0]
con = pygame.image.load("img/con.png")
c_size = pygame.Rect(con.get_rect()).size
con.set_colorkey(white)
print('c_size', c_size)
#fukidashi
f_pos = [10,40]
fukidashi =pygame.image.load("img/fukidashi.png")
f_size = pygame.Rect(fukidashi.get_rect()).size
fukidashi.set_colorkey(white)
print('f_size', f_size)
#heart
heart =pygame.image.load("img/heart.png")
h_size = pygame.Rect(heart.get_rect()).size
heart.set_colorkey(white)
print('h_size', h_size)
#definitions
def update_monster_vel():
    monster_vel[y] = 6+(score*0.2)
    monster1_vel[y] = 6+(score*0.2)
    monster2_vel[y] = 6+(score*0.2)   
    
def collision(c):
    global score
    global HP
    if (gorilla_pos[0] == c) & (monster_pos[0] == c+80) & (307 <= monster_pos[1] <= 331):
        monster_pos[x] = 1000
        if state0 == 1:
            score += 1
        else:
            score -= 1
            HP -= 1

    if (gorilla_pos[0] == c) & (monster1_pos[0] == c+80) & (307 <= monster1_pos[1] <= 331):
        monster1_pos[x] = 1000
        if state1 == 1:
            score += 1
        else:
            score -= 1
            HP -= 1

    if (gorilla_pos[0] == c) & (monster2_pos[0] == c+80) & (307 <= monster2_pos[1] <= 331):
        monster2_pos[x] = 1000
        if state2 == 1:
            score += 1
        else:
            score -= 1
            HP -= 1 

while start1:
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit() 

    g2_pos[x] += g2_ver[x]
    g2_pos[y] += g2_ver[y]
    g2_ver[y] *= -1
    window.blit(background3, [0, 0])
    window.blit(gorilla2, g2_pos)
    window.blit(kanban, k_pos)
    text3 = font.render("created by ", True, (0, 0, 0))
    window.blit(text3,[105, 390])
    text4 = font2.render("Shunsuke Nagano ", True, (0, 0, 0))
    window.blit(text4,[115, 450])    
    if g2_pos[x] < -200:
        break
# 6. Update display
    pygame.display.update()
    
# 7. Frame rate
    clock = pygame.time.Clock().tick(20)
start2 = True
while start2:
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN]:
        break
    
    window.blit(background4, [0, 0])
    window.blit(gorilla, [300, 100])
    window.blit(animals, a2_pos)
    text6 = font3.render("Catch Apples", True, (255, 0, 0))
    window.blit(text6,[53, 485])
    text5 = font3.render("Catch Apples", True, (255, 255, 255))
    window.blit(text5,[51, 487])  
    window.blit(fukidashi, f_pos)
    text7 = font4.render("Are you ready?", True, (0, 0, 0))
    text8 = font4.render("Please click ENTER!", True, (0, 0, 0))
    window.blit(text7, [45, 130])
    window.blit(text8, [45, 170])
# 6. Update display
    pygame.display.update()
    
# 7. Frame rate
    clock = pygame.time.Clock().tick(20)
        
game = True    
while game:
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit() 
#player movement

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        if gorilla_pos[0] == 170:
            gorilla_pos[0] = 340
        if gorilla_pos[0] == 0:
            gorilla_pos[0] =170
            
    if pressed[pygame.K_LEFT]:
        if gorilla_pos[0] == 170:
            gorilla_pos[0] = 0
        if gorilla_pos[0] == 340:
            gorilla_pos[0] =170

#monsters movement        
    if monster_pos[y] > 200:
        if flag1 == False:
            monster1 = True
            if random.uniform(0,1) > 0.5 :
                monster1 = pygame.image.load("img/mushi_tentoumushi2.png")
                state1 = 2
            else:
                monster1 = pygame.image.load("img/fruit_apple2.png")
                state1 = 1
            m_size = pygame.Rect(monster1.get_rect()).size
            monster1.set_colorkey(white)
            print('m_size=', m_size)
            flag1 = True

    if monster_pos[y] > 400:
        if flag2 == False:
            monster2 = True
            if random.uniform(0,1) > 0.5 :
                monster2 = pygame.image.load("img/mushi_tentoumushi2.png")
                state2 = 2
            else:
                monster2 = pygame.image.load("img/fruit_apple2.png")
                state2 = 1
            m_size = pygame.Rect(monster2.get_rect()).size
            monster2.set_colorkey(white)
            print('m_size=', m_size)
            flag2 = True        
        
    # 4.2.2 Update position
    monster_pos[x] += monster_vel[x]
    monster_pos[y] += monster_vel[y]
    
    if monster_pos[y] > 600:
        monster_pos = [random.choice(placelist), 0]
        if random.uniform(0,1) > 0.5 :
            monster = pygame.image.load("img/mushi_tentoumushi2.png")
            state0 = 2
        else:
            monster = pygame.image.load("img/fruit_apple2.png")
            state0 = 1
            
    if monster1_pos[y] > 600:
        monster1_pos = [random.choice(placelist), 0]
        if random.uniform(0,1) > 0.5 :
            monster1 = pygame.image.load("img/mushi_tentoumushi2.png")
            state1 = 2
        else:
            monster1 = pygame.image.load("img/fruit_apple2.png")
            state1 = 1
    
    if flag1 :
        monster1_pos[x] += monster1_vel[x]
        monster1_pos[y] += monster1_vel[y]
        
    if monster2_pos[y] > 600:
        monster2_pos = [random.choice(placelist), 0]
        if random.uniform(0,1) > 0.5 :
            monster2 = pygame.image.load("img/mushi_tentoumushi2.png")
            state2 = 2
        else:
            monster2 = pygame.image.load("img/fruit_apple2.png")
            state2 = 1
    
    if flag2 :
        monster2_pos[x] += monster2_vel[x]
        monster2_pos[y] += monster2_vel[y]        

#collision
 #left_collision
    collision(0)

 #center_collision
    collision(170)

 #right_collision
    collision(340)

    if HP == 0:
        end1 = True
        break

    if score == 100:
        end2 = True
        break
    
#spped up
    update_monster_vel()
#image    
    window.blit(background, [0, 0])  
    if gorilla:
        window.blit(gorilla, gorilla_pos)
    if monster:
        window.blit(monster, monster_pos)
    if flag1 :
        if monster1:
            window.blit(monster1, monster1_pos)
    if flag2 :
        if monster2:
            window.blit(monster2, monster2_pos)
     
    text1 = font.render("SCORE:"+str(score), True, (255, 255, 255))
    window.blit(text1, [50, 50])

    if HP >= 1:
        window.blit(heart, [490, 0])
    if HP >= 2:
        window.blit(heart, [540, 0])
    if HP == 3:
        window.blit(heart, [590, 0])
# 6. Update display
    pygame.display.update()
    
# 7. Frame rate
    clock = pygame.time.Clock().tick(20)

while end2:
   
    event = pygame.event.poll()

    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()    

    window.blit(background5, [0, 0])
    window.blit(tree_animals, ta_pos)
    window.blit(con, c_pos)
# 6. Update display
    pygame.display.update()
    
# 7. Frame rate
    clock = pygame.time.Clock().tick(20)
    
while end1:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit() 

    window.blit(background2, [0, 0])
    text2_ = font.render("GAME OVER! Your score is "+str(score), True, (0, 0, 0))
    text2 = font.render("GAME OVER! Your score is "+str(score), True, (255, 0, 0))
    window.blit(text2_,[31, 201])
    window.blit(text2,[30, 200])
    window.blit(ambulance, a_pos)
    a_pos[x] += a_ver[x]    
# 6. Update display
    pygame.display.update()
    
# 7. Frame rate
    clock = pygame.time.Clock().tick(20)