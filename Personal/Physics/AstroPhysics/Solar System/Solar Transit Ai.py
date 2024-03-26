import pygame
import math
import random

def window_blit(self):
    if self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) -(self.radius*(window/window_sz))< window_sz and self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) + (self.radius*2*(window/window_sz)) > 0 and self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) - (self.radius*(window/window_sz)) < window_sz and self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) + (self.radius*2*(window/window_sz))> 0:
        if self.radius*2*(window/window_sz) > 7:
            new_surface = pygame.transform.scale(self.surf, (self.radius*2*(window/window_sz), self.radius*2*(window/window_sz)))
            new_surface = new_surface.convert_alpha()
            screen.blit(new_surface,(self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) - self.radius*(window/window_sz),self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) - self.radius*(window/window_sz)))
        else:
            if self in celestials_major:
                screen.blit(pygame.transform.scale(self.surf, (5,5)),(self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz),self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)))
            elif self in celestials_minor:
                screen.blit(point,(self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz),self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)))
            else:
                screen.blit(minor_point,(self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz),self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)))

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

def Gravity(M,m,d):
    Force = (M*m*(6.7*(10**-11)))/(d**2)
    return Force

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

class Body:
    def __init__(self, absX, absY, surf, mass, velocity, radius, name):
        self.absX = absX
        self.absY = absY
        self.surf = surf
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.center = (absX + (surf.get_width()/2),absY + (surf.get_height()/2))
        self.name = name
        self.specialdata = []

mode = int(input("Earth to Moon Ai (1)\nSolar System Sandbox (2)\n"))
pygame.init()
void = pygame.Surface((1000,1000))
window_sz = 1000
center_xdis = 0
center_ydis = 0
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Solar Transit")
clock = pygame.time.Clock()
tick_freq = 10000
dig_font = pygame.font.Font("digital-7.ttf",50)
Sol = pygame.image.load("Sol.png").convert_alpha()
Earth = pygame.image.load("Earth.png").convert_alpha()
Luna = pygame.image.load("Luna.png").convert_alpha()
Mercury = pygame.image.load("Mercury.png").convert_alpha()
Venus = pygame.image.load("Venus.png").convert_alpha()
Mars = pygame.image.load("Mars.png").convert_alpha()
Jupiter = pygame.image.load("Jupiter.png").convert_alpha()
Saturn = pygame.image.load("Saturn.png").convert_alpha()
Uranus = pygame.image.load("Uranus.png").convert_alpha()
Neptune = pygame.image.load("Neptune.png").convert_alpha()
Pluto = pygame.image.load("Pluto.png").convert_alpha()
BlackHole = pygame.image.load("Black Hole.png").convert_alpha()
Ceres = pygame.image.load("Ceres.png").convert_alpha()
point = pygame.image.load("Point.png").convert_alpha()
minor_point = pygame.image.load("Minor_Point.png").convert_alpha()
last_best = None
while True:
    window = 0.0007
    celestials_major = [Body(1.496*(10**11),0,Earth,6*10**24,(0,29846),6.4*(10**6),"Earth"),Body(1.496*(10**11) + 384000000,0,Luna,7.34*(10**22),(0,1056+29846),1.74*(10**6),"Moon"),Body(0,0,Sol,1.989*(10**30),(0,0),6.95*(10**8),"Sun")]
    celestials_extra = [Body(5.8*10**10,0,Mercury,3.3*10**23,(0,47900),2.43*10**6,"Mercury"),Body(108*10**9,0,Venus,4.87*10**24,(0,35000),6.05*10**6,"Venus"),Body(228*10**9,0,Mars,0.642*10**24,(0,24100),(6792*10**3)/2,"Mars"),Body(778.5*10**9,0,Jupiter,1898*10**24,(0,13100),(142984*10**3)/2,"Jupiter"),Body(1432*10**9,0,Saturn,568*10**24,(0,9700),(274000*10**3)/2,"Saturn"),Body(2867*10**9,0,Uranus,86.8*10**24,(0,6800),(51118*10**3)/2,"Uranus"),Body(4515*10**9,0,Neptune,102*10**24,(0,5400),(49528*10**3)/2,"Neptune")]
    celestials_major.extend(celestials_extra)
    celestials = []
    celestials.extend(celestials_major)
    celestials_minor = [Body(5906.4*10**9,0,Pluto,0.013*10**24,(0,4700),(2376*10**3)/2,"Pluto"),Body(2.77*1.5*10**11,0,Ceres,9.1*10**20,(0,17900),490000,"Ceres")]
    celestials.extend(celestials_minor)
    asteroids = []
    bodies = []
    if mode == 1:
        for i in range(360):
            if not last_best:
                mass = 1000
                alpha = 2 * math.pi * random.random()
                x = 42360843 * math.cos(alpha) + 1.496*(10**11)
                y = 42360843 * math.sin(alpha) + 0
                alpha = math.degrees(alpha)
                tangent = alpha + 90
                vel = (vectorcomponent(tangent, 3080, "x") + vectorcomponent(angleturn((x,y),celestials[2].center)-90,math.sqrt((6.7*10**-11)*(1.989*10**30)/dis((x,y),celestials[2].center)),"x"),vectorcomponent(tangent, 3080, "y") + vectorcomponent(angleturn((x,y),celestials[2].center)-90,math.sqrt((6.7*10**-11)*(1.989*10**30)/dis((x,y),celestials[2].center)),"y"))
                image = random.randint(1,5)
                radius = 20
                asteroids.append(Body(x,y,pygame.image.load(f"Satellite{image}.png").convert_alpha(),mass,vel,radius,f"Satellite {i + 1}"))
                asteroids[-1].specialdata = [alpha,x,y,0,False,400,0]
            else:
                mass = 1000
                alpha = last_best.specialdata[0] + random.randint(-20,20)
                x = 42360843 * math.cos(math.radians(alpha)) + 1.496*(10**11)
                y = 42360843 * math.sin(math.radians(alpha)) + 0
                tangent = alpha + 90
                vel = (vectorcomponent(tangent, 3080, "x") + vectorcomponent(angleturn((x,y),celestials[2].center)-90,math.sqrt((6.7*10**-11)*(1.989*10**30)/dis((x,y),celestials[2].center)),"x"),vectorcomponent(tangent, 3080, "y") + vectorcomponent(angleturn((x,y),celestials[2].center)-90,math.sqrt((6.7*10**-11)*(1.989*10**30)/dis((x,y),celestials[2].center)),"y"))
                image = random.randint(1,5)
                radius = 20
                asteroids.append(Body(x,y,pygame.image.load(f"Satellite{image}.png").convert_alpha(),mass,vel,radius,f"Satellite {i + 1}"))
                newsendtime = last_best.specialdata[3] + random.random() * random.choice([-1,1])
                asteroids[-1].specialdata = [alpha,x,y,0,False,last_best.specialdata[5] + random.randint(last_best.specialdata[5]//-2,last_best.specialdata[5]//2),0]
            #angle,s,y,sendtime,sent,timeneargoal
    elif mode == 2:
        for i in range(200):
            mass = random.randint(10**12,10**14)
            alpha = 2 * math.pi * random.random()
            distance = random.randint(round(2.2*1.5*10**11),round(3.2*1.5*10**11))
            x = distance * math.cos(alpha)
            y = distance * math.sin(alpha)
            alpha = math.degrees(alpha)
            tangent = alpha + 90*random.choice([-1,1])
            vel = (vectorcomponent(angleturn((x,y),celestials[2].center)-90,math.sqrt((6.7*10**-11)*(1.989*10**30)/dis((x,y),celestials[2].center)),"x"),vectorcomponent(angleturn((x,y),celestials[2].center)-90,math.sqrt((6.7*10**-11)*(1.989*10**30)/dis((x,y),celestials[2].center)),"y"))
            image = random.randint(1,3)
            radius = random.randint(10,530000)
            asteroids.append(Body(x,y,pygame.image.load(f"Asteroid{image}.png").convert_alpha(),mass,vel,radius,f"Asteroid {i + 1}"))
    bodies.extend(celestials)
    bodies.extend(asteroids)
    center_ychange = 0
    center_xchange = 0
    window_change = 0
    t = 0
    if mode == 1:
        multiplier = 10
    else:
        multiplier = 1000
    temp_multi = multiplier
    if mode == 1:
        selected = bodies[0]
    else:
        selected = bodies[2]
    sat_timer = 0
    if mode == 1:
        sat_max_time = 24*3600/multiplier
    else:
        sat_max_time = 10000000000000000000000000000000000000000000000
    restarting = False
    while not restarting:
        mp = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                got_new = False
                for c in bodies:
                    if math.sqrt((abswin_convert(c.absX,"abs","x") - mp[0])**2 + (abswin_convert(c.absY,"abs","y") - mp[1])**2) < 20:
                        selected = c
                        got_new = True
                        break
                if not got_new:
                    selected = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    center_ychange = (700000000*1000/window)/tick_freq
                if event.key == pygame.K_s:
                    center_ychange = -(700000000*1000/window)/tick_freq
                if event.key == pygame.K_a:
                    center_xchange = (700000000*1000/window)/tick_freq
                if event.key == pygame.K_d:
                    center_xchange = -(700000000*1000/window)/tick_freq
                if event.key == pygame.K_o:
                    window_change = -0.02
                if event.key == pygame.K_i:
                    window_change = 0.02
                if event.key == pygame.K_SPACE:
                    if multiplier:
                        temp_multi = multiplier
                        multiplier = 0
                    else:
                        multiplier = temp_multi
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
                    window_change = 0
                if event.key == pygame.K_i:
                    window_change = 0
                if event.key == pygame.K_b:
                    celestials.append(Body(abswin_convert(mp[0],"win","x"),abswin_convert(mp[1],"win","y"),BlackHole,5.03652549*10**37,(0,0),0.5*1.5*10**11,"Black Hole"))
                    celestials[-1].specialdata = [0]
                    celestials_major.append(celestials[-1])
                    bodies.append(celestials[-1])
        window += window*window_change
        center_xdis += center_xchange/tick_freq
        center_ydis += center_ychange/tick_freq
        screen.blit(void,(0,0))
        #center_xdis = -celestials[0].absX
        #center_ydis = -celestials[0].absY
        if selected:
            text = dig_font.render(selected.name,True,"White")
            screen.blit(text,(0,0))
            center_xdis = -(selected.absX - 500)
            center_ydis = -(selected.absY - 500)
        daystext = dig_font.render(str((t*temp_multi)//(60*60*24)) + " days",True,"White")
        screen.blit(daystext,(window_sz - 300,0))
        hourstext = dig_font.render(str(((t*temp_multi)//(60*60)) - ((t*temp_multi)//(60*60*24)*24)) + " hours",True,"White")
        screen.blit(hourstext,(window_sz - 300,60))
        if celestials[0].absY > -10000000000 and celestials[0].absY < 0: print((t*temp_multi)/(60*60*24))
        for B in bodies:
            forces = []
            window_blit(B)
            if B.name == "Black Hole":
                B.surf = pygame.transform.rotate(BlackHole, B.specialdata[0])
                B.specialdata[0] += 1
            try:
                if B.specialdata[3] < (t*temp_multi)/(60*60*24) and not B.specialdata[4]:
                    B.specialdata[4] = True
                    forces = [(vectorcomponent(angleturn(B.center,celestials[0].center) - 90, B.specialdata[5]*B.mass, "x"),vectorcomponent(angleturn(B.center,celestials[0].center) - 90, B.specialdata[5]*B.mass, "y"))]
            except : pass
            for C in celestials:
                if C != B:
                    forces.append((vectorcomponent(angleturn(B.center,C.center),Gravity(C.mass,B.mass,dis(B.center,C.center)),"x"),vectorcomponent(angleturn(B.center,C.center),Gravity(C.mass,B.mass,dis(B.center,C.center)),"y")))
                    if C == celestials[1] and B.name[:4] == "Sate":
                        if Gravity(C.mass,B.mass,dis(B.center,C.center)) > Gravity(celestials[0].mass,B.mass,dis(B.center,celestials[0].center)):
                            B.specialdata[6] += 1
                            if dis(B.center,C.center) < C.radius:
                                multiplier = 0
                                print(f"{B.name} Has Landed!")
                    if C.name == "Black Hole":
                        if dis(B.center,C.center) < C.radius:
                            C.mass += B.mass
                            C.radius = (2*C.mass*6.7*10**-11)/(300*10**6)**2
                            bodies.remove(B)
                            try: celestials.remove(B)
                            except: pass
            for F in forces:
                B.velocity = (B.velocity[0] + (multiplier*F[0]/B.mass),B.velocity[1] + (multiplier*F[1]/B.mass))
            B.absX += multiplier*B.velocity[0]
            B.absY += multiplier*B.velocity[1]
            B.center = (B.absX,B.absY)
        pygame.display.update()
        clock.tick(tick_freq)
        if multiplier: t += 1
        if multiplier: sat_timer += 1
        if sat_timer > sat_max_time:
            restarting = True
            last_best = bodies[11]
            enroute = False
            for i, s in enumerate(bodies):
                if i > 10:
                    if s.specialdata[6] > last_best.specialdata[6]:
                        last_best = s
                    if dis(s.center,celestials[0].center) < 347600000:
                        enroute = True
            if last_best == bodies[11] and bodies[11].specialdata[6] == 0:
                restarting = False
                sat_timer = 0
                print("No closest\nResetting timer")
            elif enroute:
                restarting = False
                sat_timer = 0
                print("Satellites still on route\nResetting timer")  
            else:
                print(f"Closest: {last_best.name}\nRestarting Simulation...")
            
