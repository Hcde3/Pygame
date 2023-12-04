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
    dis = math.sqrt((o1.center[0]-o2.center[0])**2 + (o1.center[1] - o2.center[1])**2)
    return dis

def window_blit(self):
    self.rect.x = self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
    self.rect.y = self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)
    new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
    if self == objects[0] and self.strongestforce:
            if angleturn(self,self.strongestforce) <= 315 and angleturn(self,self.strongestforce) >= 225:
                new_surface = pygame.transform.rotate(new_surface,180)
            elif angleturn(self,self.strongestforce) < 225 and angleturn(self,self.strongestforce) > 135:
                new_surface = pygame.transform.rotate(new_surface,270)
            elif angleturn(self,self.strongestforce) <= 135 and angleturn(self,self.strongestforce) >= 45:
                new_surface = pygame.transform.rotate(new_surface,0)
            else:
                new_surface = pygame.transform.rotate(new_surface,90)
    new_surface = new_surface.convert_alpha()
    self.rect = new_surface.get_rect(topleft = (self.rect.x,self.rect.y))
    screen.blit(new_surface,self.rect)

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
    def __init__(self, absX, absY, rect, surf, mass, velocity, fixed, strongestforce):
        self.strongestforce = strongestforce
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
window = window_sz
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Gravity Jump")
clock = pygame.time.Clock()
void = pygame.Surface((5000,5000))
void.fill([2,0,7])
player = pygame.Surface((26,37))
player.fill("Blue")
player = pygame.image.load("Graphics/Astronaut.png").convert_alpha()
playerjetup = pygame.image.load("Graphics/AstronautJet.png").convert_alpha()
playerjetdown = pygame.image.load("Graphics/AstronautJetDown.png").convert_alpha()
playerR = player.get_rect(center = (500,-10))
planet1 = pygame.Surface((500,500))
planet1.fill("Dark Grey")
planet1 = pygame.image.load("Graphics/Asteroid.png").convert_alpha()
planet1R = planet1.get_rect(center = (0,0))
objects = [Object(playerR.x, playerR.y, playerR,player, 50, (0,0), False, None),Object(200, 400, planet1R,planet1, 500, (0,0), True, None)]
center_xdis = 0
center_ydis = 0
jet_timer = 0
jet_direction = "up"
while True:
    p = objects[0]
    for O in objects:
        O.center = (O.absX + (O.surf.get_width()/2),O.absY + (O.surf.get_height()/2))
    for event in pygame.event.get():
        mp = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p.velocity = (p.velocity[0] - vectorcomponent(angleturn(p,p.strongestforce),5,"x"),p.velocity[1] - vectorcomponent(angleturn(p,p.strongestforce),5,"y"))
                jet_direction = "up"
                jet_timer = 0.5
            if event.key == pygame.K_LSHIFT:
                p.velocity = (p.velocity[0] + vectorcomponent(angleturn(p,p.strongestforce),5,"x"),p.velocity[1] + vectorcomponent(angleturn(p,p.strongestforce),5,"y"))
                jet_direction = "down"
                jet_timer = 0.5
            if event.key == pygame.K_w:
                p.velocity = (p.velocity[0] ,p.velocity[1] - 2)
            if event.key == pygame.K_s:
                p.velocity = (p.velocity[0] ,p.velocity[1] + 2)
            if event.key == pygame.K_a:
                p.velocity = (p.velocity[0] - 2 ,p.velocity[1])
            if event.key == pygame.K_d:
                p.velocity = (p.velocity[0] + 2,p.velocity[1])
            
    screen.blit(void,(0,0))
    center_xdis = 400 - p.absX
    center_ydis = 400 - p.absY
    for O in objects:
        window_blit(O)
        forces = []
        for Oi in objects:
            if Oi != O and not O.fixed:
                forces.append((Oi,g(Oi.mass,dis(O,Oi))))
                O.velocity = (O.velocity[0] + (O.mass*vectorcomponent(angleturn(O,Oi),g(Oi.mass,dis(O,Oi)),"x")),O.velocity[1] + (O.mass*vectorcomponent(angleturn(O,Oi),g(Oi.mass,dis(O,Oi)),"y")))
                if O.rect.colliderect(Oi.rect):
                    if abs(O.center[0] - Oi.center[0]) < abs(O.center[1] - Oi.center[1])  and O.center[1] < Oi.center[1]:
                        if O.velocity[1] > 0:
                            O.velocity = (0.7*O.velocity[0],-0.7*O.velocity[1])
                    elif abs(O.center[0] - Oi.center[0]) < abs(O.center[1] - Oi.center[1])  and O.center[1] > Oi.center[1]:
                        if O.velocity[1] < 0:
                            O.velocity = (0.7*O.velocity[0],-0.7*O.velocity[1])
                    elif abs(O.center[0] - Oi.center[0]) > abs(O.center[1] - Oi.center[1])  and O.center[0] < Oi.center[0]:
                        if O.velocity[0] > 0:
                            O.velocity = (-0.7*O.velocity[0],0.7*O.velocity[1])
                    else:
                        if O.velocity[0] < 0:
                            O.velocity = (-0.7*O.velocity[0],0.7*O.velocity[1])
                O.absX += O.velocity[0]
                O.absY += O.velocity[1]
        strongestforce = 0
        for sf in forces:
            if sf[1] > strongestforce and sf[1]:
                O.strongestforce = sf[0]
    if jet_timer > 0:
        if jet_direction == "up":
            p.surf = playerjetup
        else:
            p.surf = playerjetdown
        jet_timer -= 1/60
    else:
        p.surf = player
    pygame.display.update()
    clock.tick(60)