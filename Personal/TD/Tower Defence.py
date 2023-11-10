##TO DO

#Medusa
#Money
#Rounds










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
                Angle = 0
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
        elif xdis == 0:
            if ydis > 0:
                Angle = 0
            else:
                Angle = 0
        else:
            Angle = math.degrees(math.atan(xdis/ydis))
    else:
        Angle = A
    return Angle
    
def targetstrongest():
    inrange = []
    near = 0
    for V in range(len(enemy)):
        if math.sqrt((xcords[V]-Towerscords[x][0])**2 + ((ycords[V]-Towerscords[x][1])**2)) <= TowersDownrange[x] and start[V] <= roundtimer:
            inrange.append(enemystrength[V])
            near += 1
    if len(inrange) != 0:
        targetstren = max(inrange)
        for V in range(len(enemy)):
            if enemystrength[V] == targetstren:
                target = V
        return target
    else:
        return "No"
        
    
def targetclosest():
    inrange = []
    near = 0
    for V in range(len(enemy)):
        if math.sqrt((xcords[V]-Towerscords[x][0])**2 + ((ycords[V]-Towerscords[x][1])**2)) <= TowersDownrange[x] and start[V] <= roundtimer:
            inrange.append(math.sqrt((xcords[V]-Towerscords[x][0])**2 + ((ycords[V]-Towerscords[x][1])**2)))
    if len(inrange) != 0:
        targetlen = min(inrange)
        for V in range(len(enemy)):
            if math.sqrt((xcords[V]-Towerscords[x][0])**2 + ((ycords[V]-Towerscords[x][1])**2)) == targetlen:
                target = V
        return target
    else:
        return "No"
    


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
    gaze_stone = pygame.image.load("Graphics/GazeStone.png").convert_alpha()
    flug = pygame.image.load("Graphics/Flug.png").convert_alpha()
    flug_stone = pygame.image.load("Graphics/FlugStone.png").convert_alpha()
    towersclose = pygame.image.load("Graphics/Towers.png").convert_alpha()
    towers_r = towersclose.get_rect(midbottom = (773,66))
    towersopen = pygame.image.load("Graphics/TowersOpen.png").convert_alpha()
    dirarrow = pygame.image.load("Graphics/DirectionalArrow.png").convert_alpha()
    
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
    
    medusaicon = pygame.image.load("Graphics/MDIcon.png").convert_alpha()
    medusaicon_r = snipericon.get_rect(midbottom = (670,226))
    medusaidle = pygame.image.load("Graphics/Medusaidle.png").convert_alpha()
    medusa = pygame.image.load("Graphics/Medusa.png").convert_alpha()
    
    bombericon = pygame.image.load("Graphics/BMIcon.png").convert_alpha()
    bombericon_r = snipericon.get_rect(midbottom = (730,176))
    bomberidle = pygame.image.load("Graphics/Bomberidle.png").convert_alpha()
    bomber = pygame.image.load("Graphics/Bomber.png").convert_alpha()
    
    midasicon = pygame.image.load("Graphics/MIIcon.png").convert_alpha()
    midasicon_r = snipericon.get_rect(midbottom = (730,276))
    midasidle = pygame.image.load("Graphics/Midasidle.png").convert_alpha()
    midas = pygame.image.load("Graphics/Midas.png").convert_alpha()
    
    buildericon = pygame.image.load("Graphics/BCIcon.png").convert_alpha()
    buildericon_r = buildericon.get_rect(midbottom = (670,276))
    builderidle = pygame.image.load("Graphics/Builderidle.png").convert_alpha()
    builder = pygame.image.load("Graphics/Builder.png").convert_alpha()
    trowel = pygame.image.load("Graphics/Trowel.png").convert_alpha()
    trowelplacing = pygame.image.load("Graphics/Trowelplacing.png").convert_alpha()
    brick1 = pygame.image.load("Graphics/Brick1.png").convert_alpha()
    brick2 = pygame.image.load("Graphics/Brick2.png").convert_alpha()
    brick3 = pygame.image.load("Graphics/Brick3.png").convert_alpha()
    brick4 = pygame.image.load("Graphics/Brick4.png").convert_alpha()
    brick5 = pygame.image.load("Graphics/Brick5.png").convert_alpha()
    brick6 = pygame.image.load("Graphics/Brick6.png").convert_alpha()
    brick7 = pygame.image.load("Graphics/Brick7.png").convert_alpha()
    brick8 = pygame.image.load("Graphics/Brick8.png").convert_alpha()
    brick9 = pygame.image.load("Graphics/Brick9.png").convert_alpha()
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
            presetangle = 0
            swordanimation = [swordswingright,swordswingleft]
            swordswing = pygame.mixer.Sound("Music/SwordSwing.mp3")
            rifleanimation = [rifle,rifleshot]
            riflereload = pygame.mixer.Sound("Music/SniperReload.mp3")
            rifleround = pygame.mixer.Sound("Music/SniperRound.mp3")
            trowelanimation = [trowel,trowelplacing]
            cementing = pygame.mixer.Sound("Music/Cementing.mp3")
            stonify = pygame.mixer.Sound("Music/Stonify.mp3")
            brickdowncords = []
            brickdownlevel = []
            walls = []
            wallstype = []
            wallsnum = []
            wallstowernum = []
            bricklevel = [brick1,brick2,brick3,brick4,brick5,brick6,brick7,brick8,brick9]
            towersopentrue = -1
            Towerscords = []
            TowersDown = []
            TowersDownrange = []
            TowersDownangled = []
            TowersDownangle = []
            TowersDownturntype = []
            Towers = [swordsman,sniper,builder,medusa,bomber,midas]
            Towersrange = [100,100000000,100000000,100,300,0]
            Towerspriority = ["Close","Strong","Close","Close","Strong","Close"]
            Towersidle = [swordsmanidle,sniperidle,builderidle,medusaidle,bomberidle,midasidle]
            Towersicon = [swordsmanicon_r,snipericon_r,buildericon_r,medusaicon_r,bombericon_r,midasicon_r]
            animationtimer = [1/3,5,3,0,5,0] 
            Towersappendage = [sword,rifle,trowel,False,False,False]
            TDanimationtimer = []
            TDanimationslide = []
            Towersturntype = ["90","Full","0","90","0","0"]
            xcords = [-20,-20,-20,-20]
            ycords = [200,200,200,200]
            prog = ["r1","r1","r1","r1"]
            newprog = [0,0,0,0]
            stepx = [140,140,140,140]
            stepy = [0,0,0,0]
            enemy = [gaze,gaze,gaze,flug]
            enemytype = [gaze,flug]
            enemystonesprite = [gaze_stone,flug_stone]
            enemynumber = [0,1,2,3]
            enemystrength = [1,1,1,2]
            enemyhealth = [10,10,10,50]
            enemyblocktimer = [0,0,0,0]
            enemyblockedby = ['','','','']
            stonified = [0,0,0,0]
            start = [0,4,5,6]
            path = ["r1","r2","r3","u1","l1","d1","d2","d3","l2","u2","r4","r5","r6","u3","r7","d4","d5","l3","l4","d6","d7","e"]
            while stage == 0:
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
                                        TowersDownangle.append(presetangle)
                                        TowersDownturntype.append(Towersturntype[x])
                                        TDanimationtimer.append(animationtimer[x])
                                        if Towers[x] == swordsman:
                                            TDanimationslide.append(swordanimation[1])
                                        elif Towers[x] == sniper:
                                            TDanimationslide.append(rifleanimation[0])
                                        elif Towers[x] == builder:
                                            TDanimationslide.append(trowelanimation[0])
                                        elif Towers[x] == medusa:
                                            TDanimationslide.append(False)
                                        elif Towers[x] == midas:
                                            TDanimationslide.append(False)
                                        elif Towers[x] == bomber:
                                            TDanimationslide.append(False)
                                        presetangle = 0
                            if towersopentrue == 1 and isheld == 0:
                                for x in range(len(Towers)):
                                    if Towersicon[x].collidepoint(event.pos):
                                        isheld = 1
                                        held = Towersidle[x]
                        if event.button == 3:
                            if isheld == 1:
                                isheld = 0
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            if isheld == 1:
                                for x in range(len(Towersidle)):
                                    if held == Towersidle[x]:
                                        if Towersturntype[x] == "0":
                                            presetangle += 90
                                            if presetangle == 360:
                                                presetangle = 0
                            
                            
                    
                screen.blit(background,(0,0))
                
                for x in range(len(brickdowncords)):
                    screen.blit(brickdownlevel[x],brickdowncords[x])
                for x in range(len(enemy)):
                    if roundtimer >= start[x]:
                        screen.blit(enemy[x],(xcords[x] -16,ycords[x]))
                        blocked = 0
                        for z in range(len(walls)):
                            if walls[z].collidepoint((xcords[x],ycords[x])):
                                    blocked = 1
                                    WN = z
                                    blocktype = "wall"
                        if not enemyblocktimer[x] <= 0:
                            enemyblocktimer[x] -= 1/60
                            blocked = 1
                            blocktype = "medusa"
                            stonified[x] = 1
                            for stonevar in range(len(enemytype)):
                                if enemytype[stonevar] == enemy[x]:
                                    enemy[x] = enemystonesprite[stonevar]
                        elif enemyblocktimer[x] <= 0 and stonified[x] == 1:
                            stonified[x] = 0
                            for stonevar in range(len(enemytype)):
                                if enemystonesprite[stonevar] == enemy[x]:
                                    enemy[x] = enemytype[stonevar]
                        if blocked == 0:
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
                                                    ###print(path[y],prog[x])
                                                    prog[x] = path[nextnum]
                                                    ####print(prog[x])
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
                                                        ###print(path[y],prog[x])
                                                        prog[x] = path[nextnum]
                                                        ###print(prog[x])
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
                        if blocked == 1:
                            if blocktype == "wall":
                                if wallstype[WN] == "builder":
                                    if prog[x][0] == "r":
                                        xcords[x] -= 70
                                        stepx[x] += 70
                                    elif prog[x][0] == "l":
                                        xcords[x] += 70
                                        stepx[x] -= 70
                                    elif prog[x][0] == "u":
                                        ycords[x] += 70
                                        stepy[x] -= 70
                                    elif prog[x][0] == "d":
                                        ycords[x] -= 70
                                        stepy[x] += 70
                                    DEL = "No"
                                    up = 0
                                    for BR in range(len(bricklevel)):
                                        if brickdownlevel[WN] == bricklevel[BR] and bricklevel[BR] != brick1 and up != 1:
                                            wallsnum[WN] -= 1
                                            brickdownlevel[WN] = bricklevel[BR - 1]
                                            up = 1
                                        elif brickdownlevel[WN] == brick1 and up != 1:
                                            DEL = WN
                                            up = 1
                                    if DEL != "No":
                                        #print("here")
                                        del brickdowncords[DEL]
                                        del brickdownlevel[DEL]
                                        del walls[DEL]
                                        del wallstype[DEL]
                                        del wallsnum[DEL]
                                        del wallstowernum[DEL]
                            elif blocktype == "medusa":
                                xcords[x] -= 0
                                stepx[x] += 0
                                ycords[x] -= 0
                                stepy[x] += 0
                                
                                        
                                
                for x in range(len(TowersDown)):
                    for y in range(len(Towers)):
                        if Towers[y] == TowersDown[x]:
                            if Towersappendage[y] != False:
                                animation = 0
                                if Towerspriority[y] == "Close":
                                    target = targetclosest()
                                elif Towerspriority[y] == "Strong":
                                    target = targetstrongest()
                                if target != "No":
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
                                                enemyhealth[target] -= 40
                                            else:
                                                TDanimationslide[x] = rifle
                                                pygame.mixer.Sound.play(riflereload)
                                                TDanimationtimer[x] = 3
                                        appendageanimation = TDanimationslide[x]
                                        appendage = pygame.transform.rotate(appendageanimation, TowersDownangle[x])
                                        appendagecords = (Towerscords[x][0] - 115,Towerscords[x][1] - 105)
                                    if TowersDown[x] == builder:
                                        if TDanimationtimer[x] <= 0:
                                            if TDanimationslide[x] == trowelplacing:
                                                TDanimationslide[x] = trowel
                                                TDanimationtimer[x] = 1
                                                occupied = 0
                                                for BR in range(len(brickdowncords)):
                                                    if TowersDownangle[x] == 0:
                                                        tccx = 12.5
                                                        tccy = 62
                                                        wcx = 0
                                                        wcy = 50
                                                    if TowersDownangle[x] == 180:
                                                        tccx = 12.5
                                                        tccy = -50
                                                        wcx = 0
                                                        wcy = -50
                                                    if TowersDownangle[x] == 90:
                                                        tccx = 70
                                                        tccy = 0
                                                        wcx = 70
                                                        wcy = 0
                                                    if TowersDownangle[x] == 270:
                                                        tccx = -50
                                                        tccy = 0
                                                        wcx = -60
                                                        wcy = 0
                                                    if brickdowncords[BR] == (Towerscords[x][0] + tccx,Towerscords[x][1] + tccy):
                                                        occupied = 1
                                                        brnum = BR
                                                if occupied != 1:
                                                    pygame.mixer.Sound.play(cementing)
                                                    if TowersDownangle[x] == 0:
                                                        tccx = 12.5
                                                        tccy = 62
                                                        wcx = 0
                                                        wcy = 50
                                                    if TowersDownangle[x] == 180:
                                                        tccx = 12.5
                                                        tccy = -50
                                                        wcx = 0
                                                        wcy = -50
                                                    if TowersDownangle[x] == 90:
                                                        tccx = 70
                                                        tccy = 0
                                                        wcx = 70
                                                        wcy = 0
                                                    if TowersDownangle[x] == 270:
                                                        tccx = -50
                                                        tccy = 0
                                                        wcx = -60
                                                        wcy = 0
                                                    brickdowncords.append((Towerscords[x][0] + tccx,Towerscords[x][1] + tccy))
                                                    brickdownlevel.append(brick1)
                                                    walls.append(brick9.get_rect(bottomleft = (Towerscords[x][0]+wcx,Towerscords[x][1]+wcy)))
                                                    wallstype.append("builder")    
                                                    wallstowernum.append(len(TowersDown)-1)
                                                    wallsnum.append(1)
                                                else:
                                                    up = 0
                                                    for BR in range(len(bricklevel)):
                                                        if brickdownlevel[brnum] == bricklevel[BR] and bricklevel[BR] != brick9 and up != 1:
                                                            pygame.mixer.Sound.play(cementing)
                                                            brickdownlevel[brnum] = bricklevel[BR + 1]
                                                            wallsnum[brnum] += 1
                                                            up = 1
                                            else:
                                                if TowersDownangle[x] == 0:
                                                    tccx = 12.5
                                                    tccy = 62
                                                    wcx = 0
                                                    wcy = 50
                                                if TowersDownangle[x] == 180:
                                                    tccx = 12.5
                                                    tccy = -50
                                                    wcx = 0
                                                    wcy = -50
                                                if TowersDownangle[x] == 90:
                                                    tccx = 70
                                                    tccy = 0
                                                    wcx = 70
                                                    wcy = 0
                                                if TowersDownangle[x] == 270:
                                                        tccx = -50
                                                        tccy = 0
                                                        wcx = -60
                                                        wcy = 0
                                                occupied = 0
                                                for BR in range(len(brickdowncords)):
                                                    if brickdowncords[BR] == (Towerscords[x][0] + tccx,Towerscords[x][1] + tccy):
                                                        occupied = 1
                                                        brnum = BR
                                                if occupied == 1:
                                                    if brickdownlevel[brnum] == brick9:
                                                       TDanimationslide[x] = trowel
                                                    else:
                                                        TDanimationslide[x] = trowelplacing
                                                else:
                                                    TDanimationslide[x] = trowelplacing
                                                TDanimationtimer[x] = 0.5        
                                        appendageanimation = TDanimationslide[x]
                                        appendage = pygame.transform.rotate(appendageanimation, TowersDownangle[x])
                                        appendagecords = (Towerscords[x][0] - 75,Towerscords[x][1] - 85)
                                else:
                                    if TowersDown[x] == swordsman:
                                        appendage = pygame.transform.rotate(Towersappendage[y], TowersDownangle[x])
                                        appendagecords = (Towerscords[x][0]-85,Towerscords[x][1]-85)
                                    if TowersDown[x] == sniper:
                                        appendage = pygame.transform.rotate(Towersappendage[y], TowersDownangle[x])
                                        appendagecords = (Towerscords[x][0]-85,Towerscords[x][1]-85)
                                    if TowersDown[x] == builder:
                                        appendage = pygame.transform.rotate(Towersappendage[y], TowersDownangle[x])
                                        appendagecords = (Towerscords[x][0]-75,Towerscords[x][1]-85)
                                screen.blit(appendage,appendagecords)
                            if TowersDown[x] == medusa:
                                target = targetclosest()
                                already = 0
                                if target != "No":
                                    for MD in range(len(enemyblockedby[target])):
                                        if enemyblockedby[target][MD] == Towerscords[x]:
                                            already = 1
                                if targetclosest() != "No" and already != 1:
                                    enemyblocktimer[target] = 5
                                    enemyhealth[target] -= 5
                                    pygame.mixer.Sound.play(stonify)
                                    enemyblockedby[target] = (enemyblockedby[target],Towerscords[x])
                            if Towerspriority[y] == "Close":
                                target = targetclosest()
                            elif Towerspriority[y] == "Strong":
                                target = targetstrongest()
                            if target != "No":
                                TowersDownangle[x] = angleturn(Towerscords[x][0],Towerscords[x][1],xcords[target],ycords[target],TowersDownangle[x],TowersDownturntype[x])
                                TowersDownangled[x] = pygame.transform.rotate(TowersDown[x], TowersDownangle[x])
                            screen.blit(TowersDownangled[x],Towerscords[x])
                if towersopentrue == -1:
                    screen.blit(towersclose,towers_r)
                else:
                    screen.blit(towersopen,(640,0))
                    screen.blit(swordsmanicon,swordsmanicon_r)
                    screen.blit(medusaicon,medusaicon_r)
                    screen.blit(snipericon,snipericon_r)
                    screen.blit(buildericon,buildericon_r)
                    screen.blit(bombericon,bombericon_r)
                    screen.blit(midasicon,midasicon_r)
                if isheld == 1:
                    screen.blit(held,(mp[0] - 31,mp[1] - 50))
                    dirarrow_ = pygame.transform.rotate(dirarrow, presetangle)
                    screen.blit(dirarrow_,mp)
                
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
                            ##print(len(enemy))
                ##timers##
                roundtimer += 1/60
                for x in range(len(TDanimationtimer)):
                    TDanimationtimer[x] -= 1/60
                pygame.display.update()
                clock.tick(60)