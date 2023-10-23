##TO DO

#Sniper
#Damage
#Enemies
#Warrior










from sys import exit
import pygame
from pygame import mixer
import math
play = True

def angleturn(a,b,x,y,A,B):
    xdis = a - x
    ydis = b - y
    if B == "90":
        if ydis == 0:
            if xdis > 0:
                Angle = 270
            else:
                Angle = 90
        elif xdis == 0:
            if ydis > 0:
                Angle = 180
            else:
                Angle = 0
        else:
            Angle = A
    elif B == "Full":
        if ydis == 0:
            if xdis > 0:
                Angle = 90
            else:
                Angle = 270
        else:
            Angle = math.degrees(math.atan(xdis/ydis))
    return Angle
    
def targetstrongest():
    inrange = []
    near = 0
    for V in range(len(enemy)):
        if math.sqrt((xcords[V]-Towerscords[x][0])**2 + ((ycords[V]-Towerscords[x][1])**2)) <= TowersDownrange[x]:
            inrange.append(enemystrength[V])
            near += 1
    if near != 0:
        targetstren = max(inrange)
        for V in range(len(enemy)):
            if enemystrength[V] == targetstren:
                target = enemynumber[V]
        return target
    else:
        return False
        
    
def targetclosest():
    inrange = []
    near = 0
    for V in range(len(enemy)):
        if math.sqrt((xcords[V]-Towerscords[x][0])**2 + ((ycords[V]-Towerscords[x][1])**2)) <= TowersDownrange[x]:
            inrange.append(math.sqrt((xcords[V]-Towerscords[x][0])**2 + ((ycords[V]-Towerscords[x][1])**2)))
            near += 1
    if near != 0:
        targetlen = min(inrange)
        for V in range(len(enemy)):
            if math.sqrt((xcords[V]-Towerscords[x][0])**2 + ((ycords[V]-Towerscords[x][1])**2)) == targetlen:
                target = enemynumber[V]
        print(len(xcords),target)
        return target
    else:
        return False
    


while play == True:
    ##pygame code##
    pygame.init()
    mixer.init()
    mixer.music.load('Music/Main Theme.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()
    screen = pygame.display.set_mode((826,532))
    pygame.display.set_caption("enemys TD7")
    clock = pygame.time.Clock()
    test_font = pygame.font.Font("Font/Planet-Joy.ttf",50)
    text = test_font.render("enemys",True,"Dark Green")

    background = pygame.image.load("Graphics/Background1.png").convert_alpha()
    gaze = pygame.image.load("Graphics/Gaze.png").convert_alpha()
    flug = pygame.image.load("Graphics/Flug.png").convert_alpha()
    towersclose = pygame.image.load("Graphics/Towers.png").convert_alpha()
    towers_r = towersclose.get_rect(midbottom = (773,66))
    towersopen = pygame.image.load("Graphics/TowersOpen.png").convert_alpha()
    
    swordsmanicon = pygame.image.load("Graphics/SMIcon.png").convert_alpha()
    swordsmanicon_r = swordsmanicon.get_rect(midbottom = (670,126))
    swordsmanidle = pygame.image.load("Graphics/Swordsmanidle.png").convert_alpha()
    swordsman = pygame.image.load("Graphics/Swordsman.png").convert_alpha()
    sword = pygame.image.load("Graphics/Sword.png").convert_alpha()
    swordswingright = pygame.image.load("Graphics/SwordRight.png").convert_alpha()
    swordswingleft = pygame.image.load("Graphics/SwordLeft.png").convert_alpha()
    
    snipericon = pygame.image.load("Graphics/SNIcon.png").convert_alpha()
    snipericon_r = snipericon.get_rect(midbottom = (670,176))
    sniperidle = pygame.image.load("Graphics/Sniperidle.png").convert_alpha()
    sniper = pygame.image.load("Graphics/Sniper.png").convert_alpha()
    rifle = pygame.image.load("Graphics/Rifle.png").convert_alpha()
    rifleshot = pygame.image.load("Graphics/Rifleshot.png").convert_alpha()
    ##variables##
    pycoderun = True
    pressed = 0
    stage = 0
    while pycoderun == True:
        while stage == 0:
            roundtimer = 0
            isheld = 0
            near = 0
            turned = 0
            angle = 0
            swordanimation = [swordswingright,swordswingleft]
            swordswing = pygame.mixer.Sound("Music/SwordSwing.mp3")
            rifleanimation = [rifle,rifleshot]
            riflereload = pygame.mixer.Sound("Music/SniperReload.mp3")
            rifleround = pygame.mixer.Sound("Music/SniperRound.mp3")
            towersopentrue = -1
            Towerscords = []
            TowersDown = []
            TowersDownrange = []
            TowersDownangled = []
            TowersDownangle = []
            TowersDownturntype = []
            Towers = [swordsman,sniper]
            Towersrange = [100,100000000]
            Towerspriority = ["Close","Strong"]
            Towersidle = [swordsmanidle,sniperidle]
            Towersicon = [swordsmanicon_r,snipericon_r]
            animationtimer = [1/3,5] 
            Towersappendage = [sword,rifle]
            TDanimationtimer = []
            TDanimationslide = []
            Towersturntype = ["90","Full"]
            xcords = [-20,-20,-20,-20]
            ycords = [200,200,200,200]
            prog = ["r1","r1","r1","r1"]
            newprog = [0,0,0,0]
            stepx = [140,140,140,140]
            stepy = [0,0,0,0]
            enemy = [gaze,gaze,gaze,flug]
            enemynumber = [0,1,2,3]
            enemystrength = [1,1,1,2]
            enemyhealth = [10,10,10,50]
            start = [0,1,2,4]
            path = ["r1","r2","r3","u1","l1","d1","d2","d3","l2","u2","r4","r5","r6","u3","r7","d4","d5","l3","l4","d6","d7","e"]
            while stage == 0:
                #xcords.append(-20)
                #ycords.append(200)
                #prog.append("r1")
                #newprog.append(0)
                #stepx.append(140)
                #stepy.append(0)
                #enemy.append(blue)
                #start.append((start[-1]+1))
                mp = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if towers_r.collidepoint(event.pos):
                                towersopentrue *= -1
                            if isheld == 1:
                                isheld = 0
                                for x in range(len(Towers)):
                                    if held == Towersidle[x]:
                                        TowersDown.append(Towers[x])
                                        Towerscords.append((mp[0]-25,mp[1]-25))
                                        TowersDownrange.append(Towersrange[x])
                                        TowersDownangled.append(Towers[x])
                                        TowersDownangle.append(0)
                                        TowersDownturntype.append(Towersturntype[x])
                                        TDanimationtimer.append(animationtimer[x])
                                        if Towers[x] == swordsman:
                                            TDanimationslide.append(swordanimation[1])
                                        elif Towers[x] == sniper:
                                            TDanimationslide.append(rifleanimation[0])
                            if towersopentrue == 1 and isheld == 0:
                                for x in range(len(Towers)):
                                    if Towersicon[x].collidepoint(event.pos):
                                        isheld = 1
                                        held = Towersidle[x]
                    
                screen.blit(background,(0,0))
                for x in range(len(enemy)):
                    if roundtimer >= start[x]:
                        screen.blit(enemy[x],(xcords[x] -16,ycords[x]))
                        if stepx[x] == 0: #X
                            if prog[x][0] == "r":
                                if newprog[x] != 1:
                                    for y in range(len(path)):
                                        if newprog[x] != 1:
                                            if path[y] == prog[x]:
                                                nextnum = y+1
                                                prog[x] = path[nextnum]
                                                newprog[x] = 1
                                else:
                                    stepx[x] = 140
                                    stepy[x] = 0
                                    newprog[x] = 0
                            if prog[x][0] == "l":
                                if newprog[x] != 1:
                                    for y in range(len(path)):
                                        if newprog[x] != 1:
                                            if path[y] == prog[x]:
                                                nextnum = y+1
                                                #print(path[y],prog[x])
                                                prog[x] = path[nextnum]
                                                ##print(prog[x])
                                                newprog[x] = 1
                                else:
                                    stepx[x] = -140
                                    stepy[x] = 0
                                    newprog[x] = 0
                        if stepy[x] == 0: #Y
                                if prog[x][0] == "d":
                                    if newprog[x] != 1:
                                        for y in range(len(path)):
                                            if newprog[x] != 1:
                                                if path[y] == prog[x]:
                                                    nextnum = y+1
                                                    prog[x] = path[nextnum]
                                                    newprog[x] = 1
                                    else:
                                        stepy[x] = 100
                                        stepx[x] = 0
                                        newprog[x] = 0
                                if prog[x][0] == "u":
                                    if newprog[x] != 1:
                                        for y in range(len(path)):
                                            if newprog[x] != 1:
                                                if path[y] == prog[x]:
                                                    nextnum = y+1
                                                    #print(path[y],prog[x])
                                                    prog[x] = path[nextnum]
                                                    #print(prog[x])
                                                    newprog[x] = 1
                                    else:
                                        stepy[x] = -100
                                        stepx[x] = 0
                                        newprog[x] = 0        
                        if stepx[x] != 0:
                            if prog[x][0] != "l":
                                xcords[x] += 1
                                stepx[x] -= 1
                            else:
                                xcords[x] -= 1
                                stepx[x] += 1
                        if stepy[x] != 0:
                            if prog[x][0] != "u":
                                ycords[x] += 1
                                stepy[x] -= 1
                            else:
                                ycords[x] -= 1
                                stepy[x] += 1
                for x in range(len(TowersDown)):
                    for y in range(len(Towers)):
                        if Towers[y] == TowersDown[x]:
                            if Towersappendage[y] != False:
                                animation = 0
                                if Towerspriority[y] == "Close":
                                    target = targetclosest()
                                elif Towerspriority[y] == "Strong":
                                    target = targetstrongest()
                                if target != False:
                                    animation = 1
                                if animation != 0:
                                    if TowersDown[x] == swordsman:
                                        if TDanimationtimer[x] <= 0:
                                            if TDanimationslide[x] == swordswingright:
                                                TDanimationslide[x] = swordswingleft
                                                pygame.mixer.Sound.play(swordswing)
                                                TDanimationtimer[x] = 1/3
                                                enemyhealth[target] -= 2
                                            else:
                                                TDanimationslide[x] = swordswingright
                                                pygame.mixer.Sound.play(swordswing)
                                                TDanimationtimer[x] = 1/3
                                                enemyhealth[target] -= 2
                                        appendageanimation = TDanimationslide[x]
                                        appendage = pygame.transform.rotate(appendageanimation, TowersDownangle[x])
                                        appendagecords = (Towerscords[x][0] - 85,Towerscords[x][1]-85)
                                    if TowersDown[x] == sniper:
                                        if TDanimationtimer[x] <= 0:
                                            if TDanimationslide[x] == rifle:
                                                TDanimationslide[x] = rifleshot
                                                pygame.mixer.Sound.play(rifleround)
                                                TDanimationtimer[x] = 1
                                                enemyhealth[target] -= 10
                                            else:
                                                TDanimationslide[x] = rifle
                                                pygame.mixer.Sound.play(riflereload)
                                                TDanimationtimer[x] = 3
                                        appendageanimation = TDanimationslide[x]
                                        appendage = pygame.transform.rotate(appendageanimation, TowersDownangle[x])
                                        appendagecords = (Towerscords[x][0] - 115,Towerscords[x][1] - 105)
                                else:
                                    if TowersDown[x] == swordsman:
                                        appendage = pygame.transform.rotate(Towersappendage[y], TowersDownangle[x])
                                        appendagecords = (Towerscords[x][0]-85,Towerscords[x][1]-85)
                                    if TowersDown[x] == sniper:
                                        appendage = pygame.transform.rotate(Towersappendage[y], TowersDownangle[x])
                                        appendagecords = (Towerscords[x][0]-85,Towerscords[x][1]-85)
                                screen.blit(appendage,appendagecords)
                            if Towerspriority[y] == "Close":
                                target = targetclosest()
                            elif Towerspriority[y] == "Strong":
                                target = targetstrongest()
                            if target != False:
                                TowersDownangle[x] = angleturn(Towerscords[x][0],Towerscords[x][1],xcords[target],ycords[target],TowersDownangle[x],TowersDownturntype[x])
                                TowersDownangled[x] = pygame.transform.rotate(TowersDown[x], TowersDownangle[x])
                            screen.blit(TowersDownangled[x],Towerscords[x])
                if towersopentrue == -1:
                    screen.blit(towersclose,towers_r)
                else:
                    screen.blit(towersopen,(640,0))
                    screen.blit(swordsmanicon,swordsmanicon_r)
                    screen.blit(snipericon,snipericon_r)
                if isheld == 1:
                    screen.blit(held,(mp[0] - 31,mp[1] - 50))
                
                ##damage+kills##
                for x in range(len(enemy)):
                    y = x-1
                    if enemyhealth[y] <= 0:
                            del enemyhealth[y]
                            del enemystrength[y]
                            del enemynumber[y]
                            del enemy[y]
                            del start[y]
                            del stepy[y]
                            del stepx[y]
                            del prog[y]
                            del newprog[y]
                            del xcords[y]
                            del ycords[y]
                            print(len(enemy))
                ##timers##
                roundtimer += 1/60
                for x in range(len(TDanimationtimer)):
                    TDanimationtimer[x] -= 1/60
                pygame.display.update()
                clock.tick(60)