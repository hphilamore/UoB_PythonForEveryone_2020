# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 11:50:28 2018

@author: TENDA YUDAI
"""

import pygame
import sys
import pygame.mixer as mix
import random

white = (255,255,255)
black = (0,0,0)

#initial state
x = ""
    
listX = []
listY = [] #1
listX_2 = []
listY_2 = [] #2 
listX_3 = []
listY_3 = [] #3

damage = 0
    
rain_vel = [0,8]
Min = 0
Max = 200 #1
Min2 = 250
Max2 = 400 #2
Min3 = 400
Max3 = 500 #3

# rain functions
#1 rain fall
def rainfall(a, listX, listY, rain_size):
    for n in range(a):
        pygame.draw.rect(window, black, (listX[n], listY[n], rain_size, 10))
        listY[n] += rain_vel[1]
#2 make new rain        
def listupdate(b, listX, listY, Min, Max):
    for i in range(b):
        x = random.randrange(Min,Max)
        listX.append(x) 
        y = 0
        listY.append(y)
#3 when rain hits the runner - rain_fade & count_damage         
def rain_fade(runnerX, runnerY, listX, listY, damage, point):
    for i in range(len(listY)):
        if (listY[i] >= runnerY) and (listY[i] <= 400) and (listX[i] >= runnerX+16) and (listX[i] <= runnerX+62):
            listY[i] = 400
            damage += point
    return damage
#4 rain_fall_zone changes
def rain_zone_change(Min, listX, zone_range):
    OldMin = Min
    Min = random.randrange(0,600)
    diff = Min - OldMin
        
    Max = Min + zone_range
    time_initial = pygame.time.get_ticks()
        
    for r in range(len(listX)):
        listX[r] += diff
    
    return Min, Max, time_initial, listX
                

pygame.init()

runner = pygame.image.load("img/python.runner.png")
r_size = pygame.Rect(runner.get_rect()).size
runner_pos = [200,320]

window = pygame.display.set_mode((600,400))
window.fill(white)

# time_management
time_game = 0
time_initial = pygame.time.get_ticks()
time_initial2 = pygame.time.get_ticks()

mix.init()
mix.music.load("sounds/Rain-Real_Ambi03-1.mp3")
musicPlay_flag = 0

while (time_game < 10000):
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
    image1 = pygame.image.load("img/1_1.png")
    image2 = pygame.image.load("img/1_2.png")
    image3 = pygame.image.load("img/1_3.png")
    rule = pygame.image.load("img/python_rule.png")
    
    window.fill((255,255,255))
    if time_game > 0 and time_game <= 2500:
        window.blit(image1, (0,0))
    if time_game > 2500 and time_game <= 5000:
        window.blit(image2, (0,0))
    if time_game > 5000 and time_game <= 7000: 
        window.blit(image3, (0,0))
    if time_game > 7000:
        window.blit(rule,(0,0))
        
    #countdown
    font = pygame.font.SysFont(None, 50)
    text = font.render(x, True, (0,0,0))
    if time_game == 9000:
        x = "1"
    if time_game == 8000:
        x = "2"
    if time_game == 7000:
        x = "3"
    window.blit(text, (100,200))
    
    time_now2 = pygame.time.get_ticks()
    time_game = time_now2 - time_initial2
    
    pygame.display.update()
    clock = pygame.time.Clock().tick(60)

while (time_game >= 10000 and time_game <= 30000):   
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

        
    #Decide rainy spot
    time_now = pygame.time.get_ticks()
        
    if time_now - time_initial >= 2000:
        Min, Max, time_initial, listX = rain_zone_change(Min, listX, 200)
        Min2, Max2, time_initial, listX_2 = rain_zone_change(Min2, listX_2, 150)
        Min3, Max3, time_initial, listX_3 = rain_zone_change(Min3, listX_3, 100)
        
    #Make first rain
    listupdate(5, listX, listY, Min, Max)
    listupdate(8, listX_2, listY_2, Min2, Max2)
    listupdate(5, listX_3, listY_3, Min3, Max3)
    
    window.fill(white)
    window.blit(runner,runner_pos)
    
    # rain
    if 0 in listY:
        num = listY.count(0)
        listupdate(num, listX, listY, Min, Max)
        rainfall(len(listX), listX, listY, 1)
        damage = rain_fade(runner_pos[0], runner_pos[1], listX, listY, damage, 1)
        
        num2 = listY_2.count(0)
        listupdate(num2, listX_2, listY_2, Min2, Max2)
        rainfall(len(listX_2), listX_2, listY_2, 1.5)
        damage = rain_fade(runner_pos[0], runner_pos[1], listX_2, listY_2, damage, 1.5)
        
        num3 = listY_3.count(0)
        listupdate(num3, listX_3, listY_3, Min3, Max3)
        rainfall(len(listX_3), listX_3, listY_3, 2)
        damage = rain_fade(runner_pos[0], runner_pos[1], listX_3, listY_3, damage, 2)
        
    # move the runner's posittion    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        runner_pos[0] += 5
    if pressed[pygame.K_LEFT]:
        runner_pos[0] -= 5
        
    if runner_pos[0] < -80:
        runner_pos[0] = 600
    if runner_pos[0] > 600:
        runner_pos[0] = -80
    
    #music_system
    if musicPlay_flag == 0:
        mix.music.play()
        volume = 0.5
        mix.music.set_volume(volume)
        musicPlay_flag = 1
    if musicPlay_flag == 1:
        if pressed[pygame.K_UP] and volume < 1:
            volume += 0.1
            mix.music.set_volume(volume)
        if pressed[pygame.K_DOWN] and volume > 0:
            volume -= 0.1
            mix.music.set_volume(volume)

        
    time_now2 = pygame.time.get_ticks()
    time_game = time_now2 - time_initial2
                    
    pygame.display.update()
    
    clock = pygame.time.Clock().tick(60)

# ending
while (time_game > 30000):
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    
    window.fill((255,255,0))
    mix.music.stop
    
    Hello = pygame.image.load("img/2.png")
    reac1 = pygame.image.load("img/3_1.png")
    reac2 = pygame.image.load("img/3_2.png")
    reac3 = pygame.image.load("img/3_3.png")
    rankA = pygame.image.load("img/7_A.png")
    rankB = pygame.image.load("img/7_B.png")
    rankC = pygame.image.load("img/7_C.png")
    
    if time_game <= 33000:
        window.blit(Hello,(0,0))
        
    if time_game > 33000 and time_game <= 35000:
        window.blit(reac1,(0,0))
        
    if time_game > 35000 and time_game <= 38000:
        if damage <= 1500:
            window.blit(reac3, (0,0))
        if damage > 1500 and damage <= 2500:
            window.blit(reac1, (0,0))
        if damage > 2500:
            window.blit(reac2, (0,0))
            
    if time_game > 38000:
        if damage <= 1500:
            window.blit(rankA, (0,0))
        if damage > 1500 and damage <= 2500:
            window.blit(rankB, (0,0))
        if damage > 2500:
            window.blit(rankC, (0,0))

        font = pygame.font.SysFont(None, 26)  
        text = font.render("Your damage is {0}.".format(damage), True, (0,0,0))
        window.blit(text, (100,200))

    
    time_now2 = pygame.time.get_ticks()
    time_game = time_now2 - time_initial2
    
    
    pygame.display.update()
    clock = pygame.time.Clock().tick(60)