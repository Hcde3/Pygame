from sys import exit
import files
import pygame
import math
play = True

try:
    coords = files.fileread("coords.txt")
    coords = coords.split()
    xc = int(coords[0])
    yc = int(coords[1])
    print("read")
except:
    xc = 50
    yc = 50
    files.filewrite("50 50","coords.txt")
    print("write")
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Save Coords")
clock = pygame.time.Clock()
bg = pygame.Surface((800,800))
rect = pygame.Surface((60,60))
rect.fill("Red")
rect_r = rect.get_rect(center = (xc,yc))
Xvel = 0
Yvel = 0
while play == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            coords = f"{rect_r.x} {rect_r.y}"
            files.filewrite(coords,"coords.txt")
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Yvel -= 1
            if event.key == pygame.K_s:
                Yvel += 1
            if event.key == pygame.K_a:
                Xvel -= 1
            if event.key == pygame.K_d:
                Xvel += 1
    rect_r.x += Xvel
    rect_r.y += Yvel
    screen.blit(bg,(0,0))
    screen.blit(rect,rect_r)
    pygame.display.update()
    clock.tick(60)