import pygame
pygame.init()
cl = 0
cr = 0

pygame.font.init()
font1 = pygame.font.Font("MyShrift.ttf", 30)

bx=3
by=3

win = pygame.display.set_mode((700, 500), pygame.NOFRAME)
pygame.display.set_caption("ping pong")
clock = pygame.time.Clock()
FPS = 60
game = True
background = pygame.transform.scale(pygame.image.load('back.jpg'), (700, 500))
pygame.display.flip()
class MySprite(pygame.sprite.Sprite):
    def __init__(self, picture, x, y, width, height, side='right', speed=5):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.side = side
        self.speed = speed
    
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Wall(pygame.sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

    def gor(self):
        keysr = pygame.key.get_pressed()
        if keysr[pygame.K_UP] and self.rect.y >=0:
            self.rect.y -= 5
        if keysr[pygame.K_DOWN] and self.rect.y <= 425:
            self.rect.y += 5

    def gol(self):
        keysl = pygame.key.get_pressed()
        if keysl[pygame.K_w] and self.rect.y >=0:
            self.rect.y -= 5
        if keysl[pygame.K_s] and self.rect.y <= 425:
            self.rect.y += 5

stickl = Wall(0, 0, 0, 10, 10, 10, 80)
stickr = Wall(0, 0, 0, 680, 10, 10, 80)

vixod = MySprite(picture = 'exit.png', x=300, y=450, width=50, height=50)
zanovo = MySprite(picture = 'reset.png', x=350, y=452, width=45, height=45)

ball = MySprite(picture = 'ball.png', x=350, y=250, width=50, height=50)

stopgame = False

while game:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if vixod.rect.collidepoint(x, y):
                game = False
            if zanovo.rect.collidepoint(x, y):
                cl = 0
                cr = 0
                ball.rect.x = 350
                ball.rect.y = 250
                stickl.rect.x = 10
                stickl.rect.y = 10
                stickr.rect.x = 680
                stickr.rect.y = 10
                
                
                
                stopgame = False

    if stopgame:
        if cl == 10:
            boob = font1.render("Левый игрок победил!", True, (0, 0, 0))
            win.blit(boob, (250, 200))
        if cr == 10:
            boob = font1.render("Правый игрок победил!", True, (0, 0, 0))
            win.blit(boob, (250, 200))


    if not stopgame:


        win.blit(background, (0, 0))
    
        Win = font1.render("Левый счет:"+str(cl), True, (0, 0, 0))
        Lose = font1.render("Правый счет:"+str(cr), True, (0, 0, 0))

        win.blit(Win, (40, 10))
        win.blit(Lose, (500, 10))
    
    
        stickl.draw_wall()
        stickr.draw_wall()
        
        ball.reset()
        vixod.reset()
        zanovo.reset()
        stickl.gol()
        stickr.gor()

        ball.rect.x += bx
        ball.rect.y += by
        
        if ball.rect.y < 0 or ball.rect.y > 450:
            by *= -1
        
        if ball.rect.x > 650:
            ball.rect.x = 350
            ball.rect.y = 250
            cl +=1
        
        if ball.rect.x < 0:
            ball.rect.x = 350
            ball.rect.y = 250
            cr +=1
        
        if ball.rect.colliderect(stickl.rect) or ball.rect.colliderect(stickr.rect):
            bx *= -1
    
    if cl == 10 or cr == 10:
        stopgame = True
    
    pygame.display.update()
    clock.tick(FPS)