def game_over(score):
    # 0. Import libraries
    import pygame 
    import sys
    import katamari_window
    import pygame.mixer as mix
    import text_library as text

    # 1. Initailise the pygame library
    pygame.init()
    mix.init()

    # 2. Variables
    # 2.1 Background image    
    gameover = pygame.image.load("background_images/over.jpg")
    
    # 2.2 Sound Effects
    click = mix.Sound("sound_effects/zap2.ogg")
    click.set_volume(0.3)
    
    # 2.3 Background Music
    # mix.music.load("background_music/FranticLevel.wav")
    # mix.music.play(-1, 0.0)
    # mix.music.set_volume(0.3)
            
    # 2.4 Play and Quit positions
    play_pos = [(85,400), (500,560)]
    quit_pos = [(560,695),(500,560)]
    
    # 3. Launch a game window
    window = pygame.display.set_mode((800, 600))

    # 4. Set up the main game loop
    while True:
        # 5. Event Processing
        event = pygame.event.poll()
    
        if event.type == pygame.QUIT:        
            pygame.quit()
            sys.exit()  
        
        # 5.1 Check if any mouse buttons have been pressed
        mouse_press = pygame.mouse.get_pressed()
        left_click = mouse_press[0]
        right_click = mouse_press[2]
        
        # 5.2 Save mouse position to 'mouse_position'
        mouse_position = pygame.mouse.get_pos()

        # 5.3 Check whether user clicks Play or Quit Texts on the window
        if left_click and not right_click:
            # If the user clicks 'Play Again' on the window the game begins
            if play_pos[0][0] <= mouse_position[0] <= play_pos[0][1] and \
            play_pos[1][0] <= mouse_position[1] <= play_pos[1][1]:
                click.play()        # Sound effects will play
                mix.music.stop()    # Music will stop
                # this will go back to game window in katamari_window.py
                # where the game will proceed
                katamari_window.katamari()
            # if the user clicks 'Quit' on the window the game ends
            elif quit_pos[0][0] <= mouse_position[0] <= quit_pos[0][1] and \
            quit_pos[1][0] <= mouse_position[1] <= quit_pos[1][1]:
                mix.music.stop()
                pygame.quit()
                sys.exit()

        # 6. Draw
        window.blit(gameover, [0, 0])
        text.game_over()            # print 'Game Over' on the window from text_library.py
        text.game_score(score)      # print 'Score' w/ player's score on the window from text_library.py
        text.game_options()         # print options (Play or Quit) on window from text_library.py

        # 7. Update display
        pygame.display.update()
    
        # 8. Frame rate
        clock = pygame.time.Clock().tick(60)