import pygame
import math

def g(M,d):
    g = M/(d**2)
    return g

def collideresponse(O,Oi):
    newvel = (0,0)
    if O.absY < Oi.absY:
        # O is above oi
        if O.velocity[1] > 0:
            newvel = (O.velocity[0] + -0.1*O.velocity[0],O.velocity[1] + -1.5*O.velocity[1])
            O.absY = Oi.absY - O.surf.get_height()
    elif O.absY > Oi.absY:
        # O is below Oi
        if O.velocity[1] < 0:
            newvel = (O.velocity[0] + -0.1*O.velocity[0],O.velocity[1] + -1.5*O.velocity[1])
            O.absY = Oi.absY + O.surf.get_height()
    if O.absX < Oi.absX:
        # O is left of Oi
        if O.velocity[0] > 0:
            newvel = (O.velocity[0] + -1.5*O.velocity[0],O.velocity[1] + -0.1*O.velocity[1])
            O.absX = Oi.absX - O.surf.get_height()
    elif O.absX > Oi.absX:
        # O is right of Oi
        if O.velocity[0] < 0:
            newvel = (O.velocity[0] + -1.5*O.velocity[0],O.velocity[1] + -0.1*O.velocity[1])
            O.absX = Oi.absX + O.surf.get_height()
    return newvel

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
        self.center = (absX + (surf.get_width()/2),absY + (surf.get_height()/2))

pygame.init()
window_sz = 800
window = 300
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Gravity")
clock = pygame.time.Clock()
void = pygame.Surface((5000,5000))
objects = []
rect = pygame.Surface((100,100))
rect.fill("red")
floor = pygame.Surface((10000,1000))
floor.fill("dark green")
objects.append(Object(350,350,rect.get_rect(topleft = (100,100)),rect,100,(1,0),False))
objects.append(Object(-700,1000,floor.get_rect(topleft = (1000000,1000000)),floor,100,(0,0),True))
center_xdis = 0
center_ydis = 0
while True:
    for event in pygame.event.get():
        mp = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                objects[0].velocity = (objects[0].velocity[0],-10 + objects[0].velocity[1])
    
    screen.blit(void,(0,0))
    for O in objects:
        window_blit(O)
        if not O.fixed:
            O.velocity = (O.velocity[0],O.velocity[1] + 9.8/120)
            O.absX += O.velocity[0]
            O.absY += O.velocity[1]
            for Oi in objects:
                if Oi != O:
                    if O.rect.colliderect(Oi.rect):
                        O.velocity = collideresponse(O,Oi)
                    
    pygame.display.update()
    clock.tick(120)