
import pygame
import sys
import math
import random
from pygame.locals import *
flags = FULLSCREEN | DOUBLEBUF

def window_blit(self):
    if self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) -(self.surf.get_width()*(window/window_sz))< window_sz and self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) + (self.surf.get_width()*2*(window/window_sz)) > 0 and self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) - (self.surf.get_width()*(window/window_sz)) < window_sz and self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) + (self.surf.get_width()*2*(window/window_sz))> 0:
        new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
        new_surface = new_surface.convert_alpha()
        screen.blit(new_surface,(self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz),self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)))

def window_blit_rect(self):
    if self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) -(self.surf.get_width()*(window/window_sz))< window_sz and self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) + (self.surf.get_width()*2*(window/window_sz)) > 0 and self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) - (self.surf.get_width()*(window/window_sz)) < window_sz and self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) + (self.surf.get_width()*2*(window/window_sz))> 0:
        new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
        new_surface = new_surface.convert_alpha()
        screen.blit(new_surface,(self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz),self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)))
        self.rect = new_surface.get_rect(topleft = ((self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz),self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz))))

def dis(point1,point2):
    dis = math.sqrt((point1[0]-point2[0])**2 + (point1[1] - point2[1])**2)
    return dis

def abswin_convert(point,original,xory):
    if original == "abs":
        if xory == "x":
            new_point = point*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
        else:
            new_point = point*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)
    elif original == "win":
        if xory == "x":
            new_point = (point - center_xdis*(window/window_sz) - (window_sz-window)/2)/(window/window_sz)
        else:
            new_point = (point - center_ydis*(window/window_sz) - (window_sz-window)/2)/(window/window_sz)
    return new_point

def vectorcomponent(angle, magnitude, XorY):
    if XorY == "y":
        angle -= 90
        if angle < 0:
            angle += 360
    dis = math.cos(math.radians(angle)) * magnitude
    return dis

def angle(point1,point2):
    xdis = point1[0] - point2[0]
    ydis = point1[1] - point2[1]
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

def updatedata(self):
    self.mask = pygame.mask.from_surface(self.surf)
    self.cent = (self.absC[0] + (self.surf.get_width()/2),self.absC[1] + (self.surf.get_height()/2))
    try:
        for iud, lud in enumerate(self.sides):
            self.sides[iud] = [self.sides[iud][0],self.sides[iud][1],-(self.sides[iud][3][1] + self.absC[1]) + (self.sides[iud][0]*(self.sides[iud][3][0] + self.absC[0])),self.sides[iud][3],self.sides[iud][4]]
    except: pass
    
def createlines(pts):
    lines = []
    for x in range(len(pts)):
        if x == len(pts) - 1:
            p1 = pts[x]
            p2 = pts[0]
        else:
            p1 = pts[x]
            p2 = pts[x+1]
        if p2[0] == p1[0]: slope = 99999999
        else: slope = (p2[1]-p1[1])/(p2[0]-p1[0])
        x_coef = -slope
        # y_coef is 1
        c = -p1[1] + (slope*p1[0])
        lines.append([slope,x_coef,c,p1,p2])
    return lines

def slope(pt1,pt2):
    if pt2[0] == pt1[0]: slope = 99999999
    else: slope = (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
    return slope

def perpdis(point,line):
    return abs((line[1]*point[0])+point[1]+line[2])/math.sqrt((line[1]**2) + 1)

class Player(pygame.sprite.Sprite):
    def __init__(self,absC,element,controller,health):
        pygame.sprite.Sprite.__init__(self)
        self.absC = absC
        self.surf = pygame.image.load(f"Graphics\Stickmen\{element}\Idle.png").convert_alpha()
        self.cent = (absC[0] + (self.surf.get_width()/2),absC[1] + (self.surf.get_height()/2))
        self.rect = self.surf.get_rect(center = (abswin_convert(absC[0],"abs","x"),abswin_convert(absC[1],"abs","y")))
        self.vel = (0,0)
        self.controller = controller
        self.element = element
        self.attackdata = []
        self.elementdata = []
        self.health = health
        self.stuninfo = [None,0]
        self.facingdirection = "R"
        self.falltimer = 2.5
        self.mask = pygame.mask.from_surface(self.surf)
        self.summonedobjects = []
        self.summoneddecals = []
        self.speedlimit = 8
        
        if self.element == "Earth":
            self.attackdata.append(["Ungloved",0,6]) #Gloves
            self.attackdata.append(["Unshielded",0,6,1]) #Shield
            self.attackdata.append(["Not Up", 0, 15, True]) #Stack
            self.attackdata.append([11,False]) #Earthquake
            self.elementdata.append("") #Gloved or not gloved sprite
            self.idle_ac_info = [20,0.05,6] #[untilanimate,rateofanimation,frames]
            self.stomp_ac = [("Stomp_f1",0.05),("Stomp_f2",0.2),("Stomp_f3",0.05),("Stomp_f4",0.7),("Stomp_f1",0.05)]
        
        if self.element == "Dark":
            self.idle_ac_info = [20000000,1,0] #[untilanimate,rateofanimation,frames]
            
        self.animationlock = False
        self.idle_ac = [("Idle",self.idle_ac_info[0])]
        self.idle_ac.extend([(f"Idle_s{x+1}",self.idle_ac_info[1]) for x in range(self.idle_ac_info[2])])
        self.walk_ac = [("Run_f1",0.05),("Run_f2",0.05),("Run_f3",0.05),("Run_f4",0.05),("Run_f5",0.05),("Run_f4",0.05),("Run_f3",0.05),("Run_f2",0.05),("Run_f6",0.05),("Run_f2",0.05),("Run_f3",0.05),("Run_f4",0.05),("Run_f5",0.05),("Run_f4",0.05),("Run_f3",0.05),("Run_f2",0.05),]
        self.current_step = 0
        self.current_cycle = self.idle_ac
        self.animation_timer = 20
        
class Object(pygame.sprite.Sprite):
    def __init__(self,absC,surf,gravity):
        pygame.sprite.Sprite.__init__(self)
        self.absC = absC
        self.surf = surf
        self.cent = (absC[0] + (self.surf.get_width()/2),absC[1] + (self.surf.get_height()/2))
        self.gravity = gravity
        self.rect = surf.get_rect(center = (abswin_convert(absC[0],"abs","x"),abswin_convert(absC[1],"abs","y")))
        self.vel = (0,0)
        self.mask = pygame.mask.from_surface(self.surf)
        self.uniquedata = []
        self.sides = []
        self.sl_up = []
        self.sl_dwn = []
        self.sl_rgt = []
        self.sl_lft = []


class Projectile(pygame.sprite.Sprite):
    def __init__(self,absC,surf,vel,lifetime,owner,damage,gravity):
        pygame.sprite.Sprite.__init__(self)
        self.absC = absC
        self.surf = surf
        self.cent = (absC[0] + (self.surf.get_width()/2),absC[1] + (self.surf.get_height()/2))
        self.rect = surf.get_rect(center = (abswin_convert(absC[0],"abs","x"),abswin_convert(absC[1],"abs","y")))
        self.vel = vel
        self.gravity = gravity
        self.lifetime = lifetime
        self.owner = owner
        self.damage = damage
        self.stuntype = None
        self.mask = pygame.mask.from_surface(self.surf)
        
class Decal(pygame.sprite.Sprite):
    def __init__(self,absC,surf):
        pygame.sprite.Sprite.__init__(self)
        self.absC = absC
        self.surf = surf
        self.cent = (absC[0] + (self.surf.get_width()/2),absC[1] + (self.surf.get_height()/2))
        
class Hitbox:
    def __init__(self,wah,tl):
        self.tl = tl
        self.wah = wah
        self.surf = pygame.Surface(wah)
        self.surf.fill("Red")
        self.rect = self.surf.get_rect(topleft = (tl))
        
  
pygame.init()
pygame.joystick.init()
WHITE = (250,250,250)
window_sz = 1200
window = 1200
void = pygame.Surface((window_sz,window_sz))
void.fill(WHITE)
center_xdis = 0
center_ydis = 0
center_xchange = 0
center_ychange = 0
window_change = 0
screen = pygame.display.set_mode((window_sz,window_sz))#, flags)
pygame.display.set_caption("Elelments")
clock = pygame.time.Clock()

num_joysticks = pygame.joystick.get_count()
controllers = []
if num_joysticks > 0:
    for x in range(num_joysticks):
        controllers.append(pygame.joystick.Joystick(x))
        controllers[-1].init()
        print("Controller connected:", controllers[-1].get_name())
else:
    print("No controller detected.")
    #sys.exit()

players = []
for x in range(num_joysticks):
    players.append(Player((200,200),"Earth",controllers[x],100))
players[-1].element = "Dark"
objects = [Object((100,500),pygame.image.load("Graphics\Platform.png").convert_alpha(),False)]
sds = createlines([(0,0),(1000,0),(1000,200),(886,238),(815,349),(698,359),(366,400),(101,337),(10,400)])
objects[-1].sides.extend(sds)
objects[-1].sl_up.extend([slope((0,0),(1000,0))])
objects[-1].sl_dwn.extend([slope((1000,200),(886,238)),slope((886,238),(815,349)),slope((815,349),(698,359)),slope((698,359),(366,400)),slope((366,400),(101,337)),slope((101,337),(10,400)),slope((10,400),(0,0))])
objects[-1].sl_rgt.extend([slope((1000,0),(1000,200)),slope((1000,200),(886,238)),slope((886,238),(815,349)),slope((815,349),(698,359)),slope((698,359),(366,400))])
objects[-1].sl_lft.extend([slope((366,400),(101,337)),slope((101,337),(10,400))])
projectiles = []
decals = []
visiblehitboxes = []

tick = 0
tps = 120
t_fq = tps**-1
while True:
    screen.blit(void,(0,0))
    mp = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.JOYBUTTONDOWN:
            for controller in controllers:
                if controller.get_button(0): #A
                    pass
                if controller.get_button(1): #B
                    pass
                if controller.get_button(2): #X
                    pass
                if controller.get_button(3): #Y
                    pass
                if controller.get_button(4): #-
                    pygame.quit()
                    exit()
                if controller.get_button(5): #HOME
                    pass
                if controller.get_button(6): #+
                    pass
                if controller.get_button(7): #LSD
                    pass
                if controller.get_button(8): #RSD
                    pass
                if controller.get_button(9): #L
                    pass
                if controller.get_button(10): #R
                    pass
                if controller.get_button(11): #^
                    pass
                if controller.get_button(12): #v
                    pass
                if controller.get_button(13): #<
                    pass
                if controller.get_button(14): #>
                    pass
                if controller.get_button(15): #o
                    pass
        if  event.type == pygame.JOYBUTTONUP:
            pass
            #screen.fill((0,0,0))
    for O in objects:
        on_object = False
        updatedata(O)
        window_blit_rect(O)
        if O.gravity:
            for o in objects:
                if o != O:
                    if pygame.sprite.spritecollide(O, [o], False, pygame.sprite.collide_mask):
                        on_object = True
                        if O.vel[1] > 0: O.vel = (O.vel[0] + O.vel[0]*-0.01,(O.vel[1]*-0.3))
                        else: O.vel = (O.vel[0] + O.vel[0]*-0.01,O.vel[1])
                        if o.rect.collidepoint((abswin_convert(O.absC[0] + (O.surf.get_height()/2),"abs","x"),abswin_convert(O.absC[1] + O.surf.get_height() - 5,"abs","y"))):
                            if O.vel[1] > -5: O.vel = (O.vel[0],O.vel[1] - 5)
            if not on_object:
                O.vel = (O.vel[0],O.vel[1] + (9.8/60))
        O.absC = (O.absC[0] + O.vel[0],O.absC[1] + O.vel[1])
    
    for vHB in visiblehitboxes:
        screen.blit(vHB.surf,vHB.rect)
        
    for Pr in projectiles:
        window_blit_rect(Pr)
        Pr.absC = (Pr.absC[0] + Pr.vel[0],Pr.absC[1] + Pr.vel[1])
        if Pr.gravity:
            for o in objects:
                if o != Pr:
                    if pygame.sprite.spritecollide(Pr, [o], False, pygame.sprite.collide_mask):
                        on_object = True
                        if Pr.vel[1] > 0: Pr.vel = (Pr.vel[0] + Pr.vel[0]*-0.01,(Pr.vel[1]*-0.3))
                        else: Pr.vel = (Pr.vel[0] + Pr.vel[0]*-0.01,Pr.vel[1])
                        if o.rect.collidepoint((abswin_convert(Pr.absC[0] + (Pr.surf.get_height()/2),"abs","x"),abswin_convert(Pr.absC[1] + Pr.surf.get_height() - 5,"abs","y"))):
                            if Pr.vel[1] > -5: Pr.vel = (Pr.vel[0],Pr.vel[1] - 5)
            if not on_object:
                Pr.vel = (Pr.vel[0],Pr.vel[1] + (9.8/60))
        for p in players:
            if pygame.sprite.spritecollide(Pr, [p], False, pygame.sprite.collide_mask) and p.element != Pr.owner:
                p.health -= Pr.damage
                Pr.lifetime = -1
                if Pr.stuntype == "Knock":
                    p.stuninfo = ["Knock",5]
        Pr.lifetime -= t_fq
        if Pr.lifetime < 0: projectiles.remove(Pr)
        
#__________________________________________________________________________________________________________________ PLAYERS __________________________________________________________________________________________________________________
        
    for I, P in enumerate(players):
        updatedata(P)
        x_move = 0
        y_move = 0
        on_object = False
        inanimation = False
        
#----------------------------------- Attack Updates ----------------------------------------------------------        
        
        if P.element == "Earth":
            
            
            if P.attackdata[0][1] == 0:
                if P.attackdata[0][0] == "Gloved": P.elementdata[0] = ""
                P.attackdata[0] = ["Ungloved",0,P.attackdata[0][2] + t_fq]
            if P.attackdata[1][1] > 0:
                P.attackdata[1] = ["Shielded",P.attackdata[1][1] - t_fq,0,P.attackdata[1][3]]
                inanimation = True
                x_move = P.attackdata[1][3]
            else:
                P.attackdata[1] = ["Unshielded",0,P.attackdata[1][2] + t_fq,P.attackdata[1][3]]
                
                
            if P.attackdata[2][0] == "Up":
                if P.attackdata[2][1] < 0:
                    P.attackdata[2] = ["Not Up",0,0,True]
                    objects.remove(P.summonedobjects[0])
                    P.summonedobjects.remove(P.summonedobjects[0])
                elif P.attackdata[2][1] < 14 and not P.attackdata[2][3]:
                    stcmp = False
                    P.summonedobjects[0].gravity = True
                    for p in players:
                        if pygame.sprite.spritecollide(O, [p], False, pygame.sprite.collide_mask) and p.element != "Earth":
                            p.health -= 50
                            stcmp = True
                            p.stuninfo = ["Knock",6]
                        elif dis(p.absC,O.absC) < 200 and p.element != "Earth":
                            p.health -= (200 - dis(p.absC,O.absC))/4
                            stcmp = True
                            p.stuninfo = ["Knock",(200 - dis(p.absC,O.absC))/5]
                    if stcmp: P.attackdata[2] = ["Up",P.attackdata[2][1] - t_fq,0,True]
                    else: ["Up",P.attackdata[2][1] - t_fq,0,False]
                elif P.attackdata[2][1] < 13:
                    P.attackdata[2] = ["Up",P.attackdata[2][1] - t_fq,0,True]
                else:
                    P.attackdata[2] = ["Up",P.attackdata[2][1] - t_fq,0,False]
            else:
                P.attackdata[2] = ["Not Up",0,P.attackdata[2][2] + t_fq,True]
                try:
                    objects.remove(P.summonedobjects[0])
                    P.summonedobjects.remove(P.summonedobjects[0])
                except: pass
                
                
            if P.attackdata[3][0] > 0.3 and not P.attackdata[3][1] and P.attackdata[3][0] < 1:
                P.attackdata[3][1] = True
                P.attackdata[3][0] += t_fq
                P.animationlock = True
                decals.append(Decal((P.absC[0] - 75,P.absC[1] + 100),pygame.image.load(f"Graphics\Stickmen\Earth\GroundShatter.png").convert_alpha()))
                P.summoneddecals.append(decals[-1])
                P.absC = (P.absC[0] - 20,P.absC[1] - 5)
                P.vel = (P.vel[0],10)
                dbhb = pygame.Surface((350,50))
                h_box = dbhb.get_rect(topleft = (P.absC[0] - 120,P.absC[1] + 69))
                for ped in players:
                    if ped.rect.colliderect(h_box) and ped != P:
                        ped.health -= 60
                        ped.stuninfo = ["Grounded",7]
                        ped.absC = (ped.absC[0],ped.absC[1] + 50)
            elif P.attackdata[3][0] < 1:
                P.animationlock = True
                P.attackdata[3][0] += t_fq
            else:
                if P.attackdata[3][0] > 8 and P.summoneddecals:
                    decals.remove(P.summoneddecals[0])
                    P.summoneddecals.remove(P.summoneddecals[0])
                P.attackdata[3][0] += t_fq
                P.attackdata[3][1] = False
                if P.current_cycle == P.stomp_ac:
                    P.current_cycle = P.idle_ac
                    P.current_step = 0
                    P.animation_timer = P.idle_ac[0][1]
                    P.animationlock = False
 
        if P.element == "Dark":
            if not inanimation:
                if P.falltimer < 0: P.surf = pygame.image.load(f"Graphics\Stickmen\Dark\Falling.png").convert_alpha()
                else: P.surf = pygame.image.load(f"Graphics\Stickmen\Dark\Idle.png").convert_alpha()

#----------------------------------- Sprite ----------------------------------------------------------

        if P.animation_timer < 0:
            if P.current_step + 1 < len(P.current_cycle): P.current_step += 1
            else: P.current_step = 0
            P.animation_timer = P.current_cycle[P.current_step][1]      
        P.surf = pygame.image.load(f"Graphics\Stickmen\{P.element}\{P.current_cycle[P.current_step][0]}.png").convert_alpha()
        P.animation_timer -= t_fq
        
        if P.stuninfo[0]:
            P.animationlock = True
            P.stuninfo[1] -= t_fq
            if P.element == "Earth": P.surf = pygame.image.load(f"Graphics\Stickmen\Earth\{P.elementdata[0]}{P.stuninfo[0]}.png").convert_alpha()
            else: P.surf = pygame.image.load(f"Graphics\Stickmen\{P.element}\{P.stuninfo[0]}.png").convert_alpha()
            if P.stuninfo[1] < 0: P.stuninfo = [None,0]
            
        b_s = P.surf
        if P.facingdirection == "L": P.surf = pygame.transform.flip(P.surf,1,0)
        window_blit_rect(P)
        P.surf = b_s
        
#----------------------------------- Motion ----------------------------------------------------------
        
        if (P.controller.get_axis(0) > 0.3 or P.controller.get_axis(0) < -0.3) and not P.animationlock:
            if (P.vel[0] > -5 and P.controller.get_axis(0) < 0) or (P.vel[0] < 5 and P.controller.get_axis(0) > 0): x_move = 6*P.controller.get_axis(0)
            if P.controller.get_axis(0) < 0:
                h_dir = -1
                P.facingdirection = "L"
            else:
                h_dir = 1
                P.facingdirection = "R"
            if P.current_cycle != P.walk_ac:
                P.current_cycle = P.walk_ac
                P.current_step = 0
                P.animation_timer = P.walk_ac[0][1]
        else:
            P.vel = (P.vel[0]*0.9,P.vel[1])
            if P.vel[0] < 1 and P.current_cycle != P.idle_ac and not P.animationlock:
                P.current_cycle = P.idle_ac
                P.current_step = 0
                P.animation_timer = P.idle_ac[0][1]
        #if controller.get_axis(1) > 0.3 or controller.get_axis(1) < -0.3: y_move = 2*controller.get_axis(1)
        for o in objects:
            if pygame.sprite.spritecollide(P, [o], False, pygame.sprite.collide_mask):
                on_object = True
                P.falltimer = 2.5
                closest_line = [o.sides[0],10000]
                for clc in o.sides:
                    vx1 = clc[3][0] + o.absC[0]
                    vy1 = clc[3][1] + o.absC[1]
                    vx2 = clc[4][0] + o.absC[0]
                    vy2 = clc[4][1] + o.absC[1]
                    isperp = -((((vx1-P.cent[0])*(vx2-vx1))+((vy1-P.cent[1])*(vy2-vy1)))/(((vx2-vx1)**2)+((vy2-vy1)**2)))
                    if isperp < 1 and isperp > 0:
                        if perpdis(P.cent,clc) < closest_line[1]:
                            closest_line = [clc,perpdis(P.cent,clc)]
                    else:
                        if min([dis(clc[3],P.cent),dis(clc[4],P.cent)]) < closest_line[1]:
                            closest_line = [clc,min([dis(clc[3],P.cent),dis(clc[4],P.cent)])]
                perpangle = angle((1,closest_line[0][0]),(0,0)) + 90
                
                if not (closest_line[0][0] in o.sl_rgt or closest_line[0][0] in o.sl_lft):
                    vx = 0
                    perpangle = 90
                if not (closest_line[0][0] in o.sl_up or closest_line[0][0] in o.sl_dwn):
                    vy = 0
                    perpangle = 360
                if closest_line[0][0] in o.sl_rgt:
                    vx = abs(vectorcomponent(perpangle,(8),"x"))
                elif closest_line[0][0] in o.sl_lft:
                    vx = -abs(vectorcomponent(perpangle,(8),"x"))
                if closest_line[0][0] in o.sl_up:
                    vy = -abs(vectorcomponent(perpangle,(0.2),"y"))
                elif closest_line[0][0] in o.sl_dwn:
                    if "Stack" in o.uniquedata and P.element != "Earth":
                        P.stuninfo = ["Knock",6]
                    vy = abs(vectorcomponent(perpangle,(5),"y"))
                    
                if vx > 0:
                    if P.vel[0] < vx: P.vel = ( vx ,P.vel[1] )
                else:
                    if P.vel[0] > vx: P.vel = ( vx ,P.vel[1] )
                if vy > 0:
                    if P.vel[1] < vy: P.vel = (P.vel[0],vy)
                else:
                    if P.vel[1] > vy: P.vel = (P.vel[0],vy)
                    
        if (P.controller.get_button(2) or P.controller.get_button(3)) and on_object and not inanimation:
            if P.vel[1] > -5: y_move = -5
        if not on_object:
            P.vel = (P.vel[0],P.vel[1] + (9.8/60))
            P.falltimer -= t_fq
        P.vel = (P.vel[0] + x_move,P.vel[1] + y_move)
        
#----------------------------------- Attacks ----------------------------------------------------------
        
        if P.controller.get_button(1) and not inanimation:
            if abs(P.controller.get_axis(0)) > 0.3 or abs(P.controller.get_axis(1)) > 0.3:
                if abs(P.controller.get_axis(0)) > abs(P.controller.get_axis(1)):
                    
                    #Horizontal
                    
                    if P.element == "Earth":
                        if P.attackdata[1][0] == "Unshielded" and P.attackdata[1][2] > 5:
                            P.surf = pygame.image.load(f"Graphics\Stickmen\Earth\{P.elementdata[0]}Shielding.png").convert_alpha()
                            P.attackdata[1] = ["Shielded",0.75,0,3*h_dir]
                            projectiles.append(Projectile((P.absC[0] + 60*h_dir,P.absC[1] - 45),pygame.image.load("Graphics\Stickmen\Earth\Shield.png").convert_alpha(),(7*h_dir,0),3,"Earth",30,True))
                            projectiles[-1].stuntype = "Knock"
                            
                elif P.controller.get_axis(1) > 0:
                    
                    #Downwards
                    if P.element == "Earth":
                        if P.attackdata[3][0] > 10:
                            P.attackdata[3][0] = 0
                            P.current_cycle = P.stomp_ac
                            P.current_step = 0
                            P.animation_timer = P.stomp_ac[0][1]
                            P.animationlock = True
                                
                else:
                    
                    #Upwards
                    
                    if P.element == "Earth":
                        if P.attackdata[2][0] == "Not Up" and P.attackdata[2][2] > 10:
                            P.attackdata[2] = ["Up",15,0,False]
                            objects.append(Object((P.cent[0] - 109,P.cent[1] + 100),pygame.image.load(f"Graphics\Stickmen\Earth\Stack.png").convert_alpha(),False))
                            objects[-1].vel = (0,-7)
                            objects[-1].uniquedata.append("Stack")
                            sds = createlines([(60,0),(117,0),(169,39),(191,91),(191,229),(200,250),(0,251),(25,225),(31,62)])
                            objects[-1].sides.extend(sds)
                            objects[-1].sl_up.extend([slope((60,0),(117,0)),slope((117,0),(169,39)),slope((169,39),(191,91)),slope((191,91),(191,229)),slope((191,229),(200,250)),slope((0,251),(25,225)),slope((25,225),(31,62)),slope((31,62),(60,0))])
                            objects[-1].sl_dwn.extend([slope((200,250),(0,251))])
                            objects[-1].sl_rgt.extend([slope((117,0),(169,39)),slope((169,39),(191,91)),slope((191,91),(191,229)),slope((191,229),(200,250))])
                            objects[-1].sl_lft.extend([slope((0,251),(25,225)),slope((25,225),(31,62)),slope((31,62),(60,0))])
                            P.summonedobjects.append(objects[-1])
                            P.vel = (P.vel[0],-7)
                        
            else:
                
                #Stationary
                
                if P.element == "Earth":
                    if P.attackdata[0][0] == "Ungloved" and P.attackdata[0][2] > 5 and on_object:
                        P.attackdata[0] = ["Gloved",2,0]
                        P.elementdata[0] = "Gloved_"
                        
        P.absC = (P.absC[0] + P.vel[0],P.absC[1] + P.vel[1])
        if P.vel[0] > P.speedlimit: P.vel = (P.speedlimit,P.vel[1])
        if P.vel[0] < -P.speedlimit: P.vel = (-P.speedlimit,P.vel[1])
        if P.vel[1] > P.speedlimit: P.vel = (P.vel[0],P.speedlimit)
        if P.vel[1] < -P.speedlimit: P.vel = (P.vel[0],-P.speedlimit)
#----------------------------------- Death ----------------------------------------------------------
        
        if P.absC[1] > window_sz or P.absC[0] > window_sz or P.absC[1] < 0 or P.absC[0] < 0:
            P.health -= 0.5
        
        if P.health < 0:
            players[I] = Player((200,200),P.element,P.controller,100)
            if players[I].element == "Earth":
                players[I].attackdata.append(["Ungloved",0,6])
                players[I].attackdata.append(["Unshielded",0,6,1])
                players[I].elementdata.append("")

#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

    for D in decals:
        window_blit(D)
     
     
    pygame.display.update()
    tick += 1
    clock.tick(60)