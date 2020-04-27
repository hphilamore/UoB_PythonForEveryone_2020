# This file contains functions about printing texts on the window

# Import Package
import pygame

# Initialize Pygame
pygame.init()

# 2. Variables
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)
purple = (120, 0, 120)

# Launch a game window
window = pygame.display.set_mode((800, 600))

def game_title():
    """ Prints the title of the game """
    title_font_size = 133
    title_font = pygame.font.SysFont('impact', title_font_size) 
    title = ["KATAMARI","DAMACY"]

    kata_text_pos = (130,50)
    kata_text = title_font.render(title[0], True, purple)
    kata_back = title_font.render(title[0], True, white)
    
    dama_text_pos = (170,180)
    dama_text = title_font.render(title[1], True, purple)
    dama_back = title_font.render(title[1], True, white)
    
    window.blit(kata_text, kata_text_pos)
    window.blit(kata_back, (kata_text_pos[0]-7,kata_text_pos[1]+3))
    window.blit(dama_text, dama_text_pos)
    window.blit(dama_back, (dama_text_pos[0]-7,dama_text_pos[1]+3))

def instructions():
    """ Prints the instructions of the game """
    instruct_font_size = 20
    instruct_font = pygame.font.SysFont('impact', instruct_font_size)
    instruct_pos = [(215,350), (245,380), (258,410), (200,440)]
    instruct = ["Swallow balls smaller than you to get bigger!",
                "Don't touch bigger balls or you'll die!",
                "You win when you're the last ball!",
                "Use the arrow keys (UP, DOWN, LEFT, RIGHT) to move!"]
    
    insta_text = instruct_font.render(instruct[0], True, black)
    insta_back = instruct_font.render(instruct[0], True, white)

    instb_text = instruct_font.render(instruct[1], True, black)
    instb_back = instruct_font.render(instruct[1], True, white)

    instc_text = instruct_font.render(instruct[2], True, black)
    instc_back = instruct_font.render(instruct[2], True, white)
    
    instd_text = instruct_font.render(instruct[3], True, black)
    instd_back = instruct_font.render(instruct[3], True, white)
    
    window.blit(insta_text, instruct_pos[0])
    window.blit(insta_back, (instruct_pos[0][0]-1, instruct_pos[0][1]+1))
    window.blit(instb_text, instruct_pos[1])
    window.blit(instb_back, (instruct_pos[1][0]-1, instruct_pos[1][1]+1))
    window.blit(instc_text, instruct_pos[2])
    window.blit(instc_back, (instruct_pos[2][0]-1, instruct_pos[2][1]+1))
    window.blit(instd_text, instruct_pos[3])
    window.blit(instd_back, (instruct_pos[3][0]-1, instruct_pos[3][1]+1))
    
def options():
    """ Prints the options for the player to choose: to Play or Quit game """
    options_font_size = 50
    options_font = pygame.font.SysFont('impact', options_font_size)
    options_pos = [(100,500),(570,500)]
    
    play_text = options_font.render("Play", True, black)
    quit_text = options_font.render("Quit", True, black)

    window.blit(play_text, options_pos[0])
    window.blit(quit_text, options_pos[1])

def game_over():
    """ Prints GAME OVER on the window when player loses """
    game_over_font_size = 120
    game_over_font = pygame.font.SysFont('impact', game_over_font_size)
    game_over_pos = (130,100)
    
    game_over_text = game_over_font.render("GAME OVER", True, purple)
    game_over_back = game_over_font.render("GAME OVER", True, white)

    window.blit(game_over_text, game_over_pos)
    window.blit(game_over_back, (game_over_pos[0]-7,game_over_pos[1]+3))

def game_score(score):
    """ Prints SCORE and the player's score when the player loses """
    game_score_font_size = 80
    game_score_font = pygame.font.SysFont('impact', game_score_font_size)
    game_score_pos = (170,300)
    
    game_score_text = game_score_font.render("Score", True, purple)        
    game_score_back = game_score_font.render("Score", True, white)        
    game_scorenum_text = game_score_font.render(str(score), True, white)

    window.blit(game_score_text, game_score_pos)
    window.blit(game_score_back,(game_score_pos[0]-7,game_score_pos[1]+3))
    window.blit(game_scorenum_text,(500,303))
    
def game_options():
    """ Prints the options for the player to choose: to Play or Quit game """
    game_options_font_size = 50
    game_options_font = pygame.font.SysFont('impact', game_options_font_size)
    game_options_pos = [(100,500), (570,500)]
    
    playa_text = game_options_font.render("Play again", True, white)    
    quit_text = game_options_font.render("Quit", True, white)

    window.blit(playa_text, game_options_pos[0])
    window.blit(quit_text, game_options_pos[1])

def game_winner():
    """ Prints YOU WIN! on the window when the player wins """
    winner_font_size = 143
    winner_font = pygame.font.SysFont('impact', winner_font_size)
    winner_pos = (130,100)
    winner_text = winner_font.render("YOU WIN!", True, purple)        
    winner_back = winner_font.render("YOU WIN!", True, white)

    window.blit(winner_text, winner_pos)
    window.blit(winner_back, (winner_pos[0]+3,winner_pos[1]+3))

def current_score(score):
    """ Prints SCORE and the player's score when the player loses """
    gamescore_font_size = 30
    gamescore_font = pygame.font.SysFont('impact', gamescore_font_size)
    gamescore_pos = [(50,10),(150,10)]
    
    game_score_text = gamescore_font.render("Score:", True, black)                
    game_scorenum_text = gamescore_font.render(str(score), True, black)

    window.blit(game_score_text, gamescore_pos[0])
    window.blit(game_scorenum_text,gamescore_pos[1])