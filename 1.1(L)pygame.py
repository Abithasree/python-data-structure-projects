import pygame
import random
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
enemyImg = pygame.image.load(r'other\alien.png')
enemyX ,enemyY = random.randint(0,436), random.randint(0,80)
enemyX_change= 0.2
enemyY_change=10
def enemy(x,y):
    screen.blit(enemyImg,(enemyX,enemyY))

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
                playerX_change = -0.3
            elif event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        
    screen.fill((242,172,185))
    #after drawing the screen draw the player

    screen.blit(bg, (0,0))


    #movement for our player notice how this statement is written outside the for loop
    playerX += playerX_change
    #lets keep some boundaries for player
    if playerX<0:
        playerX=0
    elif playerX>=436: #the boundary is 64 less..as player image is 64
        playerX=436

    enemyX += enemyX_change
    
    #lets keep some boundaries for enemy and change direction as it hits them
    if enemyX<0:
        enemyX_change= 0.2
        enemyY += enemyY_change
    elif enemyX>=436: #the boundary is 64 less..as player image is 64
        enemyX_change= -0.2
        enemyY += enemyY_change

    player(playerX,playerY)

    enemy(enemyX,enemyY)

    pygame.display.update() 