import pygame
import math
import plotly.express as px
import pandas as pd
import random


def window_blit(self):
    self.rect.x = self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
    self.rect.y = self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)
    new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
    new_surface = new_surface.convert_alpha()
    self.rect = new_surface.get_rect(center = (self.rect.x,self.rect.y))
    screen.blit(new_surface,self.rect)
    
def hookeslaw(ob,stri):
    dis = math.sqrt((ob.center[0] - stri.center[0])**2 + (ob.center[1] - stri.center[1])**2)
    dis = dis - stri.original_length
    Force = stri.constant*dis
    return Force

def Archimedes(O,L):
    Pressure = L.density*((L.topheight-O.absY))*0.15
    Force = (O.surf.get_width()**2)*Pressure
    Pressure = L.density*((L.topheight-O.absY)+O.surf.get_width())*0.15
    Force -= (O.surf.get_width()**2)*Pressure
    return Force*0.0001

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

def booleanflip(var):
    if var == False:
        var = True
    else:
        var = False
    return var
        
class Object:
    def __init__(self, absX, absY, rect, surf, mass, velocity, fixed):
        self.absX = absX
        self.absY = absY
        self.rect = rect
        self.surf = surf
        self.mass = mass
        self.velocity = velocity
        self.fixed = fixed
        self.center = (absX + (surf.get_width()/2),absY + (surf.get_height()/2))
        self.attached = False
        
class Liquid:
    def __init__(self, topheight, density):
        self.topheight = topheight
        self.density = density
        self.surf = pygame.Surface((800,topheight))
        self.rect = self.surf.get_rect(topleft = (0,800-topheight))

class Floor:
    def __init__(self,height,surf,bounce):
        self.height = height
        self.surf = surf
        self.rect = surf.get_rect(topleft = (0,height))
        self.bounce = bounce
        
class StringPin:
    def __init__(self,center,constant,original_length):
        self.center = center
        self.constant = constant
        self.original_length = original_length
        
#mode = input("Circular Motion(1)\nHooke's Law(2)\n")
mode = "2"
if mode == "2":
    speed = 0
    radius = 160
    center = 0
    print("Click on square to change position")
        
pygame.init()
liquids = [Liquid(100,1)]
liquids[0].surf.fill("Blue")
window_sz = 800
window = window_sz
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Physics Lab")
clock = pygame.time.Clock()
square = pygame.Surface((50,50))
square.fill("White")
square2 = pygame.Surface((50,50))
square2.fill("Blue")
pin = pygame.Surface((10,10))
pin.fill("Red")
void = pygame.Surface((800,800))
objects = [Object(400,center+radius,square.get_rect(center = (400,center+radius)),square,10,(speed,0),False),Object(600,700,square2.get_rect(center = (800,400)),square2,10,(-2,0),False)]
stringpin = StringPin((400,0),0.01,100)
objects[0].attached = True
ground = pygame.Surface((800,800-700))
ground.fill("Dark Green")
floors = [Floor(700,ground,-1.5)]
center_xdis = 0
center_ydis = 0
holding = False
t = 0
times = []
heights = []
k = 0.01
mp = (400,400)
vectors_showing = False
while True:
    temp = mp
    mp = pygame.mouse.get_pos()
    mp_acc = (mp[0]-temp[0],mp[1]-temp[1])
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    objects[0].mass += 1
                if event.key == pygame.K_n:
                    objects[0].mass -= 1
                if event.key == pygame.K_k:
                    stringpin.constant += 0.01
                if event.key == pygame.K_l:
                    if stringpin.constant != 0:
                        stringpin.constant -= 0.01
                if event.key == pygame.K_v:
                    vectors_showing = booleanflip(vectors_showing)
                if event.key == pygame.K_r:
                    new_square = pygame.Surface((50,50))
                    new_square.fill(random.choice(["White","Red","Orange","Yellow","Green","Blue","Dark Blue","Purple","Pink","Grey"]))
                    objects.append(Object(mp[0],mp[1],new_square.get_rect(center = (mp)),new_square,10,(0,0),False))
            if event.type == pygame.MOUSEBUTTONDOWN:
                for O in objects:
                    if not holding and O.rect.collidepoint(mp):
                        holding = O
            if event.type == pygame.MOUSEBUTTONUP:
                holding = False
    if holding:
        holding.absX = mp[0]
        holding.absY = mp[1]
        if vectors_showing: pygame.draw.line(void,"Red",holding.center,(holding.absX + (mp_acc[0]*holding.mass),holding.absY + (mp_acc[1]*holding.mass) ),3)
        holding.velocity = mp_acc
    screen.blit(void,(0,0))
    void.fill("Black")
    print(vectors_showing)
    for L in liquids:
        screen.blit(L.surf,L.rect)
    for O in objects:
        if mode == "2": forces = [(0,0.15*O.mass)]
        if O.attached:
            #stringpin.center = objects[1].center
            if stringpin.constant > 0: screen.blit(pin,(stringpin.center[0]-2.5,stringpin.center[1]-2.5))
            if stringpin.constant > 0: forces.append((vectorcomponent(angleturn(O,stringpin),hookeslaw(O,stringpin),"x"),(vectorcomponent(angleturn(O,stringpin),hookeslaw(O,stringpin),"y"))))
            if stringpin.constant > 0: pygame.draw.line(void,"White",O.center,stringpin.center,2)
        window_blit(O)
        for L in liquids:
            if O.rect.colliderect(L.rect):
                forces.append((0,Archimedes(O,L)))
                forces.append((O.velocity[0]*-0.5,O.velocity[1]*-0.1))
                k = 0
        for F in floors:
            screen.blit(F.surf,F.rect)
            if O.rect.colliderect(F.rect):
                forces.append((O.velocity[0]*O.mass*-0.01,O.velocity[1]*O.mass*F.bounce))
                O.absY = F.height - O.surf.get_height()/2
        for Oi in objects:
            if O.rect.colliderect(Oi.rect) and O != Oi and not Oi.fixed and not O.fixed:
                xf = 0
                yf = 0
                system_force = (O.mass*O.velocity[0]) + (Oi.mass*Oi.velocity[0])
                O.velocity = (0,O.velocity[1])
                if Oi.absX < O.absX and abs(Oi.absX - O.absX) > abs(Oi.absY - O.absY):
                    Oi.absX = O.absX - O.surf.get_width()
                    O.absX = Oi.absX + Oi.surf.get_width()
                elif abs(Oi.absX - O.absX) > abs(Oi.absY - O.absY):
                    Oi.absX = O.absX + O.surf.get_width()
                    O.absX = Oi.absX - Oi.surf.get_width()
                Oi_original_vel = Oi.velocity
                Oi.velocity = ((((3*system_force)/4)/Oi.mass),Oi.velocity[1])
                xf = system_force/4  
                system_force = (O.mass*O.velocity[1]) + (Oi.mass*Oi.velocity[1])
                O.velocity = (O.velocity[0],0)
                Oi.velocity = (Oi.velocity[0],(system_force/2)/Oi.mass)
                if Oi.absY < O.absY and abs(Oi.absX - O.absX) < abs(Oi.absY - O.absY):
                    Oi.absY = O.absY - O.surf.get_height()
                    O.absY = Oi.absY + Oi.surf.get_height()
                elif abs(Oi.absX - O.absX) < abs(Oi.absY - O.absY):
                    Oi.absY = O.absY + O.surf.get_height()
                    O.absY = Oi.absY - Oi.surf.get_height()
                Oi.velocity = (Oi.velocity[0],Oi.velocity[1] + (system_force/4)/Oi.mass)
                if vectors_showing: pygame.draw.line(void,"Red",Oi.center,(Oi.absX + (Oi_original_vel[0] - (Oi.velocity[0]/Oi.mass)*600),Oi.absY + (Oi_original_vel[1] - (Oi.velocity[1])/Oi.mass)*600),3)
                if Oi.rect.collidelist(floors):
                    yf = -system_force/4
                else:
                    yf = system_force/4 
                forces.append((xf,yf))
        if not O.fixed:
            for F in forces:
                if vectors_showing: pygame.draw.line(void,"Red",O.center,(O.absX + (F[0]/O.mass)*600,O.absY + (F[1]/O.mass)*600),3)
                O.velocity = (O.velocity[0] + (F[0]/O.mass),O.velocity[1] + (F[1]/O.mass))
        O.absX += O.velocity[0]
        O.absY += O.velocity[1]
        O.center = (O.absX,O.absY)
    t += 1
    if not t%6:
        times.append(t//6)
        heights.append(round(objects[0].absY))
    pygame.display.update()
    clock.tick(60)
    