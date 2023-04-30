#引入套件
import pygame
import random
import os
#宣告變數
WIDTH=500
HEIGHT=600
FPS=60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
#設定遊戲畫面
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("小遊戲")
clock=pygame.time.Clock()
start_time=pygame.time.get_ticks()
#載入圖片
background_img=pygame.image.load(os.path.join("img", "bg.jpg")).convert()
background_image = pygame.transform.scale(background_img,(WIDTH,HEIGHT))
player_img=pygame.image.load(os.path.join("img","BIRD.png")).convert()
pipe_img=pygame.image.load(os.path.join("img","PIPE.png")).convert()
#載入音檔
jump_sound=pygame.mixer.Sound(os.path.join("sound","shoot.wav"))
jump_sound.set_volume(0.1)
hit_sound=pygame.mixer.Sound(os.path.join("sound","rumble.ogg"))
#設定玩家操縱的player
class Player(pygame.sprite.Sprite):
    #player的基本設定
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img,(50,38))
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.center=(100,HEIGHT-150)
        self.speedy=3
        self.health=100
    #player的更新變化
    def update(self):
        self.rect.y+=self.speedy
        key_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE]:
            jump_sound.play()
            self.rect.y-=10
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>HEIGHT:
            self.rect.bottom=HEIGHT
#設定障礙物pipe  
class Pipe(pygame.sprite.Sprite):
    #pipe的基本設定
    def __init__(self,yheight):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pipe_img,(50,400))
        self.rect=self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = yheight
        self.speedx=2
    #pipe的更新變化
    def update(self):
        self.rect.x-=self.speedx
#將物件組成群組       
all_sprites=pygame.sprite.Group()
pipes=pygame.sprite.Group()
player=Player()
all_sprites.add(player)
randnum=random.randrange(70,450)
pipe=Pipe(randnum-450)
pipe2=Pipe(randnum+100)
all_sprites.add(pipe)
pipes.add(pipe)
all_sprites.add(pipe2)
pipes.add(pipe2)
#字體
font_name=os.path.join("font.ttf")
#設定文字輸入
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,WHITE)
    text_rect=text_surface.get_rect()
    text_rect.centerx=x
    text_rect.top=y
    surf.blit(text_surface, text_rect)
#血量條
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
#gameover畫面
def show_gameover(score):
    screen.fill(BLACK)
    draw_text(screen,"your score:"+str(score),64,WIDTH/2,HEIGHT/4)
    draw_text(screen,"press m to restart",22,WIDTH/2,HEIGHT/2)
    pygame.display.update()
    waiting=True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            #結束遊戲
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            #按m繼續
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    waiting=False
                    return False
#遊戲開始畫面
def show_startgame():
    screen.fill(BLACK)
    draw_text(screen,"按 Left_Shift 開始",48,WIDTH/2,HEIGHT/4)
    draw_text(screen,"press space to jump",22,WIDTH/2,HEIGHT/2)
    pygame.display.update()
    waiting=True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    waiting=False
                    return False
#設定變數                       
running=True
score=0
game_over=False
start_game=True
#執行
while running:
    #當gameover
    if game_over:
        close=show_gameover(score)
        if close:
            break
        #新的player，分數歸零
        player=Player()
        all_sprites.add(player)
        game_over=False
        score=0
        start_time=pygame.time.get_ticks()
    #當開始遊戲
    if start_game:
        close=show_startgame()
        if close:
            break
        start_game=False
        score=0
        start_time=pygame.time.get_ticks()
    #遊戲幀數
    clock.tick(FPS)    
    #結束遊戲
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False 
    #成績=遊玩秒數
    time_elapsed = pygame.time.get_ticks()-start_time
    score = time_elapsed//1000
    #所有物件更新
    all_sprites.update()
    #當pipe移動到畫面左側邊界時，從畫面右側產生新的pipe
    if pipe.rect.left<0 or pipe2.rect.left<0:
        randnum=random.randrange(70,450)
        pipe.rect.x=WIDTH
        pipe2.rect.x=WIDTH
        pipe.rect.y=randnum-450
        pipe2.rect.y=randnum+100
    #當碰撞時
    hits=pygame.sprite.spritecollide(player,pipes,False)
    for hit in hits: 
        #播放音檔
        hit_sound.play()
        #扣血
        player.health-=50
        #當health歸零，player消失，gameover畫面
        if player.health<=0:
            game_over=True 
            player.kill()
        #從畫面右側產生新的pipe
        randnum=random.randrange(70,450)
        pipe.rect.x=WIDTH
        pipe2.rect.x=WIDTH       
        pipe.rect.y=randnum-450
        pipe2.rect.y=randnum+100
    #背景
    screen.blit(background_image,(0,0))
    all_sprites.draw(screen)
    draw_text(screen,str(score),18,WIDTH/2,15)
    draw_health(screen,player.health,5,10)
    pygame.display.update()
pygame.quit()