#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:46:37 2018

@author: ikechan
"""

import pygame
import sys
import random

from pygame.math import Vector2

x = 0
y = 1

"""
-------------------------------------------------------------------------------
0. Functions Definition
-------------------------------------------------------------------------------
"""
# Hit test between Point and Rectangle
def hitTestRec(point, rec):
    x = 0
    y = 1
    rx = rec.left
    ry = rec.top
    w = rec.width
    h = rec.height
    
    return rx < point[x] < rx + w and ry < point[y] < ry + h
        

# Get (distance**2) between two points
def distanceSquared(pos1, pos2):
    return (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2

# HitTest between Point and Circle
def hitTest(pos1, pos2, radius):
    x = 0
    y = 1
    return (pos1[x] - pos2[x])**2 + (pos1[y] - pos2[y])**2 < radius**2

# The point is hitting the current portal?
def hitCurrentPortal(pos):
    global portalPos, currentPortalId, portalRadius
    
    return  hitTest(portalPos[currentPortalId], pos, portalRadius)
    
# The point is hitting the id's portal?
def hitPortal(pos, id):
    global portalPos, portalRadius
    
    return hitTest(portalPos[id], pos, portalRadius)
    
# The point is hitting any portal?
def hitAnyPortal(pos):
    global portalRadius, portalPos   
    for pPos in portalPos:
        if hitTest(pos, pPos, portalRadius):
            return True   
    return False

# Player move to the point
def moveTo(pos):
    global playerPos
    playerPos = pos;
    
# Player move to the id portal
def moveToPortal(id):
    global playerPos, portalPos
    
    moveTo(portalPos[id])

# Player move along the vec
# id: The id of the objective portal
# if arrive the objective portal, return True
def moveToPortalByStep(id, vec):
    global playerPos, portalPos
    x = 0
    y = 1
    
    if distanceSquared(playerPos, portalPos[id]) > vec.length()**2:
    
        playerPos = (playerPos[x] + vec[x], playerPos[y] + vec[y])
        return False
    
    else:
        playerPos = portalPos[id]
        return True

# Get id of the portal that contains pos point
# If no portal contains pos point, return -1
def getPortalId(pos):
    global portalRadius, portalPos
    
    for id, pPos in enumerate(portalPos):
        if hitTest(pPos, pos, portalRadius):
            return id
    
    return -1

"""
-------------------------------------------------------------------------------
1. Read score file
-------------------------------------------------------------------------------
"""
    
# read the score file
with open("score/score.txt","r") as scoreFile:
    scores = scoreFile.read().split("\n")


"""
-------------------------------------------------------------------------------
2. Init pygame
-------------------------------------------------------------------------------
"""

pygame.init()


"""
-------------------------------------------------------------------------------
3. Variables
-------------------------------------------------------------------------------
"""
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)
gray = (230,230,230)
snow = (255, 250, 250)


win_size = [1200, 800]
window = pygame.display.set_mode((win_size[x], win_size[y]))


"""
-------------------------------------------------------------------------------
4. Sprite Set Up
-------------------------------------------------------------------------------
"""
# Player
player = pygame.image.load("image/player.png")
player_l = player
player_r = pygame.transform.flip(player, True, False)

playerSize = pygame.Rect(player.get_rect()).size
playerPos = [0,0]
velVec = Vector2(0,0) # moving direction
velocity = 5 # moving speed
alive = False

# Beans(bullets)
bean = pygame.image.load("image/bean.png")
beanSize = pygame.Rect(bean.get_rect()).size
beanPos = []
beanVel = []
beanVelocity = 10

# Enemies
enemy = pygame.image.load("image/enemy.png")
enemySize = pygame.Rect(player.get_rect()).size
enemyPos = [] # Center point of the rectangle
enemyVel = []
minVel = 1
maxVel = 5
frequency = 10 # frequency of enemy appearance

# EnemyB (color blue)
# chase after player
enemyB = pygame.image.load("image/enemy2.png")
enemyBSize = pygame.Rect(player.get_rect()).size
enemyBPos = [1000,700] # Center of the rectangle
enemyBVel = [0,0]


# Portals
portalPos = [[60,60], [700,60], [400,300], [500,500], [200, 750],[1000, 700], [1100,600], [600,400],[800,400]]
portalRadius = 30
portalColor = (211,211,211)
portalColor_selected = (255, 182, 193)

# PLayer and Portal
currentPortalId = random.randrange(0,len(portalPos)) # the portal on which player is
onTransition = False # player is moving now?
readyMove = False # Is cursor selecting next portal?


# Parameters and UI
score = 0
hitCounter = 0
level = 1
mp = 0
special = False

# UI
font = pygame.font.SysFont('helveticaneuedeskinterface', 30)
button = pygame.Rect(win_size[x]/2 - 50, win_size[y]*0.4 - 25, 100, 50)
label = font.render("START", True, black)
buttonColor = gray
endLabel = font.render("RETURN", True, black)


while True:    
    """
    -------------------------------------------------------------------------------
    5. quit game
    -------------------------------------------------------------------------------
    """
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()    
    
    
    """
    -------------------------------------------------------------------------------
    6. Start new game
    -------------------------------------------------------------------------------
    """
    if not alive:
        """
        6-1. initial set up of variables
        """
        playerPos = [0,0]
        velVec = Vector2(0,0)
        velocity = 5
        alive = True
        
        beanPos = []
        beanVel = []
        beanVelocity = 10
        
        enemyPos = []
        enemyVel = []
        minVel = 1
        maxVel = 5
        frequency = 10
        
        enemyBPos = [1000,700]
        enemyBVel = [0,0]
        
        currentPortalId = random.randrange(0,len(portalPos))
        onTransition = False
        readyMove = False

        score = 0
        hitCounter = 0
        level = 1
        mp = 0
        special = False

        moveToPortal(currentPortalId)

        """
        6-2. start menu  
        """
        while True:
            event = pygame.event.poll()
            mousePos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and hitTestRec(mousePos,button):
                break
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            window.fill(white)
            pygame.draw.rect(window, buttonColor, button)
            window.blit(label, (win_size[x]/2 - label.get_width()/2, win_size[y]*0.4 - label.get_height()/2))
            
            
            
            scoreLabel = font.render("-SCORE RANKING-",True,black)
            window.blit(scoreLabel, (win_size[x]/2 - scoreLabel.get_width()/2, win_size[y]/2 - scoreLabel.get_height()/2))
            for i, s in enumerate(scores):
                scoreLabel = font.render(s,True,black)
                window.blit(scoreLabel, (win_size[x]/2 - scoreLabel.get_width()/2, win_size[y]/2 - scoreLabel.get_height()/2 + (scoreLabel.get_height()+10)*(i+1)))
            
            
            pygame.display.update()
            clock = pygame.time.Clock().tick(60)


    """
    -------------------------------------------------------------------------------
    7. Delete Sprite out of Window
    -------------------------------------------------------------------------------
    """
    ## enemy
    for id in range(len(enemyPos)):
        if id >= len(enemyPos):
            break
        
        if (enemyPos[id][x] + enemySize[x] < 0 or win_size[x] < enemyPos[id][x] or
            enemyPos[id][y] + enemySize[y] < 0 or win_size[y] < enemyPos[id][y]):
               del enemyPos[id]
               del enemyVel[id]
               
    ## beans
    for id in range(len(beanPos)):
        if id >= len(beanPos):
            break

        if (beanPos[id][x] + beanSize[x] < 0 or win_size[x] < beanPos[id][x] or
            beanPos[id][y] + beanSize[y] < 0 or win_size[y] < beanPos[id][y]):
               del beanPos[id]
               del beanVel[id]   


    """
    -------------------------------------------------------------------------------
    8. Create New Enemy
    -------------------------------------------------------------------------------
    """
    
    """
    8-1. enemy speed up
    """
    # speed up by 5 points
    if hitCounter >= 5:
        maxVel += 1
        level += 1
        hitCounter = 0

    """
    8-2. create new enemy
    """
    # create new enemy randomly
    if random.randrange(0, frequency) == 0:
    
        # from which side, the enemy appear
        side = random.randrange(0,4)
        
        # decide initial location of new enemy
        if side == 0:
            xPos = random.randrange(-enemySize[x], win_size[x] + enemySize[x])
            yPos = -enemySize[y]
            
            
        elif side == 1:
            xPos = win_size[x] + enemySize[x]
            yPos = random.randrange(-enemySize[y], win_size[y] + enemySize[y])
        
        elif side == 2:
            xPos = random.randrange(-enemySize[x], win_size[x] + enemySize[x])
            yPos = win_size[y] + enemySize[y]
            
        else:
            xPos = -enemySize[x]
            yPos = random.randrange(-enemySize[y], win_size[y] + enemySize[y])
        
        # decide the direction of new enemy
        vel = Vector2(random.randrange(1,win_size[x]), random.randrange(1,win_size[y])).normalize()
        
        # register new enemy
        enemyPos.append([xPos, yPos])
        enemyVel.append([vel[x] * random.randrange(minVel, maxVel),vel[y] * random.randrange(minVel, maxVel)])
        

    """
    -------------------------------------------------------------------------------
    9. Special Time
    -------------------------------------------------------------------------------
    """
    # if mp > 100 and press SPACE, enter into "special time"
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE] and mp > 100:
        special = True

    # if mp == 0, then stop "special time"
    if mp <= 0:
        special = False
    
    
    """
    -------------------------------------------------------------------------------
    10. Emit beans
    -------------------------------------------------------------------------------
    """
    # Emit beans
    mousePress = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    
    ## normal time
    if event.type == pygame.MOUSEBUTTONUP and not readyMove and not special:
        beanPos.append([playerPos[x], playerPos[y]])
        beanVel.append(Vector2(mousePos[x] - playerPos[x], mousePos[y] - playerPos[y]).normalize() * beanVelocity)
    
    ## special time (during special time, need not to click)
    elif special and not readyMove:
        beanPos.append([playerPos[x], playerPos[y]])
        beanVel.append(Vector2(mousePos[x] - playerPos[x], mousePos[y] - playerPos[y]).normalize() * beanVelocity)
        mp -= 1

    
    """
    -------------------------------------------------------------------------------
    11. Update Position
    -------------------------------------------------------------------------------
    """
    
    """
    11-1. Player Movement
    """
    
    if onTransition:
        # if player is on transition, NOT accept user input
        # Player move little by little
        end = moveToPortalByStep(currentPortalId, velVec)
        
        if end:
            onTransition = False;
            mp += 10
    else:
    # accept user input only when player not moving  
        if mousePress[0] or mousePress[1] or mousePress[2]: 
     
            # if click currentPortal, start ready to move
            if hitCurrentPortal(mousePos):
                readyMove = True
    
        elif readyMove:
            readyMove = False
            
            id = getPortalId(mousePos)
            # If mouse was released on any portal except current one
            if 0 <= id and id != currentPortalId:
                #update currentPortalId veriable
                currentPortalId = id
                
                # Start transition
                onTransition = True
                
                # Calculate velocity vector
                velVec = Vector2(portalPos[id][x] - playerPos[x], portalPos[id][y] - playerPos[y]).normalize()
                velVec *= velocity
    
    """
    11-2. Update Position of other sprites
    """
    # Update position
    for (pos, vel) in zip(enemyPos, enemyVel):
        pos[x] += vel[x]
        pos[y] += vel[y]
                                 
    for (pos, vel) in zip(beanPos, beanVel):
         pos[x] += vel[x]
         pos[y] += vel[y]
    
    if playerPos[x] - enemyBPos[x] == 0 and playerPos[y] - enemyBPos[y] == 0:
        enemyBPos[x] += 1
        
    enemyBVel = Vector2(playerPos[x] - enemyBPos[x], playerPos[y] - enemyBPos[y]).normalize()
    enemyBPos[x] += enemyBVel[x] * (minVel + maxVel)/2
    enemyBPos[y] += enemyBVel[y] * (minVel + maxVel)/2
    
     
    """
    -------------------------------------------------------------------------------
    12. HitTest
    -------------------------------------------------------------------------------
    """
    # HitTest
    for eId, ePos in enumerate(enemyPos):
        if eId >= len(enemyPos):
            break
        
        #Hit with enemy and player
        if ((ePos[x] - enemySize[x]/2 < playerPos[x] - playerSize[x]/2 < ePos[x] + enemySize[x]/2 or 
             ePos[x] - enemySize[x]/2 < playerPos[x] + playerSize[x]/2 < ePos[x] + enemySize[x]/2) and
            (ePos[y] - enemySize[y]/2 < playerPos[y] - playerSize[y]/2 < ePos[y] + enemySize[y]/2 or
             ePos[y] - enemySize[y]/2 < playerPos[y] + playerSize[y]/2 < ePos[y] + enemySize[y]/2)):
           alive = False
        
        #Hit with enemy and beans
        for bId, bPos in enumerate(beanPos):
            if bId >= len(beanPos):
                break
            
            if ((ePos[x] - enemySize[x]/2 < bPos[x] - beanSize[x]/2 < ePos[x] + enemySize[x]/2 or 
                ePos[x] - enemySize[x]/2 < bPos[x] + beanSize[x]/2 < ePos[x] + enemySize[x]/2) and
               (ePos[y] - enemySize[y]/2 < bPos[y] - beanSize[y]/2 < ePos[y] + enemySize[y]/2 or
                ePos[y] - enemySize[y]/2 < bPos[y] + beanSize[y]/2 < ePos[y] + enemySize[y]/2)):  
                if eId >= len(enemyPos):
                    break
    
                del beanPos[bId]
                del beanVel[bId]
                del enemyPos[eId]
                del enemyVel[eId]
                score += 10 + level
                hitCounter += 1
                
                mp += 1
    
    # Hit with enemy2 and player
    if ((enemyBPos[x] - enemyBSize[x]/2 < playerPos[x] - playerSize[x]/2 < enemyBPos[x] + enemyBSize[x]/2 or 
         enemyBPos[x] - enemyBSize[x]/2 < playerPos[x] + playerSize[x]/2 < enemyBPos[x] + enemyBSize[x]/2) and
        (enemyBPos[y] - enemyBSize[y]/2 < playerPos[y] - playerSize[y]/2 < enemyBPos[y] + enemyBSize[y]/2 or
         enemyBPos[y] - enemyBSize[y]/2 < playerPos[y] + playerSize[y]/2 < enemyBPos[y] + enemyBSize[y]/2)):
        alive = False
    
    # Hit with enemy2 and beans
    for bId, bPos in enumerate(beanPos):
        
        if ((enemyBPos[x] - enemyBSize[x]/2 < bPos[x] - beanSize[x]/2 < enemyBPos[x] + enemyBSize[x]/2 or 
             enemyBPos[x] - enemyBSize[x]/2 < bPos[x] + beanSize[x]/2 < enemyBPos[x] + enemyBSize[x]/2) and
            (enemyBPos[y] - enemyBSize[y]/2 < bPos[y] - beanSize[y]/2 < enemyBPos[y] + enemyBSize[y]/2 or
             enemyBPos[y] - enemyBSize[y]/2 < bPos[y] + beanSize[y]/2 < enemyBPos[y] + enemyBSize[y]/2)):  
  
            del beanPos[bId]
            del beanVel[bId]
            
            mp += 5

            # Reset enemy2 position
            side = random.randrange(0,4)        
            if side == 0:
                xPos = random.randrange(-enemySize[x], win_size[x] + enemySize[x])
                yPos = -enemySize[y]
            
            
            elif side == 1:
                xPos = win_size[x] + enemySize[x]
                yPos = random.randrange(-enemySize[y], win_size[y] + enemySize[y])
                
            elif side == 2:
                xPos = random.randrange(-enemySize[x], win_size[x] + enemySize[x])
                yPos = win_size[y] + enemySize[y]
            
            else:
                xPos = -enemySize[x]
                yPos = random.randrange(-enemySize[y], win_size[y] + enemySize[y])
            enemyBPos = [xPos, yPos]
            
            score += (10 + level) * 5
            hitCounter += 1  

    """
    -------------------------------------------------------------------------------
    13. Draw Sprites
    -------------------------------------------------------------------------------
    """
    ## window
    window.fill(white)
    
    ## portal
    for id, pos in enumerate(portalPos):
        if readyMove and hitPortal(mousePos, id) and id != currentPortalId:
            pygame.draw.circle(window, portalColor_selected, (pos[x], pos[y]), portalRadius)
        else:
            pygame.draw.circle(window, portalColor, (pos[x], pos[y]), portalRadius)
        
    ## enemy
    for pos in enemyPos:
        #pygame.draw.rect(window, black, pygame.Rect(int(pos[x]- enemySize[x]/2), int(pos[y]- enemySize[y]/2), enemySize[x], enemySize[y]))
        window.blit(enemy, (pos[x] - enemySize[x]/2, pos[y] - enemySize[y]/2))
    
    ## enemyB
    window.blit(enemyB, (enemyBPos[x] - enemyBSize[x]/2, enemyBPos[y] - enemyBSize[y]/2))
    
    ## bean
    for pos in beanPos:
        window.blit(bean, (pos[x] - beanSize[x]/2, pos[y] - beanSize[y]/2))
        
        
    ## line between player and cursor
    if readyMove:
        pygame.draw.aaline(window, black, portalPos[currentPortalId], mousePos)
    
    if onTransition:
        pygame.draw.aaline(window, black, playerPos, portalPos[currentPortalId])

    ## player
    if alive:
        if mousePos[x] < playerPos[x]:
            window.blit(player_l, (playerPos[x] - playerSize[x]/2, playerPos[y] - playerSize[y]/2))
        else:
            window.blit(player_r, (playerPos[x] - playerSize[x]/2, playerPos[y] - playerSize[y]/2))
        
    # UI
    text = font.render("MP: "+ str(mp) + " Level: " + str(level) + " SCORE: " + str(score), True, black)
    window.blit(text, (win_size[x] - text.get_width(), win_size[y] - text.get_height()))
       
    
    """
    -------------------------------------------------------------------------------
    14. result menu
    -------------------------------------------------------------------------------
    """
    # result menu
    if not alive:  
        # update ranking
        for i in range(len(scores)):
            if i == 0 and score >= int(scores[0]) or i != 0 and int(scores[i-1]) > score >= int(scores[i]):
                scores.insert(i,str(score))
                scores.pop()
                break
       
        scoreText = "\n".join(scores)
        with open("score/score.txt", "w") as scoreFile:
            scoreFile.write(scoreText)   
        
        # result
        while True:
            event = pygame.event.poll()
            mousePos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and hitTestRec(mousePos, button):
                break
            
            message = font.render("Gameover...", True, black)
            window.blit(message, ((win_size[x] - message.get_width())/2, (win_size[y] - message.get_height())/2 - 5))
            
            scoreLabel = font.render("SCORE: " + str(score), True, black)
            window.blit(scoreLabel, (win_size[x]/2 - scoreLabel.get_width()/2, win_size[y]/2 - scoreLabel.get_height()/2 + message.get_height() + 5))

            pygame.draw.rect(window, buttonColor, button)
            window.blit(endLabel, (win_size[x]/2 - label.get_width()/2, win_size[y]*0.4 - label.get_height()/2))
    
            pygame.display.update()
            clock = pygame.time.Clock().tick(60)
            
            
    """
    -------------------------------------------------------------------------------
    15. update display
    -------------------------------------------------------------------------------
    """
    pygame.display.update()
    
   
    """
    -------------------------------------------------------------------------------
    16. Frame rate
    -------------------------------------------------------------------------------
    """
    clock = pygame.time.Clock().tick(60)    
            
            
            
            
            
            