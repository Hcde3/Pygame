import pygame
import math
import random

def window_blit(self):
    self.rect.x = self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
    self.rect.y = self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)
    new_surface = pygame.transform.scale(self.surf, (self.radius*(window/window_sz), self.radius*(window/window_sz)))
    new_surface = new_surface.convert_alpha()
    self.rect = new_surface.get_rect(center = (self.rect.x,self.rect.y))
    if new_surface.get_height() < 0.5: new_surface = minor_point
    if self.rect.x > 0 and self.rect.x < window_sz and self.rect.y > 0 and self.rect.y < window_sz: screen.blit(new_surface,self.rect)

def vectorcomponent(angle, magnitude, XorY):
    if XorY == "y":
        angle -= 90
        if angle < 0:
            angle += 360
    dis = math.cos(math.radians(angle)) * magnitude
    return dis

def angleturn(o1,o2):
    xdis = o1.center[0] - o2.center[0]
    ydis = o1.center[1] - o2.center[1]
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

def Gravity(M,m,d):
    Force = (M*m*(6.7*(10**-11)))/(d**2)
    return Force

def dis(o1,o2):
    dis = math.sqrt((o1.center[0]-o2.center[0])**2 + (o1.center[1] - o2.center[1])**2)
    return dis

class Body:
    def __init__(self, absX, absY, rect, surf, mass, velocity, radius):
        self.absX = absX
        self.absY = absY
        self.rect = rect
        self.surf = surf
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.center = (absX + (surf.get_width()/2),absY + (surf.get_height()/2))

pygame.init()
void = pygame.Surface((1000,1000))
window_sz = 1000
window = 0.0007
center_xdis = 0
center_ydis = 0
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Solar Transit")
clock = pygame.time.Clock()
tick_freq = 600
circle = pygame.image.load("Body.png").convert_alpha()
circle2 = pygame.image.load("Body2.png").convert_alpha()
circle3 = pygame.image.load("Body3.png").convert_alpha()
point = pygame.image.load("Point.png").convert_alpha()
minor_point = pygame.image.load("Minor_Point.png").convert_alpha()
sattelite = pygame.image.load("Sattelite.png").convert_alpha()
celestials = [Body(0,0,circle2.get_rect(center = (0,0)),circle2,6*(10**24),(0,29846),6.4*(10**6)),Body(384000000,0,circle.get_rect(center = (0,0)),circle,7.34*(10**22),(0,1056+29846),1.74*(10**6)),Body(1.496*(10**11),0,circle3.get_rect(center = (0,0)),circle3,1.989*(10**30),(0,0),6.95*(10**8)),Body(42360843,0,sattelite.get_rect(center = (0,0)),sattelite,1200,(0,29846+3080),10)]
center_ychange = 0
center_xchange = 0
window_change = 0
t = 0
thrust = False
while True:
    mp = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                center_ychange = 700000/window
            if event.key == pygame.K_s:
                center_ychange = -700000/window
            if event.key == pygame.K_a:
                center_xchange = 700000/window
            if event.key == pygame.K_d:
                center_xchange = -700000/window
            if event.key == pygame.K_o:
                window_change = -0.01
            if event.key == pygame.K_i:
                window_change = 0.01
            if event.key == pygame.K_SPACE:
                thrust = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                center_ychange = 0
            if event.key == pygame.K_s:
                center_ychange = 0
            if event.key == pygame.K_a:
                center_xchange = 0
            if event.key == pygame.K_d:
                center_xchange = 0
            if event.key == pygame.K_o:
                window_change = 0
            if event.key == pygame.K_i:
                window_change = 0
    window += window*window_change
    center_xdis += center_xchange/tick_freq
    center_ydis += center_ychange/tick_freq
    screen.blit(void,(0,0))
    center_xdis = -celestials[0].absX
    center_ydis = -celestials[0].absY
    for C in celestials:
        forces = []
        window_blit(C)
        if thrust:
            if C == celestials[3]:
                thrust = False
                forces.append((-3000,3000))
        for Ci in celestials:
            if Ci != C:
                forces.append((vectorcomponent(angleturn(C,Ci),Gravity(Ci.mass,C.mass,dis(C,Ci)),"x"),vectorcomponent(angleturn(C,Ci),Gravity(Ci.mass,C.mass,dis(C,Ci)),"y")))
        for F in forces:
            C.velocity = (C.velocity[0] + (100*F[0]/C.mass),C.velocity[1] + (100*F[1]/C.mass))
        C.absX += 100*C.velocity[0]
        C.absY += 100*C.velocity[1]
        C.center = (C.absX,C.absY)
    pygame.display.update()
    clock.tick(tick_freq)
    t += 1
