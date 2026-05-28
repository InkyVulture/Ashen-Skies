import pygame
class Player:
    def __init__(self):
        self.lives = 3
        self.maxshots = 5
        self.babysaves = 0
        self.xpos = 400
        self.ypos = 500
        self.speed = 2
        self.specialcharge = 0.0
        self.shotsfired = []
        self.lastshot = 0
        self.lastreload = pygame.time.get_ticks()
        self.shots = self.maxshots
        self.shotsprite = pygame.image.load("/Users/windera27/Library/CloudStorage/OneDrive-BarkerCollege/2026/Software Engineering/Ashen Skies Game/images/temporaryfireball").convert_alpha()
        self.shotsprite = pygame.transform.scale(self.shotsprite, (20, 20))
        self.charsprite = pygame.Rect(self.xpos, self.ypos, 152, 100)
        
    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.charsprite)
        
    def move(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_a] and self.xpos >= 0:
            self.xpos -= (3*self.speed)
            
        if key[pygame.K_d] and self.xpos <= 648:
            self.xpos += (3*self.speed)
            
        if key[pygame.K_s] and self.ypos <= 500:
            self.ypos += (3*self.speed)
            
        if key[pygame.K_w] and self.ypos >= 100:
            self.ypos -= (3*self.speed)
            
        self.charsprite.x = self.xpos
        self.charsprite.y = self.ypos
            
    
    def attack(self, screen):
        key = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
        
        if self.shots == 0 and now - self.lastreload > 4000:
            self.shots = self.maxshots
            self.lastreload = now
            
        if key[pygame.K_SPACE] and self.shots > 0 and now - self.lastshot > 250:
            self.shotsfired.append(pygame.Rect(self.xpos + 75, self.ypos + 45, 20, 20))
            self.shots -= 1
            self.lastshot = now
            
        for i in self.shotsfired:
            i.y -= 10
            screen.blit(self.shotsprite, (i.x, i.y))
            
            if i.y < 0:
                self.shotsfired.remove(i)