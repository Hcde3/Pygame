import pygame
import math
import random

def window_blit(self):
    if self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) -(self.surf.get_width()*(window/window_sz))< window_sz and self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) + (self.surf.get_width()*2*(window/window_sz)) > 0 and self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) - (self.surf.get_width()*(window/window_sz)) < window_sz and self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) + (self.surf.get_width()*2*(window/window_sz))> 0:
        new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
        new_surface = new_surface.convert_alpha()
        screen.blit(new_surface,(self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz),self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)))
    
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

def angleturn(point1,point2):
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

def wherethefuckdoesthesecomefromimlosingmymind(unit):
    for x in humans[0].tasks:
        if x[0] == "Build":
            if len(x[1].info[0][1]) == 4:
                print("FUCKING HERE AT UNIT",unit)

class Human:
    def __init__(self,absC,surf,traits):
        self.absC = absC
        self.surf = surf
        self.traits = traits #format: [Health,Stamina,Boredom,Fighting,Building,Mining,Hunting,Farming]
        self.tasks = [["Idle"]]
        self.idleprocess = [[0,0],[0,0]] #format: [Timer+TimerMode,Movement]
        self.inventory = []
        
class Tile:
    def __init__(self, absC, surf, layer):
        self.absC = absC
        self.surf = surf
        self.biome = None
        self.layer = layer
        self.info = []
        self.inventory = []
        
class Material:
    def __init__(self,absC,surf,name):
        self.name = name
        self.absC = absC
        self.surf = surf
        self.holder = None

pygame.init()
void = pygame.Surface((1000,1000))
void.fill("DarkGreen")
window_sz = 1000
window = window_sz
center_xdis = 0
center_ydis = 0
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Task AI")
clock = pygame.time.Clock()

tilecentres = []
for y in range(-10000,10000,50):
    for x in range(-10000,10000,50):
        tilecentres.append((x,y))

man = pygame.image.load("Human.png").convert_alpha()
rocks = pygame.image.load("Rocks.png").convert_alpha()
humans = [Human((100,100),man,[10,10,0,0,5,0,0,0]),Human((100,100),man,[40,40,0,0,1,0,0,0])]
tiles = []
materials = [Material((700,700),rocks,"Rocks") ]
blueprint = pygame.image.load("Blueprint.png").convert_alpha()
stone = pygame.image.load("StoneBlock.png").convert_alpha()
pb = pygame.image.load("ProgressBar.png").convert_alpha()

center_xchange = 0
center_ychange = 0
window_change = 0
while True:
    wherethefuckdoesthesecomefromimlosingmymind(10)
    screen.blit(void,(0,0))
    mp = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                distance = 1000000
                mppoint = ((abswin_convert(mp[0],"win","x")-25)//1,(abswin_convert(mp[1],"win","y")-25)//1)
                for tc in tilecentres:
                    if dis(mppoint,tc) < distance:
                        place_cords = tc
                        distance = dis(mppoint,tc)
                go = True
                for t in tiles:
                    if t.absC == place_cords:
                        if t.layer == 1:
                            go = False
                if go:
                    tiles.append(Tile(place_cords,blueprint,1))
                    tiles[-1].info = [[[],["Rocks","Rocks"]],[0.1,20]] #format: [[[resources_in],[resources_needed]],[buildprogress,buildtime]]
            if event.button == 1:
                materials.append(Material((abswin_convert(mp[0],"win","x")-20,abswin_convert(mp[1],"win","y")-10),rocks,"Rocks"))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                center_ychange = 10
            if event.key == pygame.K_s:
                center_ychange = -10
            if event.key == pygame.K_a:
                center_xchange = 10
            if event.key == pygame.K_d:
                center_xchange = -10
            if event.key == pygame.K_o:
                window_change = -0.02
            if event.key == pygame.K_i:
                window_change = 0.02
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
                window_change = -0
            if event.key == pygame.K_i:
                window_change = 0
    if window + window*window_change < 12250 and window + window*window_change > 240: window += window*window_change
    center_xdis += center_xchange
    center_ydis += center_ychange
    
    for T in tiles:
        window_blit(T)
        if T.surf == blueprint:
            builder = max([x.traits[4] for x in humans if x.traits[4] > 0])
            for x in humans:
                if x.traits[4] == builder: builder = x
            if not ["Build",T] in builder.tasks and not ["Build",T,"Gathering"] in builder.tasks:
                builder.tasks.append(["Build",T])
                
    for M in materials:
        if not M.holder: window_blit(M)
    
    for H in humans:
        wherethefuckdoesthesecomefromimlosingmymind(0)
        window_blit(H)
        task_index_start = 0
        for i,t in enumerate(H.tasks):
            if t == ["Idle"]:
                H.tasks = [x for x in H.tasks if x != ["Idle"]]
                H.tasks.append(t)
            if "Impossible" in t and i == task_index_start or "Gathering" in t and i == task_index_start:
                if t[0] == "Gather":
                    for m in materials:
                        if m.name == t[1][0] and not m.holder:
                            try: t.remove("Impossible")
                            except: pass
                if t[0] == "Build":
                    inv_names = []
                    for x in H.inventory:
                        if x.name in t[1].info[0][1] and len(inv_names) < len(t[1].info[0][1]):
                            inv_names.append(x.name)
                    if inv_names == t[1].info[0][1]:
                        try: t.remove("Gathering")
                        except: pass
                task_index_start = i+1
                wherethefuckdoesthesecomefromimlosingmymind(1)
        if H.tasks[task_index_start][0] == "Gather":
            for t in H.tasks:
                if t[0] == "Build":
                    if t[1].info[0][1] == H.tasks[task_index_start][1] and not "Gathering" in t:
                        wherethefuckdoesthesecomefromimlosingmymind(2.1)
                        H.tasks[task_index_start][1].extend(t[1].info[0][1])
                        wherethefuckdoesthesecomefromimlosingmymind(2)
                        t.append("Gathering")
            target = None
            for m in materials:
                if m.name == H.tasks[task_index_start][1][0] and not m.holder:
                    target = m
            if not target:
                if not "Impossible" in H.tasks[task_index_start]:
                    H.tasks[task_index_start].append("Impossible")
            else:
                try: H.tasks[task_index_start][0].remove("Impossible")
                except: pass
                if dis(H.absC,target.absC) > 70:
                    angle = angleturn(H.absC,target.absC)
                    H.absC = [H.absC[0] + vectorcomponent(angle,H.traits[1]/5,"x"),H.absC[1] + vectorcomponent(angle,H.traits[1]/5,"y")]
                    H.surf = pygame.transform.rotate(man, -angle)
                else:
                    target.holder = H
                    H.inventory.append(target)
                    H.tasks[task_index_start][2].append(target.name)
                    wherethefuckdoesthesecomefromimlosingmymind(3)
            if H.tasks[task_index_start][1] == H.tasks[task_index_start][2]:
                H.tasks.remove(H.tasks[task_index_start])
                wherethefuckdoesthesecomefromimlosingmymind(4)
        elif H.tasks[task_index_start][0] == "Build":
            inv_names = []
            for x in H.inventory:
                if x.name in H.tasks[task_index_start][1].info[0][1] and len(inv_names) < len(H.tasks[task_index_start][1].info[0][1]):
                    inv_names.append(x.name)
            if inv_names != H.tasks[task_index_start][1].info[0][1]:
                if not "Gathering" in H.tasks[task_index_start]:
                    H.tasks[task_index_start].append("Gathering")
                    H.tasks.insert(0,["Gather",list(H.tasks[task_index_start][1].info[0][1]),[]]) #format: [Gather, names of resources needed, resources gathered]
                    wherethefuckdoesthesecomefromimlosingmymind(5)
            else:
                if dis(H.absC,H.tasks[task_index_start][1].absC) > 70:
                    angle = angleturn(H.absC,H.tasks[task_index_start][1].absC)
                    H.absC = [H.absC[0] + vectorcomponent(angle,H.traits[1]/5,"x"),H.absC[1] + vectorcomponent(angle,H.traits[1]/5,"y")]
                    H.surf = pygame.transform.rotate(man, -angle)
                else:
                    wherethefuckdoesthesecomefromimlosingmymind(6)
                    for i in H.tasks[task_index_start][1].info[0][1]:
                        repeat = False
                        for i2 in H.inventory:
                            if i== i2.name and not repeat:
                                repeat = True
                                H.inventory.remove(i2)
                                i2.holder = H.tasks[0][1]
                                H.tasks[task_index_start][1].inventory.append(i2)
                                H.tasks[task_index_start][1].info[0][1].remove(i)
                                wherethefuckdoesthesecomefromimlosingmymind(7)
                    screen.blit(pb,(abswin_convert(H.absC[0],"abs","x"),abswin_convert(H.absC[1],"abs","y")))
                    pb = pygame.transform.scale(pb,(1+((H.tasks[task_index_start][1].info[1][0]/H.tasks[task_index_start][1].info[1][1])*70),10))
                    H.tasks[task_index_start][1].info[1][0] += H.traits[4]/60
                    wherethefuckdoesthesecomefromimlosingmymind(8)
                    if H.tasks[task_index_start][1].info[1][0] > 20:
                        H.tasks[task_index_start][1].surf = stone
                        H.tasks.remove(H.tasks[task_index_start])
        elif H.tasks[task_index_start] == ["Idle"]:
            if H.idleprocess[0][0] < 0:
                if H.idleprocess[0][1] == 0:
                    xmove = random.randint(-5,5)/5
                    ymove = random.randint(-5,5)/5
                    H.idleprocess[1] = [xmove,ymove]
                    H.idleprocess[0][0] = 5
                    H.idleprocess[0][1] = 1
                else:
                    H.idleprocess[1] = [0,0]
                    H.idleprocess[0][0] = 5
                    H.idleprocess[0][1] = 0
            origC = H.absC
            H.absC = [H.absC[0] + H.idleprocess[1][0],H.absC[1] + H.idleprocess[1][1]]
            if H.absC != origC: H.surf = pygame.transform.rotate(man, -angleturn(origC,H.absC))
            H.idleprocess[0][0] -= 1/60
                
    wherethefuckdoesthesecomefromimlosingmymind(9)        
    pygame.display.update()
    clock.tick(60)