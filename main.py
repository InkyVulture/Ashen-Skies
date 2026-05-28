import pygame
from player import Player
from dragon import *
from enemy import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ASHEN SKIES")
bgimage = pygame.image.load("/Users/windera27/Library/CloudStorage/OneDrive-BarkerCollege/2026/Software Engineering/Ashen Skies Game/images/startbackground.png").convert()
bgimage = pygame.transform.scale(bgimage, (800, 600))
startbutton = pygame.image.load("/Users/windera27/Library/CloudStorage/OneDrive-BarkerCollege/2026/Software Engineering/Ashen Skies Game/images/startbtn.png").convert_alpha()
startbutton = pygame.transform.scale(startbutton, (400, 150))
quitbutton = pygame.image.load("/Users/windera27/Library/CloudStorage/OneDrive-BarkerCollege/2026/Software Engineering/Ashen Skies Game/images/quitbtn.png").convert_alpha()
quitbutton = pygame.transform.scale(quitbutton, (400, 150))
clock = pygame.time.Clock()
running = True
gamestart = False
startbutton_rect = startbutton.get_rect(center=(400, 300))
quitbutton_rect = quitbutton.get_rect(center=(400, 500))

p1 = Dragon()

e1 = Enemy()

while running:
    screen.blit(bgimage, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if startbutton_rect.collidepoint(event.pos):
                gamestart = True
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if quitbutton_rect.collidepoint(event.pos):
                running = False
                

    if not gamestart:
        screen.blit(startbutton, startbutton_rect)
        screen.blit(quitbutton, quitbutton_rect)

    if gamestart:
        screen.fill((0, 0, 0))
        e1.draw(screen)
        p1.draw(screen)
        p1.update()
        e1.update(screen)
        p1.attack(screen)
        p1.move()

    pygame.display.update()
    clock.tick(60)

pygame.quit()