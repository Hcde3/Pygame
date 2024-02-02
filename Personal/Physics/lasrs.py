import pygame
import math
import plotly.express as px
import pandas as pd
import random

class Object(pygame.sprite.Sprite):
    def __init__(self, absX, absY, rect, surf, mass, velocity, fixed):
        pygame.sprite.Sprite.__init__(self)
        self.absX = absX
        self.absY = absY
        self.rect = rect
        self.surf = surf
        self.mass = mass
        self.velocity = velocity
        self.fixed = fixed
        self.center = (absX + (surf.get_width()/2),absY + (surf.get_height()/2))
        self.attached = False
        self.angle = 0
        self.angled_surf = surf
        self.mask = pygame.mask.from_surface(self.angled_surf)
        
class Laser():
    def __init__(self,source,slope):
        self.source = source
        self.slope = slope
        self.obstruction = (400,400)
        self.rays = [[source,slope,(400,400)]]
        # [source,(rise,run),past bounce]
        
def window_blit(self):
    self.rect.x = self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
    self.rect.y = self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)
    new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
    new_surface = new_surface.convert_alpha()
    self.rect = new_surface.get_rect(center = (self.rect.x,self.rect.y))
    screen.blit(new_surface,self.rect)
    

pygame.init()
window_sz = 800
window = window_sz
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Physics Lab")
clock = pygame.time.Clock()
square = pygame.image.load("Air.png").convert_alpha()
objects = [Object(200,200,square.get_rect(center = (200,200)),square,10,(0,0),False)]
objects[0].angle = 0
lasers = [Laser((400,400),(1,-1))]
mp = (0,0)
center_xdis = 0
center_ydis = 0
void = pygame.Surface((800,800))
holding = False
t = 0
while True:
    screen.blit(void,(0,0))
    temp = mp
    mp = pygame.mouse.get_pos()
    mp_acc = (mp[0]-temp[0],mp[1]-temp[1])
    screen.blit(void,(0,0))
    void.fill("Black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                #df = pd.DataFrame(dict(
                #    x = times,
                #    y = heights
                #))
                #df = df.sort_values(by="x")
                #fig = px.line(df, x="x", y="y", title="Harmonic Motion") 
                #fig.show()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for O in objects:
                if not holding and O.rect.collidepoint(mp):
                    holding = O
        if event.type == pygame.MOUSEBUTTONUP:
             holding = False
    if holding:
        holding.absX = mp[0]
        holding.absY = mp[1]
        holding.velocity = mp_acc
    for O in objects:
        window_blit(O)
        forces = []
        #if O == objects[1]: forces.append((0,1,0,25))
        xmoments = 0
        ymoments = 0
        for F in forces:
            if F[2] != 0:
                xmoments += (F[2]*F[0])/O.mass
            if F[3] != 0:
                ymoments += (F[3]*F[1])/O.mass
        O.angle += ymoments
        #if O.angle > 360: O.angle -= 360
        O.surf = pygame.transform.rotate(square,O.angle)
        for Oi in objects:
            if O != Oi:
                other_objects =[]
                for oo in objects:
                    if oo != O:
                        other_objects.append(oo)
                if pygame.sprite.spritecollide(O, other_objects, False, pygame.sprite.collide_mask):
                    print(t)
    for L in lasers:
        for i, R in enumerate(L.rays):
            reflected = False
            
            for O in objects:
                for u in range(400):
                    if O.rect.collidepoint((R[0][0] + (R[1][0]*u),R[0][1] + (R[1][1]*u))) and (R[0][0] + (R[1][0]*u),R[0][1] + (R[1][1]*u)) != R[0]:
                        if reflected:
                            if math.sqrt((reflected[0] - R[0][0])**2 + (reflected[1] - R[0][1])**2) > math.sqrt((R[0][0] + (R[1][0]*u) - R[0][0])**2 + (R[0][1] + (R[1][1]*u) - R[0][1])**2) and math.sqrt(((R[0][0] + 50) - R[0][0])**2 + ((R[0][1] + 50) - R[0][1])**2) < math.sqrt((R[0][0] + (R[1][0]*u) - R[0][0])**2 + (R[0][1] + (R[1][1]*u) - R[0][1])**2):
                                reflected = (R[0][0] + (R[1][0]*u),R[0][1] + (R[1][1]*u))
                                if abs(reflected[0] - O.absX) > abs(reflected[1] - O.absY):
                                    bounce = "top"
                                else:
                                    bounce = "side"
                                R[2] = (R[1][0]*u,R[1][1]*u)
                        else:
                            reflected = (R[0][0] + (R[1][0]*u),R[0][1] + (R[1][1]*u))
                            if abs(reflected[0] - O.absX) > abs(reflected[1] - O.absY):
                                    bounce = "top"
                            else:
                                    bounce = "side"
            if reflected:
                try:
                    L.rays[i+1]
                    if L.rays[i+1][0] != reflected:
                        if bounce == "side":
                            L.rays[i+1] = [(reflected[0],reflected[1]),(R[1][0]*-1,R[1][1]),(400,400)]
                        if bounce == "top":
                            L.rays[i+1] = [(reflected[0],reflected[1]),(R[1][0],R[1][1]*-1),(400,400)]
                except:
                    if bounce == "side":
                        L.rays.append([(reflected[0],reflected[1]),(R[1][0]*-1,R[1][1]),(400,400)])
                    if bounce == "top":
                        L.rays.append([(reflected[0],reflected[1]),(R[1][0],R[1][1]*-1),(400,400)])
                pygame.draw.line(void,"Yellow",(R[0][0],R[0][1]),reflected,5)
            else:
                pygame.draw.line(void,"Yellow",(R[0][0],R[0][1]),(R[0][0] + (R[1][0]*400),R[0][1] + (R[1][1]*400)),5)
                new_rays = []
                for i1, r1 in enumerate(L.rays):
                    if i1 <= i:
                        new_rays.append(r1)
                L.rays = new_rays        
    t += 1
    pygame.display.update()
    clock.tick(60)
    
    

    
