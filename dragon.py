import pygame
from player import Player
class Dragon(Player):
    def __init__(self):
        self.lives = 3
        self.shots = 5
        self.maxshots = 5
        self.babysaves = 0
        self.xpos = 400
        self.ypos = 500
        self.speed = 2
        self.specialcharge = 0.0
        self.shotsfired = []
        self.lastshot = 0
        self.lastreload = pygame.time.get_ticks()
        self.onfire = False
        self.shots = self.maxshots
        self.shotsprite = pygame.image.load("/Users/windera27/Library/CloudStorage/OneDrive-BarkerCollege/2026/Software Engineering/Ashen Skies Game/images/temporaryfireball").convert_alpha()
        self.shotsprite = pygame.transform.scale(self.shotsprite, (20, 20))
        self.charsprite = pygame.Rect(self.xpos, self.ypos, 152, 100)
            
            
    def update(self):
        key = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
        self.specialstart = pygame.time.get_ticks()
        
        
        if self.specialcharge < 100:
            self.specialcharge += 0.05
            
        if self.onfire == True:
            now = pygame.time.get_ticks()

        if now - self.specialstart > 7000:
            self.specialactive = False
            
        if key[pygame.K_e] and self.specialcharge == 100:
            self.special()
            self.specialstart = pygame.time.get_ticks()
            
            
    def special(self):
            self.onfire = True
            self.specialcharge = 0