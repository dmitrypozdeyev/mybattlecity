import pygame

from objectts import *

cl = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pl = Player(screen)

preps.add(WPrep(screen, pl.bullets, 350, 250))


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