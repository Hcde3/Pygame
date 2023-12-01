import pygame
import random
import math

window_sz = 1300

def traitrandomise(gene, extremity):
    change = random.uniform(-1*extremity,extremity)
    gene += gene*change
    return gene

    
def vectorcomponent(angle, magnitude, XorY):
    if XorY == "y":
        angle -= 90
        if angle < 0:
            angle += 360
    dis = math.cos(math.radians(angle)) * magnitude
    return dis

def boundarycheck(Cb):
    if Cb.rect.x < 0:
        if Cb.angle >= 90 and Cb.angle <= 180:
            dif = 180 - Cb.angle
            Cb.angle = dif
            #print("DownLeft")
        elif Cb.angle >= 180 and Cb.angle <= 270:
            dif = Cb.angle - 180
            Cb.angle = 360 - dif
            #print("UpLeft")
    if Cb.rect.x > (window_sz - Cb.size/2):
        if Cb.angle >= 270 and Cb.angle <= 360:
            dif = 360 - Cb.angle
            Cb.angle = 180 + dif
            #print("UpRight")
        elif Cb.angle >= 0 and Cb.angle <= 90:
            Cb.angle = 180 - Cb.angle
            #print("DownRight")
    if Cb.rect.y < 0:
        if Cb.angle >= 180 and Cb.angle <= 270:
            dif = 270 - Cb.angle
            Cb.angle = 90 + dif
            #print("UpLeft")
        elif Cb.angle >= 270 and Cb.angle <= 360:
            dif = 360 - Cb.angle
            Cb.angle = dif
            #print("UpRight")
    if Cb.rect.y > (window_sz - Cb.size/2):
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
            Angle = 90
        else:
            Angle = 270
    else:
        Angle = math.degrees(math.atan(ydis/xdis))
    if xdis <= 0 and ydis <= 0:
        Angle = 0 + Angle
    elif xdis <= 0 and ydis >= 0:
        Angle = 180 + Angle
    elif xdis >= 0 and ydis >= 0:
        Angle = 180 + Angle
    elif xdis >= 0 and ydis <= 0:
        Angle = 360 + Angle
    return Angle
    
    
            

class Cell:
    def __init__(self, rect, surf, angle, speed, vision, colour, size, split_energy, energy, turn_range, split_time, move_time, move_timer):
        self.all = f"Rect: {rect} \nSurface: {surf} \nAngle: {angle} \nSpeed: {speed} \nVision: {vision} \nColour: {colour} \nSize: {size} \nSplit_Energy: {split_energy} \nTurn_Range: {turn_range} \nSplit_Time: {split_time} \nMove_Time: {move_time}"
        self.rect = rect
        self.surf = surf
        self.vision = vision
        self.colour = colour
        self.angle = angle
        self.speed = speed
        self.size = size
        self.split_energy = split_energy
        self.energy = energy
        self.turn_range = turn_range
        self.split_time = split_time
        self.move_time = move_time
        self.move_timer = move_timer

class Pellet:
    def __init__(self, rect):
        self.rect = rect

while True:
    pygame.init()
    screen = pygame.display.set_mode((window_sz,window_sz))
    pygame.display.set_caption("Cells")
    clock = pygame.time.Clock()
    bg = pygame.Surface((window_sz,window_sz))
    cell = pygame.Surface((12,12))
    cell.fill((200,200,200))
    cellR = cell.get_rect(center = (300,300))
    pellet = pygame.Surface((2,2))
    pellet.fill("White")
    pelletR = pellet.get_rect(center = (400,400))
    pellet_L = [Pellet(pelletR)]
    play = True
    cell_L = []
    c1 = Cell(cell.get_rect(center = (300,300)), cell, 45, 3, 50, [255,255,255], 12, 6, 100, 90, 0, 5, 5)
    cell_L.append(c1)
    tick = 60
    global_timer = 0
    pellettimer = 1
    pause = 1
    while play:
        for event in pygame.event.get():
            mp = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for C in cell_L:
                    if C.rect.collidepoint(event.pos):
                        print(C.all)
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    play = False
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
        screen.blit(bg,(0,0))
        for C in cell_L:
            C.rect.x += vectorcomponent(C.angle, C.speed, "x")
            C.rect.y += vectorcomponent(C.angle, C.speed, "y")
            screen.blit(C.surf,C.rect)
            for P in pellet_L:
                screen.blit(pellet,P.rect)
                if C.rect.colliderect(P.rect):
                    C.energy += 10
                    pellet_L.remove(P)
                    if C.energy >= C.split_energy and C.split_time <= 0:
                        C.energy /= 2
                        n_ang = C.angle - 180
                        if n_ang < 0:
                            n_ang += 360
                        n_sz = traitrandomise(C.size,0.1)
                        n_cell = pygame.Surface((n_sz,n_sz))
                        n_spd = traitrandomise(C.speed,0.1)
                        n_mt = traitrandomise(C.move_time,0.2)
                        n_tr = traitrandomise(C.turn_range,0.2)
                        n_tr //= 1
                        n_se = traitrandomise(C.split_energy,0.2)
                        n_v = traitrandomise(C.vision,0.3)
                        if n_spd <= 2:
                            n_r = 0
                        elif n_spd >= 4:
                            n_r = 255
                        else:
                            n_r = (n_spd - 2)*(255/2)
                        if n_sz <= 8:
                            n_g = 255
                        elif n_sz >= 16:
                            n_g = 0
                        else:
                            n_g = 255 - ((n_sz - 8)*(255/8))
                        if n_sz <= 50:
                            n_b = 0
                        elif n_sz >= 150:
                            n_b = 255
                        else:
                            n_b = (n_sz - 50)*(255/100)
                        n_cell.fill((n_r,n_g,n_b))
                        cell_L.append(Cell(n_cell.get_rect(center = (C.rect.x,C.rect.y)), n_cell, n_ang, n_spd, n_v, [n_r,n_g,n_b], n_sz, n_se, C.energy/2, n_tr, 5, n_mt, n_mt))
                        C.split_time = 5
            inrange = []
            for P in pellet_L:
                if math.sqrt((P.rect.x - C.rect.x)**2 + (P.rect.y - C.rect.y)**2) <= C.vision:
                    inrange.append(math.sqrt((P.rect.x - C.rect.x)**2 + (P.rect.y - C.rect.y)**2))
            if len(inrange) > 0:
                dspl = min(inrange)
                for ppl in pellet_L:
                    if math.sqrt((ppl.rect.x - C.rect.x)**2 + (ppl.rect.y - C.rect.y)**2) == dspl:
                        focus = ppl
                C.angle = angleturn(C,focus)
                C.angle //= 1
            if C.split_time > 0:
                C.split_time -= 1/tick
            if C.move_timer > 0:
                C.move_timer -= 1/tick
            else:
                inrange = []
                for P in pellet_L:
                    if math.sqrt((P.rect.x - C.rect.x)**2 + (P.rect.y - C.rect.y)**2) <= C.vision:
                        inrange.append(math.sqrt((P.rect.x - C.rect.x)**2 + (P.rect.y - C.rect.y)**2))
                if len(inrange) > 0:
                    dspl = min(inrange)
                    for ppl in pellet_L:
                        if math.sqrt((ppl.rect.x - C.rect.x)**2 + (ppl.rect.y - C.rect.y)**2) == dspl:
                            focus = ppl
                    C.angle = angleturn(C,focus)
                    C.angle //= 1
                else:
                    C.angle = random.randint(C.angle - C.turn_range,C.angle + C.turn_range)
                C.move_timer = C.move_time
                if C.angle > 360:
                    C.angle -= 360
                elif C.angle < 0:
                    C.angle += 360
            if C.energy <= 0:
                pellet_L.append(Pellet(pellet.get_rect(center = (C.rect.x,C.rect.y))))
                cell_L.remove(C)
            else:
                C.energy -= (C.speed*C.size/(48))/tick + (C.size/(48))/tick + (C.vision/(200))/tick
            boundarycheck(C) 
        av_sz = 0
        av_spd = 0
        av_mt = 0
        av_tr = 0
        av_e = 0
        av_se = 0
        av_v = 0
        for x in cell_L:
            av_sz += x.size
            av_spd += x.speed
            av_mt += x.move_time
            av_tr += x.turn_range
            av_e += x.energy
            av_se += x.split_energy
            av_v += x.vision
        if len(cell_L):
            av_sz /= len(cell_L)
            av_spd /= len(cell_L)
            av_mt /= len(cell_L)
            av_tr /= len(cell_L)
            av_e /= len(cell_L)
            av_se /= len(cell_L)
            av_v /= len(cell_L)
            alive = len(cell_L)
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCells Alice: {alive}\nAverage Speed: {av_spd}\nAverage Size: {av_sz}\nAverage Move Time: {av_mt}\nAverage Turn Range: {av_tr}\nAverage Energy: {av_e}\nAverage Split Energy: {av_se}\nAverage Vision Range: {av_v}\n\n\n\n\n\n\n\n\n\n\n\n\n")
        if global_timer == 0:
            for i in range(window_sz//800 * 40):
                n_x = random.randint(10,window_sz-10)
                n_y = random.randint(10,window_sz-10)
                pellet_L.append(Pellet(pellet.get_rect(center = (n_x,n_y))))
        if pellettimer < 0:
            pellettimer = window_sz//800 * 1/2
            n_x = random.randint(10,window_sz-10)
            n_y = random.randint(10,window_sz-10)
            pellet_L.append(Pellet(pellet.get_rect(center = (n_x,n_y))))
        else:
            pellettimer -= 1/tick
        global_timer += 1/tick
        pygame.display.update()
        clock.tick(tick)
