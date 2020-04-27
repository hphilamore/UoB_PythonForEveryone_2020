"""
Created on Tue May  8 09:02:36 2018

@author: hemma

A template with the basic Pygame setup :
0. Import libraries
1. Initailise the pg library
2. Variables
3. Launch a game window
4. Set up the main game loop
5. Event Processing
6. Calculations 
7. Draw 
8. Update display once per loop
9. Set frame rate

"""

# 0. Import libraries
import pygame as pg 
import sys
from pygame.draw import rect, polygon

# 1. Initailise the pg library
pg.init()


# FUNCTION DEFINITIONS
def tree():
    "Draws a tree"
    rect(window, black, [160, 300, 30, 45])
    polygon(window, green, [[250, 300], [175, 150], [100, 300]])
    polygon(window, green, [[240, 250], [175, 130], [110, 250]])
    

# 2. Variables
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# 3. Launch a game window
window = pg.display.set_mode((600, 400))


# 4. Set up the main game loop
while True:
    
    # 5. Event Processing
    event = pg.event.poll()
    if event.type == pg.QUIT:        
        pg.quit()
        sys.exit()  
#    elif event.type == pg.MOUSEBUTTONDOWN:
#        print("User pressed a mouse button")
        
    # 6. Calculations
        
    # 7. Draw 
    window.fill(blue)
#    rect(window, black, [160, 300, 30, 45])
#    polygon(window, green, [[250, 300], [175, 150], [100, 300]])
#    polygon(window, green, [[240, 250], [175, 130], [110, 250]])
    tree()
    

    # 8. Update display
    pg.display.update()
    
    # 9. Frame rate
    clock = pg.time.Clock().tick(60)