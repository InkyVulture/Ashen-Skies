import pygame
from player import Player
from dragon import *
from wyvern import *
from amphithere import *
from cockatrice import *
from enemy import *


# Pygame Init and Window Setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ASHEN SKIES")
clock = pygame.time.Clock()
bgimage = pygame.image.load("images/startbackground.png").convert()
bgimage = pygame.transform.scale(bgimage, (800, 600))

# Game States
running = True
gamestart = False
speciesselect = False

# Sound Effects/Music
pygame.mixer.music.load("sounds/menutrack.ogg")
pygame.mixer.music.play(-1)
drgroar = pygame.mixer.Sound("sounds/dragonroar.wav")
wyvroar = pygame.mixer.Sound("sounds/wyvernroar.wav")
amproar = pygame.mixer.Sound("sounds/amphithereroar.wav")
ctrroar = pygame.mixer.Sound("sounds/cockatriceroar.wav")


#Buttons + Collision Rects
startbutton = pygame.image.load("images/startbtn.png").convert_alpha()
startbutton = pygame.transform.scale(startbutton, (400, 150))
startbutton_rect = startbutton.get_rect(center=(400, 300))
quitbutton = pygame.image.load("images/quitbtn.png").convert_alpha()
quitbutton = pygame.transform.scale(quitbutton, (400, 150))
quitbutton_rect = quitbutton.get_rect(center=(400, 500))

dragoninfo = pygame.image.load("images/dragoninfoscr.png").convert_alpha()
dragoninfo = pygame.transform.scale(dragoninfo, (376, 276))
wyverninfo = pygame.image.load("images/wyverninfoscr.png").convert_alpha()
wyverninfo = pygame.transform.scale(wyverninfo, (376, 276))
ampiinfo = pygame.image.load("images/ampiinfoscr.png").convert_alpha()
ampiinfo = pygame.transform.scale(ampiinfo, (376, 276))
cockatriceinfo = pygame.image.load("images/cockatriceinfoscr.png").convert_alpha()
cockatriceinfo = pygame.transform.scale(cockatriceinfo, (376, 276))

drginforect = dragoninfo.get_rect(topleft=(12, 12))
wyvinforect = wyverninfo.get_rect(topleft=(400, 12))
ampinforect = ampiinfo.get_rect(topleft=(12, 300))
ctrinforect = cockatriceinfo.get_rect(topleft=(400, 300))

# Death Screen Animation
deathframes = [
    pygame.transform.scale(pygame.image.load("images/deathf1.png").convert_alpha(), (800, 600)),
    pygame.transform.scale(pygame.image.load("images/deathf2.png").convert_alpha(), (800, 600)),
    pygame.transform.scale(pygame.image.load("images/deathf3.png").convert_alpha(), (800, 600))
]
current_frame = 0
animation_speed = 0.1

e1 = Enemy()

def deathanimation():
    global current_frame

    if current_frame < len(deathframes) - 1:
        current_frame += animation_speed

    screen.blit(deathframes[int(current_frame)], (0, 0))
    

def playerupdate():
    plyr.draw(screen)
    plyr.update(screen)
    plyr.attack(screen, e1)
    plyr.move()
    
    
def collision():
    if plyr.rect.colliderect(e1.rect) and plyr.specialactive == True:
        print("player collided with enemy while on fire")
    elif plyr.rect.colliderect(e1.rect):
        print("plyr collided with enemy")
        
        
def switch_to_gameplay_music():
    pygame.mixer.music.fadeout(500)
    pygame.mixer.music.load("sounds/gameplaytrack.ogg")
    pygame.mixer.music.play(-1)
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:

            # MAIN MENU
            if not speciesselect:
                

                if startbutton_rect.collidepoint(event.pos):
                    speciesselect = True

                if quitbutton_rect.collidepoint(event.pos):
                    running = False

            # SPECIES SELECT
            elif speciesselect and not gamestart:

                if drginforect.collidepoint(event.pos):
                    plyr = Dragon()
                    gamestart = True
                    speciesselect = False
                    drgroar.play()
                    switch_to_gameplay_music()
                    

                elif wyvinforect.collidepoint(event.pos):
                    plyr = Wyvern()
                    gamestart = True
                    speciesselect = False
                    wyvroar.play()
                    switch_to_gameplay_music()
                    

                elif ampinforect.collidepoint(event.pos):
                    plyr = Amphithere()
                    gamestart = True
                    speciesselect = False
                    amproar.play()
                    switch_to_gameplay_music()
                    

                elif ctrinforect.collidepoint(event.pos):
                    plyr = Cockatrice()
                    gamestart = True
                    speciesselect = False
                    ctrroar.play()
                    switch_to_gameplay_music()
                    
                

    if not speciesselect and not gamestart:
        screen.blit(bgimage, (0, 0))
        screen.blit(startbutton, startbutton_rect)
        screen.blit(quitbutton, quitbutton_rect)
        
    if speciesselect:
        screen.fill((50, 50, 50))
        screen.blit(dragoninfo, (12, 12))
        screen.blit(wyverninfo, (400, 12))
        screen.blit(ampiinfo, (12, 300))
        screen.blit(cockatriceinfo, (400, 300))
        
    if gamestart:
        screen.fill((0, 0, 0))
        playerupdate()
        collision()
        e1.draw(screen)
        e1.update(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()