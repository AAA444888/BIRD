import pygame
import random
import os

WIDTH=500
HEIGHT=600
FPS=60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("第一個遊戲") 
clock=pygame.time.Clock()
start_time=pygame.time.get_ticks()

background_img=pygame.image.load(os.path.join("img", "background.png")).convert()
player_img=pygame.image.load(os.path.join("img","player.png")).convert()
rock_imgs=[]
for i in range(7):
    rock_imgs.append(pygame.image.load(os.path.join("img",f"rock{i}.png")).convert())

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img,(50,38))
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.center=(200,HEIGHT-150)
        self.speedx=3
        self.health=100
        
    def update(self):
        key_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x+=self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x-=self.speedx
        if key_pressed[pygame.K_UP]:
            self.rect.y-=self.speedx
        if key_pressed[pygame.K_DOWN]:
            self.rect.y+=self.speedx
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>HEIGHT:
            self.rect.bottom=HEIGHT
            
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(rock_imgs)
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedx=random.randrange(-3,3)
        self.speedy=random.randrange(4,7)
        
    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.top>HEIGHT or self.rect.left>WIDTH or self.rect.right<0:
            self.rect.x=random.randrange(0,WIDTH-self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speedx=random.randrange(-3,3)
            self.speedy=random.randrange(4,7)
            
            
            
all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)
rocks=pygame.sprite.Group()
for i in range(7):
    rock=Rock()
    rocks.add(rock)
    all_sprites.add(rock)
    
font_name=pygame.font.match_font("arial")

def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,WHITE)
    text_rect=text_surface.get_rect()
    text_rect.centerx=x
    text_rect.top=y
    surf.blit(text_surface, text_rect)
    
def draw_health(surf,hp,x,y):
    if hp<0:
        hp=0
    bar_length=100
    bar_height=10
    fill=(hp/100)*bar_length
    outline_rect=pygame.Rect(x,y,bar_length,bar_height)
    fill_rect=pygame.Rect(x,y,fill,bar_height)
    pygame.draw.rect(surf,GREEN,fill_rect)
    pygame.draw.rect(surf,WHITE,outline_rect,2)
    
def new_rock():
    rock=Rock()
    rocks.add(rock)
    all_sprites.add(rock)
    
def show_gameover(score):
    screen.fill(BLACK)
    draw_text(screen,"your score:"+str(score),64,WIDTH/2,HEIGHT/4)
    draw_text(screen,"press m to restart",22,WIDTH/2,HEIGHT/2)
    pygame.display.update()
    waiting=True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    waiting=False
                    return False

running=True
score=0
game_over=False

while running:
    if game_over:
        close=show_gameover(score)
        if close:
            break
        player=Player()
        all_sprites.add(player)
        game_over=False
        score=0
        start_time=pygame.time.get_ticks()
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False 
    time_elapsed = pygame.time.get_ticks()-start_time
    score = time_elapsed//1000
            
    all_sprites.update()
    
    hits=pygame.sprite.spritecollide(player,rocks,True)
    for hit in hits:
        player.health-=25
        if player.health<=0:
            game_over=True
            player.kill()
        new_rock()
        
    screen.fill(WHITE)
    screen.blit(background_img,(0,0))
    all_sprites.draw(screen)
    draw_text(screen,str(score),18,WIDTH/2,15)
    draw_health(screen,player.health,5,10)
    pygame.display.update()
pygame.quit()