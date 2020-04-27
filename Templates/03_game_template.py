# 0. Import libraries
import pygame as pg
import sys


# 1. Initailise the pygame library
pg.init()

# 2. Variables
black = (0,0,0)
white = (255, 255, 255)

# 3. Launch a game window
window = pg.display.set_mode((600, 400))

# 4. Set up the main game loop
while True:
    event = pg.event.poll()

    if event.type == pg.QUIT:        
        pg.quit()
        sys.exit()  
      
# 7. Draw
window.fill(blue)

# 8. Update display
pg.display.update()

# 9. Frame rate
clock = pg.time.Clock().tick(60)