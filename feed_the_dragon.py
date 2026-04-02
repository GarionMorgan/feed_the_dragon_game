import pygame

#initialize pygame
pygame.init()

#set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Dragon")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()
#set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100
score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY
#set colors
GREEN = (0,255,0)
DARKGREEN = (10,50,10)
WHITE = (255,255,255)
BLACK = (0,0,0)
#set fonts
font = pygame.font.Font('./feed_the_dragon_assets/AttackGraffiti.ttf', 32)
#set text
score_text = font.render("Score:" + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10,10)
title_text = font.render("Feed the Dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10
lives_text = font.render("Lives: " + str(player_lives))
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)
#set sounds and music

#set images

#the main game loop
running = True
while running:
    #check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#end game
pygame.quit()