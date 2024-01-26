from sys import exit
import pygame

def Archimedes(Density,Depth,Gravity,Surf,Height):
    Pressure = Density*Depth*Gravity
    F = Surf*Pressure
    Pressure = Density*(Depth+Height)*Gravity
    F -= Surf*Pressure
    return F

Wh = int(input("Water Height(m):  "))
Rs = int(input("Rectangle Size(cm):  "))
Wh = 895-(Wh*100)
pygame.init()
screen = pygame.display.set_mode((800,1000))
clock = pygame.time.Clock()
pygame.display.set_caption("Move Rect")
background = pygame.Surface((800,1000))
rectangle = pygame.Surface((Rs,Rs))
rectangle.fill("White")
rect = rectangle.get_rect(center = (400,500))
floor = pygame.Surface((800,1000))
floor.fill("Dark Green")
floor_r = floor.get_rect(topleft = (0,895))

water = pygame.Surface((800,800))
water.fill("Blue")
water_r = water.get_rect(topleft = (0,Wh))

Velocity = 0
Mass = ((Rs/100)**3)*4.6
print(Mass)
Acceleration = []
Force = 0
setgrav = 0.5
grav = 0.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Acceleration.append(-15)
            if event.key == pygame.K_s:
                Acceleration.append(15)

    ##Dynamics##
    Acceleration.append(grav)
    for x in range(len(Acceleration)):
        Force += Mass*Acceleration[x]
    if rect.y > floor_r.y-Rs:
        if Velocity > 0:
            Force = Force*-1 - (Velocity*1.3)
        rect.y = floor_r.y-Rs
    if Wh != 895:
        floor.fill("Yellow")
    if rect.y > Wh-Rs:
        Force += Archimedes(10,(rect.y-Wh-Rs)/100,setgrav,(Rs/100)**2,Rs/100)
        Velocity *= 0.98 # Water Resistance not finished works best at 60cm
    Velocity += Force
    rect.y += Velocity
    Acceleration = []
    Force = 0
    
    
    ##Blitting##
    screen.blit(background,(0,0))
    screen.blit(water,water_r)
    screen.blit(floor,floor_r)
    screen.blit(rectangle,rect)
    pygame.display.update()
    clock.tick(120)