from sys import exit
import pygame
import math
play = True
while play == True:
    ##pygame code##
    pygame.init()
    screen = pygame.display.set_mode((548,483))
    pygame.display.set_caption("Golf")
    clock = pygame.time.Clock()
    test_font = pygame.font.Font("Font/Planet-Joy.ttf",60)
    text = test_font.render("Nothing",True,"Yellow")
    baltext = test_font.render("200",True,"Yellow")

    background = pygame.image.load("Graphics/Background.jpg").convert_alpha()
    hole_s = pygame.image.load("Graphics/Hole.png").convert_alpha()
    hole_r = hole_s.get_rect(midbottom = (200,200))
    ball_s = pygame.image.load("Graphics/Ball.png").convert_alpha()
    ball_r = ball_s.get_rect(midbottom = (400,400))
    mp = ball_s.get_rect(midbottom = (400,400))
    ##variables##
    pycoderun = True
    pressed = 0
    stage = 0
    upvel = 0
    lfvel = 0
    held = 0
    letgo = 0
    
    while pycoderun == True:
        while stage == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if ball_r.collidepoint(event.pos):
                          held = 1
                        else:
                            held = 0
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if held == 1:
                            held = 0
                            letgo = 1
                            ##triganometry##
                            #mp = pygame.mouse.get_pos()
                            ydif = (mp[1] - ball_r.y)
                            xdif = (mp[0] - ball_r.x)
                            print(ydif,xdif)
                            if ydif < 0:
                                ydif = ydif*1
                                print("here")
                            if xdif < 0:
                                xdif = xdif*1
                            print(ydif,xdif)
                            ydis = math.sqrt(ydif*ydif)
                            xdis = math.sqrt(xdif*xdif)
                            print(ydis,xdis)
                            aX = math.degrees(math.atan(ydis/xdis))
                            aY = 90-aX
                            print(aX,aY)
                            power = math.sqrt((xdif*xdif) + (ydif*ydif))
                            print(power)
            mp = pygame.mouse.get_pos()
            
            ##ballmechanics##
            if letgo == 1:
                print(power)
                letgo = 0
                upvel =  power * math.cos(aY)
                lfvel =  power * math.cos(aY)
                if mp[1] - ball_r.y < 0:
                    upvel = upvel * -1
                if mp[0] - ball_r.x > 0:
                    lfvel = lfvel * -1
                print(upvel)
                print(lfvel)
                upvel = upvel/10
                lfvel = lfvel/10
            if held == 0:
                ball_r.x -= lfvel
                ball_r.y -= upvel
            if ball_r.x <= 0:
                lfvel = lfvel * -1
            if ball_r.y <= 0:
                upvel = upvel * -1
            if ball_r.x >= 540:
                lfvel = lfvel * -1
            if ball_r.y >= 475:
                upvel = upvel * -1
            ##blits##
            screen.blit(background,(0,0))
            screen.blit(hole_s,hole_r)
            screen.blit(ball_s,ball_r)
            pygame.display.update()
            clock.tick(60)