import pygame, sys, time
from pygame.locals import *
from car import car
from wall_up import wall_up
from wall_left import wall_left
from wall_down import wall_down
from wall_right import wall_right

pygame.init()

ground = 175
coord = 0
coord_y = 385
coord2 = 686
FPS = 50
lives = 1

wall = pygame.sprite.Group()

user = car(ground)
wall_u = wall_up(coord)
wall_l = wall_left(coord)
wall_d = wall_down(coord_y)
wall_r = wall_right(coord2)

wall.add(wall_l)
wall.add(wall_u)
wall.add(wall_d)
wall.add(wall_r)

DISPLAYSURF = pygame.display.set_mode((700, 400), 0, 32)
pygame.display.set_caption("Mania Parking")
fpsClock = pygame.time.Clock()

BLACK = (0,0,0)

def update_car():
    DISPLAYSURF.blit(user.image, user.rect)

def update_u_wall():
    DISPLAYSURF.blit(wall_u.image, wall_u.rect)

def update_l_wall():
    DISPLAYSURF.blit(wall_l.image, wall_l.rect)

def update_d_wall():
    DISPLAYSURF.blit(wall_d.image, wall_d.rect)

def update_r_wall():
    DISPLAYSURF.blit(wall_r.image, wall_r.rect)

def check_walltouser_collision():
    global lives
    for ch in wall:
        if pygame.sprite.collide_rect(ch, user):
            lives = lives - 1

def display_message(text, x, y, s):
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    Surf = BASICFONT.render(text, 1, (255, 255, 255))
    Rect = Surf.get_rect()
    Rect.topleft = (x,y)
    DISPLAYSURF.blit(Surf, Rect)

def game_over_dis():
    display_message('You Crashed!', 250, 120, 60)
    display_message('Press space to play again', 170, 180, 40)
    user.kill()

left = False
right = False
run_game = True

while True:
    if run_game == True:
        DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if run_game == False:
            if event.type == KEYDOWN:
                if (event.key == K_SPACE):
                    run_game = True
                    user = car(ground)
                    lives = 1

        if run_game == True:
            left = False
            right = False
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    left = True
                if event.key == K_UP:
                    right = True

            if event.type == KEYUP:
                if event.key == K_SPACE:
                    continue
                if (event.key == K_UP):
                    right = False
                if (event.key == K_DOWN):
                    left = False

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if run_game == True:
        if right == True:
            user.right()
        if left == True:
            user.left()

        update_car()
        update_u_wall()
        update_l_wall()
        update_d_wall()
        update_r_wall()
        check_walltouser_collision()

        if lives == 0:
            run_game = False

    if run_game == False:
        DISPLAYSURF.fill(BLACK)
        game_over_dis()

    pygame.display.update()
    fpsClock.tick(FPS)
