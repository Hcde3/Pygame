import pygame
import random
import math
from pygame.locals import *
flags = FULLSCREEN | DOUBLEBUF


window_sz = 1500
window = window_sz

while True:
    pygame.init()
    screen = pygame.display.set_mode((2560,1440), flags)
    screen.set_alpha(None)
    pygame.display.set_caption("Cell Evolution")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None ,20)
    big_font = pygame.font.Font(None ,50)
    text = font.render("Info",True,"White")
    void = pygame.Surface((2560,1440))
    
    settings = True
    clock_body = pygame.Surface((100,100))
    clock_body.fill("White")
    clock_outline = pygame.Surface((120,120))
    clock_rect = clock_outline.get_rect(topleft = (495,790))
    clock_outline.fill("Grey")
    clock_head = pygame.Surface((50,20))
    clock_head.fill("Dark Grey")
    clock_Shand = pygame.Surface((40,5))
    clock_Bhand = pygame.Surface((5,50))
    clock_flame = pygame.Surface((150,150))
    clock_flame.fill("Red")
    clock_Iflame = pygame.Surface((130,130))
    clock_Iflame.fill("Orange")
    flameline = pygame.Surface((20,60))
    flameline.fill("Red")
    
    set_cell = pygame.Surface((90,90))
    set_cell.fill("Blue")
    set_cell_outline = pygame.Surface((110,110))
    set_cell_outline.fill("Dark Blue")
    set_cell_rect = set_cell_outline.get_rect(topleft = (920,790))
    set_cellbump = pygame.Surface((30,30))
    set_cellbump.fill("Blue")
    set_cellbump_outline = pygame.Surface((50,50))
    set_cellbump_outline.fill("Dark Blue")
    set_cellshine = pygame.Surface((20,10))
    set_cellshine.fill("White")
    
    map_box = pygame.Surface((300,300))
    map_box.fill([10,10,10])
    map_box_outline = pygame.Surface((350,350))
    map_box_outline.fill("White")
    set_pellet = pygame.Surface((2,2))
    set_pellet.fill("White")
    set_bud = pygame.Surface((8,8))
    set_bud.fill("Dark Green")
    random_rect = map_box_outline.get_rect(topleft = (175+205,175))
    random_pellets = []
    random_buds = []
    random_TF = False
    split_rect = map_box_outline.get_rect(topleft = (575+205,175))
    split_pellets = []
    split_buds = []
    split_TF = False
    circle1_rect = map_box_outline.get_rect(topleft = (975+205,175))
    circle1_pellets = []
    circle1_buds = []
    circle1_TF = False
    circle2_rect = map_box_outline.get_rect(topleft = (1375+205,175))
    circle2_pellets = []
    circle2_buds = []
    circle2_TF = False
    
    set_gate = pygame.Surface((20,190))
    set_gate.fill("White")
    w_gate = pygame.Surface((200,190))
    w_gate.fill([50,50,50])
    wholegate = w_gate.get_rect(topleft = (1350,750))
    
    smallcell = pygame.Surface((20,20))
    maxedcells = pygame.Surface((200,200))
    cellmax_rect = maxedcells.get_rect(topleft = (1650,750))
    
    go_button = pygame.Surface((300,300))
    go_button.fill("Green")
    go_button_middle = pygame.Surface((100,100))
    go_button_middle.fill("White")
    
    tick_speed_select = 60
    mutation_multiplier = 1
    barrierchoice = 1
    selectedmap = None
    cell_cap = 100
    while settings:
        for event in pygame.event.get():
            pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN])
            mp = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    play = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clock_rect.collidepoint(mp):
                    tick_speed_select *= 2
                    if tick_speed_select > 120:
                        tick_speed_select = 30
                if set_cell_rect.collidepoint(mp):
                    mutation_multiplier *= 2
                    if mutation_multiplier > 2:
                        mutation_multiplier = 0.5
                if wholegate.collidepoint(mp):
                    barrierchoice = abs(barrierchoice-1)
                if random_rect.collidepoint(mp):
                    selectedmap = "random"
                if split_rect.collidepoint(mp):
                    selectedmap = "split"
                if circle1_rect.collidepoint(mp):
                    selectedmap = "circle1"
                if circle2_rect.collidepoint(mp):
                    selectedmap = "circle2"
                if cellmax_rect.collidepoint(mp):
                    cell_cap *= 2
                    if cell_cap > 800:
                        cell_cap = 50
        screen.blit(void,(0,0))
        text = big_font.render("Random",True,"White")
        screen.blit(text,(175+205,145))
        if selectedmap == "random":
            map_box_outline.fill("Green")
            screen.blit(map_box_outline,(175+205,175))
            map_box_outline.fill("White")
        else:
            screen.blit(map_box_outline,(175+205,175))
        screen.blit(map_box,(200+205,200))
        if not random_TF:
            for i in range(300):
                n_x = random.randint(445,665)
                n_y = random.randint(215,475)
                random_pellets.append((n_x,n_y))
            for i in range(40):
                n_x = random.randint(445,665)
                n_y = random.randint(215,475)
                random_buds.append((n_x,n_y))
            random_TF = True
        for rp in random_pellets:
            screen.blit(set_pellet,rp)
        for rb in random_buds:
            screen.blit(set_bud,rb)
        text = big_font.render("Split",True,"White")
        screen.blit(text,(575+205,145))
        if selectedmap == "split":
            map_box_outline.fill("Green")
            screen.blit(map_box_outline,(575+205,175))
            map_box_outline.fill("White")
        else:
            screen.blit(map_box_outline,(575+205,175))
        screen.blit(map_box,(600+205,200))
        if not split_TF:
            for i in range(300):
                n_x = random.randint(445+400,665+400)
                n_y = random.randint(215,475)
                split_pellets.append((n_x,n_y))
            for i in range(40):
                n_x = random.randint(600+400,665+400)
                n_y = random.randint(215,475)
                split_buds.append((n_x,n_y))
            split_TF = True
        for sp in split_pellets:
            screen.blit(set_pellet,sp)
        for sb in split_buds:
            screen.blit(set_bud,sb)
        text = big_font.render("Circle 1",True,"White")
        screen.blit(text,(975+205,145))
        if selectedmap == "circle1":
            map_box_outline.fill("Green")
            screen.blit(map_box_outline,(975+205,175))
            map_box_outline.fill("White")
        else:
            screen.blit(map_box_outline,(975+205,175))
        screen.blit(map_box,(1000+205,200))
        if not circle1_TF:
            for i in range(300):
                circular = False
                while not circular:
                    n_x = random.randint(445+800,665+800)
                    n_y = random.randint(215,475)
                    if math.sqrt((n_x - 1355)**2 + (n_y - 345)**2) <= 150:
                        circle1_pellets.append((n_x,n_y))
                        circular = True
                    else:
                        circular = False
            for i in range(80):
                circular = False
                while not circular:
                    n_x = random.randint(445+800,665+800)
                    n_y = random.randint(215,475)
                    if math.sqrt((n_x - 1355)**2 + (n_y - 345)**2) <= 50:
                        circle1_buds.append((n_x,n_y))
                        circular = True
                    else:
                        circular = False
            circle1_TF = True
        for c1p in circle1_pellets:
            screen.blit(set_pellet,c1p)
        for c1b in circle1_buds:
            screen.blit(set_bud,c1b)
        text = big_font.render("Circle 2",True,"White")
        screen.blit(text,(1375+205,145))
        if selectedmap == "circle2":
            map_box_outline.fill("Green")
            screen.blit(map_box_outline,(1375+205,175))
            map_box_outline.fill("White")
        else:
            screen.blit(map_box_outline,(1375+205,175))
        screen.blit(map_box,(1400+205,200))
        if not circle2_TF:
            for i in range(300):
                circular = False
                while not circular:
                    n_x = random.randint(445+1200,665+1200)
                    n_y = random.randint(215,475)
                    if math.sqrt((n_x - 1755)**2 + (n_y - 345)**2) <= 100:
                        circle2_pellets.append((n_x,n_y))
                        circular = True
                    else:
                        circular = False
            for i in range(100):
                circular = False
                while not circular:
                    n_x = random.randint(445+1200,665+1200)
                    n_y = random.randint(215,475)
                    if math.sqrt((n_x - 1755)**2 + (n_y - 345)**2) <= 125 and math.sqrt((n_x - 1755)**2 + (n_y - 345)**2) >= 100:
                        circle2_buds.append((n_x,n_y))
                        circular = True
                    else:
                        circular = False
            circle2_TF = True
        for c2p in circle2_pellets:
            screen.blit(set_pellet,c2p)
        for c2b in circle2_buds:
            screen.blit(set_bud,c2b)
        
        ## Objects ##
        text = big_font.render("Tick Speed",True,"White")
        screen.blit(text,(465,700))
        if tick_speed_select == 120:
            clock_flame.fill("Red")
            clock_Iflame.fill("Orange")
            flameline.fill("Red")
            screen.blit(clock_flame,(480,775))
            screen.blit(flameline,(490,745))
            screen.blit(flameline,(530,755))
            screen.blit(flameline,(550,735))
            screen.blit(flameline,(590,765))
            screen.blit(clock_Iflame,(490,785))
        elif tick_speed_select == 60:
            pass
        elif tick_speed_select == 30:
            clock_flame.fill("Light Blue")
            clock_Iflame.fill("Blue")
            flameline.fill("Light Blue")
            screen.blit(clock_flame,(480,775))
            screen.blit(flameline,(490,900))
            screen.blit(flameline,(530,920))
            screen.blit(flameline,(550,890))
            screen.blit(flameline,(590,870))
            screen.blit(clock_Iflame,(490,785))
        screen.blit(clock_head,(530,770))
        screen.blit(clock_outline,(495,790))
        screen.blit(clock_body,(505,800))
        screen.blit(clock_Shand,(550,850))
        screen.blit(clock_Bhand,(550,800))
        text = big_font.render("Mutation",True,"White")
        screen.blit(text,(900,700))
        screen.blit(set_cell_outline,(920,790))
        if mutation_multiplier == 1:
            set_cell_outline.fill("Dark Blue")
            set_cell.fill("Blue")
            set_cellbump.fill("Blue")
            set_cellbump_outline.fill("Dark Blue")
            screen.blit(set_cellbump_outline,(1000,785))
            screen.blit(set_cellbump,(1010,795))
            screen.blit(set_cellbump_outline,(910,865))
            screen.blit(set_cellbump,(920,875))
            screen.blit(set_cell,(930,800))
        elif mutation_multiplier == 0.5:
            set_cell_outline.fill("Dark Green")
            set_cell.fill("Green")
            screen.blit(set_cell,(930,800))
            screen.blit(set_cellshine,(990,810))
        elif mutation_multiplier == 2:
            set_cell_outline.fill("Dark Red")
            set_cell.fill("Red")
            set_cellbump.fill("Red")
            set_cellbump_outline.fill("Dark Red")
            screen.blit(set_cellbump_outline,(1000,785))
            screen.blit(set_cellbump,(1010,795))
            screen.blit(set_cellbump_outline,(910,865))
            screen.blit(set_cellbump,(920,875))
            screen.blit(set_cellbump_outline,(910,805))
            screen.blit(set_cellbump,(920,815))
            screen.blit(set_cellbump_outline,(1000,855))
            screen.blit(set_cellbump,(1010,865))
            screen.blit(set_cellbump_outline,(930,765))
            screen.blit(set_cellbump,(940,775))
            screen.blit(set_cell,(930,800))
            screen.blit(set_cellbump_outline,(950,820))
            screen.blit(set_cellbump,(960,830))
        text = big_font.render("Barriers",True,"White")
        screen.blit(text,(1280,700))
        screen.blit(w_gate,(1250,750))
        if barrierchoice:
            set_gate.fill("White")
            screen.blit(set_gate,(1250,750))
            screen.blit(set_gate,(1450,750))
            screen.blit(pygame.transform.rotate(set_gate,90),(1260,750))
            screen.blit(pygame.transform.rotate(set_gate,90),(1260,920))
        else:
            pass
        
        text = big_font.render("Cell Cap",True,"White")
        screen.blit(text,(1680,700))
        if cell_cap == 50:
            smallcell.fill("Blue")
            screen.blit(smallcell,(1750,850))
        if cell_cap == 100:
            smallcell.fill("Green")
            screen.blit(smallcell,(1750,850))
            screen.blit(smallcell,(1700,800))
            screen.blit(smallcell,(1790,800))
            screen.blit(smallcell,(1700,880))
        if cell_cap == 200:
            smallcell.fill("Orange")
            screen.blit(smallcell,(1750,850))
            screen.blit(smallcell,(1700,800))
            screen.blit(smallcell,(1790,800))
            screen.blit(smallcell,(1700,880))
            screen.blit(smallcell,(1750,820))
            screen.blit(smallcell,(1660,770))
            screen.blit(smallcell,(1790,860))
            screen.blit(smallcell,(1850,850))
        if cell_cap == 400:
            smallcell.fill("Red")
            screen.blit(smallcell,(1750,850))
            screen.blit(smallcell,(1700,800))
            screen.blit(smallcell,(1790,800))
            screen.blit(smallcell,(1700,880))
            screen.blit(smallcell,(1750,820))
            screen.blit(smallcell,(1660,770))
            screen.blit(smallcell,(1790,860))
            screen.blit(smallcell,(1850,850))
            screen.blit(smallcell,(1720,830))
            screen.blit(smallcell,(1800,750))
            screen.blit(smallcell,(1790,800))
            screen.blit(smallcell,(1730,870))
            screen.blit(smallcell,(1780,835))
            screen.blit(smallcell,(1830,790))
            screen.blit(smallcell,(1680,860))
            screen.blit(smallcell,(1830,890))
        if cell_cap == 800:
            maxedcells.fill("Purple")
            screen.blit(maxedcells,(1650,750))
        
        screen.blit(go_button,(0,350))
        screen.blit(go_button_middle,(100,450))
        pygame.display.update()
        clock.tick(60)