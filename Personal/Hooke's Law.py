import pygame
import math

def window_blit(self):
    self.rect.x = self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
    self.rect.y = self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)
    new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
    new_surface = new_surface.convert_alpha()
    self.rect = new_surface.get_rect(topleft = (self.rect.x,self.rect.y))
    screen.blit(new_surface,self.rect)
    
def hookeslaw(point,center,constant):
    dis = math.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2)
    Force = -1*(constant*dis)
    return Force

def vectorcomponent(angle, magnitude, XorY):
    if XorY == "y":
        angle -= 90
        if angle < 0:
            angle += 360
    dis = math.cos(math.radians(angle)) * magnitude
    return dis

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
        self.center = (absX + (surf.get_width()/2),absY + (surf.get_height()/2))
        self.rotation = "up"
        
pygame.init()
window_sz = 800
window = window_sz
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Hooke's Law")
clock = pygame.time.Clock()
square = pygame.Surface((100,100))
square.fill("Blue")
void = pygame.Surface((800,800))
objects = [Object(350,350,square.get_rect(topleft = (100,100)),square,10,(0,0),False)]
center_xdis = 0
center_ydis = 0
while True:
    screen.blit(void,(0,0))
    for O in objects:
        window_blit(O)
        forces = [(0,(0.16*O.mass))]
        forces.append((hookeslaw((400,0),(O.absX,O.absY),0.01),hookeslaw((400,0),(O.absX,O.absY),0.01)))
        if not O.fixed:
            for F in forces:
                O.velocity = (O.velocity[0] + (F[0]/O.mass),O.velocity[1] + (F[1]/O.mass))
        O.absX += O.velocity[0]
        O.absY += O.velocity[1]
    pygame.display.update()
    clock.tick(60)
    
    
