from sys import exit
import pygame

pygame.init()
screen = pygame.display.set_mode((1000,500))
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")
background = pygame.Surface((1000,500))

#ai_ans = input("Single Player (s) \nMultiplayer (m)\nChoose a Gamemode:  ")
#if ai_ans == "s":
    #dif = input("Simple (0) \nEasy (1)\nNormal (2)\nHard (3)\nImpossible (4)\nChoose a Difficulty:  ")
    
ai_ans = "s"
dif = "4"

while True:
    pt1 = 0
    pt2 = 0
    while True:
        p1v = 0
        p2v = 0
        bxv = 0
        byv = 0
        dest = 190
        ping1 = pygame.Surface((15,120))
        ping1_r = ping1.get_rect(topleft = (60,190))
        ping1.fill("Blue")
        ping2 = pygame.Surface((15,120))
        ping2_r = ping2.get_rect(topleft = (925,190))
        ping2.fill("Red")
        ball = pygame.Surface((20,20))
        ball_r = ball.get_rect(topleft = (485,235))
        ball.fill("White")
        pointblue = pygame.Surface((40,20))
        pointblue.fill("Blue")
        pointred = pygame.Surface((40,20))
        pointred.fill("Red")
        timer = 0
        reacttimer = 0
        start = False
        roundon = True
        while roundon == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        p1v -= 2
                    if event.key == pygame.K_s:
                        p1v += 2
                    if event.key == pygame.K_UP and ai_ans == "m":
                        p2v -= 2
                    if event.key == pygame.K_DOWN and ai_ans == "m":
                        p2v += 2
            
            if ball_r.colliderect(ping1_r):
                if bxv < 0:
                    bxv *= -1.2
                    byv *= 1.2
                    ball.fill("Blue")
            if ball_r.colliderect(ping2_r):
                if bxv > 0:
                    bxv *= -1.2
                    byv *= 1.2
                    ball.fill("Red")

            if ball_r.y > 480:
                if byv > 0:
                    byv *= -1
            if ball_r.y < 0:
                if byv < 0:
                    byv *= -1
            if ball_r.x > 990:
                roundon = False
                pt1 += 1
            if ball_r.x < 0:
                roundon = False
                pt2 += 1
            if ai_ans == "s":
                if dif == "4":
                    if reacttimer > 0.0001:
                        reacttimer = 0
                        if ping2_r.y > 360:
                            p2v -= 3
                        elif ping2_r.y < 20:
                            p2v += 3
                        elif (ball_r.y+10) < (ping2_r.y+60):
                            p2v -= 3
                        else:
                            p2v += 3
                elif dif == "3":
                    if reacttimer > 0.1:
                        reacttimer = 0
                        if (ball_r.y+10) < (ping2_r.y+60):
                            p2v -= 2
                        else:
                            p2v += 2
                elif dif == "2":
                    if reacttimer > 0.2:
                        reacttimer = 0
                        if (ball_r.y+10) < (ping2_r.y+60):
                            p2v -= 3
                        else:
                            p2v += 3
                elif dif == "1":
                    if reacttimer > 0.6:
                        reacttimer = 0
                        if (ball_r.y+10) < (ping2_r.y+60):
                            p2v -= 5
                        else:
                            p2v += 5
                elif dif == "0":
                    if reacttimer > 1:
                        reacttimer = 0
                        if (ball_r.y+10) < (ping2_r.y+60):
                            p2v -= 5
                        else:
                            p2v += 5
                    
                
            
            ping1_r.y += p1v
            ping2_r.y += p2v
            p1v *= 1/1.03
            p2v *= 1/1.03
            ball_r.x += bxv
            ball_r.y += byv
            

            screen.blit(background,(0,0))
            screen.blit(ping1,ping1_r)
            screen.blit(ping2,ping2_r)
            screen.blit(ball,ball_r)
            for x in range(pt1):
                sep = (x+1)*-60
                screen.blit(pointblue,(500+sep,20))
            for x in range(pt2):
                sep = (x+1)*60
                screen.blit(pointred,(500+sep,20))
            
            timer += 1/60
            reacttimer += 1/60
            if timer > 3 and start != True:
                bxv = -2
                byv = 2
                start = True
            pygame.display.update()
            clock.tick(60)
