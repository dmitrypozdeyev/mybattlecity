import pygame

from objectts import *

prepsmap =[
    [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

cl = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pl = Player(screen, color='blue', x=15, y=11)


for y in range(len(prepsmap)):
    for x in range(len(prepsmap[y])):
        if prepsmap[y][x] == 1:
            WPrep(screen, pl.bullets, x * 50, y * 50)
        elif prepsmap[y][x] == 2:
            SPrep(screen, pl.bullets, x * 50, y * 50)
        elif prepsmap[y][x] == 3:
            MPrep(screen, pl.bullets, x * 50, y * 50)
        


def check_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pl.start_move_forw()
            elif event.key == pygame.K_DOWN:
                pl.start_move_back()
            elif event.key == pygame.K_LEFT:
                pl.start_move_left()
            elif event.key == pygame.K_RIGHT:
                pl.start_move_right()
            elif event.key == pygame.K_SPACE:
                pl.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                pl.stop_move_right()
            elif event.key == pygame.K_LEFT:
                pl.stop_move_left()
            elif event.key == pygame.K_UP:
                pl.stop_move_forw()
            elif event.key == pygame.K_DOWN:
                pl.stop_move_back()
                
    

def main():
    global run
    run = True
    while run:
        screen.fill((0, 0, 0))
        check_events()
        pl.bullets.update()
        pl.update()
        preps.update()
        pygame.display.update()
        cl.tick(200)
        
                
if __name__ == "__main__":
    main()