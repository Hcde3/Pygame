import pygame
import file
import random

class Block:
    def __init__(self, column, row, blocktype, health):
        self.surf = pygame.Surface((50,50))
        self.rect = pygame.Surface((50,50)).get_rect(topleft = (column*50,row*50))
        self.blocktype = blocktype
        self.absX = column*50
        self.absY = row*50
        self.center = (column*50 + 25,row*50 + 25)
        self.health = health
        self.column = column
        self.row = row
        self.showing = False

class Player:
    def __init__(self, surf, rect, absX, absY):
        self.surf = surf
        self.rect = rect
        self.absX = absX
        self.absY = absY
        self.center = (absX + (surf.get_width()/2),absY + (surf.get_height()/2))
        self.velocity = (0,0)
        
def window_blit(self):
    self.rect.x = self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
    self.rect.y = self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)
    new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
    new_surface = new_surface.convert_alpha()
    self.rect = new_surface.get_rect(topleft = (self.rect.x,self.rect.y))
    screen.blit(new_surface,self.rect)

def seedcreate():
    file.filereplace("WorldData\Data.txt", "WorldData\DataBase.txt")
    ores = ["i","G","D"]
    orerate = [970,990,999]
    orevein = [800,700,800]
    oreheight = [124,164,217]
    for s in range(476):
        if s < 21 or s > 456:
            farlands = True
        else:
            farlands = False
        bt_data = file.fileread("WorldData\Data.txt",s)
        for i in range(len(bt_data)):
            if bt_data[i] == "s":
                for I,o in enumerate(ores):
                    if i >= oreheight[I]:
                        close = False
                        if bt_data[i+1] == o or bt_data[i-1] == o:
                            close = True
                        elif file.fileread("WorldData\Data.txt",s+1)[i] == o or file.fileread("WorldData\Data.txt",s-1)[i] == o:
                            close = True
                        if close and random.randint(1,1000) > orevein[I]:
                            bt_data = bt_data[:i] + o + bt_data[i+1:]
                        elif random.randint(1,1000) > orerate[I]:
                            bt_data = bt_data[:i] + o + bt_data[i+1:]
            if bt_data[i] == "g":
                if random.randint(1,1000) >= 950:
                    bt_data = bt_data[:i-1] + "w" + bt_data[i:]
                    bt_data = bt_data[:i-2] + "w" + bt_data[i-1:]
                    bt_data = bt_data[:i-3] + "w" + bt_data[i-2:]
                    bt_data = bt_data[:i-4] + "l" + bt_data[i-3:]
                    bt_data = bt_data[:i-5] + "l" + bt_data[i-4:]
                    bt_data_2 = file.fileread("WorldData\Data.txt",s-1)
                    bt_data_2 = bt_data_2[:i-4] + "l" + bt_data_2[i-3:]
                    file.filewrite("WorldData\Data.txt",s-1,bt_data_2.strip())
                    bt_data_2 = file.fileread("WorldData\Data.txt",s+1)
                    bt_data_2 = bt_data_2[:i-4] + "l" + bt_data_2[i-3:]
                    file.filewrite("WorldData\Data.txt",s+1,bt_data_2.strip())
            if farlands:
                bt_data = bt_data[:i] + "B" + bt_data[i+1:]
        file.filewrite("WorldData\Data.txt",s,bt_data.strip())
        screen.blit(loadingseedscreen,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        
def inventoryadd(block,amm,default_pos):
    present = False
    for I,i in enumerate(inventory):
        if i[0] == block:
            inventory[I] = [i[0],i[1] + amm]
            present = True
    if not present:
        pos = default_pos
        for i in inventory:
            if i[0] == "Air":
                pos = inventory.index(i)
                inventory[pos] = [block,amm]
                return
        try: inventory.insert(pos,[block,amm])
        except: inventory.insert(-1,[block,amm])

def inventoryremoveblock(block,amm):
    for I,i in enumerate(inventory):
        if i[0] == block:
            inventory[I] = [i[0],i[1] - amm]
            present = True
            if i[1] - amm <= 0:
                inventory.remove(inventory[I])
                inventory.insert(I,["Air",1])
        
def blockinfocheck(inp,input_index,output_index):
    for b in blockinfo:
        try:
            if b[input_index] == inp:
                return b[output_index]
        except:
            return "Failed"
    return "Failed"

def iteminfocheck(inp,input_index,output_index):
    for i in iteminfo:
        try:
            if i[input_index] == inp:
                return i[output_index]
        except:
            return "Failed"
    return "Failed"

def listify(string):
    open_bracket_index = 0
    new_list = []
    for i,s in enumerate(string):
        if s == "(" or s == "[":
            open_bracket_index = i+1
        if s == ")" or s == "]":
            variable = string[open_bracket_index:i]
            temp = variable
            last_comma = 0
            commas = 0
            variable = [None,None,""]
            for i2,v in enumerate(temp):
                if v == ",":
                    variable[commas] = temp[last_comma:i2]
                    commas += 1
                    last_comma = i2+1
                if commas == 2:
                    if v != ",":
                        variable[2] = variable[2] + v
            new_list.append(variable)
    return new_list
#blockinfo = (Blocktype,LoadSymbol,Health,Optimal_Tool)
blockinfo = [["Air","a",0,"Sword"],["Bedrock","B",100000000,"Pickaxe"],["Chest","c",1,"Axe"],["Diamond","D",3,"Pickaxe"],["Dirt","d",0.5,"Shovel"],["Furnace","f",1,"Pickaxe"],["Gold","G",3,"Pickaxe"],["Grass","g",0.5,"Shovel"],["Iron","i",2,"Pickaxe"],["Leaf","l",0.1,"Sword"],["Stone","s",1,"Pickaxe"],["Wood","w",1,"Axe"],["Wood Planks","p",1,"Axe"]]
#iteminfo = (ItemName,ItemType,ItemMultiplier,Stack)
iteminfo = [["Diamond Axe","Axe",5,1],["Diamond Pickaxe","Pickaxe",5,1],["Gold Axe","Axe",6,1],["Gold Pickaxe","Pickaxe",6,1],["Iron Axe","Axe",4,1],["Iron Pickaxe","Pickaxe",4,1],["Sticks","Sticks",1,64],["Stone Axe","Axe",3,1],["Stone Pickaxe","Pickaxe",3,1],["Wood Axe","Axe",2,1],["Wood Pickaxe","Pickaxe",2,1],["Wood Sword","Sword",2,1]]
pygame.init()
window_sz = 1000
window = window_sz
screen = pygame.display.set_mode((window_sz,window_sz))
center_xdis = 0
center_ydis = 0
pygame.display.set_caption("CraftMine")
void = pygame.Surface((window_sz,window_sz))
clock = pygame.time.Clock()


inventory = []
steve = pygame.image.load(f"Graphics\Steve.png").convert_alpha()
font = pygame.font.Font("Graphics\Font\MinecraftRegular-Bmg3.otf",20)
loadingseedscreen = pygame.image.load("Graphics\Loading Screen.png").convert_alpha()
slot = pygame.image.load("Graphics\Slot.png").convert_alpha()
s_slot = pygame.image.load("Graphics\SelectedSlot.png").convert_alpha()
c_slot = pygame.image.load("Graphics\CraftingSlot.png").convert_alpha()
cout_slot = pygame.image.load("Graphics\CraftOutput.png").convert_alpha()
cout_rect = c_slot.get_rect(topleft = (window_sz/2+180-100+60,window_sz/2+60-330))
slot_r = slot.get_rect(topleft = (0,0))
slots = []
for y in range(-140,140,70):
    for x in range(-140,140,70):
        slots.append(slot.get_rect(topleft = (window_sz/2+x+35,window_sz/2+y+10)))
c_slots = []
for y in range(3):
    for x in range(3):
        c_slots.append(((slot.get_rect(topleft = (window_sz/2+(x*60)-100,window_sz/2+(y*60)-330))),(y,x)))
c_inventory = [(None,0,(0,0)),(None,0,(0,1)),(None,0,(0,2)),(None,0,(1,0)),(None,0,(1,1)),(None,0,(1,2)),(None,0,(2,0)),(None,0,(2,1)),(None,0,(2,2))]
c_layout = []
woodplanks_recipe = [["N","N","N","N","N","N","N","N","Wood"],["N","N","N","N","N","N","N","Wood","N"],["N","N","N","N","N","N","Wood","N","N"],["N","N","N","N","N","Wood","N","N","N"],["N","N","N","N","Wood","N","N","N","N"],["N","N","N","Wood","N","N","N","N","N"],["N","N","Wood","N","N","N","N","N","N"],["N","Wood","N","N","N","N","N","N","N"],["Wood","N","N","N","N","N","N","N","N"]]
sticks_recipe = [["Wood Planks","N","N","Wood Planks","N","N","N","N","N"],["N","Wood Planks","N","N","Wood Planks","N","N","N","N"],["N","N","Wood Planks","N","N","Wood Planks","N","N","N"],["N","N","N","Wood Planks","N","N","Wood Planks","N","N"],["N","N","N","N","Wood Planks","N","N","Wood Planks","N"],["N","N","N","N","N","Wood Planks","N","N","Wood Planks"]]
woodpickaxe_recipe = [["Wood Planks","Wood Planks","Wood Planks","N","Sticks","N","N","Sticks","N"]]
stonepickaxe_recipe = [["Stone","Stone","Stone","N","Sticks","N","N","Sticks","N"]]
ironpickaxe_recipe = [["Iron","Iron","Iron","N","Sticks","N","N","Sticks","N"]]
goldpickaxe_recipe = [["Gold","Gold","Gold","N","Sticks","N","N","Sticks","N"]]
diamondpickaxe_recipe = [["Diamond","Diamond","Diamond","N","Sticks","N","N","Sticks","N"]]
woodaxe_recipe = [["N","Wood Planks","Wood Planks","N","Sticks","Wood Planks","N","Sticks","N"]]
stoneaxe_recipe = [["N","Stone","Stone","N","Sticks","Stone","N","Sticks","N"]]
ironaxe_recipe = [["N","Iron","Iron","N","Sticks","Iron","N","Sticks","N"]]
goldaxe_recipe = [["N","Gold","Gold","N","Sticks","Gold","N","Sticks","N"]]
diamondaxe_recipe = [["N","Diamond","Diamond","N","Sticks","Diamond","N","Sticks","N"]]
chest_recipe = [["Wood Planks","Wood Planks","Wood Planks","Wood Planks","N","Wood Planks","Wood Planks","Wood Planks","Wood Planks"]]
furnace_recipe = [["Stone","Stone","Stone","Stone","N","Stone","Stone","Stone","Stone"]]
recipes = [chest_recipe,diamondaxe_recipe,diamondpickaxe_recipe,furnace_recipe,goldaxe_recipe,goldpickaxe_recipe,ironaxe_recipe,ironpickaxe_recipe,sticks_recipe,stoneaxe_recipe,stonepickaxe_recipe,woodaxe_recipe,woodpickaxe_recipe,woodplanks_recipe]
recipes_o = [("Chest",1),("Diamond Axe",1),("Diamond Pickaxe",1),("Furnace",1),("Gold Axe",1),("Gold Pickaxe",1),("Iron Axe",1),("Iron Pickaxe",1),("Sticks",4),("Stone Axe",1),("Stone Pickaxe",1),("Wood Axe",1),("Wood Pickaxe",1),("Wood Planks",4)]


ans = input("Generate new seed?\n")
if ans == "y":
    seedcreate()
elif ans == "e":
    file.filereplace("WorldData\Data.txt","WorldData\Example.txt")
blocks = []
for b in range(1):
    column = b + 239
    blocktypes = file.fileread("WorldData\Data.txt",column)
    for i,t in enumerate(blocktypes):
        t = blockinfocheck(t,1,0)
        h = blockinfocheck(t,0,2)
        if t == "Failed":
            t = "Bedrock"
            h = blockinfocheck("Bedrock",0,2)
        blocks.append(Block(column, i, t, h))
        blocks[-1].surf = pygame.image.load(f"Graphics\{t}.png").convert_alpha()


player_rect = steve.get_rect(topleft = (0,0))
p = Player(steve, player_rect, 11925, 5150)
x_move = 0
jumping = False
timer = 0
breaking = False
building = False
mp = (-100,-100)
primary_block = "Air"
primary_item = "Air"
selected_slot = 0
tickspeed = 120
inventoryopen = 1
invload = True
helditem = False
craftingopen = -1
swapping = True
item_lost = True
items_on_open = None

items_on_open = listify(file.fileread("WorldData\PlayerData.txt",0)[1:-2])
for I,i in enumerate(items_on_open):
    i[0] = i[0].replace("'","")
    inventory.insert(int(i[2]),[i[0],int(i[1])])
while True:
    right_voided = True
    left_voided = True
    screen.blit(void,(0,0))
    for event in pygame.event.get():
        mp = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            save_inventory = []
            for I,i in enumerate(inventory):
                save_inventory.append([i[0],i[1],I])
            file.filewrite("WorldData\PlayerData.txt",0,f"{save_inventory}")
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if inventoryopen == 1:
                    for s in range(len(slots)):
                        if slots[s].collidepoint(mp):
                            try:
                                if inventory[s][0] != "Air":
                                    helditem = inventory[s]
                                    helditem_index = s
                                    inventory[s] = ["Air",1]
                            except: pass
                    if cout_rect.collidepoint(mp):
                       for i,R in enumerate(recipes):
                            for r in R:
                                if r == c_layout:
                                    inventoryadd(recipes_o[i][0],recipes_o[i][1],-1)
                                    for i,c in enumerate(c_inventory):
                                        if c[0] != None:
                                            c_inventory[i] = (c[0],c[1]-1,c[2])
                                            if c_inventory[i][1] <= 0:
                                                c_inventory[i] = (None,0,c[2])
                else:
                    breaking = True
            if event.button == 3:
                if craftingopen == 1 or inventoryopen == 1:
                    for C in range(len(c_slots)):
                        if helditem and swapping:
                            for s in range(len(slots)):
                                if slots[s].collidepoint(mp):
                                    try:
                                        if helditem:
                                            if inventory[s][0] == helditem[0]:
                                                if inventory[s] == inventory[helditem_index] and inventory[helditem_index] == helditem:
                                                    inventory[s] = inventory[s]
                                                    helditem = False
                                                else:
                                                    inventory[s] = (helditem[0],inventory[s][1] + 1)
                                            else:
                                                if inventory[s][0] != "Air":
                                                    inventory[helditem_index] = inventory[s]
                                                    inventory[s] = (helditem[0],1)
                                                else:
                                                    inventory[s] = (helditem[0],1)
                                            helditem = (helditem[0],helditem[1]-1)
                                            swapping = False
                                            if helditem[1] <= 0:
                                                helditem = False
                                    except:
                                        if helditem:
                                            inventoryremoveblock(helditem[0],1)
                                            inventory.insert(s,(helditem[0],1))
                                            helditem = (helditem[0],helditem[1]-1)
                                            if helditem[1] <= 0:
                                                helditem = False
                            if c_slots[C][0].collidepoint(mp):
                                try:
                                    c_inventory[c_inventory.index((None,0,c_slots[C][1]))] = (helditem[0],1,c_slots[C][1])
                                    helditem = (helditem[0],helditem[1]-1)
                                except:
                                    for i,c in enumerate(c_inventory):
                                        if c[0] == helditem[0] and c_slots[C][1] == c[2]:
                                            c_inventory[i] = (helditem[0],c[1] + 1,c_slots[C][1])
                                            helditem = (helditem[0],helditem[1]-1)
                                if helditem[1] <= 0:
                                    helditem = False
                        else:
                            if c_slots[C][0].collidepoint(mp):
                                for i,c in enumerate(c_inventory):
                                        if c[0] != None and c[2] == c_slots[C][1]:
                                            inventoryadd(c[0],c[1],-1)
                                            c_inventory[i] = (None,0,c_slots[C][1])
                else:
                    building = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                breaking = False
                if helditem:
                    item_lost = True
                    for s in range(len(slots)):
                        if slots[s].collidepoint(mp):
                            try:
                                if helditem[0] == inventory[s][0]:
                                    inventory[s] = [helditem[0],inventory[s][1] + helditem[1]]    
                                else:
                                    inventory[helditem_index] = inventory[s]
                                    inventory[s] = helditem
                            except:
                                inventory.remove(helditem)
                                inventory.insert(s,helditem)
                            item_lost = False
                    for s in range(len(c_slots)):
                        if c_slots[s][0].collidepoint(mp):
                            try: c_inventory[c_inventory.index((None,0,c_slots[s][1]))] = (helditem[0],helditem[1],c_slots[s][1]); inventoryremoveblock(helditem[0],helditem[1])
                            except:
                                for i,c in enumerate(c_inventory):
                                    if c[0] == helditem[0] and c_slots[s][1] == c[2]:
                                        c_inventory[i] = (helditem[0],c[1] + helditem[1],c_slots[s][1])
                                        inventoryremoveblock(helditem[0],helditem[1])
                            item_lost = False
                    if item_lost:
                        inventory[helditem_index] = helditem
                        item_lost = True                    
                    helditem = False
            if event.button == 3:
                building = False
                swapping = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                jumping = True
            if event.key == pygame.K_d:
                x_move = 6
            if event.key == pygame.K_a:
                x_move = -6
            if event.key == pygame.K_e:
                inventoryopen *= -1
                craftingopen *= -1
                helditem = False
            if event.key == pygame.K_1:
                selected_slot = 0
            if event.key == pygame.K_2:
                selected_slot = 1
            if event.key == pygame.K_3:
                selected_slot = 2
            if event.key == pygame.K_4:
                selected_slot = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                jumping = False
            if event.key == pygame.K_d:
                x_move = 0
            if event.key == pygame.K_a:
                x_move = 0
    for I,B in enumerate(blocks):
        if abs(B.absX-p.absX) <= window_sz/2+200:
            if abs(B.absY-p.absY) <= window_sz/2+200:
                window_blit(B)
                B.showing = True
        else:
            blocktypes = ""
            forremoval = []
            for i in blocks:
                if i.column == B.column:
                    i.showing = False
                    if blockinfocheck(i.blocktype,0,1) == "Failed":
                        blocktypes = blocktypes + "B"
                    else:
                        blocktypes = blocktypes + blockinfocheck(i.blocktype,0,1)
                    forremoval.append(i)
            for fr in forremoval:
                blocks.remove(fr)
            file.filewrite("WorldData\Data.txt",B.column,blocktypes)
        if B.rect.collidepoint(window_sz+15,500):
            r_column = B.column
            right_voided = False
        if B.rect.collidepoint(-15,500):
            left_voided = False
            l_column = B.column
        if B.showing:
            if B.blocktype == "Bedrock":
                B.health = 100000000
            if B.rect.collidepoint(mp):
                if breaking and B.blocktype != "Air":
                    if blockinfocheck(B.blocktype,0,3) == iteminfocheck(inventory[selected_slot][0],0,1):
                        B.health -= (1*iteminfocheck(iteminfocheck(inventory[selected_slot][0],0,0),0,2))/tickspeed
                    else:
                        B.health -= 1/tickspeed
                    if B.health <= 0:
                        inventoryadd(B.blocktype,1,-1)
                if building and B.blocktype == "Air" and not B.rect.colliderect(p.rect) and blockinfocheck(inventory[selected_slot][0],0,0) != "Failed":
                    B.blocktype = blockinfocheck(inventory[selected_slot][0],0,0)
                    B.health = blockinfocheck(inventory[selected_slot][0],0,2)
                    B.surf = pygame.image.load(f"Graphics\{blockinfocheck(inventory[selected_slot][0],0,0)}.png").convert_alpha()
                    inventoryremoveblock(blockinfocheck(inventory[selected_slot][0],0,0),1)
            if B.health <= 0 and not B.health == -699.127:
                B.blocktype = "Air"
                B.surf = pygame.image.load("Graphics\Air.png").convert_alpha()
                B.health = -699.127
            if p.rect.colliderect(B.rect) and B.blocktype != "Air":
                if abs(p.center[0] - B.center[0]) < abs(p.center[1] - B.center[1])  and p.center[1] < B.center[1]:
                    if p.velocity[1] > 0:
                        p.velocity = (0.7*p.velocity[0],-0.3*p.velocity[1])
                        p.absY = B.absY - p.surf.get_height()
                    if jumping:
                        p.velocity = (p.velocity[0],p.velocity[1] -  5)
                        jumping = False
                elif abs(p.center[0] - B.center[0]) < abs(p.center[1] - B.center[1])  and p.center[1] > B.center[1]:
                    if p.velocity[1] < 0:
                        p.velocity = (0.7*p.velocity[0],-0.3*p.velocity[1])
                elif abs(p.center[0] - B.center[0]) > abs(p.center[1] - B.center[1])  and p.center[0] < B.center[0]:
                    if p.velocity[0] > 0:
                        p.velocity = (-0.3*p.velocity[0],0.7*p.velocity[1])
                        p.absX = B.absX - p.surf.get_width()
                else:
                    if p.velocity[0] < 0:
                        p.velocity = (-0.3*p.velocity[0],0.7*p.velocity[1])
                        p.absX = B.absX + p.surf.get_width()
    p.velocity = (x_move, p.velocity[1] + 9.8/tickspeed)
    p.absX += p.velocity[0]
    p.absY += p.velocity[1]
    p.center = (p.absX + (p.surf.get_width()/2),p.absY + (p.surf.get_height()/2))
    center_xdis = (window_sz/2) - p.absX
    center_ydis = (window_sz/2) - p.absY
    window_blit(p)
    
    
    for inv_i,i in enumerate(inventory):
        if inv_i <= 3:
            if selected_slot == inv_i: screen.blit(s_slot,(inv_i*70,0))
            else: screen.blit(slot,(inv_i*70,0))
            try:
                screen.blit(pygame.image.load(f"Graphics\{i[0]}.png").convert_alpha(),((inv_i*70)+5,0+5))
                if inventory[inv_i][1] == 1: pass
                else:
                    if i[1] < 10:
                        screen.blit(font.render(f"{i[1]}",True,"White"),((inv_i*70)+40,0+35))
                    else:
                        screen.blit(font.render(f"{i[1]}",True,"White"),((inv_i*70)+25,0+35))
            except:
                inventory.insert(inv_i,("Air",1))
    if inventoryopen == 1:
        inv_i = -1
        added = False
        for y in range(-140,140,70):
            inv_i += 1
            added = True
            for x in range(-140,140,70):
                if not added:
                    inv_i += 1
                if selected_slot == inv_i: screen.blit(s_slot,(window_sz/2+x+35,window_sz/2+y+10))
                else: screen.blit(slot,(window_sz/2+x+35,window_sz/2+y+10))
                try:
                    screen.blit(pygame.image.load(f"Graphics\{inventory[inv_i][0]}.png").convert_alpha(),(window_sz/2+x+40,window_sz/2+y+15))
                    if inventory[inv_i][1] == 1: pass
                    else:
                        if inventory[inv_i][1] < 10:
                            screen.blit(font.render(f"{inventory[inv_i][1]}",True,"White"),(window_sz/2+x+75,window_sz/2+y+45))
                        else:
                            screen.blit(font.render(f"{inventory[inv_i][1]}",True,"White"),(window_sz/2+x+60,window_sz/2+y+45))
                except:
                    inventory.insert(inv_i,("Air",1))
                added = False
    
    if craftingopen == 1:
        c_layout = []
        screen.blit(cout_slot,(window_sz/2+180-100,window_sz/2+60-330))
        for y in range(3):
            for x in range(3):
                screen.blit(c_slot,(window_sz/2+(x*60)-100,window_sz/2+(y*60)-330))
                for c in c_inventory:
                    if c[2] == (y,x):
                        if c[0] != None:
                            screen.blit(pygame.image.load(f"Graphics\{c[0]}.png").convert_alpha(),(window_sz/2+(x*60)-95,window_sz/2+(y*60)-325))
                            if c[1] == 1: pass
                            else:
                                if c[1] < 10:
                                    screen.blit(font.render(f"{c[1]}",True,"White"),(window_sz/2+(x*60)-95+35,window_sz/2+(y*60)-325+30))
                                else:
                                    screen.blit(font.render(f"{c[1]}",True,"White"),(window_sz/2+(x*60)-95+20,window_sz/2+(y*60)-325+30))
                            c_layout.append(c[0])
                        else:
                            c_layout.append("N")
        for i,R in enumerate(recipes):
            for r in R:
                if r == c_layout:
                    screen.blit(pygame.image.load(f"Graphics\{recipes_o[i][0]}.png").convert_alpha(),(window_sz/2+185-100+60,window_sz/2+65-330))
                    if recipes_o[i][1] == 1: pass
                    else:
                        if recipes_o[i][1] < 10:
                            screen.blit(font.render(f"{recipes_o[i][1]}",True,"White"),(window_sz/2+185-100+60+35,window_sz/2+65-330+30))
                        else:
                            screen.blit(font.render(f"{recipes_o[i][1]}",True,"White"),(window_sz/2+185-100+60+20,window_sz/2+65-330+30))
                
            
    
    if helditem:
        screen.blit(pygame.image.load(f"Graphics\{helditem[0]}.png").convert_alpha(),mp)
    
    if right_voided and blocks[-1].column + 1 <= 477:
        column = blocks[-1].column + 1
        blocktypes = file.fileread("WorldData\Data.txt",column)
        for i,t in enumerate(blocktypes):
            skip = False
            t = blockinfocheck(t,1,0)
            h = blockinfocheck(t,0,2)
            if t == "Failed":
                if len(blocks) > 0:
                    if blocks[-1].blocktype == "Bedrock":
                        skip = True
                    else:
                        t = "Bedrock"
                        h =blockinfocheck("Bedrock",0,2)
            if not skip:
                blocks.append(Block(column, i, t, h))
                blocks[-1].surf = pygame.image.load(f"Graphics\{t}.png").convert_alpha()
    if left_voided and blocks[0].column - 1 >= 0:
        column = blocks[0].column - 1
        l_column = column
        blocktypes = file.fileread("WorldData\Data.txt",column)
        new_blocks = []
        for i,t in enumerate(blocktypes):
            skip = False
            t = blockinfocheck(t,1,0)
            h = blockinfocheck(t,0,2)
            if t == "Failed":
                if len(new_blocks) > 0:
                    if new_blocks[-1].blocktype == "Bedrock":
                        skip = True
                    else:
                        t = "Bedrock"
                        h =blockinfocheck("Bedrock",0,2)
            if not skip:
                new_blocks.append(Block(column, i, t, h))
                new_blocks[-1].surf = pygame.image.load(f"Graphics\{t}.png").convert_alpha()
        new_blocks.extend(blocks)
        blocks = new_blocks
    timer += 1/tickspeed
    if invload:
        invload = False
        inventoryopen = -1
    pygame.display.update()
    clock.tick(tickspeed)