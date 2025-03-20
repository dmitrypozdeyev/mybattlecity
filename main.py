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

cl = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pl1 = Player(screen, color='red', x=15, y=11)
pl2 = Player(screen, color='blue', x=0, y=11)

pl1gui = GUILeft(screen, pl1)
pl2gui = GUIRight(screen, pl2, x=600)
        
def endGame(playername):
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
    fontBig = pygame.font.Font('files/font.ttf', 50)
    fontSmall = pygame.font.Font('files/font.ttf', 20)
    mainText = fontBig.render(f"{playername} игрок победил!", False, (255, 255, 255))
    text = fontSmall.render("Нажмите пробел чтобы начать заново", False, (255, 255, 255))
    screen.blit(mainText, (400 - mainText.get_width() / 2, 200 ))
    screen.blit(text, (400 - text.get_width() / 2, 205 + mainText.get_height()))
    global pl1
    global pl2
    global pl1gui
    global pl2gui
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                players.empty()
                pl1 = Player(screen, color='red', x=15, y=11)
                pl2 = Player(screen, color='blue', x=0, y=11)
                pl1gui = GUILeft(screen, pl1)
                pl2gui = GUIRight(screen, pl2, x=600)

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
        pl1gui.update()
        pl2gui.update()
        if pl1.health == 0:
            endGame("Второй")
        elif pl2.health == 0:
            endGame("Первый")
        pygame.display.update()
        print(pl1.ammo, pl2.ammo)
        cl.tick(200)
        
                
if __name__ == "__main__":
    main()