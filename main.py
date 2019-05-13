import pygame, sys, time
from pygame.locals import *
from car import car

pygame.init()
ground = 175
user = car(ground)
FPS = 50

DISPLAYSURF = pygame.display.set_mode((700, 400), 0, 32)
pygame.display.set_caption("Mania Parking")
fpsClock = pygame.time.Clock()

BLACK = (0,0,0)

def update_car():
    DISPLAYSURF.blit(user.image, user.rect)

def check_walltouser_collision():
    global lives
    if pygame.sprite.collide_rect(user, right):
        if user.rect.x < 0:
            lives = lives - 1
        if user.rect.x > 618:
            lives = lives - 1

def display_message(text, x, y, s):
    BASICFONT = pygame.font.Font('fressansbold.ttf', 16)
    Surf = BASICFONT.render(text, 1, (0, 0, 0))
    rect = surf.get_rect()
    Rect.topleft = (x,y)
    DISPLAYSURF.blit(Surf, Rect)

def game_over_dis():
    display_message('You Crashed!', 250, 120, 60)
    display_message('Press space to play again', 170, 180, 40)
    user.kill()

def lives():
    global lives

left = False
right = False
run_game = True
u_border_l = False
u_border_r = False
u_border_u = False
u_border_d = False

while True:
    if run_game == True:
        DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if run_game == False:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    run_game = True
                    user = car(ground)
                    lives = 1

        if run_game == True:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    right = True
                if event.key == K_DOWN:
                    left = True
            if event.type == KEYUP:
                if event.key == K_UP:
                    right = False
                if event.key == K_DOWN:
                    left = False

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if run_game == True:
        if user.rect.x < 0:
            u_border_l = True
        if user.rect.x > 618:
            u_border_r = True
        if user.rect.x > 0:
            u_border_l = False
        if user.rect.x < 618:
            u_border_r = False
        if user.rect.y < 0:
            u_border_u = True
        if user.rect.y > 318:
            u_border_d = True
        if user.rect.y > 0:
            u_border_u = False
        if user.rect.y < 318:
            u_border_d = False
        if right == True and u_border_r == False:
            user.right()
        if left == True and u_border_l == False:
            user.left()

        check_walltouser_collision()
        update_car()

        if lives == 0:
            run_game = False

    if run_game == False:
        DISPLAYSURF.fill(BLACK)
        game_over_dis()

    pygame.display.update()
    fpsClock.tick(FPS)
