import pygame
pygame.init()
pygame.init()
screen = pygame.display.set_mode((1500,800))
pygame.display.set_caption("Mapping")
clock = pygame.time.Clock()
l1 = "OOXXXXXOXXOOXXXXOOOOOXXXXOOOXX"
l2 = "XXXXXXOXOOOOOXXOOOOOXXOXXXXXXX"
l3 = "OOOXXXXXOOOOOOXOXOXOOXOOXXXXXX"
l4 = "OOOXXXXOOOOOOOOOOOXOXXXXXXXXXX"
l5 = "OOOXXOOXOOOOOOOOOOOXXXXXXXXOXO"
l6 = "OOOOXXOOOOOOOOOOOOXXXOXOXOXXXX"
l7 = "XOOOOXXXOOOOOOOOOOOXOXOOOXOOOX"
l8 = "OOOOXXXXXOOOOOOOOXXXXXXOXXXOXX"
l9 = "OOOOXXXXOOOOOOOOXXXXXXXXXXXXXO"
l10 ="OOOOOXXOOOOOOOOOXXXXXXXXXXXXOO"
l11 ="OOOOOXXOOOOOOOOOOXXXXXXXXXXXXX"
l12 ="OOOOOOXXOOOOOOOOOOOXXXXXXXXXXO"
Map = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
ocean_tile = pygame.Surface((50,50))
ocean_tile.fill("Blue")
grass_tile = pygame.Surface((50,50))
grass_tile.fill("Green")
while True:
    for event in pygame.event.get():
        mp = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for l in range(len(Map)):
        for t in range(len(Map[l])):
            if Map[l][t] == "O":
                screen.blit(ocean_tile,(t*50,l*50))
            elif Map[l][t] == "X":
                screen.blit(grass_tile,(t*50,l*50))
    pygame.display.update()
    clock.tick(60)
    