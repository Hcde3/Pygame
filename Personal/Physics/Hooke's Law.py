import pygame
import math
import plotly.express as px
import pandas as pd


def window_blit(self):
    self.rect.x = self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
    self.rect.y = self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)
    new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
    new_surface = new_surface.convert_alpha()
    self.rect = new_surface.get_rect(center = (self.rect.x,self.rect.y))
    screen.blit(new_surface,self.rect)
    
def hookeslaw(point,center,constant,original_length,axis):
    dis = math.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2)
    dis = dis - original_length
    Force = constant*dis
    return Force

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
        self.rotation = "up"

mode = input("Circular Motion(1)\nHooke's Law(2)\n")
if mode == "2":
    speed = 0
    radius = 160
    center = 0
    print("Click on square to change position")
if mode == "1":
    center = 400
    mode_dec = input("Set Linear Velocity(1)\nSet Radius(2)\n")
    if mode_dec == "1":
        speed = int(input("Input velocity:   "))
        radius = 10*(speed**2)
    if mode_dec == "2":
        radius = int(input("Input radius:   "))
        speed = math.sqrt(radius/10)
pygame.init()
window_sz = 800
window = window_sz
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Hooke's Law")
clock = pygame.time.Clock()
square = pygame.Surface((50,50))
square.fill("Blue")
pin = pygame.Surface((10,10))
pin.fill("Red")
void = pygame.Surface((800,800))
objects = [Object(400,center+radius,square.get_rect(center = (400,center+radius)),square,10,(speed,0),False),Object(400,center,pin.get_rect(center = (400,center)),pin,0,(0,0),True)]
center_xdis = 0
center_ydis = 0
holding = False
t = 0
times = []
heights = []
k = 0.01
while True:
    for event in pygame.event.get():
            mp = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                df = pd.DataFrame(dict(
                    x = times,
                    y = heights
                ))
                df = df.sort_values(by="x")
                fig = px.line(df, x="x", y="y", title="Harmonic Motion") 
                fig.show()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    objects[0].mass += 1
                if event.key == pygame.K_n:
                    objects[0].mass -= 1
                if event.key == pygame.K_k:
                    k += 0.01
                if event.key == pygame.K_l:
                    k -= 0.01
            if event.type == pygame.MOUSEBUTTONDOWN:
                for O in objects:
                    if not holding and O.rect.collidepoint(mp):
                        holding = O
            if event.type == pygame.MOUSEBUTTONUP:
                holding = False
    if holding:
        holding.absX = mp[0]
        holding.absY = mp[1]
        holding.velocity = (0,0)
    pygame.draw.line(void,"White",objects[0].center,objects[1].center,2)
    screen.blit(void,(0,0))
    void.fill("Black")
    for O in objects:
        window_blit(O)
        if mode == "2": forces = [(0,(0.15*O.mass))]
        if mode == "1": forces = [(0,0)]
        if not O.fixed:
            forces.append((vectorcomponent(angleturn(O,objects[1]),hookeslaw(objects[1].center,O.center,k,100,"x"),"x"),(vectorcomponent(angleturn(O,objects[1]),hookeslaw(objects[1].center,O.center,k,100,"y"),"y"))))
            for F in forces:
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
    
    