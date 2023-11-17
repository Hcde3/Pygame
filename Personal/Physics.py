from sys import exit
import pygame

pygame.init()
screen = pygame.display.set_mode((800,500))
clock = pygame.time.Clock()
pygame.display.set_caption("Move Rect")
background = pygame.Surface((800,500))
rectangle = pygame.Surface((60,60))
rectangle.fill("Purple")
rect = rectangle.get_rect(center = (400,250))
floor = pygame.Surface((800,1000))
floor.fill("Dark Green")
floor_r = floor.get_rect(topleft = (0,395))

Velocity = 0
Mass = 1
Acceleration = []
Force = 0
setgrav = 0.5
grav = 0.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Acceleration.append(-15)
            if event.key == pygame.K_s:
                Acceleration.append(15)

    ##Dynamics##
    Acceleration.append(grav)
    for x in range(len(Acceleration)):
        Force += Mass*Acceleration[x]
    if rect.y > 335:
        if Velocity > 0:
            Force = Force*-1 - (Velocity*1.3)
        rect.y = 335
    else:
        grav = setgrav
    Velocity += Force
    rect.y += Velocity
    Acceleration = []
    Force = 0
    
    
    ##Blitting##
    screen.blit(background,(0,0))
    screen.blit(floor,floor_r)
    screen.blit(rectangle,rect)
    pygame.display.update()
    clock.tick(90)