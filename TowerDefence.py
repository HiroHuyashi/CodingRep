import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1280,720
COLORS={
    "Black" : (0, 0, 0) ,
    "White" : (255,255,255) ,
    "Red" : (180,0,0) ,
    "Green" : (21,69,9) ,
    "Blue" : (0,0,180) ,
    "Yellow" : (180,180,0)}
LIGHTCOLORS={
    "lightRed" : (255,0,0) ,
    "lightGreen" : (31,98,15) ,
    "lightBlue" : (0,0,255) ,
    "lightYellow" : (255,255,0),
    "Gray": (20,20,20)}
BLOCK_SIZE=20
x,y=WIDTH//BLOCK_SIZE,HEIGHT//BLOCK_SIZE
RUNNING=True
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TowerDefence")
FPS=60
CLOCK=pygame.time.Clock()

####        UI      ####
rightWindow=[(860,0),(860,710),(1280,710),(1280,0)]
rightWindowSub=[(860,360),(1280,360)]
font=pygame.font.SysFont(None, 36)
rightUpWinText=font.render("Level Info: ", True, COLORS["White"])
rightDownWinText=font.render("Tower Info: ", True, COLORS["White"])
bottomWinSize = [(0,600), (860,600),(860,710),(0,710)]
bottomWinText = font.render("Available towers: ", True, COLORS["White"])

def drawUI():
    pygame.draw.lines(screen,COLORS["White"],True,bottomWinSize, BLOCK_SIZE)
    pygame.draw.lines(screen,COLORS["White"],True,rightWindow, BLOCK_SIZE)
    pygame.draw.lines(screen,COLORS["White"],False,rightWindowSub, BLOCK_SIZE)
    screen.blit(rightUpWinText,(875,15))
    screen.blit(rightDownWinText,(875,375))
    screen.blit(bottomWinText,(15,620))

road=[(0,140), (260,140), (260,240), (380,240), (380,120), (620,120), (620,500)]

#size (0,0) to (63,35)
userTowers=[(5,3),(15,8),(24,8)]

def tower_to_screen(x, y):
    towerX=x*BLOCK_SIZE
    towerY=y*BLOCK_SIZE
    return towerX,towerY  

while RUNNING:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    screen.fill(COLORS["Black"])
    pygame.draw.lines(screen,COLORS["Green"],False,road, BLOCK_SIZE)
    drawUI()
    for tower_grid_pos in userTowers:
        tower_screen_pos=tower_to_screen(*tower_grid_pos)
        pygame.draw.rect(screen, COLORS["Red"], (*tower_screen_pos, 2*BLOCK_SIZE, 2*BLOCK_SIZE))
    
    pygame.display.flip()