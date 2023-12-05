import pygame
import random
import math
from pygame.locals import *
flags = FULLSCREEN | DOUBLEBUF


window_sz = 1500
window = window_sz


def window_blit(self):
    self.rect.x = self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
    self.rect.y = self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)
    new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_width()*(window/window_sz)))
    new_surface = new_surface.convert_alpha() 
    self.rect = new_surface.get_rect(topleft = (self.rect.x,self.rect.y))
    screen.blit(new_surface,self.rect)

def traitrandomise(gene, extremity, minamm, maxamm):
    NA = True
    while NA:
        change = random.uniform(-1*extremity,extremity)
        if not gene + change < minamm and not gene + change > maxamm:
            NA = False
    gene += change
    return gene
    
    
def vectorcomponent(angle, magnitude, XorY):
    if XorY == "y":
        angle -= 90
        if angle < 0:
            angle += 360
    dis = math.cos(math.radians(angle)) * magnitude
    return dis

def boundarycheck(Cb):
    if Cb.absX < 0:
        if Cb.angle >= 90 and Cb.angle <= 180:
            dif = 180 - Cb.angle
            Cb.angle = dif
            #print("DownLeft")
        elif Cb.angle >= 180 and Cb.angle <= 270:
            dif = Cb.angle - 180
            Cb.angle = 360 - dif
            #print("UpLeft")
    if Cb.absX > (window_sz - Cb.size/2):
        if Cb.angle >= 270 and Cb.angle <= 360:
            dif = 360 - Cb.angle
            Cb.angle = 180 + dif
            #print("UpRight")
        elif Cb.angle >= 0 and Cb.angle <= 90:
            Cb.angle = 180 - Cb.angle
            #print("DownRight")
    if Cb.absY < 0:
        if Cb.angle >= 180 and Cb.angle <= 270:
            dif = 270 - Cb.angle
            Cb.angle = 90 + dif
            #print("UpLeft")
        elif Cb.angle >= 270 and Cb.angle <= 360:
            dif = 360 - Cb.angle
            Cb.angle = dif
            #print("UpRight")
    if Cb.absY > (window_sz - Cb.size/2):
        if Cb.angle >= 0 and Cb.angle <= 90:
            Cb.angle = 360 - Cb.angle
            #print("DownRight")
        elif Cb.angle >= 90 and Cb.angle <= 180:
            dif = 180 - Cb.angle
            Cb.angle = 180 + dif
            #print("DownLeft")

def angleturn(cell,pellet):
    xdis = cell.rect.x - pellet.rect.x
    ydis = cell.rect.y - pellet.rect.y
    if not xdis:
        if ydis >= 0:
            Angle = 270
        else:
            Angle = 90
    else:
        Angle = math.degrees(math.atan(ydis/xdis))
    if xdis <= 0 and ydis <= 0:
        Angle = 0 + Angle
        #print("UpLeft")
    elif xdis <= 0 and ydis >= 0:
        Angle = 360 + Angle
        #print("DownLeft")
    elif xdis >= 0 and ydis >= 0:
        Angle = 180 + Angle
        #print("DownRight")
    elif xdis >= 0 and ydis <= 0:
        Angle = 180 + Angle
        #print("UpRight")
    return Angle
    
    
class BackGround:
    def __init__(self, absX, absY, rect, surf):
        self.rect = rect
        self.surf = surf
        self.absX = absX
        self.absY = absY

class Cell:
    def __init__(self, absX, absY, rect, surf, angle, speed, vision, nutrition, colour, size, split_energy, energy, health, turn_range, split_time, move_time, move_timer, eat_timer):
        self.all = f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRect: {rect} \nSurface: {surf} \nAngle: {angle} \nSpeed: {speed} \nVision: {vision} \nColour: {colour} \nSize: {size} \nSplit_Energy: {split_energy} \nTurn_Range: {turn_range} \nSplit_Time: {split_time} \nMove_Time: {move_time}\nNutrition: {nutrition}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        self.rect = rect
        self.surf = surf
        self.vision = vision
        self.nutrition = nutrition
        self.colour = colour
        self.angle = angle
        self.speed = speed
        self.size = size
        self.health = health
        self.split_energy = split_energy
        self.energy = energy
        self.turn_range = turn_range
        self.split_time = split_time
        self.move_time = move_time
        self.move_timer = move_timer
        self.eat_timer = eat_timer
        self.absX = absX
        self.absY = absY


class Pellet:
    def __init__(self, absX, absY, surf, rect, size):
        self.rect = rect
        self.surf = surf
        self.size = size
        self.absX = absX
        self.absY = absY
class Bud:
    def __init__(self, absX, absY, surf, rect, size):
        self.rect = rect
        self.surf = surf
        self.size = size
        self.absX = absX
        self.absY = absY
class Meat:
    def __init__(self, absX, absY, surf, rect, size, rot):
        self.rect = rect
        self.surf = surf
        self.size = size
        self.absX = absX
        self.absY = absY
        self.rot = rot

while True:
    pygame.init()
    screen = pygame.display.set_mode((2560,1440), flags)
    screen.set_alpha(None)
    pygame.display.set_caption("Cell Evolution")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None ,20)
    text = font.render("Info",True,"White")
    
    void = pygame.Surface((2560,1440))
    bg = pygame.Surface((window_sz,window_sz))
    bg.fill([10,10,10])
    bg_r = bg.get_rect(topleft = (0,0))
    background = BackGround(0, 0, bg_r, bg)
    
    pellet = pygame.Surface((2,2))
    pellet.fill("White")
    pelletR = pellet.get_rect(center = (400,400))
    pellet_L = [Pellet(400,400,pellet, pelletR, 2)]
    pellettimer = 1
    bud = pygame.Surface((8,8))
    bud.fill("Dark Green")
    budR = bud.get_rect(center = (900,200))
    bud_L = [Bud(900,200,bud, budR, 8)]
    budtimer = 1
    meat = pygame.Surface((5,5))
    meat.fill("Dark Red")
    meatR = meat.get_rect(center = (200,200))
    meat_L = [Meat(300,300,meat, meatR, 5, 0)]
    meattimer = 1
    
    
    cell = pygame.Surface((12,12))
    cell.fill((200,200,200))
    cellR = cell.get_rect(center = (300,300))
    cell_L = []
    c1 = Cell(300, 300, cell.get_rect(center = (300,300)), cell, 45, 3, 60, 5, [255,255,255], 12, 10, 100, 12, 90, 2, 5, 5, 0)
    cell_L.append(c1)
    
    tick = 60
    global_timer = 0
    
    pause = 1
    window = window_sz
    windowchange = 0
    center_xdis = 0
    center_ydis = 0
    center_xchange = 0
    center_ychange = 0
    
    play = True
    selectedmap = "circle2"
    while play:
        for event in pygame.event.get():
            pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN])
            mp = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for C in cell_L:
                    if C.rect.collidepoint(event.pos):
                        print(C.all)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_o:
                    windowchange = 0
                if event.key == pygame.K_i:
                    windowchange = 0
                if event.key == pygame.K_w:
                    center_ychange = 0
                if event.key == pygame.K_s:
                    center_ychange = 0 
                if event.key == pygame.K_a:
                    center_xchange = 0
                if event.key == pygame.K_d:
                    center_xchange = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    play = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_v:
                    window = window_sz
                    center_ydis = 0
                    center_xchange = 0
                    center_xdis = 0
                    center_ychange = 0
                if event.key == pygame.K_o:
                    if window - 100 > 0:
                        windowchange = -400
                if event.key == pygame.K_i:
                    windowchange = 400
                if event.key == pygame.K_w:
                    center_ychange = 200
                if event.key == pygame.K_s:
                    center_ychange = -200
                if event.key == pygame.K_a:
                    center_xchange = 200
                if event.key == pygame.K_d:
                    center_xchange = -200
                if event.key == pygame.K_SPACE:
                    pause *= -1
                    while pause == -1:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                for C in cell_L:
                                    if C.rect.collidepoint(event.pos):
                                        print(C.all)
                    
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    pause *= -1
                                if event.key == pygame.K_r:
                                    play = False
        screen.blit(void,(0,0))
        window_blit(background)
        center_xdis += center_xchange/tick
        center_ydis += center_ychange/tick
        if window < 100:
            if windowchange < 0:
                windowchange = 0
        window += windowchange/tick
        for C in cell_L:
            if C.energy < 2:
                k = 1/2
            else:
                k = 1
            C.absX += (vectorcomponent(C.angle, C.speed, "x"))*k
            C.absY += (vectorcomponent(C.angle, C.speed, "y"))*k
            window_blit(C)
            if C.eat_timer <= 0:
                for P in pellet_L:
                        if math.sqrt((P.absX - C.absX)**2 + (P.absY - C.absY)**2) <= 15:
                            C.eat_timer = 0
                            enplus = 10 - abs(5 - C.nutrition)
                            if C.energy + enplus >= C.size:
                                C.energy = C.size
                            else:
                                C.energy += enplus
                            pellet_L.remove(P)
                for M in meat_L:
                        if math.sqrt((M.absX - C.absX)**2 + (M.absY - C.absY)**2) <= 10:
                            C.eat_timer = 0.2
                            enplus = (10 - C.nutrition)*2
                            if C.energy + enplus >= C.size:
                                C.energy = C.size
                            else:
                                C.energy += enplus
                            meat_L.remove(M)
                if C.nutrition <= 4 and C.split_time <= 4:
                    for Ci in cell_L:
                            if math.sqrt((Ci.absX - C.absX)**2 + (Ci.absY - C.absY)**2) <= 20 and Ci != C:
                                dmg = C.nutrition**-1 + (C.speed/Ci.speed) + (C.size/Ci.size)
                                Ci.health -= dmg*2
                                enplus = (10 - C.nutrition)*2
                                if Ci.health < 0:
                                    if C.energy + enplus >= C.size:
                                        C.energy = C.size
                                    else:
                                        C.energy += enplus
                                    cell_L.remove(Ci)
                                else:
                                    C.eat_timer = 0.5
                for B in bud_L:
                        if math.sqrt((B.absX - C.absX)**2 + (B.absY - C.absY)**2) <= 10:
                            enplus = C.nutrition/2
                            if C.energy + enplus >= C.size:
                                C.energy = C.size
                            else:
                                C.energy += enplus
                            B.size -= 1
                            if B.size <= 0:
                                bud_L.remove(B)
                            else:
                                C.eat_timer = 2.5
            if C.energy >= C.split_energy and C.split_time <= 0:
                C.energy /= 2
                n_ang = C.angle - 180
                if n_ang < 0:
                    n_ang += 360
                n_sz = traitrandomise(C.size,1,2,20)
                n_cell = pygame.Surface((n_sz,n_sz))
                n_spd = traitrandomise(C.speed,0.5,0.5,10)
                n_mt = traitrandomise(C.move_time,1,0,100)
                n_tr = traitrandomise(C.turn_range,15,0,360)
                n_tr //= 1
                n_se = traitrandomise(C.split_energy,1.5,n_sz//5,n_sz-1)
                n_v = traitrandomise(C.vision,15,0,700)
                n_nu = traitrandomise(C.nutrition,0.5,0,10)
                if n_nu >= 5:
                    n_r = 50
                else:
                    n_r = 250 - (n_nu*40)
                if n_nu <= 5:
                    n_g = 50
                else:
                    n_g = 50 + ((n_nu - 5)*40)
                n_b = 250 - (abs(5-n_nu)*40)
                n_cell.fill((n_r,n_g,n_b))
                cell_L.append(Cell(C.absX, C.absY, n_cell.get_rect(center = (C.rect.x,C.rect.y)), n_cell, n_ang, n_spd, n_v, n_nu, [n_r,n_g,n_b], n_sz, n_se, C.energy/2, n_sz, n_tr, 1, n_mt, n_mt, 0))
                C.split_time = 5
            inrange = []
            for P in pellet_L:
                if math.sqrt((P.absX - C.absX)**2 + (P.absY - C.absY)**2) <= C.vision:
                    inrange.append(math.sqrt((P.absX - C.absX)**2 + (P.absY - C.absY)**2))
            if C.nutrition >= 4:
                for B in bud_L:
                    if math.sqrt((B.absX - C.absX)**2 + (B.absY - C.absY)**2) <= C.vision:
                        inrange.append(math.sqrt((B.absX - C.absX)**2 + (B.absY - C.absY)**2))
            if C.nutrition <= 6:
                for M in meat_L:
                    if math.sqrt((M.absX - C.absX)**2 + (M.absY - C.absY)**2) <= C.vision:
                        inrange.append(math.sqrt((M.absX - C.absX)**2 + (M.absY - C.absY)**2))
            if C.nutrition <= 4:
                for Ci in cell_L:
                    if math.sqrt((Ci.absX - C.absX)**2 + (Ci.absY - C.absY)**2) <= C.vision and Ci != C and C.split_time <= 0:
                        inrange.append(math.sqrt((Ci.absX - C.absX)**2 + (Ci.absY - C.absY)**2))
            if len(inrange) > 0:
                dspl = min(inrange)
                found = False
                for ppl in pellet_L:
                    if math.sqrt((ppl.absX - C.absX)**2 + (ppl.absY - C.absY)**2) == dspl:
                        focus = ppl
                        found = True
                if not found:
                    for ppl in bud_L:
                        if math.sqrt((ppl.absX - C.absX)**2 + (ppl.absY - C.absY)**2) == dspl:
                            focus = ppl
                            found = True
                if not found:
                    for ppl in meat_L:
                        if math.sqrt((ppl.absX - C.absX)**2 + (ppl.absY - C.absY)**2) == dspl:
                            focus = ppl
                            found = True
                if not found:
                    for ppl in cell_L:
                        if math.sqrt((ppl.absX - C.absX)**2 + (ppl.absY - C.absY)**2) == dspl:
                            focus = ppl
                            found = True
                            C.absX += (vectorcomponent(C.angle, C.speed, "x"))*k
                            C.absY += (vectorcomponent(C.angle, C.speed, "y"))*k
                C.angle = angleturn(C,focus)
                C.angle //= 1
            if C.split_time > 0:
                C.split_time -= 1/tick
            if C.eat_timer > 0:
                C.eat_timer -= 1/tick
            if C.move_timer > 0:
                C.move_timer -= 1/tick
            else:
                C.angle = random.randint(C.angle - C.turn_range,C.angle + C.turn_range)
                C.move_timer = C.move_time
                if C.angle > 360:
                    C.angle -= 360
                elif C.angle < 0:
                    C.angle += 360
            if C.energy <= 0:
                C.health -= 3/tick
                if C.nutrition >= 7 and C.eat_timer > 0:
                    C.energy -= ((C.speed*C.size/(96))/tick + (C.size/(65))/tick + (C.vision/(150))/tick)/50
                else:
                    C.energy -= (C.speed*C.size/(96))/tick + (C.size/(65))/tick + (C.vision/(150))/tick
            else:
                if C.nutrition >= 7 and C.eat_timer > 0:
                    C.energy -= ((C.speed*C.size/(48))/tick + (C.size/(48))/tick + (C.vision/(200))/tick)/50
                else:
                    C.energy -= (C.speed*C.size/(48))/tick + (C.size/(48))/tick + (C.vision/(200))/tick
            if C.health <= 0:
                meat_L.append(Meat(C.absX, C.absY, meat, meat.get_rect(center = (C.rect.x,C.rect.y)),5,0))
                cell_L.remove(C)
            boundarycheck(C)
        for P in pellet_L:
            window_blit(P)
        for B in bud_L:
            window_blit(B)
        for M in meat_L:
            window_blit(M)
            M.rot += 1/tick
            if M.rot > 20:
                meat_L.remove(M)
        av_sz = 0
        av_spd = 0
        av_mt = 0
        av_tr = 0
        av_e = 0
        av_se = 0
        av_v = 0
        av_nu = 0
        herbi = 0
        omni = 0
        carni = 0
        for x in cell_L:
            av_sz += x.size
            av_spd += x.speed
            av_mt += x.move_time
            av_tr += x.turn_range
            av_e += x.energy
            av_se += x.split_energy
            av_v += x.vision
            av_nu += x.nutrition
            if x.nutrition <= 4:
                carni += 1
            elif x.nutrition >= 6:
                herbi += 1
            else:
                omni += 1
        if len(cell_L):
            av_sz /= len(cell_L)
            av_spd /= len(cell_L)
            av_mt /= len(cell_L)
            av_tr /= len(cell_L)
            av_e /= len(cell_L)
            av_se /= len(cell_L) 
            av_v /= len(cell_L)
            av_nu /= len(cell_L)
            alive = len(cell_L)
        text = font.render(f"Time = {int(global_timer//1)}",True,"White")
        screen.blit(text,(0,0))
        text = font.render(f"Cells Alive: {alive}",True,"White")
        screen.blit(text,(0,20))
        text = font.render(f"Average Speed: {av_spd}",True,"White")
        screen.blit(text,(0,40))
        text = font.render(f"Average Size: {av_sz}",True,"White")
        screen.blit(text,(0,60))
        text = font.render(f"Average Move Time: {av_mt} / Average Turn Range: {av_tr}",True,"White")
        screen.blit(text,(0,80))
        text = font.render(f"Average Energy: {av_e}",True,"White")
        screen.blit(text,(0,100))
        text = font.render(f"Average Split Energy: {av_se}",True,"White")
        screen.blit(text,(0,120))
        text = font.render(f"Average Vision Range: {av_v}",True,"White")
        screen.blit(text,(0,140))
        text = font.render(f"Average Nutrition: {av_nu} (H:{herbi},O:{omni},C:{carni})",True,"White")
        screen.blit(text,(0,160))
        #print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTime = {int(global_timer//1)}\nCells Alive: {alive}   ({herbi},{omni},{carni})\nAverage Speed: {av_spd}\nAverage Size: {av_sz}\nAverage Move Time: {av_mt}\nAverage Turn Range: {av_tr}\nAverage Energy: {av_e}\nAverage Split Energy: {av_se}\nAverage Vision Range: {av_v}\nAverage Nutrition: {av_nu}\n\n\n\n\n\n\n\n\n\n\n\n")
        if selectedmap == "split":
            if global_timer == 0:
                for i in range(window_sz//800 * 40):
                    n_x = random.randint(10,window_sz-10)
                    n_y = random.randint(10,window_sz-10)
                    pellet_L.append(Pellet(n_x, n_y, pellet, pellet.get_rect(center = (n_x,n_y)),2))
            if pellettimer < 0:
                pellettimer = 0.3
                n_x = random.randint(10,window_sz-10)
                n_y = random.randint(10,window_sz-10)
                pellet_L.append(Pellet(n_x, n_y, pellet, pellet.get_rect(center = (n_x,n_y)),2))
            else:
                pellettimer -= 1/tick
            if budtimer < 0 and len(bud_L) < 100 and global_timer >= 20:
                n_x = random.randint(-200,200)
                n_y = random.randint(0,window_sz)
                bud_L.append(Bud(1000 + n_x,n_y, bud, bud.get_rect(center = (n_x,n_y)), 8))
                budtimer = 0.1
            else:
                budtimer -= 1/tick
        elif selectedmap == "random":
            if global_timer == 0:
                for i in range(window_sz//800 * 40):
                    n_x = random.randint(10,window_sz-10)
                    n_y = random.randint(10,window_sz-10)
                    pellet_L.append(Pellet(n_x, n_y, pellet, pellet.get_rect(center = (n_x,n_y)),2))
            if pellettimer < 0:
                pellettimer = 0.3
                n_x = random.randint(10,window_sz-10)
                n_y = random.randint(10,window_sz-10)
                pellet_L.append(Pellet(n_x, n_y, pellet, pellet.get_rect(center = (n_x,n_y)),2))
            else:
                pellettimer -= 1/tick
            if budtimer < 0 and len(bud_L) < 40 and global_timer >= 20:
                n_x = random.randint(10,window_sz-10)
                n_y = random.randint(10,window_sz-10)
                bud_L.append(Bud(n_x,n_y, bud, bud.get_rect(center = (n_x,n_y)), 8))
                budtimer = 0.1
            else:
                budtimer -= 1/tick
        elif selectedmap == "circle1":
            if global_timer == 0:
                for i in range(100):
                    circular = False
                    while not circular:
                        n_x = random.randint(100,window_sz-100)
                        n_y = random.randint(100,window_sz-100)
                        if math.sqrt((n_x-(window_sz/2))**2 + (n_y-(window_sz/2))**2) <= window_sz-200:
                            pellet_L.append(Pellet(n_x, n_y, pellet, pellet.get_rect(center = (n_x,n_y)),2))
                            circular = True
                        else:
                            circular = False
            if pellettimer < 0:
                pellettimer = 0.3
                circular = False
                while not circular:
                    n_x = random.randint(100,window_sz-100)
                    n_y = random.randint(100,window_sz-100)
                    if math.sqrt((n_x-(window_sz/2))**2 + (n_y-(window_sz/2))**2) <= window_sz-200:
                        pellet_L.append(Pellet(n_x, n_y, pellet, pellet.get_rect(center = (n_x,n_y)),2))
                        circular = True
                    else:
                        circular = False
            else:
                pellettimer -= 1/tick
            if budtimer < 0 and len(bud_L) < 100 and global_timer >= 20:
                circular = False
                while not circular:
                    print("here")
                    n_x = random.randint(500,window_sz-500)
                    n_y = random.randint(500,window_sz-500)
                    if math.sqrt((n_x-(window_sz/2))**2 + (n_y-(window_sz/2))**2) <= window_sz-500:
                        bud_L.append(Bud(n_x,n_y, bud, bud.get_rect(center = (n_x,n_y)), 8))
                        circular = True
                    else:
                        circular = False
                budtimer = 0.1
            else:
                budtimer -= 1/tick
        elif selectedmap == "circle2":
            if global_timer == 0:
                for i in range(100):
                    circular = False
                    while not circular:
                        n_x = random.randint(300,window_sz-300)
                        n_y = random.randint(300,window_sz-300)
                        if math.sqrt((n_x-(window_sz/2))**2 + (n_y-(window_sz/2))**2) <= window_sz-300:
                            pellet_L.append(Pellet(n_x, n_y, pellet, pellet.get_rect(center = (n_x,n_y)),2))
                            circular = True
                        else:
                            circular = False
            if pellettimer < 0:
                pellettimer = 0.3
                circular = False
                while not circular:
                    n_x = random.randint(100,window_sz-100)
                    n_y = random.randint(100,window_sz-100)
                    if math.sqrt((n_x-(window_sz/2))**2 + (n_y-(window_sz/2))**2) <= 400:
                        pellet_L.append(Pellet(n_x, n_y, pellet, pellet.get_rect(center = (n_x,n_y)),2))
                        circular = True
                    else:
                        circular = False
            else:
                pellettimer -= 1/tick
            if budtimer < 0 and len(bud_L) < 100 and global_timer >= 20:
                circular = False
                while not circular:
                    print(n_x,n_y)
                    n_x = random.randint(200,window_sz-200)
                    n_y = random.randint(200,window_sz-200)
                    if math.sqrt((n_x-(window_sz/2))**2 + (n_y-(window_sz/2))**2) <= 600 and math.sqrt((n_x-(window_sz/2))**2 + (n_y-(window_sz/2))**2) >= 400:
                        bud_L.append(Bud(n_x,n_y, bud, bud.get_rect(center = (n_x,n_y)), 8))
                        circular = True
                    else:
                        circular = False
                budtimer = 0.1
            else:
                budtimer -= 1/tick
                        
        if global_timer >= 30:
            try:
                cell_L.remove(c1)
            except:
                pass
        global_timer += 1/tick
        pygame.display.update()
        clock.tick(tick)
