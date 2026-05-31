import pygame
class Enemy:
    def __init__(self):
        self.xpos = 400
        self.ypos = 100
        self.firerate = 1
        self.body = pygame.Rect(self.xpos, self.ypos, 70, 70)
        self.bullets = []
        self.bulsprite = pygame.Rect(self.xpos, self.ypos, 20, 20)
        self.lastshot = pygame.time.get_ticks()
        
        self.charsprite = pygame.image.load("images/shipplaceholder.png").convert_alpha()
        self.charsprite = pygame.transform.scale(self.charsprite, (70, 70))
        self.rect = self.charsprite.get_rect()
        self.rect.x = self.xpos
        self.rect.y = self.ypos
        
        
    def draw(self, screen):
        screen.blit(self.charsprite, self.rect)
        
    def update(self, screen):
        now = pygame.time.get_ticks()
        
        if now - self.lastshot > (2000/ self.firerate):
            self.bullets.append(pygame.Rect(self.xpos, self.ypos, 20, 20))
            self.lastshot = now
            
        for i in self.bullets:
            i.y += 10
            pygame.draw.rect(screen, "red", i)
            
            if i.y > 850:
                self.bullets.remove(i)