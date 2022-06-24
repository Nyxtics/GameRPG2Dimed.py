#Modulo do jogo
import pygame
import cadastro 
import random
import math
#Musica
from pygame import mixer

pygame.init()
screen=pygame.display.set_mode((800,600))
backgroundimage=pygame.image.load("data/background.png")

#Icone e titulo
pygame.display.set_caption("RPG ShotterDragon")
icon=pygame.image.load("data/logo.png")
pygame.display.set_icon(icon)

#Imagem do jogador
playerimage=pygame.image.load("data/dragao.png")
playerX=370
playerY=480
playerX_change=0

#Musica do fundo
mixer.music.load('data/musicafundo.mp3')
mixer.music.play(-1)

#Imagem dos inimigos
enemyImg =[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=13

for i in range(num_of_enemies):
   
    enemyImg.append(pygame.image.load("data/warrior.png")) 
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(20)

#Bola de fogo do dragão
bulletImg =pygame.image.load("data/fogo.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

#Mortes 
score_value=0

font=pygame.font.Font('freesansbold.ttf',32)
over_font=pygame.font.Font('freesansbold.ttf',64)

textX=10
textY=10

#Funções

def show_score(x,y):
    score=font.render("Experiência:"+str(score_value),True, (255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerimage,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+16))

def collision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return False

def game_over_text():
    over_text=font.render("Voce morreu!",True, (255,255,255))
    screen.blit(over_text,(325,300))

running=True

while running:
    screen.fill((0,0,0))
    screen.blit(backgroundimage,(0,0))

#Evento do teclado    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-5

            if event.key==pygame.K_RIGHT:
                playerX_change=5

            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound('data/fogosaindo.wav')
                    bullet_sound.play()
                    bulletX=playerX
                    fire_bullet(bulletX, bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0

        
    playerX+=playerX_change
    

    if(playerX<=0):
        playerX=0
    elif playerX>=736:
        playerX=736
    
#Movimento do inimigo
    for i in range(num_of_enemies):
        if enemyY[i]>440 :
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break
       
        enemyX[i]+=enemyX_change[i]
        
        if(enemyX[i]<=0):
            enemyX_change[i]=4
            enemyY[i]+=enemyY_change[i]
        
        elif enemyX[i]>=736:
            enemyX_change[i]=-4
            enemyY[i]+=enemyY_change[i]
    
#Colisões com warrios

        collisionvalue=collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collisionvalue:
            explosion_sound=mixer.Sound('data/hitwarrior.wav')
            explosion_sound.play()
            bulletY=480
            bullet_state="ready"
            score_value+=1
            enemyX[i]=random.randint(0, 800)
            enemyY[i]=random.randint(50, 150)

        enemy(enemyX[i], enemyY[i],i)
    
#Movimento do fogo
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY-=bulletY_change

#Render  
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
            
