import random
import math
import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

background = pygame.image.load("background.png")

playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0


enemyImg =[]
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
nOfEnemies = 6

scoreValue = 0
testX = 10
testY = 10
font = pygame.font.Font('freesansbold.ttf',32)

def showScore(x,y):
    score = font.render("Score : "+str(scoreValue),True,(255,255,255))
    screen.blit(score,(x,y))

for i in range(nOfEnemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(5)
    enemyY_change.append(50)

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY =playerY
bulletX_change = 0
bulletY_change = 10
bulltetStatus = "ready"

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def gameOverText():
    overText = font.render("GAME OVER",True,(255,255,255))
    screen.blit(overText,(250,250))

def fire_bullet(x,y):
    global bulltetStatus
    bulltetStatus = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False

    
    
running = True
while running:
    screen.fill((0,0,0))

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key ==pygame.K_RIGHT:
                playerX_change= 5
            if event.key == pygame.K_SPACE:
                if(bulltetStatus == "ready"):
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                playerX_change = 0


    playerX  = playerX + playerX_change
    if playerX<0:
        playerX=0
    elif playerX>=736:
        playerX = 736


    for i in range(nOfEnemies):
        if enemyY[i]>440:
            for j in range(nOfEnemies):
                enemyY[j]=2000
            gameOverText()
            break

        enemyX[i] = enemyX[i]+enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i] = 5
            enemyY[i] = enemyY[i]+enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i] = -5
            enemyY[i] = enemyY[i]+enemyY_change[i]

        collision = iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bulltetStatus = "ready"
            scoreValue = scoreValue+1
            enemyX[i]  = random.randint(0,736) 
            enemyY[i] = random.randint(50,150)
    
       
        enemy(enemyX[i],enemyY[i],i)

    if bulletY <= 0:
        bulletY = 480
        bulltetStatus = "ready"
    
    if bulltetStatus == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY = bulletY - bulletY_change

  
    player(playerX,playerY)
    showScore(testX,testY)
    pygame.display.update()




