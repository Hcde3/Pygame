##TO DO

#Pikeman Art
#Spider
#Rockstar
#B&W










from sys import exit
import pygame
from pygame import mixer
import math
import random
play = True

def angleturn(a,b,x,y,A,B):
    xdis = a - x
    ydis = b - y
    if ydis == 0:
        if xdis < 0:
            Angle = 90
        elif xdis > 0:
            Angle = 90
        else:
            Angle = 90
    else:
        Angle = math.degrees(math.atan(xdis/ydis))
    if xdis <= 0 and ydis <= 0:
        Angle = 0 + Angle
    elif xdis <= 0 and ydis >= 0:
        Angle = 180 + Angle
    elif xdis >= 0 and ydis >= 0:
        Angle = 180 + Angle
    elif xdis >= 0 and ydis <= 0:
        Angle = 360 + Angle
    if B == "None":
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
    
def areaaffectattack(tx,ty,r,d):
    killernum = "None"
    if math.sqrt((xcords[BN]-tx)**2 + ((ycords[BN]-ty)**2)) <= r and start[BN] <= roundtimer:
        enemyhealth[BN] -= d
        if enemyhealth[BN] <= 0:
            killernum = x
    return killernum
        

while play == True:
    ##pygame code##
    pygame.init()
    mixer.init()
    mixer.music.load('Music/Main Theme.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()
    screen = pygame.display.set_mode((826,532))
    pygame.display.set_caption("Doodle Defence 1")
    clock = pygame.time.Clock()
    test_font = pygame.font.Font("Font/Planet-Joy.ttf",20)
    under_cursor_font = pygame.font.Font("Font/Planet-Joy.ttf",15)
    text = test_font.render("0",True,"Dark Green")

    background = pygame.image.load("Graphics/Background1.png").convert_alpha()
    blank = pygame.image.load("Graphics/Blank.png").convert_alpha()
    gaze = pygame.image.load("Graphics/Gaze.png").convert_alpha()
    playbutton = pygame.image.load("Graphics/Play.png").convert_alpha()
    playbutton_r = playbutton.get_rect(midbottom = (50,50))
    gaze_stone = pygame.image.load("Graphics/GazeStone.png").convert_alpha()
    flug = pygame.image.load("Graphics/Flug.png").convert_alpha()
    flug_stone = pygame.image.load("Graphics/FlugStone.png").convert_alpha()
    golem = pygame.image.load("Graphics/Golem.png").convert_alpha()
    stare = pygame.image.load("Graphics/Stare.png").convert_alpha()
    towersclose = pygame.image.load("Graphics/Towers.png").convert_alpha()
    towers_r = towersclose.get_rect(midbottom = (773,66))
    towersopen = pygame.image.load("Graphics/TowersOpen.png").convert_alpha()
    dirarrow = pygame.image.load("Graphics/DirectionalArrow.png").convert_alpha()
    wip = pygame.image.load("Graphics/WIP.png").convert_alpha()
    
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
    bomb = pygame.image.load("Graphics/Bomb.png").convert_alpha()
    bombedge = pygame.image.load("Graphics/Bombedged.png").convert_alpha()
    bombdrop = pygame.image.load("Graphics/Bombdrop.png").convert_alpha()
    explosion = pygame.image.load("Graphics/Explosion.png").convert_alpha()
    landing = pygame.image.load("Graphics/Landing.png").convert_alpha()
    
    midasicon = pygame.image.load("Graphics/MIIcon.png").convert_alpha()
    midasicon_r = snipericon.get_rect(midbottom = (730,276))
    midasidle = pygame.image.load("Graphics/Midasidle.png").convert_alpha()
    midas = pygame.image.load("Graphics/Midas.png").convert_alpha()
    skull = pygame.image.load("Graphics/skull.png").convert_alpha()
    goldskull = pygame.image.load("Graphics/goldskull.png").convert_alpha()
    goldskull2 = pygame.image.load("Graphics/goldskull2.png").convert_alpha()
    
    wizardicon = pygame.image.load("Graphics/WZIcon.png").convert_alpha()
    wizardicon_r = wizardicon.get_rect(midbottom = (730,226))
    wizardidle = pygame.image.load("Graphics/Wizardidle.png").convert_alpha()
    wizard = pygame.image.load("Graphics/Wizard.png").convert_alpha()
    staff = pygame.image.load("Graphics/Staff.png").convert_alpha()
    lightning = pygame.image.load("Graphics/Lightning.png").convert_alpha()
    lightning1 = pygame.image.load("Graphics/Lightning1.png").convert_alpha()
    
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
    
    boxericon = pygame.image.load("Graphics/BXIcon.png").convert_alpha()
    boxericon_r = boxericon.get_rect(midbottom = (730,126))
    boxeridle = pygame.image.load("Graphics/Boxeridle.png").convert_alpha()
    boxer = pygame.image.load("Graphics/Boxer.png").convert_alpha()
    bothfist = pygame.image.load("Graphics/BothFist.png").convert_alpha()
    rightfist = pygame.image.load("Graphics/RightFist.png").convert_alpha()
    leftfist = pygame.image.load("Graphics/LeftFist.png").convert_alpha()
    superpunch = pygame.image.load("Graphics/SuperPunch.png").convert_alpha()
    
    rockstaricon = pygame.image.load("Graphics/RSIcon.png").convert_alpha()
    rockstaricon_r = rockstaricon.get_rect(midbottom = (790,226))
    
    spidericon = pygame.image.load("Graphics/SPIcon.png").convert_alpha()
    spidericon_r = spidericon.get_rect(midbottom = (790,176))
    
    blackwhiteicon = pygame.image.load("Graphics/BWIcon.png").convert_alpha()
    blackwhiteicon_r = spidericon.get_rect(midbottom = (790,276))
    
    pikemanicon = pygame.image.load("Graphics/PMIcon.png").convert_alpha()
    pikemanicon_r = spidericon.get_rect(midbottom = (790,126))
    pikemanidle = pygame.image.load("Graphics/Swordsmanidle.png").convert_alpha()
    pikeman = pygame.image.load("Graphics/Pikeman.png").convert_alpha()
    pike = pygame.image.load("Graphics/Pike.png").convert_alpha()
    pikeforward = pygame.image.load("Graphics/Pikeforward.png").convert_alpha()
    pikebackward = pygame.image.load("Graphics/Pikebackward.png").convert_alpha()
    
    ##variables##
    pycoderun = True
    pressed = 0
    stage = 0
    while pycoderun == True:
        while stage == 0:
            roundtimer = 0
            roundstart = False
            balance = 150
            isheld = 0
            near = 0
            turned = 0
            angle = 0
            presetangle = 0
            swordanimation = [sword,sword]
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
            midascords = []
            moneying = pygame.mixer.Sound("Music/Moneying.mp3")
            midasactivated = []
            bombanimation = [bomb,bombedge,bombdrop,explosion,blank]
            boom = pygame.mixer.Sound("Music/Boom.mp3")
            fused = pygame.mixer.Sound("Music/Lit Fuse.mp3")
            falling = pygame.mixer.Sound("Music/Falling.mp3")
            ossilation = 0
            staffanimation = [lightning,lightning1]
            zap = pygame.mixer.Sound("Music/Zap.mp3")
            zaptimer = 0
            fistanimation = [bothfist,rightfist,leftfist]
            handchange = 1
            hit = pygame.mixer.Sound("Music/Punch.mp3")
            superhit = pygame.mixer.Sound("Music/SuperPunch.mp3")
            pikeanimation = [pike,pikeforward,pikebackward]
            
            
            
            hitbox = []
            towersopentrue = -1
            Towerscords = []
            TowersDown = []
            TowersDownrange = []
            TowersDownangled = []
            TowersDownangle = []
            TowersDownturntype = []
            Towers = [swordsman,sniper,builder,medusa,bomber,midas,wizard,boxer,pikeman]
            Towercost = [100,250,50,150,400,50,100,50,150]
            Towersrange = [100,100000000,100000000,100,200,0,125,85,100000000]
            Towerspriority = ["Close","Strong","Close","Close","Strong","Close","Strong","Close","Close"]
            Towersidle = [swordsmanidle,sniperidle,builderidle,medusaidle,bomberidle,midasidle,wizardidle,boxeridle,pikemanidle]
            Towersicon = [swordsmanicon_r,snipericon_r,buildericon_r,medusaicon_r,bombericon_r,midasicon_r,wizardicon_r,boxericon_r,pikemanicon_r]
            animationtimer = [1,5,3,0,5,10,1,0.1,2] 
            Towersappendage = [sword,rifle,trowel,False,blank,False,staff,bothfist,pike]
            TDanimationtimer = []
            TDanimationslide = []
            Towersturntype = ["Full","Full","None","None","None","None","Full","Full","None"]
            TDdmgmult = []
            
            
            xcords = []
            ycords = []
            prog = []
            newprog = []
            stepx = []
            stepy = []
            enemytype = [gaze,flug,golem,stare]
            enemycash = [10,50,75,150]
            enemystonesprite = [gaze_stone,flug_stone,golem,stare]
            enemytypestrength = [1,2,3,4]
            enemytypehealth = [10,50,75,150]
            enemyhealth = []
            enemystrength = []
            enemyblocktimer = []
            enemyblockedby = []
            stonified = []
            
            begin = "Error"
            currentround = begin
            roundswapped = 0
            round1start = [1,2,3,4]
            round1enemies = [gaze,gaze,gaze,flug]
            round1enemydown = [False,False,False,False]
            round1 = (round1enemies,round1start,round1enemydown)
            round2start = [1,2,4,5,6,7]
            round2enemies = [gaze,gaze,flug,flug,flug,flug]
            round2enemydown = [False,False,False,False,False,False]
            round2 = (round2enemies,round2start,round2enemydown)
            round3start = [1,2,3,4,5,6,7,8,9,10]
            round3enemies = [flug,flug,flug,flug,flug,flug,flug,flug,flug,flug]
            round3enemydown = [False,False,False,False,False,False,False,False,False,False]
            round3 = (round3enemies,round3start,round3enemydown)
            round4start = [2,4,6]
            round4enemies = [golem,golem,golem]
            round4enemydown = [False,False,False]
            round4 = (round4enemies,round4start,round4enemydown)
            round5start = [1,2,3,4,5,7,9,11,13,15,17,19,22]
            round5enemies = [gaze,gaze,gaze,gaze,gaze,flug,flug,flug,flug,golem,golem,golem,stare]
            round5enemydown = [False,False,False,False,False,False,False,False,False,False,False,False,False]
            round5 = (round5enemies,round5start,round5enemydown)
            round6start = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
            round6enemies = [gaze,gaze,gaze,gaze,flug,flug,flug,flug,golem,golem,golem,golem,golem,golem,stare,stare,stare,stare,stare]
            round6enemydown = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
            round6 = (round6enemies,round6start,round6enemydown)
            enemy = []
            enemieskilled = 0
            start = []
            rounds = [begin,round1,round2,round3,round4,round5,round6]
            
            path = ["r1","r2","r3","u1","l1","d1","d2","d3","l2","u2","r4","r5","r6","u3","r7","d4","d5","l3","l4","d6","d7","e"]
            while stage == 0:
                mp = pygame.mouse.get_pos()
                if roundstart == True and roundswapped == 0:
                    for i in range(len(rounds)):
                        if  rounds[i] == currentround and roundswapped == 0:
                            currentround = rounds[i+1]
                            roundswapped = 1
                            rnd = i+1
                    if roundswapped == 0:
                        currentround = round6
                elif roundstart == True:
                    for x in range(len(rounds[rnd][0])):
                        for y in range(len(enemytype)):
                            if rounds[rnd][0][x] == enemytype[y]:
                                if rounds[rnd][2][x] != True:
                                    enemy.append(rounds[rnd][0][x])
                                    start.append(rounds[rnd][1][x])
                                    xcords.append(-20)
                                    ycords.append(200)
                                    prog.append("r1")
                                    newprog.append(0)
                                    stepx.append(140)
                                    stepy.append(0)
                                    enemyhealth.append(enemytypehealth[y])
                                    enemystrength.append(enemytypestrength[y])
                                    enemyblocktimer.append(0)
                                    enemyblockedby.append('')
                                    stonified.append(0)
                                    rounds[rnd][2][x] = True
                                
                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if towers_r.collidepoint(event.pos):
                                towersopentrue *= -1
                            if playbutton_r.collidepoint(event.pos):
                                roundstart = True
                            if isheld == 1:
                                isheld = 0
                                for x in range(len(Towers)):
                                    if held == Towersidle[x]:
                                        TowersDown.append(Towers[x])
                                        Towerscords.append((mp[0],mp[1]))
                                        TowersDownrange.append(Towersrange[x])
                                        TowersDownangled.append(Towers[x])
                                        TowersDownangle.append(presetangle)
                                        TowersDownturntype.append(Towersturntype[x])
                                        TDanimationtimer.append(animationtimer[x])
                                        TDdmgmult.append(1)
                                        if Towers[x] == swordsman:
                                            hitbox.append("None")
                                            TDanimationslide.append(swordanimation[1])
                                        elif Towers[x] == sniper:
                                            hitbox.append("None")
                                            TDanimationslide.append(rifleanimation[0])
                                        elif Towers[x] == builder:
                                            hitbox.append("None")
                                            TDanimationslide.append(trowelanimation[0])
                                        elif Towers[x] == medusa:
                                            hitbox.append("None")
                                            TDanimationslide.append(False)
                                        elif Towers[x] == bomber:
                                            hitbox.append("None")
                                            TDanimationslide.append(blank)
                                        elif Towers[x] == midas:
                                            hitbox.append("None")
                                            TDanimationslide.append(False)
                                            midascords.append((mp[0],mp[1]))
                                            midasactivated.append(0)
                                        elif Towers[x] == wizard:
                                            hitbox.append("None")
                                            TDanimationslide.append(lightning)
                                        elif Towers[x] == boxer:
                                            hitbox.append("None")
                                            TDanimationslide.append(fistanimation[0])
                                        elif Towers[x] == pikeman:
                                            hitbox.append("None")
                                            TDanimationslide.append(pikeanimation[0])
                                        presetangle = 0
                            if towersopentrue == 1 and isheld == 0:
                                for x in range(len(Towers)):
                                    if Towersicon[x].collidepoint(event.pos) and Towercost[x] <= balance:
                                        balance -= Towercost [x]
                                        isheld = 1
                                        held = Towersidle[x]
                        if event.button == 3:
                            if isheld == 1:
                                isheld = 0
                                for x in range(len(Towers)):
                                    if Towersidle[x] == held:
                                        balance+= Towercost [x]
                                        held = 0
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            if isheld == 1:
                                for x in range(len(Towersidle)):
                                    if held == Towersidle[x]:
                                        if Towersturntype[x] == "None":
                                            presetangle += 90
                                            if presetangle == 360:
                                                presetangle = 0
                        if event.key == pygame.K_d:
                            balance += 99999
                            
                            
                    
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
                                
                                        
                for x in range(len(midascords)):
                    if midasactivated[x] >= 5:
                        midasactivated[x] -= 1/60
                        appendage = pygame.transform.rotate(goldskull, 0)
                        appendagecords = ((midascords[x][0] - appendage.get_width()/2),(midascords[x][1] - appendage.get_height()/2))
                        screen.blit(appendage,appendagecords)
                    elif midasactivated[x] > 0:
                        midasactivated[x] -= 1/60
                        appendage = pygame.transform.rotate(goldskull2, 0)
                        appendagecords = ((midascords[x][0] - appendage.get_width()/2),(midascords[x][1] - appendage.get_height()/2))
                        screen.blit(appendage,appendagecords)
                    else:
                        appendage = pygame.transform.rotate(skull, 0)
                        appendagecords = ((midascords[x][0] - appendage.get_width()/2),(midascords[x][1] - appendage.get_height()/2))
                        screen.blit(appendage,appendagecords)
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
                                                enemyhealth[target] -= 3
                                            else:
                                                TDanimationslide[x] = swordswingright
                                                pygame.mixer.Sound.play(swordswing)
                                                TDanimationtimer[x] = 1/3
                                                enemyhealth[target] -= 3
                                            if enemyhealth[target] <= 0:
                                                killernum = x
                                        appendageanimation = TDanimationslide[x]
                                        appendage = pygame.transform.rotate(appendageanimation, TowersDownangle[x])
                                        appendagecords = ((Towerscords[x][0] - appendage.get_width()/2),(Towerscords[x][1] - appendage.get_height()/2))
                                    if TowersDown[x] == sniper:
                                        if TDanimationtimer[x] <= 0:
                                            if TDanimationslide[x] == rifle:
                                                TDanimationslide[x] = rifleshot
                                                pygame.mixer.Sound.play(rifleround)
                                                TDanimationtimer[x] = 1
                                                enemyhealth[target] -= 40
                                                if enemyhealth[target] <= 0:
                                                    killernum = x
                                            else:
                                                TDanimationslide[x] = rifle
                                                pygame.mixer.Sound.play(riflereload)
                                                TDanimationtimer[x] = 3
                                        appendageanimation = TDanimationslide[x]
                                        appendage = pygame.transform.rotate(appendageanimation, TowersDownangle[x])
                                        appendagecords = ((Towerscords[x][0] - appendage.get_width()/2),(Towerscords[x][1] - appendage.get_height()/2))
                                    if TowersDown[x] == builder:
                                        if TDanimationtimer[x] <= 0:
                                            if TDanimationslide[x] == trowelplacing:
                                                TDanimationslide[x] = trowel
                                                TDanimationtimer[x] = 1
                                                occupied = 0
                                                for BR in range(len(brickdowncords)):
                                                    if TowersDownangle[x] == 0:
                                                        wcx = -18
                                                        wcy = 27.5
                                                    if TowersDownangle[x] == 180:
                                                        wcx = -18
                                                        wcy = -65
                                                    if TowersDownangle[x] == 90:
                                                        wcx = 27.5
                                                        wcy = -18
                                                    if TowersDownangle[x] == 270:
                                                        wcx = -65
                                                        wcy = -18
                                                    if brickdowncords[BR] == (Towerscords[x][0] + wcx,Towerscords[x][1] + wcy):
                                                        occupied = 1
                                                        brnum = BR
                                                if occupied != 1:
                                                    pygame.mixer.Sound.play(cementing)
                                                    if TowersDownangle[x] == 0:
                                                        wcx = -18
                                                        wcy = 27.5
                                                    if TowersDownangle[x] == 180:
                                                        wcx = -18
                                                        wcy = -65
                                                    if TowersDownangle[x] == 90:
                                                        wcx = 27.5
                                                        wcy = -18
                                                    if TowersDownangle[x] == 270:
                                                        wcx = -65
                                                        wcy = -18
                                                    brickdowncords.append((Towerscords[x][0]+wcx,Towerscords[x][1]+wcy))
                                                    brickdownlevel.append(brick1)
                                                    walls.append(brick9.get_rect(bottomleft = (brickdowncords[-1])))
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
                                                    wcx = -18
                                                    wcy = 27.5
                                                if TowersDownangle[x] == 180:
                                                    wcx = -18
                                                    wcy = -65
                                                if TowersDownangle[x] == 90:
                                                    wcx = 27.5
                                                    wcy = -18
                                                if TowersDownangle[x] == 270:
                                                    wcx = -65
                                                    wcy = -18
                                                occupied = 0
                                                for BR in range(len(brickdowncords)):
                                                    if brickdowncords[BR] == (Towerscords[x][0] + wcx,Towerscords[x][1] + wcy):
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
                                        appendagecords = ((Towerscords[x][0] - appendage.get_width()/2),(Towerscords[x][1] - appendage.get_height()/2))
                                        appendageanimation = TDanimationslide[x]
                                        appendage = pygame.transform.rotate(appendageanimation, TowersDownangle[x])
                                        appendagecords = ((Towerscords[x][0] - appendage.get_width()/2),(Towerscords[x][1] - appendage.get_height()/2))
                                    if TowersDown[x] == bomber:
                                        if TDanimationtimer[x] <= 0:
                                            if TDanimationslide[x] == bomb:
                                                TDanimationslide[x] = bombedge
                                                TDanimationtimer[x] = 5
                                            elif TDanimationslide[x] == bombedge:
                                                TDanimationslide[x] = bombdrop
                                                pygame.mixer.Sound.play(falling)
                                                TDanimationtimer[x] = 1
                                            elif TDanimationslide[x] == bombdrop:
                                                TDanimationslide[x] = explosion
                                                pygame.mixer.Sound.play(boom)
                                                TDanimationtimer[x] = 1.5
                                                enemyhealth[target] -= 30
                                                for BN in range(len(enemy)):
                                                    killernum = areaaffectattack(xcords[target],ycords[target],150,50)
                                                if enemyhealth[target] <= 0:
                                                    killernum = x
                                            elif TDanimationslide[x] == explosion:
                                                TDanimationslide[x] = blank
                                                TDanimationtimer[x] = 3
                                            elif TDanimationslide[x] == blank:
                                                TDanimationslide[x] = bomb
                                                pygame.mixer.Sound.play(fused)
                                                TDanimationtimer[x] = 3
                                        appendageanimation = TDanimationslide[x]
                                        appendage = pygame.transform.rotate(appendageanimation, TowersDownangle[x])
                                        appendagecords = (((xcords[target] - appendage.get_width()/2)-ossilation),((ycords[target] - appendage.get_height()/2)-ossilation))
                                    if TowersDown[x] == wizard:
                                        if TDanimationtimer[x] <= 0:
                                            if TDanimationslide[x] == lightning1:
                                                TDanimationslide[x] = lightning
                                                TDanimationtimer[x] = 1
                                                enemyhealth[target] -= 2*TDdmgmult[x]
                                                zaptimer -= 1/60
                                                TDdmgmult[x] *= 1.2
                                            elif TDanimationslide[x] == lightning:
                                                TDanimationslide[x] = lightning1
                                                pygame.mixer.Sound.play(zap)
                                                TDanimationtimer[x] = 1
                                                enemyhealth[target] -= 2*TDdmgmult[x]
                                                zaptimer -= 1/60
                                                TDdmgmult[x] *= 1.2
                                                if zaptimer <= 0:
                                                    pygame.mixer.Sound.play(zap)
                                                    zaptimer = 60
                                        if enemyhealth[target] <= 0:
                                            killernum = x
                                        appendageanimation = staff
                                        appendage = pygame.transform.rotate(appendageanimation, TowersDownangle[x])
                                        appendagecords = ((Towerscords[x][0] - appendage.get_width()/2),(Towerscords[x][1] - appendage.get_height()/2))
                                        dis = math.sqrt((xcords[target]-Towerscords[x][0])**2 + ((ycords[target]-Towerscords[x][1])**2))
                                        lightning_a = pygame.transform.scale(lightning, (200,140 + dis))
                                        lightning_a = pygame.transform.rotate(lightning_a, TowersDownangle[x])
                                        lightning_c = ((Towerscords[x][0] - lightning_a.get_width()/2),(Towerscords[x][1] - lightning_a.get_height()/2))
                                        screen.blit(lightning_a,lightning_c)
                                    if TowersDown[x] == boxer:
                                        if TDanimationtimer[x] <= 0:
                                            if TDanimationslide[x] == rightfist:
                                                TDanimationtimer[x] = 0.1
                                                handchange = handchange * -1
                                                TDanimationslide[x] = bothfist
                                                enemyhealth[target] -= 1
                                                pygame.mixer.Sound.play(hit)
                                            elif TDanimationslide[x] == leftfist:
                                                TDanimationtimer[x] = 0.1
                                                handchange = handchange * -1
                                                TDanimationslide[x] = bothfist
                                                enemyhealth[target] -= 1
                                                pygame.mixer.Sound.play(hit)
                                            elif TDanimationslide[x] == bothfist:
                                                if handchange == -1:
                                                    TDanimationslide[x] = leftfist
                                                else:
                                                    TDanimationslide[x] = rightfist
                                                    if random.randint(1,10) == 5:
                                                        TDanimationslide[x] = superpunch
                                                TDanimationtimer[x] = 0.1
                                            elif TDanimationslide[x] == superpunch:
                                                enemyhealth[target] -= 20
                                                pygame.mixer.Sound.play(superhit)
                                                TDanimationtimer[x] = 1
                                                handchange = handchange * -1
                                                TDanimationslide[x] = bothfist
                                        if enemyhealth[target] <= 0:
                                            killernum = x
                                        appendageanimation = TDanimationslide[x]
                                        appendage = pygame.transform.rotate(appendageanimation, TowersDownangle[x])
                                        appendagecords = ((Towerscords[x][0] - appendage.get_width()/2),(Towerscords[x][1] - appendage.get_height()/2))
                                    if TowersDown[x] == pikeman:
                                        if TDanimationtimer[x] <= 0:
                                            if TDanimationslide[x] == pike:
                                                TDanimationslide[x] = pikebackward
                                                TDanimationtimer[x] = 1
                                            elif TDanimationslide[x] == pikebackward:
                                                TDanimationslide[x] = pikeforward
                                                TDanimationtimer[x] = 1
                                                for pk in range(len(enemy)):
                                                    if TowersDownangle[x] == 270:
                                                        if xcords[pk] < Towerscords[x][0] and xcords[pk] > (Towerscords[x][0] - 200):
                                                            if ycords[pk] > Towerscords[x][1] - 40 and ycords[pk] < Towerscords[x][1] + 40: 
                                                                enemyhealth[pk] -= 60
                                                                if enemyhealth[pk] <= 0:
                                                                    killernum = x
                                                    elif TowersDownangle[x] == 90:
                                                        if xcords[pk] > Towerscords[x][0] and xcords[pk] < (Towerscords[x][0] + 200):
                                                            if ycords[pk] > Towerscords[x][1] - 40 and ycords[pk] < Towerscords[x][1] + 40: 
                                                                enemyhealth[pk] -= 60
                                                                if enemyhealth[pk] <= 0:
                                                                    killernum = x
                                                    elif TowersDownangle[x] == 0:
                                                        if xcords[pk] < Towerscords[x][0] + 25 and xcords[pk] > Towerscords[x][0] - 25:
                                                            if ycords[pk] > Towerscords[x][1] and ycords[pk] < Towerscords[x][1] + 250: 
                                                                enemyhealth[pk] -= 60
                                                                if enemyhealth[pk] <= 0:
                                                                    killernum = x
                                                    elif TowersDownangle[x] == 180:
                                                        if xcords[pk] < Towerscords[x][0] + 25 and xcords[pk] > Towerscords[x][0] - 25:
                                                            if ycords[pk] > Towerscords[x][1] - 250 and ycords[pk] < Towerscords[x][1]: 
                                                                enemyhealth[pk] -= 60
                                                                if enemyhealth[pk] <= 0:
                                                                    killernum = x
                                                    
                                            else:
                                                TDanimationslide[x] = pike
                                                TDanimationtimer[x] = 1
                                        appendageanimation = TDanimationslide[x]
                                        appendage = pygame.transform.rotate(appendageanimation, TowersDownangle[x])
                                        appendagecords = ((Towerscords[x][0] - appendage.get_width()/2),(Towerscords[x][1] - appendage.get_height()/2))
                                else:
                                    TDdmgmult[x] = 1
                                    appendage = pygame.transform.rotate(Towersappendage[y], TowersDownangle[x])
                                    appendagecords = ((Towerscords[x][0] - appendage.get_width()/2),(Towerscords[x][1] - appendage.get_height()/2))
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
                                    if enemyhealth[target] <= 0:
                                        killernum = x
                                    pygame.mixer.Sound.play(stonify)
                                    enemyblockedby[target] = (enemyblockedby[target],Towerscords[x])
                            if Towerspriority[y] == "Close":
                                target = targetclosest()
                            elif Towerspriority[y] == "Strong":
                                target = targetstrongest()
                            if target != "No":
                                TowersDownangle[x] = angleturn(Towerscords[x][0],Towerscords[x][1],xcords[target],ycords[target],TowersDownangle[x],TowersDownturntype[x])
                                TowersDownangled[x] = pygame.transform.rotate(TowersDown[x], TowersDownangle[x])
                                xwidth = int(TowersDownangled[x].get_width()/2)
                            if TowersDown[x] == bomber:
                                screen.blit(landing,((Towerscords[x][0] - landing.get_width()/2),(Towerscords[x][1] - landing.get_height()/2)))
                                if target != "No":
                                    if ossilation >= 0:
                                        ossilation -= 1/10
                                    else:
                                        ossilation = 5
                                    screen.blit(TowersDownangled[x],((xcords[target] - TowersDownangled[x].get_width()/2),((ycords[target] - TowersDownangled[x].get_height()/2)-ossilation)))
                                else:
                                    screen.blit(TowersDownangled[x],((Towerscords[x][0] - TowersDownangled[x].get_width()/2),(Towerscords[x][1] - TowersDownangled[x].get_height()/2)))
                            else:
                                screen.blit(TowersDownangled[x],((Towerscords[x][0] - TowersDownangled[x].get_width()/2),(Towerscords[x][1] - TowersDownangled[x].get_height()/2)))
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
                    screen.blit(wizardicon,wizardicon_r)
                    screen.blit(boxericon,boxericon_r)
                    screen.blit(rockstaricon,rockstaricon_r)
                    screen.blit(wip,rockstaricon_r)
                    screen.blit(spidericon,spidericon_r)
                    screen.blit(wip,spidericon_r)
                    screen.blit(blackwhiteicon,blackwhiteicon_r)
                    screen.blit(wip,blackwhiteicon_r)
                    screen.blit(pikemanicon,pikemanicon_r)
                    text = test_font.render((str(balance)+"$"),True,"Black")
                    screen.blit(text,(675,50))
                if isheld == 1:
                    screen.blit(held,(mp[0] - 31,mp[1] - 50))
                    dirarrow_ = pygame.transform.rotate(dirarrow, presetangle)
                    screen.blit(dirarrow_,mp)
                if towersopentrue == 1 and isheld == 0:
                    for x in range(len(Towers)):
                        if Towersicon[x].collidepoint(mp):
                            text = under_cursor_font.render(str(Towercost[x]),True,"Black")
                            screen.blit(text,(mp[0],mp[1]-10))
                ##damage+kills##
                for x in range(len(enemy)):
                    y = x-1
                    if not len(enemy) - y <= 0:
                        if enemyhealth[y] <= 0:
                                del enemystrength[y]
                                del start[y]
                                del stepy[y]
                                del stepx[y]
                                del prog[y]
                                del newprog[y]
                                del xcords[y]
                                del ycords[y]
                                enemieskilled += 1
                                for z in range(len(enemytype)):
                                    if enemytype[z] == enemy[y]:
                                        et = z
                                balance += enemycash[et]
                                for i in range(len(midascords)):
                                    if math.sqrt((Towerscords[killernum][0]-midascords[i][0])**2 + ((Towerscords[killernum][1]-midascords[i][1])**2)) <= 200:
                                        pygame.mixer.Sound.play(moneying)
                                        balance += enemycash[et]*0.2
                                        midasactivated[i] = 6
                                del enemyhealth[y]
                                del enemy[y]
                                
                ##timers##
                if roundstart == True:
                    roundtimer += 1/60
                    if roundtimer > 1:
                        if enemieskilled == len(rounds[rnd][0]):
                            roundstart = False
                            roundtimer = 0
                            enemieskilled = 0
                            roundswapped  =0
                            #balance += 50*(rnd/2)
                else:
                    screen.blit(playbutton,playbutton_r)
                for x in range(len(TDanimationtimer)):
                    TDanimationtimer[x] -= 1/60
                pygame.display.update()
                clock.tick(60)