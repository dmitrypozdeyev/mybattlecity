import pygame
preps = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, pl):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x-5, self.y-5, 10, 10)
        self.pl = pl
        self.direction = pl.direction
    
    def update(self):
        self.rect = pygame.Rect(self.x-5, self.y-5, 10, 10)
        pygame.draw.circle(self.screen, (219, 160, 36), (self.x, self.y), 5)
        if self.direction == 'right':
            self.x += 5
        elif self.direction == 'left':
            self.x -= 5
        elif self.direction == 'forw':
            self.y -= 5
        elif self.direction == 'back':
            self.y += 5

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x = 0, y = 0):
        super().__init__()
        self.image = pygame.image.load("files/playerforw.png")
        self.rect = self.image.get_rect(topleft = (x, y))
        self.x = x
        self.y = y
        self.screen = screen
        self.move_right = False
        self.move_left = False
        self.move_forw = False
        self.move_back = False
        self.bullets = pygame.sprite.Group()
        self.direction = 'forw'
        
    def rot_right(self):
        self.image = pygame.image.load("files/playerright.png")
        self.direction = 'right'
        
    def rot_left(self):
        self.image = pygame.image.load("files/playerleft.png")
        self.direction = 'left'
    
    def rot_forw(self):
        self.image = pygame.image.load("files/playerforw.png")
        self.direction = 'forw'
    
    def rot_back(self):
        self.image = pygame.image.load("files/playerback.png")
        self.direction = 'back'
    
    def start_move_right(self):
        self.rot_right()
        self.move_right = True

    def stop_move_right(self):
        self.move_right = False
        
    def start_move_left(self):
        self.rot_left()
        self.move_left = True

    def stop_move_left(self):
        self.move_left = False
        
    
    def start_move_forw(self):
        self.rot_forw()
        self.move_forw = True

    def stop_move_forw(self):
        self.move_forw = False
        
    def start_move_back(self):
        self.rot_back()
        self.move_back = True

    def stop_move_back(self):
        self.move_back = False
        
    def shoot(self):
        self.bullets.add(Bullet(self.screen, self.x + 25, self.y + 25, self))
        
       
    
    
            
    def update(self):
        self.screen.blit(self.image, (self.x, self.y))
        if self.move_right: 
            self.x += 1
        elif self.move_left:
            self.x -= 1
        elif self.move_forw: 
            self.y -= 1
        elif self.move_back:
            self.y += 1
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        for prep in preps:
            for y in range(self.rect.top, self.rect.top + self.rect.height):
                if prep.rect.collidepoint(self.rect.right, y):
                    self.move_right = False
                elif prep.rect.collidepoint(self.rect.left, y):
                    self.move_left = False
            for x in range(self.rect.left, self.rect.left + self.rect.width):
                if prep.rect.collidepoint(x, self.rect.top):
                    self.move_forw = False
                elif prep.rect.collidepoint(x, self.rect.bottom):
                    self.move_back = False
            
        
        
class Prep(pygame.sprite.Sprite):
    def __init__(self, screen, bullets, x = 0, y = 0):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.health = 3
        self.image = pygame.image.load('files/prep3.png')
        self.rect = self.image.get_rect(topleft = (x, y))
        self.bullets = bullets
    
    
        
    
    def update(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        
        for bullet in self.bullets:
            if self.rect.colliderect(bullet.rect):
                self.health -= 1
                bullet.kill()
        
        if self.health == 3:
            self.image = pygame.image.load('files/prep3.png')
        elif self.health == 2:
            self.image = pygame.image.load('files/prep2.png')
        elif self.health == 1:
            self.image = pygame.image.load('files/prep1.png')
        elif self.health == 0:
            self.kill()
            
    
                