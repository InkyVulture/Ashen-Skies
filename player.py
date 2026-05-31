import pygame
class Player:
    def __init__(self):
        self.lives = 3
        self.maxshots = 5
        self.xpos = 400
        self.ypos = 500
        self.speed = 2
        self.specialcharge = 0.0
        self.shotsfired = []
        self.lastshot = 0
        self.lastreload = pygame.time.get_ticks()
        self.shots = self.maxshots
        self.shotsprite = pygame.image.load("images/temporaryfireball").convert_alpha()
        self.shotsprite = pygame.transform.scale(self.shotsprite, (20, 20))
        self.charwidth = 184*2
        self.charheight = 110*2
        self.charsprite = pygame.image.load("images/dragon.png").convert_alpha()
        self.charsprite = pygame.transform.scale(self.charsprite, (self.charwidth, self.charheight))
        self.rect = self.charsprite.get_rect()
        self.rect.x = self.xpos
        self.rect.y = self.ypos
        self.shoteffect = pygame.mixer.Sound("sounds/fireball.wav")
        self.firerate = 250
        
        
        
    def draw(self, screen):
        screen.blit(self.charsprite, self.rect)
        
    def move(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_a] and self.xpos >= (0 - (self.charwidth/4)):
            self.xpos -= (3*self.speed)
            
        if key[pygame.K_d] and self.xpos <= (800 - (self.charwidth - (self.charwidth/4))):
            self.xpos += (3*self.speed)
            
        if key[pygame.K_s] and self.ypos <= 500:
            self.ypos += (3*self.speed)
            
        if key[pygame.K_w] and self.ypos >= 100:
            self.ypos -= (3*self.speed)
            
        self.rect.x = self.xpos
        self.rect.y = self.ypos
            
    
    def attack(self, screen, enemy):
        key = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
        
        if self.shots == 0 and now - self.lastreload > 4000:
            self.shots = self.maxshots
            self.lastreload = now
            
        if key[pygame.K_SPACE] and self.shots > 0 and now - self.lastshot > self.firerate:
            self.shoteffect.play()
            self.shotsfired.append(pygame.Rect((self.xpos + (self.charwidth/2) - 10), self.ypos, 20, 20))
            self.shots -= 1
            self.lastshot = now
            
        for i in self.shotsfired:
            i.y -= 10
            screen.blit(self.shotsprite, (i.x, i.y))
            
            if i.y < 0:
                self.shotsfired.remove(i)
                
            if i.colliderect(enemy.rect):
                #print("hit enemy")
                self.shotsfired.remove(i)