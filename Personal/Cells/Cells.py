import pygame
import random
import math

def traitrandomise(gene):
    change = random.uniform(-0.1,0.1)
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
        if Cb.angle > 90 and Cb.angle < 180:
            dif = 180 - Cb.angle
            Cb.angle = dif
            #print("DownLeft")
        elif Cb.angle > 180 and Cb.angle < 270:
            dif = Cb.angle - 180
            Cb.angle = 360 - dif
            #print("UpLeft")
    if Cb.rect.x > (800 - Cb.size/2):
        if Cb.angle > 270 and Cb.angle < 360:
            dif = 360 - Cb.angle
            Cb.angle = 180 + dif
            #print("UpRight")
        elif Cb.angle > 0 and Cb.angle < 90:
            Cb.angle = 180 - Cb.angle
            #print("DownRight")
    if Cb.rect.y < 0:
        if Cb.angle > 180 and Cb.angle < 270:
            dif = 270 - Cb.angle
            Cb.angle = 90 + dif
            #print("UpLeft")
        elif Cb.angle > 270 and Cb.angle < 360:
            dif = 360 - Cb.angle
            Cb.angle = dif
            #print("UpRight")
    if Cb.rect.y > (800 - Cb.size/2):
        if Cb.angle > 0 and Cb.angle < 90:
            Cb.angle = 360 - Cb.angle
            #print("DownRight")
        elif Cb.angle > 90 and Cb.angle < 180:
            dif = 180 - Cb.angle
            Cb.angle = 180 + dif
            #print("DownLeft")
    
            

class Cell:
    def __init__(self, rect, surf, angle, speed, colour, size, energy, turn_range, split_time, move_time, move_timer):
        self.rect = rect
        self.surf = surf
        self.colour = colour
        self.angle = angle
        self.speed = speed
        self.size = size
        self.energy = energy
        self.turn_range = turn_range
        self.split_time = split_time
        self.move_time = move_time
        self.move_timer = move_timer

class Crumb:
    def __init__(self, rect):
        self.rect = rect


pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Cells")
clock = pygame.time.Clock()
bg = pygame.Surface((800,800))
cell = pygame.Surface((12,12))
cell.fill((200,200,200))
cellR = cell.get_rect(center = (300,300))
crumb = pygame.Surface((2,2))
crumb.fill("White")
crumbR = crumb.get_rect(center = (400,400))
crumbL = [Crumb(crumbR)]
play = True
cell_L = []
c1 = Cell(cell.get_rect(center = (300,300)), cell, 45, 3, [200,200,200], 12, 12, 90, 0, 5, 5)
cell_L.append(c1)
tick = 60
crumbtimer = 1
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                pygame.quit()
                exit()
    screen.blit(bg,(0,0))
    for B in cell_L:
        B.rect.x += vectorcomponent(B.angle, B.speed, "x")
        B.rect.y += vectorcomponent(B.angle, B.speed, "y")
        screen.blit(B.surf,B.rect)
        for C in crumbL:
            screen.blit(crumb,C.rect)
            if B.rect.colliderect(C.rect) and B.split_time <= 0:
                n_ang = B.angle - 180
                if n_ang < 0:
                    n_ang += 360
                n_sz = traitrandomise(B.size)
                n_cell = pygame.Surface((n_sz,n_sz))
                NA = True
                while NA:
                    n_r = traitrandomise(B.colour[0])
                    n_g = traitrandomise(B.colour[1])
                    n_b = traitrandomise(B.colour[2])
                    if n_r > 255 or n_g > 255 or n_b > 255:
                        NA = True
                    else:
                        NA = False
                n_cell.fill((n_r,n_g,n_b))
                n_spd = traitrandomise(B.speed)
                n_mt = traitrandomise(B.move_time)
                n_tr = traitrandomise(B.turn_range)
                n_tr //= 1
                cell_L.append(Cell(n_cell.get_rect(center = (B.rect.x,B.rect.y)), n_cell, n_ang, n_spd,[n_r,n_g,n_b], n_sz, B.energy/2, n_tr, 5, n_mt, n_mt))
                B.split_time = 5
                crumbL.remove(C)
        if B.split_time > 0:
            B.split_time -= 1/tick
        if B.move_timer > 0:
            B.move_timer -= 1/tick
        else:
            B.move_timer = B.move_time
            B.angle = random.randint(B.angle - B.turn_range,B.angle + B.turn_range)
        if B.angle > 360:
            B.angle -= 360
        elif B.angle < 0:
            B.angle += 360
        boundarycheck(B)
    av_sz = 0
    av_spd = 0
    av_mt = 0
    av_tr = 0
    for x in cell_L:
        av_sz += x.size
        av_spd += x.speed
        av_mt += x.move_time
        av_tr += x.turn_range
    av_sz /= len(cell_L)
    av_spd /= len(cell_L)
    av_mt /= len(cell_L)
    av_tr /= len(cell_L)
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAverage Speed: {av_spd}\nAverage Size: {av_sz}\nAverage Move Time: {av_mt}\nAverage Turn Range: {av_tr}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    if crumbtimer < 0:
        crumbtimer = 1
        n_x = random.randint(10,790)
        n_y = random.randint(10,790)
        crumbL.append(Crumb(crumb.get_rect(center = (n_x,n_y))))
    else:
        crumbtimer -= 1/tick
    pygame.display.update()
    clock.tick(tick)