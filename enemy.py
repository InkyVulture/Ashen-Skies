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
        
    def draw(self, screen):
        pygame.draw.rect(screen, "blue", self.body)
        
    def update(self, screen):
        now = pygame.time.get_ticks()
        
        if now - self.lastshot > (1000/ self.firerate):
            self.bullets.append(pygame.Rect(self.xpos, self.ypos, 20, 20))
            self.lastshot = now
            
        for i in self.bullets:
            i.y += 10
            pygame.draw.rect(screen, "red", i)
            
            if i.y > 850:
                self.bullets.remove(i)