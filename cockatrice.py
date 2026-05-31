import pygame
from player import Player
class Cockatrice(Player):
    def __init__(self):
        self.lives = 3
        self.shots = 5
        self.maxshots = 5
        self.xpos = 400 - (168*2)
        self.ypos = 500
        self.speed = 4
        self.specialcharge = 0.0
        self.shotsfired = []
        self.lastshot = 0
        self.lastreload = pygame.time.get_ticks()
        self.specialactive =  False
        self.shots = self.maxshots
        self.shotsprite = pygame.image.load("images/stone.png").convert_alpha()
        self.shotsprite = pygame.transform.scale(self.shotsprite, (20, 20))
        self.charwidth = 168*2
        self.charheight = 103*2
        self.normal_sprite = pygame.image.load("images/cockatrice.png").convert_alpha()
        self.normal_sprite = pygame.transform.scale(self.normal_sprite, (self.charwidth, self.charheight))
        self.rect = self.normal_sprite.get_rect()
        self.rect.x = self.xpos
        self.rect.y = self.ypos

        #self.fire_sprite = pygame.image.load("images/dragonfire.png").convert_alpha()
        #self.fire_sprite = pygame.transform.scale(self.fire_sprite, (self.charwidth, self.charheight))

        self.charsprite = self.normal_sprite
        
        self.shoteffect = pygame.mixer.Sound("sounds/fireball.wav")
        self.firerate = 200
            
            
    def update(self, screen):
        key = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
        font = pygame.font.Font(None, 36)
        text_surface = font.render(str(self.specialcharge), True, "White")
        screen.blit(text_surface, (50, 50))
        
        
        if self.specialcharge < 100 and not self.specialactive:
            self.specialcharge += 100 / (60 * 15)
            
        if self.specialactive == True:
            now = pygame.time.get_ticks()
            #self.charsprite = self.fire_sprite

        if self.specialactive and now - self.specialstart > 7000:
            self.specialactive = False
            #self.charsprite = self.normal_sprite
            
        if key[pygame.K_e] and self.specialcharge >= 100 and not self.specialactive:
            self.special()
            self.specialstart = pygame.time.get_ticks()
            
            
    def special(self):
            self.specialactive = True
            self.specialcharge = 0