import pygame
import math

def g(M,d):
    g = M/(d**2)
    return g

def vectorcomponent(angle, magnitude, XorY):
    if XorY == "y":
        angle -= 90
        if angle < 0:
            angle += 360
    dis = math.cos(math.radians(angle)) * magnitude
    return dis

def dis(o1,o2):
    dis = math.sqrt((o1.rect.x - o2.rect.x)**2 + (o1.rect.y - o2.rect.y)**2)
    return dis

def window_blit(self):
    self.rect.x = self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
    self.rect.y = self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)
    new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
    new_surface = new_surface.convert_alpha() 
    self.rect = new_surface.get_rect(topleft = (self.rect.x,self.rect.y))
    screen.blit(new_surface,self.rect)

def angleturn(o1,o2):
    xdis = o1.rect.x - o2.rect.x
    ydis = o1.rect.y - o2.rect.y
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

pygame.init()
window_sz = 800
window = window_sz
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Gravity")
clock = pygame.time.Clock()
void = pygame.Surface((5000,5000))
player = pygame.Surface((20,20))
player.fill("Grey")
playerR = player.get_rect(center = (600,200))
planet1 = pygame.Surface((100,100))
planet1.fill("Dark Blue")
planet1R = planet1.get_rect(center = (200,400))
objects = [Object(600, 200, playerR,player, 50, (0,1), False),Object(200, 400, planet1R,planet1, 1000, (0,0), True)]
center_xdis = 0
center_ydis = 0
while True:
    for event in pygame.event.get():
        mp = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(void,(0,0))
    for O in objects:
        window_blit(O)
        for Oi in objects:
            if Oi != O and not O.fixed:
                O.velocity = (O.velocity[0] + vectorcomponent(angleturn(O,Oi),g(Oi.mass,dis(O,Oi)),"x"),O.velocity[1] + vectorcomponent(angleturn(O,Oi),g(Oi.mass,dis(O,Oi)),"y"))
                O.absX += O.velocity[0]
                O.absY += O.velocity[1]
    pygame.display.update()
    clock.tick(60)