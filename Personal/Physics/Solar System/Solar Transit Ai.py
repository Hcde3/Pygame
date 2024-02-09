import pygame
import math
import random

def window_blit(self):
    if self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) < window_sz and self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) > 0 and self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) < window_sz and self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) > 0:
        if self.radius*2*(window/window_sz) > 7:
            new_surface = pygame.transform.scale(self.surf, (self.radius*2*(window/window_sz), self.radius*2*(window/window_sz)))
            new_surface = new_surface.convert_alpha()
            screen.blit(new_surface,(self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) - self.radius*(window/window_sz),self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) - self.radius*(window/window_sz)))
        else:
            screen.blit(minor_point,(self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz),self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)))

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

def abswin_convert(point,choice):
    if choice == "abs":
        new_point = point*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
    elif choice == "win":
        new_point = (point - center_xdis*(window/window_sz) - (window_sz-window)/2)/(window/window_sz)
    return new_point

class Body:
    def __init__(self, absX, absY, surf, mass, velocity, radius, name):
        self.absX = absX
        self.absY = absY
        self.surf = surf
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.center = (absX + (surf.get_width()/2),absY + (surf.get_height()/2))
        self.name = name

pygame.init()
void = pygame.Surface((1000,1000))
window_sz = 1000
window = 0.0007
center_xdis = 0
center_ydis = 0
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Solar Transit")
clock = pygame.time.Clock()
tick_freq = 10000
dig_font = pygame.font.Font("digital-7.ttf",50)
Sol = pygame.image.load("Sol.png").convert_alpha()
Earth = pygame.image.load("Earth.png").convert_alpha()
Luna = pygame.image.load("Luna.png").convert_alpha()
Mercury = pygame.image.load("Mercury.png").convert_alpha()
Venus = pygame.image.load("Venus.png").convert_alpha()
Mars = pygame.image.load("Mars.png").convert_alpha()
Jupiter = pygame.image.load("Jupiter.png").convert_alpha()
Saturn = pygame.image.load("Saturn.png").convert_alpha()
Uranus = pygame.image.load("Uranus.png").convert_alpha()
Neptune = pygame.image.load("Neptune.png").convert_alpha()
Pluto = pygame.image.load("Pluto.png").convert_alpha()
point = pygame.image.load("Point.png").convert_alpha()
minor_point = pygame.image.load("Minor_Point.png").convert_alpha()
sattelite = pygame.image.load("Sattelite.png").convert_alpha()
celestials = [Body(1.496*(10**11),0,Earth,6*10**24,(0,29846),6.4*(10**6),"Earth"),Body(1.496*(10**11) + 384000000,0,Luna,7.34*(10**22),(0,1056+29846),1.74*(10**6),"Moon"),Body(0,0,Sol,1.989*(10**30),(0,0),6.95*(10**8),"Sun")]
celestials_minor = [Body(5.8*10**10,0,Mercury,3.3*10**23,(0,47900),2.43*10**6,"Mercury"),Body(108*10**9,0,Venus,4.87*10**24,(0,35000),6.05*10**6,"Venus"),Body(228*10**9,0,Mars,0.642*10**24,(0,24100),(6792*10**3)/2,"Mars"),Body(778.5*10**9,0,Jupiter,1898*10**24,(0,13100),(142984*10**3)/2,"Jupiter"),Body(1432*10**9,0,Saturn,568*10**24,(0,9700),(120536*10**3)/2,"Saturn"),Body(2867*10**9,0,Uranus,86.8*10**24,(0,6800),(51118*10**3)/2,"Uranus"),Body(4515*10**9,0,Neptune,102*10**24,(0,5400),(49528*10**3)/2,"Neptune"),Body(5906.4*10**9,0,Pluto,0.013*10**24,(0,4700),(2376*10**3)/2,"Pluto")]
celestials.extend(celestials_minor)
asteroids = []
bodies = []
for i in range(100):
    #pass
    position = random.randint(int(2.2*1.5*(10**11)),int(3.2*1.5*(10**11)))
    mass = random.randint(10**12,10**14)
    radius = random.randint(1,530000)
    vel = math.sqrt(((6.7*10**-11)*(1.989*10**30))/position)
    image = random.randint(1,3)
    asteroids.append(Body(position,0,pygame.image.load(f"Asteroid{image}.png").convert_alpha(),mass,(0,vel),radius,f"Asteroid {i + 1}"))
bodies.extend(celestials)
bodies.extend(asteroids)
center_ychange = 0
center_xchange = 0
window_change = 0
t = 0
thrust = False
multiplier = 1000
temp_multi = multiplier
selected = None
while True:
    mp = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            got_new = False
            for c in bodies:
                if math.sqrt((abswin_convert(c.absX,"abs") - mp[0])**2 + (abswin_convert(c.absY,"abs") - mp[1])**2) < 20:
                    selected = c
                    got_new = True
                    break
            if not got_new:
                selected = None
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
                if multiplier:
                    temp_multi = multiplier
                    multiplier = 0
                else:
                    multiplier = temp_multi
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
    #center_xdis = -celestials[0].absX
    #center_ydis = -celestials[0].absY
    if selected:
        text = dig_font.render(selected.name,True,"White")
        screen.blit(text,(0,0))
        center_xdis = -selected.absX
        center_ydis = -selected.absY
    text = dig_font.render(str((t*temp_multi)//(60*60*24)) + " days",True,"White")
    screen.blit(text,(window_sz - 300,0))    
    for B in bodies:
        forces = []
        window_blit(B)
        for C in celestials:
            if C != B:
                forces.append((vectorcomponent(angleturn(B,C),Gravity(C.mass,B.mass,dis(B,C)),"x"),vectorcomponent(angleturn(B,C),Gravity(C.mass,B.mass,dis(B,C)),"y")))
        for F in forces:
            B.velocity = (B.velocity[0] + (multiplier*F[0]/B.mass),B.velocity[1] + (multiplier*F[1]/B.mass))
        B.absX += multiplier*B.velocity[0]
        B.absY += multiplier*B.velocity[1]
        B.center = (B.absX,B.absY)
    pygame.display.update()
    clock.tick(tick_freq)
    if multiplier: t += 1
