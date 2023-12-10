import pygame
import math
import random
from pygame import mixer
import sys
sys.path.append('C:\\Users\\harry\\Python Learning\\Gravity\\Cutscenes')

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
    if self == p and self.strongestforce:
            if angleturn(self,self.strongestforce) <= 315 and angleturn(self,self.strongestforce) >= 225:
                new_surface = pygame.transform.rotate(new_surface,180)
                self.rotation = "down"
            elif angleturn(self,self.strongestforce) < 225 and angleturn(self,self.strongestforce) > 135:
                new_surface = pygame.transform.rotate(new_surface,270)
                self.rotation = "left"
            elif angleturn(self,self.strongestforce) <= 135 and angleturn(self,self.strongestforce) >= 45:
                new_surface = pygame.transform.rotate(new_surface,0)
                self.rotation = "up"
            else:
                new_surface = pygame.transform.rotate(new_surface,90)
                self.rotation = "right"
    new_surface = new_surface.convert_alpha()
    self.rect = new_surface.get_rect(topleft = (self.rect.x,self.rect.y))
    if self in objects:
        if dis(self,p) < 15000:
            screen.blit(new_surface,self.rect)
    else:
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
        self.rotation = "up"

pygame.init()
mixer.init()
window_sz = 1300
window = window_sz
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Gravity Jump")
clock = pygame.time.Clock()
void = pygame.image.load("Graphics\Void.png").convert_alpha()
SHOWG_font = pygame.font.Font("Font\digital-7.ttf",50)
time_text = SHOWG_font.render("Time",True,"White")
boom = pygame.mixer.Sound("SFX\Boom.mp3")
goal = pygame.image.load("Graphics\Goal.png").convert_alpha()
goalR = goal.get_rect(center = (9500,8900))
arrow = pygame.image.load("Graphics\Marrow.png").convert_alpha()
s_arrow = pygame.image.load("Graphics\Sarrow.png").convert_alpha()
goal_arrow = pygame.image.load("Graphics\StarArrow.png").convert_alpha()
trialpasscard = pygame.image.load("Graphics/TrialPass.png").convert_alpha()
trialfailcard = pygame.image.load("Graphics/TrialFail.png").convert_alpha()
trialinjuredcard = pygame.image.load("Graphics/TrialDeath.png").convert_alpha()
controls = pygame.image.load("Graphics/Controls.png").convert_alpha()
trialbutton = pygame.Surface((151,37))
trialbuttonR = trialbutton.get_rect(topleft = (691,697))
player = pygame.image.load("Graphics/Astronaut.png").convert_alpha()
playerwalk = pygame.image.load("Graphics/AstronautWalk.png").convert_alpha()
playerjump = pygame.image.load("Graphics/AstronautJump.png").convert_alpha()
playerstomp = pygame.image.load("Graphics/AstronautStomp.png").convert_alpha()
playerjetup = pygame.image.load("Graphics/AstronautJet.png").convert_alpha()
playerjetdown = pygame.image.load("Graphics/AstronautJetDown.png").convert_alpha()
playerstabilising = pygame.image.load("Graphics/AstronautStabilise.png").convert_alpha()
playerR = player.get_rect(center = (9500,8900))
moon1 = pygame.image.load("Graphics/Moon.png").convert_alpha()
moon1R = moon1.get_rect(center = (0,0))
earth = pygame.image.load("Graphics\Earth.png").convert_alpha()
earth = pygame.transform.scale(earth,(2000,2000))
mars = pygame.image.load("Graphics\Mars.png").convert_alpha()
asteroid = pygame.image.load("Graphics/Asteroid.png").convert_alpha()
asteroid = pygame.transform.scale(asteroid,(100,100))
M_arrow = Object(playerR.x, playerR.y, arrow.get_rect(center = (10,10)),arrow, 0, (0,0), True, None)
S_arrow = Object(playerR.x, playerR.y, s_arrow.get_rect(center = (10,10)),s_arrow, 0, (0,0), True, None)
G_arrow = Object(playerR.x, playerR.y, goal_arrow.get_rect(center = (10,10)),goal_arrow, 0, (0,0), True, None)
stage = 0
stages = ["Introduction: 1","Introduction: 2","STAGELOOP"]
while True:
    if stages[stage] == "STAGELOOP":
        stage = 0
    if stages[stage] == "Introduction: 1":
        objects = [Object(9500, 8900, playerR,player, 50, (0,0), False, None),Object(-2000, -2000, moon1R,moon1, 500, (0,0), True, None)]
        objects.append(Object(9000, 9000, earth.get_rect(center = (1000,1000)), earth, 10000, (0,0), True, None))
        Goal_star = Object(160-2200,400-2200,goalR,goal,0,(0,0),True,None)
        objects.append(Goal_star)
        center_xdis = 0
        center_ydis = 0
        player_rotation = "up"
        jet_timer = 0
        jet_direction = "up"
        walk_timer = 0
        walk_direction = "right"
        LorR = 0
        velchange = (0,0)
        velchanging = 0
        velchanging_app = 0
        p_movement = (0,0)
        p_moving = False
        windowchange = 0
        stabilising = 0
        p = objects[0]
        objects.remove(p)
        objects.append(p)
        g_s_angle = 0
        complete = 0
        end_condition = "fail"
        maxtime = 120
        gametime = 0
        near = True
        controlsshowing = True
        intrial = True
        import Cutscene1
        mixer.music.load('SFX/In Time.mp3')
        mixer.music.set_volume(0.8)
        mixer.music.play()
    elif stages[stage] == "Introduction: 2":
        objects = [Object(9500, 8900, playerR,player, 50, (0,0), False, None),Object(-2000, -2000, moon1R,moon1, 500, (0,0), True, None)]
        objects.append(Object(9000, 9000, earth.get_rect(center = (1000,1000)), earth, 10000, (0,0), True, None))
        objects.append(Object(-537000, 9000, mars.get_rect(center = (1000,1000)), mars, 2000, (0,0), True, None))
        for x in range(1000):
            n_x = random.randint(-516000,-10000)
            n_y = random.randint(-10000,20000)
            n_sz = random.randint(5,50)
            n_asteroid = pygame.transform.scale(asteroid,(n_sz,n_sz))
            objects.append(Object(n_x, n_y, asteroid.get_rect(center = (1000,1000)), n_asteroid, n_sz/50 , (0,0), True, None))
        Goal_star = Object(-537020,9500,goalR,goal,0,(0,0),True,None)
        objects.append(Goal_star)
        center_xdis = 0
        center_ydis = 0
        player_rotation = "up"
        jet_timer = 0
        jet_direction = "up"
        walk_timer = 0
        walk_direction = "right"
        LorR = 0
        velchange = (0,0)
        velchanging = 0
        velchanging_app = 0
        p_movement = (0,0)
        p_moving = False
        windowchange = 0
        stabilising = 0
        p = objects[0]
        objects.remove(p)
        objects.append(p)
        g_s_angle = 0
        complete = 0
        end_condition = "fail"
        maxtime = 360
        gametime = 0
        near = True
        controlsshowing = False
        intrial = True
        mixer.music.load('SFX/In Time.mp3')
        mixer.music.set_volume(0.8)
        mixer.music.play()
    while intrial:
        ## Inputs ##
        p = objects[-1]
        lesserforces = []
        for O in objects:
            O.center = (O.absX + (O.surf.get_width()/2),O.absY + (O.surf.get_height()/2))
        for event in pygame.event.get():
            mp = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if trialbuttonR.collidepoint(mp) and complete:
                    intrial = False
                    if end_condition == "fail" or end_condition == "injured":
                        stage = stage
                    else:
                        stage += 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    velchanging_app = 0
                if event.key == pygame.K_o:
                    windowchange = 0
                if event.key == pygame.K_i:
                    windowchange = 0
                if event.key == pygame.K_x:
                    stabilising = 0
                if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d:
                    p_moving = False
                    p_movement = (0,0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if controlsshowing:
                        controlsshowing = False
                if not controlsshowing and not complete:
                    if event.key == pygame.K_x:
                        stabilising = 1
                    if event.key == pygame.K_SPACE:
                        velchanging_app = 1
                    if event.key == pygame.K_LSHIFT:
                        p.velocity = (p.velocity[0] + vectorcomponent(angleturn(p,p.strongestforce),10,"x"),p.velocity[1] + vectorcomponent(angleturn(p,p.strongestforce),10,"y"))
                        jet_direction = "down"
                        jet_timer = 0.5
                    if event.key == pygame.K_o:
                        if window - 100 > 0:
                            windowchange = -400
                    if event.key == pygame.K_i:
                        windowchange = 400
                    if event.key == pygame.K_w:
                        if p.rotation == "up":
                            walk_direction = "up"
                        elif p.rotation == "right":
                            walk_direction = "right"
                            LorR = 0
                        elif p.rotation == "left":
                            walk_direction = "left"
                            LorR = 1
                        else:
                            walk_direction = "down"
                        p_moving = True
                        p_movement = (0,-3)
                    if event.key == pygame.K_s:
                        if p.rotation == "up":
                            walk_direction = "down"
                        elif p.rotation == "right":
                            walk_direction = "left"
                            LorR = 1
                        elif p.rotation == "left":
                            walk_direction = "right"
                            LorR = 0
                        else:
                            walk_direction = "up"
                        p_moving = True
                        p_movement = (0,3)
                    if event.key == pygame.K_a:
                        if p.rotation == "up":
                            walk_direction = "left"
                            LorR = 1
                        elif p.rotation == "right":
                            walk_direction = "up"
                        elif p.rotation == "left":
                            walk_direction = "down"
                        else:
                            walk_direction = "right"
                            LorR = 0
                        p_moving = True
                        p_movement = (-3,0)
                    if event.key == pygame.K_d:
                        if p.rotation == "up":
                            walk_direction = "right"
                            LorR = 0
                        elif p.rotation == "right":
                            walk_direction = "down"
                        elif p.rotation == "left":
                            walk_direction = "up"
                        else:
                            walk_direction = "left"
                            LorR = 1
                        p_moving = True
                        p_movement = (3,0)
        p.velocity = (p.velocity[0] + (p_movement[0]/20),p.velocity[1]+ (p_movement[1]/20))
        if velchanging_app:
            velchange = (velchange[0] + 0.2/60,velchange[1] + 0.2/60)
            jet_direction = "up"
            jet_timer = 0.5
            velchanging = 1
        else:
            if velchange[0] > 0:
                velchange = (velchange[0] - 0.1/60, velchange[1] - 0.1/60)
            velchanging = 0
        if p.strongestforce:            
            p.velocity = (p.velocity[0] - vectorcomponent(angleturn(p,p.strongestforce),(velchange[0]*velchanging),"x"),p.velocity[1] - vectorcomponent(angleturn(p,p.strongestforce),(velchange[1]*velchanging),"y"))
        if stabilising:
            p.velocity = (p.velocity[0]*0.9,p.velocity[1]*0.9)
        screen.blit(void,(0,0))
        center_xdis = (window_sz/2) - p.absX
        center_ydis = (window_sz/2) - p.absY
        if window < 100:
            if windowchange < 0:
                windowchange = 0
        if window > 1600:
            if windowchange > 0:
                windowchange = 0
        window += windowchange/60
        if p.velocity[0] > 300:
            p.velocity = (300,p.velocity[1])
        if p.velocity[1] > 300:
            p.velocity = (p.velocity[0],300)
        if p.velocity[0] < -300:
            p.velocity = (-300,p.velocity[1])
        if p.velocity[1] < -300:
            p.velocity = (p.velocity[0],-300)
        ## Objects ##
        for O in objects:
            window_blit(O)
            forces = []
            if not O.fixed:
                for Oi in objects:
                    if Oi != O and not complete:
                        forces.append((Oi,g(Oi.mass,dis(O,Oi))))
                        O.velocity = (O.velocity[0] + (O.mass*vectorcomponent(angleturn(O,Oi),g(Oi.mass,dis(O,Oi)),"x")),O.velocity[1] + (O.mass*vectorcomponent(angleturn(O,Oi),g(Oi.mass,dis(O,Oi)),"y")))
                        if O.rect.colliderect(Oi.rect):
                            if O == p:
                                p.velocity = (p.velocity[0] + (p_movement[0]/2),p.velocity[1]+ (p_movement[1]/2))
                                if math.sqrt((p.velocity[0])**2 + (p.velocity[1])**2) > 100:
                                    complete = 1
                                    end_condition = "injured"
                                    pygame.mixer.Sound.play(boom)
                            if Oi == Goal_star:
                                complete = 1
                                end_condition = "win"
                            if abs(O.center[0] - Oi.center[0]) < abs(O.center[1] - Oi.center[1])  and O.center[1] < Oi.center[1]:
                                if O.velocity[1] > 0:
                                    O.velocity = (0.7*O.velocity[0],-0.5*O.velocity[1])
                                    
                            elif abs(O.center[0] - Oi.center[0]) < abs(O.center[1] - Oi.center[1])  and O.center[1] > Oi.center[1]:
                                if O.velocity[1] < 0:
                                    O.velocity = (0.7*O.velocity[0],-0.5*O.velocity[1])
                            elif abs(O.center[0] - Oi.center[0]) > abs(O.center[1] - Oi.center[1])  and O.center[0] < Oi.center[0]:
                                if O.velocity[0] > 0:
                                    O.velocity = (-0.5*O.velocity[0],0.7*O.velocity[1])
                            else:
                                if O.velocity[0] < 0:
                                    O.velocity = (-0.5*O.velocity[0],0.7*O.velocity[1])
                if not complete:
                    O.absX += O.velocity[0]
                    O.absY += O.velocity[1]
                strongestforce = [None,0]
                for sf in forces:
                    if sf[1] > strongestforce[1]:
                        O.strongestforce = sf[0]
                        if strongestforce[0] != None:
                            lesserforces.append(strongestforce[0])
                        strongestforce = sf
                    else:
                        if sf[0] != None:
                            lesserforces.append(sf[0])
        if p.absY > 70000 or p.absY < -50000:
            if not complete:
                pygame.mixer.Sound.play(boom)
            complete = 1
            end_condition = "injured"
        ## Graphics ##
        if p_moving:
            if walk_timer > 0:
                if walk_direction == "right":
                    p.surf = playerwalk
                elif walk_direction == "left":
                    p.surf = pygame.transform.flip(playerwalk,1,0)
                elif walk_direction == "up":
                    p.surf = pygame.transform.flip(playerjump,LorR,0)
                else:
                    p.surf = pygame.transform.flip(playerstomp,LorR,0)
                walk_timer -= 1/60
            elif walk_timer < -0.1:
                walk_timer = 0.1
            else:
                p.surf = pygame.transform.flip(player,LorR,0)
                walk_timer -= 1/60
        else:
            walk_timer = 0.1
            p.surf = pygame.transform.flip(player,LorR,0) 
        if jet_timer > 0:
            if jet_direction == "up":
                p.surf = pygame.transform.flip(playerjetup,LorR,0)
            else:
                p.surf = pygame.transform.flip(playerjetdown,LorR,0)
            jet_timer -= 1/60
        else:
            if not p_moving:
                p.surf = pygame.transform.flip(player,LorR,0)
        if stabilising:
            p.surf = pygame.transform.flip(playerstabilising,LorR,0)
        #for lf in lesserforces:
            #if lf != Goal_star:
                #S_arrow.absX = p.center[0] - S_arrow.surf.get_width()/2
                #S_arrow.absY = p.center[1] - S_arrow.surf.get_height()/2
                #arrow_angle = 360 - angleturn(lf,p)
                #S_arrow.surf = pygame.transform.rotate(s_arrow, arrow_angle)
                #window_blit(S_arrow)
        
        M_arrow.absX = p.center[0] - M_arrow.surf.get_width()/2
        M_arrow.absY = p.center[1] - M_arrow.surf.get_height()/2
        arrow_angle = 360 - angleturn(p.strongestforce,p)
        M_arrow.surf = pygame.transform.rotate(arrow, arrow_angle)
        M_arrow.surf = pygame.transform.rotate(arrow, arrow_angle)
        window_blit(M_arrow)
        
        g_s_angle += 1
        Goal_star.surf = pygame.transform.rotate(goal, g_s_angle)
        G_arrow.absX = p.center[0] - G_arrow.surf.get_width()/2
        G_arrow.absY = p.center[1] - G_arrow.surf.get_height()/2
        arrow_angle = 360 - angleturn(Goal_star,p)
        G_arrow.surf = pygame.transform.rotate(goal_arrow, arrow_angle)
        G_arrow.surf = pygame.transform.rotate(goal_arrow, arrow_angle)
        window_blit(G_arrow)
        
        time_text = SHOWG_font.render(f"{int(gametime//1)} t",True,"White")
        speed_text = SHOWG_font.render(f"{int((math.sqrt((p.velocity[0])**2 + (p.velocity[1])**2)))} u/t",True,"White")
        coords_text = SHOWG_font.render(f"{int(p.absX)}u , {int(p.absY)}u",True,"White")
        screen.blit(coords_text,(800,0))
        screen.blit(time_text,(0,0))
        screen.blit(speed_text,(100,0))
        if not complete and not controlsshowing:
            gametime += 1/60
        if gametime > maxtime:
            complete = 1
        if complete:
            if end_condition == "win":
                screen.blit(trialpasscard,((window_sz/2)-200,(window_sz/2)-100))
            elif end_condition == "fail":
                screen.blit(trialfailcard,((window_sz/2)-200,(window_sz/2)-100))
            elif end_condition == "injured":
                screen.blit(trialinjuredcard,((window_sz/2)-200,(window_sz/2)-100))
        if controlsshowing:
            screen.blit(controls,((window_sz/2)-400,(window_sz/2)-400))
        pygame.display.update()
        clock.tick(60)
        
