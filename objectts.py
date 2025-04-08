import pygame
preps = pygame.sprite.Group()
bullets = pygame.sprite.Group()
players = pygame.sprite.Group()
bonus = pygame.sprite.Group()


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
    def __init__(self, screen, color = 'red', x = 0, y = 0):
        super().__init__()
        self.image = pygame.image.load("files/playerforw.png")
        self.rect = self.image.get_rect(topleft = (x, y))
        self.x = x * 50
        self.y = y * 50
        self.screen = screen
        self.move_right = False
        self.move_left = False
        self.move_forw = False
        self.move_back = False
        self.direction = 'forw'
        self.color = color
        self.image.fill(self.color, special_flags=pygame.BLEND_ADD)
        self.health = 20
        self.ammo = 30
        self.add(players)
        self.shootsound = pygame.mixer.Sound('files/shoot.mp3')
        self.destroedsound = pygame.mixer.Sound('files/destroed.mp3')
        self.motorsound = pygame.mixer.Sound('files/motor.mp3')
        self.damsound = pygame.mixer.Sound('files/tankdam.mp3')
        
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
        # self.motorsound.play()

    def stop_move_right(self):
        self.move_right = False
        self.motorsound.stop()
        
    def start_move_left(self):
        self.rot_left()
        self.move_left = True
        # self.motorsound.play()

    def stop_move_left(self):
        self.move_left = False
        self.motorsound.stop()
        
    
    def start_move_forw(self):
        self.rot_forw()
        self.move_forw = True
        # self.motorsound.play()

    def stop_move_forw(self):
        self.move_forw = False
        self.motorsound.stop()
        
    def start_move_back(self):
        self.rot_back()
        self.move_back = True
        # self.motorsound.play()

    def stop_move_back(self):
        self.move_back = False
        self.motorsound.stop()
        
    def shoot(self):
        if self.ammo > 0:
            if self.direction == 'forw':
                bullets.add(Bullet(self.screen, self.x + 25, self.y - 10, self))
            elif self.direction == 'back':
                bullets.add(Bullet(self.screen, self.x + 25, self.y + 60, self))
            elif self.direction == 'right':
                bullets.add(Bullet(self.screen, self.x + 60, self.y + 25, self))
            elif self.direction == 'left':
                bullets.add(Bullet(self.screen, self.x - 10, self.y + 25, self))
            self.ammo -= 1
            self.shootsound.play()
            
        
       
    
    
            
    def update(self):
        self.screen.blit(self.image, (self.x, self.y))
        if self.move_right and self.x <= 800 - self.rect.width: 
            self.x += 1
        elif self.move_left and self.x >= 0:
            self.x -= 1
        elif self.move_forw and self.y >= 0: 
            self.y -= 1
        elif self.move_back and self.y <= 600 - self.rect.height:
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
        self.image.fill(self.color, special_flags=pygame.BLEND_ADD)
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                self.health -= 1
                self.damsound.play()
                bullet.kill()
                if self.health <= 0:
                    self.destroedsound.play()
                    self.kill()
    
        
            
            
            
        
        
class Prep(pygame.sprite.Sprite):
    def __init__(self, screen, x = 0, y = 0):
        super().__init__()
        self.x = x * 50
        self.y = y * 50
        self.screen = screen
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        preps.add(self)
    
    
        
    
    def render(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.damsound = pygame.mixer.Sound('files/prepdam.mp3')
        
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                self.health -= 1
                self.damsound.play()
                bullet.kill()
        
class MPrep(Prep):
    def __init__(self, screen, x = 0, y = 0):
        self.health = 3
        self.image = pygame.image.load('files/mprep3.png')
        super().__init__(screen, x, y)
    
    def update(self):
        self.render()
        if self.health == 3:
            self.image = pygame.image.load('files/mprep3.png')
        elif self.health == 2:
            self.image = pygame.image.load('files/mprep2.png')
        elif self.health == 1:
            self.image = pygame.image.load('files/mprep1.png')
        elif self.health == 0:
            self.kill()
    
class SPrep(Prep):
    def __init__(self, screen, x = 0, y = 0):
        self.health = 2
        self.image = pygame.image.load('files/sprep2.png')
        super().__init__(screen, x, y)
    
    def update(self):
        self.render()
        if self.health == 2:
            self.image = pygame.image.load('files/sprep2.png')
        elif self.health == 1:
            self.image = pygame.image.load('files/sprep1.png')
        elif self.health == 0:
            self.kill()
            
class WPrep(Prep):
       
    def __init__(self, screen, x = 0, y = 0):
        self.health = 1
        self.image = pygame.image.load('files/dprep.png')
        super().__init__(screen, x, y)
    
    def update(self, *args, **kwargs):
        self.render()
        if self.health == 0:
            self.kill()

class GUILeft(pygame.sprite.Sprite):
    def __init__(self, screen, player : Player, x = 0, y = 0):
        self.ammofont = pygame.font.Font('files/font.ttf', 20)
        self.healthbar = pygame.Rect(x, y + 25, 10 * player.health, 20)
        self.screen = screen
        self.player = player
        self.x = x
        self.y = y
        super().__init__()
        
    def update(self):
        self.screen.blit(self.ammofont.render(str(self.player.ammo), False, (255, 255, 255)), (self.x, self.y))
        pygame.draw.rect(self.screen, self.player.color, self.healthbar)
        self.healthbar = pygame.Rect(self.x, self.y + 25, 10 * self.player.health, 20)
    
class GUIRight(pygame.sprite.Sprite):
    def __init__(self, screen, player : Player, x = 0, y = 0):
        self.ammofont = pygame.font.Font('files/font.ttf', 20)
        self.healthbar = pygame.Rect(x, y + 25, 10 * player.health, 20)
        self.screen = screen
        self.player = player
        self.x = x
        self.y = y
        super().__init__()
        
    def update(self):
        ammocountimage = self.ammofont.render(str(self.player.ammo), False, (255, 255, 255))
        self.screen.blit(ammocountimage, (self.x + 200 - ammocountimage.get_width(), self.y))
        pygame.draw.rect(self.screen, self.player.color, self.healthbar)
        self.healthbar = pygame.Rect(self.x + (200 - self.player.health * 10), self.y + 25, 10 * self.player.health, 20)
        
class Heal(pygame.sprite.Sprite):
    def __init__(self, screen, x = 0, y = 0):
        super().__init__()
        self.x = x * 50
        self.y = y * 50
        self.screen = screen
        self.image = pygame.image.load('files/heal.png')
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.takebonussound = pygame.mixer.Sound('files/takebonus.mp3')
        bonus.add(self)
        pygame.mixer.Sound('files/bonusspawn.mp3').play()
    
    def update(self):
        self.screen.blit(self.image, (self.x, self.y))
        for player in players:
            if self.rect.colliderect(player.rect):
                self.takebonussound.play()
                if player.health < 15:
                    player.health += 5
                else: 
                    player.health = 20
                self.kill()
    
class AmmoBonus(pygame.sprite.Sprite):
    def __init__(self, screen, x = 0, y = 0):
        super().__init__()
        self.x = x * 50
        self.y = y * 50
        self.screen = screen
        self.image = pygame.image.load('files/ammobonus.png')
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.takebonussound = pygame.mixer.Sound('files/takebonus.mp3')
        bonus.add(self)
        pygame.mixer.Sound('files/bonusspawn.mp3').play()
    
    def update(self):
        self.screen.blit(self.image, (self.x, self.y))
        for player in players:
            if self.rect.colliderect(player.rect):
                self.takebonussound.play()
                player.ammo += 5
                self.kill()