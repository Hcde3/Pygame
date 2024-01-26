from sys import exit
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Block")
clock = pygame.time.Clock()

background = pygame.Surface((500,500))


ball = pygame.Surface((15,15))
ball_r = ball.get_rect(center = (250,250))
ball.fill("White")

p1 = pygame.Surface((25,25))
p1r = p1.get_rect(center = (100,250))
p1.fill("Blue")

p2 = pygame.Surface((25,25))
p2r = p2.get_rect(center = (400,250))
p2.fill("Red")

p1x = 0
p1y = 0
p2x = 0
p2y = 0
bx = 0
by = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1y -= 1
            if event.key == pygame.K_s:
                p1y += 1
            if event.key == pygame.K_d:
                p1x += 1
            if event.key == pygame.K_a:
                p1x -= 1
            if event.key == pygame.K_UP:
                p2y -= 1
            if event.key == pygame.K_DOWN:
                p2y += 1
            if event.key == pygame.K_RIGHT:
                p2x += 1
            if event.key == pygame.K_LEFT:
                p2x -= 1
    p1r.x += p1x
    p1r.y += p1y
    p2r.x += p2x
    p2r.y += p2y
    ball_r.x += bx
    ball_r.y += by
    if p1r.colliderect(ball_r):
        if by > 0 and p1y > 0 or by < 0 and p1y < 0:
            by += p1y*1.5
        else:
            by *= -1
            by += p1y*1.5
        if bx > 0 and p1x > 0 or bx < 0 and p1x < 0:
            bx += p1x*1.5
        else:
            by *= -1
            bx += p1x*1.5
    if p2r.colliderect(ball_r):
        if by > 0 and p2y > 0 or by < 0 and p2y < 0:
            by += p2y*1.5
        else:
            by *= -1
            by += p2y*1.5
        if bx > 0 and p2x > 0 or bx < 0 and p2x < 0:
            bx += p2x*1.5
        else:
            by *= -1
            bx += p2x*1.5
    screen.blit(background,(0,0))
    screen.blit(ball,ball_r)
    screen.blit(p1,p1r)
    screen.blit(p2,p2r)
    pygame.display.update()
    clock.tick(60)
