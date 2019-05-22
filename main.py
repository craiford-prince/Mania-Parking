import pygame, sys, time
from pygame.locals import *
from car import car
from wall_up import wall_up
from wall_left import wall_left
from wall_down import wall_down
from wall_right import wall_right
from bystander_car import bystander_car

pygame.init()

ground = 175
yground2 = 90
xground2 = 555
coord = 0
coord_y = 385
coord2 = 686
FPS = 50
lives = 1

wall = pygame.sprite.Group()
bcar = pygame.sprite.Group()

user = car(ground)
wall_u = wall_up(coord)
wall_l = wall_left(coord)
wall_d = wall_down(coord_y)
wall_r = wall_right(coord2)

b_car = bystander_car(xground2, yground2)

wall.add(wall_l)
wall.add(wall_u)
wall.add(wall_d)
wall.add(wall_r)

bcar.add(b_car)

DISPLAYSURF = pygame.display.set_mode((700, 400), 0, 32)
pygame.display.set_caption("Mania Parking")
fpsClock = pygame.time.Clock()

GRAY = (80, 80, 80)

def update_car():
    DISPLAYSURF.blit(user.image, user.rect)

def update_bcar():
    DISPLAYSURF.blit(b_car.image, b_car.rect)

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

def check_bcartocar_collision():
    global lives
    for ch in bcar:
        if pygame.sprite.collide_rect(ch, user):
            lives = lives - 1

def display_message(text, x, y, s):
    BASICFONT = pygame.font.Font('freesansbold.ttf', 24)
    Surf = BASICFONT.render(text, 1, (255, 255, 255))
    Rect = Surf.get_rect()
    Rect.topleft = (x,y)
    DISPLAYSURF.blit(Surf, Rect)

def game_over_dis():
    display_message('You Crashed!', 240, 120, 60)
    display_message('Press space to play again', 175, 200, 40)
    user.kill()

def win_round1():
    display_message('Congratulations!', 240, 120, 60)
    display_message('Press Tab For Level 2', 175, 200, 40)
    user.kill()

left = False
right = False
win_borderR = False
win_borderL = False
win_borderU = False
win_borderD = False
run_game = True
next_round = False
run_game2 = False
reset_game = False

while True:
    if run_game == True:
        DISPLAYSURF.fill(GRAY)
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
        if user.rect.x > 555:
            win_borderL = True
        if user.rect.x < 620:
            win_borderR = True
        if user.rect.y > 110:
            win_borderU = True
        if user.rect.y < 220:
            win_borderD = True
        if win_borderL == True and win_borderR == True and win_borderU == True and win_borderD == True and right == False:
            next_round = True

        update_car()
        update_u_wall()
        update_l_wall()
        update_d_wall()
        update_r_wall()
        update_bcar()

        check_walltouser_collision()
        check_bcartocar_collision()

        if lives == 0:
            run_game = False

    if run_game == False:
        DISPLAYSURF.fill(GRAY)
        update_u_wall()
        update_l_wall()
        update_d_wall()
        update_r_wall()
        update_car()
        update_bcar()
        game_over_dis()

    if next_round == True:
        win_round1()

        if run_game2 == False:
            if event.type == KEYDOWN:
                if (event.key == K_TAB):
                    DISPLAYSURF.fill(GRAY)
                    run_game2 == True
                    user = car(ground)
                    lives = 1

        if run_game2 == True:
            left = False
            right = False
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    left = True
                if event.key == K_UP:
                    right = True

            if event.type == KEYUP:
                if event.key == K_TAB:
                    continue
                if event.key == K_UP:
                    right = False
                if event.key == K_DOWN:
                    left = False

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if run_game2 == True:
        if right == True:
            user.right()
        if left == True:
            user.left()
        update_u_wall()
        update_l_wall()
        update_d_wall()
        update_r_wall()
        update_car()
        update_bcar()

        if lives == 0:
            reset_game = True

    if reset_game == True:
        update_u_wall()
        update_l_wall()
        update_d_wall()
        update_r_wall()
        update_car()
        update_bcar()
        game_over_dis()


    pygame.display.update()
    fpsClock.tick(FPS)
