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

class Floor:
    def __init__(self,height,surf,bounce):
        self.height = height
        self.surf = surf
        self.rect = surf.get_rect(topleft = (0,height))
        self.bounce = bounce

def window_blit(self):
    self.rect.x = self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
    self.rect.y = self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)
    new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
    new_surface = new_surface.convert_alpha()
    self.rect = new_surface.get_rect(center = (self.rect.x,self.rect.y))
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

def smartcollide(O,Oi):
    Oi_corners = [(Oi.absX,Oi.absY),(Oi.absX + Oi.surf.get_width(),Oi.absY),(Oi.absX + Oi.surf.get_width(),Oi.absY+ Oi.surf.get_height()),(Oi.absX,Oi.absY+ Oi.surf.get_height())]
    O_corners = [(O.absX,O.absY),(O.absX + O.surf.get_width(),O.absY),(O.absX + O.surf.get_width(),O.absY+ O.surf.get_height()),(O.absX,O.absY+ O.surf.get_height())]
    collide = False
    for corner in Oi_corners:
        if not collide:
            if (Oi_corners[0][0]-O_corners[0][0]) != 0 and (Oi_corners[2][0]-O_corners[2][0]) != 0:
                if math.degrees(math.atan((Oi_corners[0][1]-O_corners[0][1])/(Oi_corners[0][0]-O_corners[0][0]))) >= O.angle and math.degrees(math.atan((Oi_corners[0][1]-O_corners[0][1])/(Oi_corners[0][0]-O_corners[0][0]))) <= O.angle + 90 and math.degrees(math.atan((Oi_corners[2][1]-O_corners[2][1])/(Oi_corners[2][0]-O_corners[2][0]))) >= -O.angle and math.degrees(math.atan((Oi_corners[2][1]-O_corners[2][1])/(Oi_corners[2][0]-O_corners[2][0]))) <= 90-O.angle and Oi_corners[0][1] <= O_corners[0][1] and Oi_corners[2][1] >= O_corners[2][1]:
                    print(t)
                elif math.degrees(math.atan((Oi_corners[1][1]-O_corners[1][1])/(Oi_corners[1][0]-O_corners[1][0]))) >= 90+O.angle and math.degrees(math.atan((Oi_corners[1][1]-O_corners[1][1])/(Oi_corners[1][0]-O_corners[1][0]))) <= O.angle + 180 and math.degrees(math.atan((Oi_corners[3][1]-O_corners[3][1])/(Oi_corners[3][0]-O_corners[3][0]))) >= 90-O.angle and math.degrees(math.atan((Oi_corners[3][1]-O_corners[3][1])/(Oi_corners[3][0]-O_corners[3][0]))) <= 180-O.angle and Oi_corners[1][1] <= O_corners[1][1] and Oi_corners[3][1] >= O_corners[3][1]:
                    print(t)

def check_for_collisions(O,Oi):
    #We calculate the offset of the second mask relative to the first mask.
    offset_x = O.mask_rect[0] - Oi.mask_rect[0]
    offset_y = O.mask_rect[1] - Oi.mask_rect[1]
    # See if the two masks at the offset are overlapping.
    overlap = O.mask.overlap(Oi.mask, (offset_x, offset_y))
    if overlap:
        print("the two masks overlap!")

pygame.init()
window_sz = 800
window = window_sz
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Physics Lab")
clock = pygame.time.Clock()
square = pygame.image.load("Air.png").convert_alpha()
ground = pygame.Surface((800,800-700))
ground.fill("Dark Green")
floors = [Floor(700,ground,-0.75)]
objects = [Object(200,200,square.get_rect(center = (200,200)),square,10,(0,0),False),Object(400,400,square.get_rect(center = (400,400)),square,10,(0,0),False)]
objects[0].angle = 30
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
        forces = [(0,0.15*O.mass,0,0)]
        xmoments = 0
        ymoments = 0
        for F in floors:
            screen.blit(F.surf,F.rect)
            if O.rect.colliderect(F.rect):
                forces.append((O.velocity[0]*O.mass*-0.01,O.velocity[1]*O.mass*F.bounce,0,O.angle))
                O.absY = F.height - O.surf.get_height()/2
                O.grounded = True
                print(forces[-1])
        for F in forces:
            if F[2] != 0:
                xmoments += (F[2]*F[0])/O.mass
            if F[3] != 0:
                ymoments += (F[3]*F[1])/O.mass
        O.angle += ymoments
        #print(O.angle)
        if O.angle > 360: O.angle -= 360
        O.surf = pygame.transform.rotate(square,O.angle)
        for Oi in objects:
            if O != Oi:
                other_objects =[]
                for Oi in objects:
                    if Oi != O:
                        other_objects.append(Oi)
                        if pygame.sprite.spritecollide(O, [Oi], False, pygame.sprite.collide_mask):
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
            for F in forces:
                O.velocity = (O.velocity[0] + (F[0]/O.mass),O.velocity[1] + (F[1]/O.mass))
            O.absX += O.velocity[0]
            O.absY += O.velocity[1]
            O.center = (O.absX,O.absY)
    t += 1
    pygame.display.update()
    clock.tick(60)
