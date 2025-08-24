import pygame
import random
import math
from pygame import mixer
#create a simple arcade game of space ship 
pygame.init()
#create screen...(width,height)
screen= pygame.display.set_mode((500,500))

#bcakground
bg = pygame.image.load('other\space.jpg')


#player
#player and his/her position info
playerImg = pygame.image.load('other\spaceship.png')
playerX= 250
playerY=350
playerX_change=0

#create player's stuff
def player(x,y):
    #blit means drawing basicalyy
    screen.blit(playerImg, (x,y))

#enemy
enemyX_change= []
enemyY_change=[]
num_of_enemies=5
enemyImg=[]
enemyX ,enemyY =[],[]
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(r'other\alien.png'))
    enemyX.append(random.randint(0,436))
    enemyY.append(random.randint(0,80))
    enemyX_change.append(0.2)
    enemyY_change.append(10)

def enemy(x,y,i):
    
    screen.blit(enemyImg[i],(enemyX[i],enemyY[i]))

#bullet
bulletImg = pygame.image.load(r'other\bullet.png')
bulletY = playerY 
bulletX=0
bulletY_change=0.4
bullet_state="ready"
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y))


#score
score=0
font = pygame.font.Font("other\CheekyRabbit.ttf",32)
textX=10
textY=10
def show_score(x,y):
    score_val =font.render("Score: "+str(score), True, (255,255,255))
    screen.blit(score_val, (x, y))

#game over!
GOfont = pygame.font.Font("other\CheekyRabbit.ttf",80)
def show_gameOver():
    gameOver_text= GOfont.render(" Game Over ",True,(255,255,255))
    screen.blit(gameOver_text,(50,170))

#collision
def isCollision(enemyX,enemyY,bulletX,bulletY):
    dist= math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if dist<27:
            return True
    else:
            return False


#Title and icon
pygame.display.set_caption(" abi's game")
icon = pygame.image.load('other\genius-at-work-logo.png')
pygame.display.set_icon(icon)
#to close the window
run= True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            elif event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            elif event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    bullet_sound = mixer.Sound('other\laser.wav')
                    bullet_sound.play()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key== pygame.K_RIGHT:
                playerX_change=0
            
               
                


    screen.fill((242,172,185))
    #after drawing the screen draw the player

    screen.blit(bg, (0,0))

    #player
    #movement for our player notice how this statement is written outside the for loop
    playerX += playerX_change
    #lets keep some boundaries for player
    if playerX<0:
        playerX=0
    elif playerX>=436: #the boundary is 64 less..as player image is 64
        playerX=436

    #bullet
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #enemy
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        #game over if enemy crosses the player
        if enemyY[i]>=playerY-32:
            for j in range(num_of_enemies):
                enemyY[j]=1000
            show_gameOver()
            break

        
        #lets keep some boundaries for enemy and change direction as it hits them
        if enemyX[i]<0:
            enemyX_change[i]= 0.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i]>=436: #the boundary is 64 less..as player image is 64
            enemyX_change[i]= -0.2
            enemyY[i] += enemyY_change[i]
    
        #colliding or not
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision and (bullet_state=="fire") and enemyY[i]<playerY+32:
            bulletY= playerY
            bullet_state="ready"
            score +=1
            print(score)
            enemyX[i] ,enemyY[i] = random.randint(0,436), random.randint(0,80)
            explode_sound = mixer.Sound('other\explosion.wav')
            explode_sound.play()
        enemy(enemyX[i],enemyY[i],i)



    player(playerX,playerY)
    show_score(textX,textY)
   

    pygame.display.update() 