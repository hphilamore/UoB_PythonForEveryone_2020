# 0. Import libraries
import pygame 
import sys
import pygame.mixer as mix
import text_library as text
import katamari_window

# 1. Initailise the pygame library
pygame.init()
mix.init()

# 2. Variables
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)
purple = (120, 0, 120)

# 2.1 Play and Quit Text Positions
play_pos = [(85,235), (500,560)]
quit_pos = [(560,695), (500,560)]

# 2.2 Background image, sound effects and music
startbackground = pygame.image.load("background_images/startbackground.jpg")

click = mix.Sound("sound_effects/zap2.ogg")
click.set_volume(0.3)

#mix.music.load("background_music/MainTheme.wav")
#mix.music.play(-1, 0.0)
#mix.music.set_volume(0.4)

# 3. Launch a game window
window = pygame.display.set_mode((800, 600))

# 4. Set up the main game loop
while True:
    # 5. Event Processing
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:    
        mix.music.stop()
        pygame.quit()
        sys.exit()  
    
    # 5.1 Check if any mouse buttons have been pressed
    mouse_press = pygame.mouse.get_pressed()
    left_click = mouse_press[0]
    mid_click = mouse_press[1]
    right_click = mouse_press[2]

    # 5.2 Saving the postion of the mouse to variable 'mouse_position'
    mouse_position = pygame.mouse.get_pos()

    # 5.3 Check whether user clicks Play or Quit Texts on the window
    if left_click and not right_click:
        # If the user clicks 'Play' on the window the game begins
        if play_pos[0][0] <= mouse_position[0] <= play_pos[0][1] and \
        play_pos[1][0] <= mouse_position[1] <= play_pos[1][1]:
            click.play()
            # this will change to another window in katamari_window.py
            # where the game will proceed
            katamari_window.katamari()
        # if the user clicks 'Quit' on the window the game ends
        elif quit_pos[0][0] <= mouse_position[0] <= quit_pos[0][1] and \
        quit_pos[1][0] <= mouse_position[1] <= quit_pos[1][1]:
            pygame.quit()
            sys.exit()
    
    # 5. Draw
    window.blit(startbackground, [0, 0])
    text.game_title()       # print game title on window from text_library.py
    text.instructions()     # print instructions on window from text_library.py
    text.options()          # print options (Play or Quit) on window from text_library.py

    # 6. Update display
    pygame.display.update()
    
    # 7. Frame rate
    clock = pygame.time.Clock().tick(60)