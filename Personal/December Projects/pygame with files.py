from sys import exit
import pygame
play = True

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Save Coords")
clock = pygame.time.Clock()
bg = pygame.Surface((800,800))
size = 60
rect = pygame.Surface((size,size))
rect.fill("Red")
pellet = pygame.Surface((10,10))
pellet.fill("White")
pellet_r = pellet.get_rect(center = (400,400))
X = 200
Y = 200
rect_r = rect.get_rect(center = (X,Y))
move_X = 0
move_Y = 0
zoom = 1
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_Y = 5
            if event.key == pygame.K_s:
                move_Y = -5
            if event.key == pygame.K_a:
                move_X = 5
            if event.key == pygame.K_d:
                move_X = -5
            if event.key == pygame.K_i:
                zoom -= 0.1
            if event.key == pygame.K_o:
                zoom += 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_Y = 0
            if event.key == pygame.K_s:
                move_Y = 0
            if event.key == pygame.K_a:
                move_X = 0
            if event.key == pygame.K_d:
                move_X = 0
    X += move_X
    Y += move_Y
    rect_r.y = Y
    rect_r.x = X
    screen.blit(bg,(0,0))
    screen.blit(rect,rect_r)
    scaledSurf = pygame.transform.scale(rect, (size*zoom, size*zoom))
    scaledSurf.fill("Blue")
    rect_r = scaledSurf.get_rect(center = (X,Y))
    screen.blit(scaledSurf, (X-(scaledSurf.get_width()/2),Y-(scaledSurf.get_width()/2)))
    screen.blit(pellet, pellet_r)
    if rect_r.colliderect(pellet_r):
        print("Collision")
    else:
        print("\n")
    pygame.display.update()
    clock.tick(60)