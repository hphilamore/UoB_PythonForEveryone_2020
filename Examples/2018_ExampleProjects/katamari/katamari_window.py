def katamari():
    import pygame 
    import sys
    import random
    import pygame.mixer as mix
    import over_window
    import winner_window
    import text_library as text

    # 1. Initailise the pygame library
    pygame.init()
    mix.init()

    # 2. Variables
    x = 0
    y = 1

    # 2.1 colours 
    black = (0,0,0)
    white = (255, 255, 255)
    red =   (255, 0, 0)
    green = (0, 255, 0)
    blue =  (0, 0, 255)
    purple = (120, 0, 120)
    
    # 2.2 Sound Effects
    swallow = mix.Sound("sound_effects/zap5a.ogg")
    swallow.set_volume(0.8)
    die = mix.Sound("sound_effects/zap8a.ogg")
    die.set_volume(0.8)
    
    # 2.2 Background image
    mainbackground = pygame.image.load("background_images/mainbackground.jpg")
    
    # 2.3 Background music
    # mix.music.load("background_music/happy.mp3")
    # mix.music.play(-1, 0.0)
    # mix.music.set_volume(0.3)
    
    # 2.4 Window
    win_width = 800
    win_height = 600
    
    # 2.5 Player's ball
    mball_rad = 8
    mball_pos = [win_width//2, win_height//2] 
    mball_vel = [0,0]

    # 2.6 Other balls
    ballrad = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    ballpos = []
    ballvel = []
    ballcol = []
    
    # 2.6.1 Assign randomly the velocity, position, and color of the balls
    for i in range(len(ballrad)):
        ballvel.append([random.randrange(1,8),
                        random.randrange(1,8)])
        ballpos.append([random.randrange(0 + ballrad[i], win_width - ballrad[i]),
                        random.randrange(0 + ballrad[i] ,win_height - ballrad[i])])
        ballcol.append([random.randrange(0,255),
                        random.randrange(0,255),
                        random.randrange(0,255)])    

    for vel in ballvel:
        if random.randrange(0,2) == 0:
            vel[x] *= -1
        if random.randrange(0,2) == 0:
            vel[y] *= -1
    
    # 2.7 Other variables
    score = 0;
    radfive = True   # radfive is initially assigned True while there are still 5-radius balls in ballrad

    # 3. Launch a game window
    window = pygame.display.set_mode((800, 600))
    
    # 4. Set up the main game loop
    while True:
        
        # 5. Event processing
        event = pygame.event.poll()
        
        # 5.1 Check if the user has quit the game
        if event.type == pygame.QUIT:        
            pygame.quit()
            sys.exit()  
    
        # 5.2 Check if any keys have been pressed    
        pressed = pygame.key.get_pressed()
        
        # 5.2.1 Player's Ball velocity determined by UP, DOWN, LEFT and RIGHT of Keyboard
        if pressed[pygame.K_UP] & pressed[pygame.K_DOWN]:
            mball_vel[y] = 0
        elif pressed[pygame.K_UP]: 
            mball_vel[y] = -8
        elif pressed[pygame.K_DOWN]: 
            mball_vel[y] = 8
        else: 
            mball_vel[y] = 0
    
        if pressed[pygame.K_LEFT] & pressed[pygame.K_RIGHT]: 
            mball_vel[x] = 0
        elif pressed[pygame.K_LEFT]: 
            mball_vel[x] = -8
        elif pressed[pygame.K_RIGHT]: 
            mball_vel[x] = 8
        else: 
            mball_vel[x] = 0
        
        # 6. Calculations
        # 6.1 Collision between Player's ball and other balls
        for i in range(len(ballrad)):
            # If statement states that if the player's ball position (the center of the player's ball)
            # is within the ball's range, the following statements will be executed
            # This makes the game harder, since the user will be very mindful of his/her
            # ball getting near to the bigger balls 
            if ballpos[i][x] - ballrad[i] <= mball_pos[x] <= ballpos[i][x] + ballrad[i] and \
            ballpos[i][y] - ballrad[i] <= mball_pos[y] <= ballpos[i][y] + ballrad[i]:    
            # This commented if-statement also works, but it is not in the perspective of the player's ball
            # This makes the game easier since the user have just to avoid the center
            # of the bigger balls. If you encounter immediate game over right after clicking 'Play',
            # it might be because the randomized position of the bigger balls is near the
            # initial position of the player's ball, which is in the center of the window
#            if mball_pos[x] - mball_rad <= ballpos[i][x] <= mball_pos[x] + mball_rad and \
#            mball_pos[y] - mball_rad <= ballpos[i][y] <= mball_pos[y] + mball_rad:
                # a nested if statement to determine if the ball that collided with the player's
                # ball is smaller than the player's ball
                if ballrad[i] <= mball_rad:
                    # A nested if-statement to determine if the ball that collided with the player's
                    # ball has radius 5 (note that there are 10 5-radius balls)
                    if ballrad[i] == 5:
                        swallow.play()  # sound effects will play
                        # score will be added by the radius of the ball that collided 
                        # with the player's ball
                        score += ballrad[i]
                        ballrad[i] = 0  # radius of the collided ball changed to 0
                        ballcol[i] = white # color of the collided ball changed to white
                        # player's ballsize is not yet changed here
                    if ballrad[i] > 5:
                        swallow.play()  # sound effects will play
                        # score will be added by the radius of the ball that collided 
                        # with the player's ball
                        score += ballrad[i]    
                        mball_rad += 5  # player's ballsize added by 5
                        ballrad[i] = 0  # radius of the collided ball changed to 0
                        ballcol[i] = white# color of the collided ball changed to white
                # if the ball that collided with the player's ball is smaller than the player's ball
                else:
                    die.play()  # sound effects will play
                    mix.music.stop()    # music will stop
                    # and the window will change to another window in over_window
                    # named game_over, where score is presented and options are given
                    # whether to play again or not
                    over_window.game_over(score)
                
        count = 0       # initializing 'count' to 0
        radcount = 0    # initializing 'radcount' to 0
        
        # for-loop that count the number of 5-radius balls (saved in 'count')
        # and also counts the number of nonzero-radius balls (saved in 'radcount')
        for i in range(len(ballrad)):
            if ballrad[i] == 5:
                count += 1
            if ballrad[i] != 0:
                radcount += 1
        # if radfive is True, this means that there are still 5-radius balls in this loop
        if radfive == True:
            # a nested-if statement that checks whether there are no more 5-radius balls
            if count == 0: 
                # This is the time when the player's ball size is increased by 5
                # so the player has to swallow all 5-radius balls first in order to get bigger
                mball_rad += 5 
                # if this happens, radfive will be assigned to False so the if-statement
                # will not be executed anymore
                radfive = False
        # this if-statement checks whether the player has swallowed all the balls
        if radcount == 0:
            mix.music.stop()    # the music will stop
            # and the window will change to another window in winner_window.py
            # named winner(), where player will be declared the winner of the game and
            # options are given whether to play again or not
            winner_window.winner()    
                    
        # 6.2 Reverse direction of travel if edge is reached
        for pos, vel, rad in zip(ballpos, ballvel, ballrad):
            if pos[x] > (win_width-rad) or pos[x] < rad:
                vel[x] *= -1
            if pos[y] > (win_height-rad) or pos[y] < rad:
                vel[y] *= -1
            pos[x]+=vel[x]
            pos[y]+=vel[y]
             
        # 6.3 Update player's ball position
        if ((mball_pos[x] > mball_rad and mball_pos[x] < win_width - mball_rad) or
        (mball_pos[x] >= win_width - mball_rad and mball_vel[x] < 0) or
        (mball_pos[x] <= mball_rad and mball_vel[x] > 0)):
            mball_pos[x] += mball_vel[x]
        
        if ((mball_pos[y] > mball_rad and mball_pos[y] < win_height - mball_rad) or
        (mball_pos[y] >= win_height - mball_rad and mball_vel[y] < 0) or
        (mball_pos[y] <= mball_rad and mball_vel[y] > 0)):
            mball_pos[y] += mball_vel[y]
    
        # 7. Draw everything
        # 7.1 Draw Window
        window.blit(mainbackground, [0, 0])
        
        # 7.2 Draw Player's Ball
        pygame.draw.circle(window, blue, (int(mball_pos[x]), int(mball_pos[y])), mball_rad)
        
        # 7.3 Draw the other balls
        for rad, pos, col in zip (ballrad, ballpos, ballcol):
            pygame.draw.circle(window, col, (int(pos[x]), int(pos[y])), rad)
        
        # 7.4 Print Player's Current Score
        text.current_score(score)

        # 8. Update display
        pygame.display.update()
        
        # 9. Frame rate
        clock = pygame.time.Clock().tick(60)