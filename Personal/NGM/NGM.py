import pygame
import math
import random

def window_blit(self):
    if self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) -(self.surf.get_width()*(window/window_sz))< window_sz and self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) + (self.surf.get_width()*2*(window/window_sz)) > 0 and self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) - (self.surf.get_width()*(window/window_sz)) < window_sz and self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) + (self.surf.get_width()*2*(window/window_sz))> 0:
        new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
        new_surface = new_surface.convert_alpha()
        screen.blit(new_surface,(self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz),self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)))
    
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

class Tile:
    def __init__(self, absX, absY, surf):
        self.absX = absX
        self.absY = absY
        self.surf = surf
        self.biome = None
        
pygame.init()
void = pygame.Surface((1000,1000))
window_sz = 1000
window = window_sz
center_xdis = -1000
center_ydis = -1000
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Ants")
clock = pygame.time.Clock()

biome_variety = 25
mapsize = 3000//50

tile = pygame.image.load("tile.png").convert_alpha()
tiles = []
for y in range(mapsize):
    tiles.extend([Tile(49*y,49*x,tile) for x in range(mapsize)])
hot_biome_choices = ["Desert","Desert","Desert","Jungle","Jungle","Mountain","Plains","Plains","Mesa","Mesa","Swamp"]
cold_biome_choices = ["Artic","Artic","Artic","Mountain","Mountain","Plains","Forest","Water","Taiga","Taiga","Taiga"]
temp_biome_choices = ["Mountain","Plains","Plains","Plains","Plains","Plains","Forest","Forest","Forest","Water","Water","Taiga","Swamp"]
tropical_biome_choices = ["Desert","Jungle","Jungle","Jungle","Mountain","Mountain","Plains","Mesa","Water","Swamp","Swamp"]
biome_choices = random.choice([hot_biome_choices,cold_biome_choices,temp_biome_choices,temp_biome_choices,temp_biome_choices,tropical_biome_choices])
biomes = []
for x in range(biome_variety):
    r = random.randint(0,len(biome_choices) - 1)
    biomes.append(biome_choices[r])
    #biome_choices.remove(biome_choices[r]) 
biomeorgins_X = [random.randint(0,mapsize*50) for x in range(biome_variety)]
biomeorgins_Y = [random.randint(0,mapsize*50) for x in range(biome_variety)]
lakes_X = [random.randint(0,mapsize*50) for x in range(biome_variety)]
lakes_Y = [random.randint(0,mapsize*50) for x in range(biome_variety)]        
for T in tiles:
    distance = 1000000000000000
    biome = "Desert"
    for i,X in enumerate(biomeorgins_X):
        Y = biomeorgins_Y[i]
        if dis((T.absX,T.absY),(X,Y)) < distance:
            biome = biomes[i]
            distance = dis((T.absX,T.absY),(X,Y))
        if dis((T.absX,T.absY),(lakes_X[i],lakes_Y[i])) < 150 and dis((T.absX,T.absY),(lakes_X[i],lakes_Y[i])) < distance:
            biome = "Water"
    T.biome = biome
    T.surf = pygame.image.load(f"{biome}.png").convert_alpha()

for rivrep in range(5):
    river_centre = (random.randint(0,mapsize)*49,random.randint(0,mapsize)*49)
    bias = random.choice(["rise","run"])
    if bias == "rise":
        river_rise = random.randint(-5,5)
        while abs(river_rise) < 2: river_rise = random.randint(-5,5)
        if river_rise <= 0: st_change = -1
        else: st_change = 1
        step = 0
        river_run = random.choice([-1,1])
        current_point = river_centre
        for x in range(2000):
            step += st_change
            if step == river_rise: step = 0
            for T in tiles:
                if (T.absX,T.absY) == current_point: current = T
            current.biome = "Water"
            current.surf = pygame.image.load("Water.png").convert_alpha()
            if step == 0: current_point = (current_point[0] + (river_run*49),current_point[1])
            else: current_point = (current_point[0],current_point[1] + 49)
            if not x%10: river_rise += random.randint(-1,1)
    else:
        river_run = random.randint(-5,5)
        while abs(river_run) < 2: river_run = random.randint(-5,5)
        if river_run <= 0: st_change = -1
        else: st_change = 1
        step = 0
        river_rise = random.choice([-1,1])
        current_point = river_centre
        for x in range(1000):
            step += st_change
            if step == river_run: step = 0
            for T in tiles:
                if (T.absX,T.absY) == current_point: current = T
            current.biome = "Water"
            current.surf = pygame.image.load("Water.png").convert_alpha()
            if step == 0: current_point = (current_point[0],current_point[1] + (river_rise*49))
            else: current_point = (current_point[0] + 49,current_point[1])
            if not x%10:
                change = random.randint(-1,1)
                if abs(river_run + change) < 2:
                    river_run -= change
                else:
                    river_run += change
            

center_xchange = 0
center_ychange = 0
window_change = 0
while True:
    screen.blit(void,(0,0))
    mp = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            hot_biome_choices = ["Desert","Desert","Desert","Jungle","Jungle","Mountain","Plains","Plains","Mesa","Mesa","Swamp"]
            cold_biome_choices = ["Artic","Artic","Artic","Mountain","Mountain","Plains","Forest","Water","Taiga","Taiga","Taiga"]
            temp_biome_choices = ["Mountain","Plains","Plains","Plains","Forest","Forest","Forest","Water","Water","Taiga","Swamp"]
            tropical_biome_choices = ["Desert","Jungle","Jungle","Jungle","Mountain","Mountain","Plains","Mesa","Water","Swamp","Swamp"]
            biome_choices = random.choice([hot_biome_choices,cold_biome_choices,temp_biome_choices,tropical_biome_choices])
            biomes = []
            for x in range(biome_variety):
                r = random.randint(0,len(biome_choices) - 1)
                biomes.append(biome_choices[r])
            biomeorgins_X = [random.randint(0,mapsize*50) for x in range(biome_variety)]
            biomeorgins_Y = [random.randint(0,mapsize*50) for x in range(biome_variety)]
            lakes_X = [random.randint(0,mapsize*50) for x in range(biome_variety)]
            lakes_Y = [random.randint(0,mapsize*50) for x in range(biome_variety)]           
            for T in tiles:
                distance = 1000000000000000
                biome = "Desert"
                for i,X in enumerate(biomeorgins_X):
                    Y = biomeorgins_Y[i]
                    if dis((T.absX,T.absY),(X,Y)) < distance:
                        biome = biomes[i]
                        distance = dis((T.absX,T.absY),(X,Y))
                    if dis((T.absX,T.absY),(lakes_X[i],lakes_Y[i])) < 150 and dis((T.absX,T.absY),(lakes_X[i],lakes_Y[i])) < distance:
                        biome = "Water"
                T.biome = biome
                T.surf = pygame.image.load(f"{biome}.png").convert_alpha()
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
    pygame.display.update()
    clock.tick(60)
    