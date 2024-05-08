import pygame
import math

def window_blit(self):
    self.rect.x = self.absX*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz)
    self.rect.y = self.absY*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)
    new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
    new_surface = new_surface.convert_alpha() 
    self.rect = new_surface.get_rect(topleft = (self.rect.x,self.rect.y))
    screen.blit(new_surface,self.rect)
    
class Wave:
    def __init__(self,amplitude,frequency,surf,absC):
        self.amplitude = amplitude
        self.frequency = frequency
        self.midline = 0
        self.timeline = 0
        self.absC = absC
        self.surf = surf
        
        
def window_blit(self):
    if self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) -(self.surf.get_width()*(window/window_sz))< window_sz and self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz) + (self.surf.get_width()*2*(window/window_sz)) > 0 and self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) - (self.surf.get_width()*(window/window_sz)) < window_sz and self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz) + (self.surf.get_width()*2*(window/window_sz))> 0:
        new_surface = pygame.transform.scale(self.surf, (self.surf.get_width()*(window/window_sz), self.surf.get_height()*(window/window_sz)))
        new_surface = new_surface.convert_alpha()
        screen.blit(new_surface,(self.absC[0]*(window/window_sz) + (window_sz-window)/2 + center_xdis*(window/window_sz),self.absC[1]*(window/window_sz) + (window_sz-window)/2 + center_ydis*(window/window_sz)))
    
pygame.init()
window_sz = 1000
window = 1000
screen = pygame.display.set_mode((window_sz,window_sz))
pygame.display.set_caption("Waves")
clock = pygame.time.Clock()
void = pygame.Surface((5000,5000))
rect = pygame.Surface((50,50))
rect.fill("yellow")
waves = []
waves.append(Wave(2000,0.1,rect,(0,0)))
center_xdis = 0
center_ydis = 0
window_change = 0
center_ychange = 0
center_xchange = 0
while True:
    for event in pygame.event.get():
        mp = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    center_ychange = 20
                if event.key == pygame.K_s:
                    center_ychange = -20
                if event.key == pygame.K_a:
                    center_xchange = 20
                if event.key == pygame.K_d:
                    center_xchange = -20
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
                    window_change = 0
                if event.key == pygame.K_i:
                    window_change = 0
                if event.key == pygame.K_m:
                    waves[0].frequency *= 1.2
                if event.key == pygame.K_n:
                    waves[0].frequency /= 1.2    
    window += window*window_change
    center_xdis += center_xchange
    center_ydis += center_ychange
    screen.blit(void,(0,0))
    for W in waves:
        window_blit(W)
        W.timeline += 0.1
        W.absC = (W.absC[0] + 1,W.midline + (W.amplitude*math.sin(W.frequency*W.timeline)))
    pygame.display.update()
    clock.tick(1000)
        