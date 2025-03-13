import pygame

from objectts import *

prepsmap =[
    [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,3,2,0,0,0,0,0,0,0,0],
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
players = pygame.sprite.Group()
cl = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pl1 = Player(screen, color='red', x=15, y=11)
pl2 = Player(screen, color='blue', x=0, y=11)
players.add(pl1, pl2)


for y in range(len(prepsmap)):
    for x in range(len(prepsmap[y])):
        if prepsmap[y][x] == 1:
            WPrep(screen, x, y)
        elif prepsmap[y][x] == 2:
            SPrep(screen, x, y)
        elif prepsmap[y][x] == 3:
            MPrep(screen, x, y)
        


def check_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pl1.start_move_forw()
            elif event.key == pygame.K_DOWN:
                pl1.start_move_back()
            elif event.key == pygame.K_LEFT:
                pl1.start_move_left()
            elif event.key == pygame.K_RIGHT:
                pl1.start_move_right()
            elif event.key == pygame.K_RETURN:
                pl1.shoot()
            elif event.key == pygame.K_w:
                pl2.start_move_forw()
            elif event.key == pygame.K_s:
                pl2.start_move_back()
            elif event.key == pygame.K_a:
                pl2.start_move_left()
            elif event.key == pygame.K_d:
                pl2.start_move_right()
            elif event.key == pygame.K_SPACE:
                pl2.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                pl1.stop_move_right()
            elif event.key == pygame.K_LEFT:
                pl1.stop_move_left()
            elif event.key == pygame.K_UP:
                pl1.stop_move_forw()
            elif event.key == pygame.K_DOWN:
                pl1.stop_move_back()
            elif event.key == pygame.K_d:
                pl2.stop_move_right()
            elif event.key == pygame.K_a:
                pl2.stop_move_left()
            elif event.key == pygame.K_w:
                pl2.stop_move_forw()
            elif event.key == pygame.K_s:
                pl2.stop_move_back()
           
            
                
    

def main():
    global run
    run = True
    while run:
        screen.fill((0, 0, 0))
        check_events()
        bullets.update()
        players.update()
        preps.update()
        pygame.display.update()
        cl.tick(200)
        
                
if __name__ == "__main__":
    main()