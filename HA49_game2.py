import pygame
pygame.init()
#--------------------
white = (255,255,255)
red = (255, 0 , 0)
black = (0,0,0)
col = (130, 130, 130)
col2 = (120,255,120)
# create window
screen_width = 900
screen_height = 600
gamewindow = pygame.display.set_mod((screen_width,screen_height))
pygame.display.set_caption('Game')
pygame.display.update()
#------
clock = pygame.time.Clock()
def gameloop():
    exit_game = False
    game_over = False
    point_x = 45
    point_y = 55
    velocity_x = 0
    velocity_y = 0

    init_velocity = 5
    point_size = 30
    fps = 60
