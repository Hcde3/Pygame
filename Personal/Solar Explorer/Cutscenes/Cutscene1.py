import pygame
import math
from pygame import mixer

on = True
pygame.init()
screen = pygame.display.set_mode((1300,1300))
pygame.display.set_caption("Gravity Jump")
pageturn = pygame.mixer.Sound("SFX\pageturn.mp3")
S1 = pygame.image.load("Graphics\Cutscenes\C1S1.png").convert_alpha()
S2 = pygame.image.load("Graphics\Cutscenes\C1S2.png").convert_alpha()
S3 = pygame.image.load("Graphics\Cutscenes\C1S3.png").convert_alpha()
S4 = pygame.image.load("Graphics\Cutscenes\C1S4.png").convert_alpha()
S5 = pygame.image.load("Graphics\Cutscenes\C1S5.png").convert_alpha()
slides = [S1,S2,S3,S4,S5]
clock = pygame.time.Clock()
c_slide = 0
while on:
    for event in pygame.event.get():
        mp = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.Sound.play(pageturn)
            if slides[c_slide] == slides[-1]:
                on = False
            else:
                c_slide += 1
    screen.blit(slides[c_slide],(0,0))
    pygame.display.update()
    clock.tick(60)
