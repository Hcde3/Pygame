from sys import exit
import pygame

def window_apply(surface,rectangle,A_X,A_Y):
    rectangle.x = A_X*(window/800) + (800-window)/2 + center_xdis*(window/800)
    rectangle.y = A_Y*(window/800) + (800-window)/2 + center_ydis*(window/800)
    surface = pygame.transform.scale(surface, (surface.get_width()/(window/800), surface.get_width()/(window/800)))
    rectangle = surface.get_rect(topleft = (rectangle.x,rectangle.y))
    
    
    

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
pygame.display.set_caption("Move Rect")
background = pygame.Surface((800,800))
rect = pygame.Surface((60,60))
R = rect.get_rect(topleft = (300,200))
rect2 = pygame.Surface((40,40))
R2 = rect2.get_rect(topleft = (600,550))
center = pygame.Surface((5,5))
center.fill("White")
rect.fill("Red")
rect2.fill("Green")
play = True
window = 800
abs_x1 = 300
abs_y1 = 200
abs_x2 = 600
abs_y2 = 550
center_xdis = 0
center_ydis = 0
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                if window - 100 > 0:
                    window -= 100
            if event.key == pygame.K_i:
                window += 100
            if event.key == pygame.K_w:
                center_ydis -= 10
            if event.key == pygame.K_s:
                center_ydis += 10 
            if event.key == pygame.K_a:
                center_xdis -= 10
            if event.key == pygame.K_d:
                center_xdis += 10
    abs_x1 += 1
    abs_y1 += 1
    screen.blit(background,(0,0))
    window_apply(rect,R, abs_x1, abs_y1)
    window_apply(rect2,R2, abs_x2, abs_y2)
    n_rect = pygame.transform.scale(rect, (rect.get_width()*(window/800), rect.get_width()*(window/800)))
    R = n_rect.get_rect(topleft = (R.x,R.y))
    n_rect2 = pygame.transform.scale(rect2, (rect2.get_width()*(window/800), rect2.get_width()*(window/800)))
    R2 = n_rect2.get_rect(topleft = (R2.x,R2.y))
    screen.blit(n_rect,R)
    screen.blit(n_rect2,R2)
    screen.blit(center,(400,400))
    if R.colliderect(R2):
        print("Collision")
    else:
        print("\n")
    pygame.display.update()
    clock.tick(60)