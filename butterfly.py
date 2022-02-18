import pygame
pygame.init()

YELLOW = (255,255,0)
BLACK = (0,0,0)
PURPLE = (150,0,250)
PURPLE1 = (100,0,200)
TEST = (255,0,0)
class butterfly:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        pygame.draw.circle(screen, (PURPLE), (self.xpos+50, self.ypos+20), 100)
        pygame.draw.circle(screen, (PURPLE), (self.xpos-50, self.ypos+20), 100)
        pygame.draw.circle(screen, (PURPLE1), (self.xpos+50, self.ypos-40), 100)
        pygame.draw.circle(screen, (PURPLE1), (self.xpos-50, self.ypos-40), 100)
        pygame.draw.ellipse(screen, (YELLOW), (self.xpos-35, self.ypos-140, 75,275))
        pygame.draw.line(screen, (TEST), (self.xpos-30,self.ypos-175),(self.xpos-5,self.ypos-125),5)
        pygame.draw.line(screen, (TEST), (self.xpos+30,self.ypos-175),(self.xpos-5,self.ypos-125),5)
        
butterfly1 = butterfly(400,500)


screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("butterfly")

doExit = False
clock = pygame.time.Clock()

while not doExit:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
            
    butterfly1.draw()
    
    pygame.display.flip()
    
pygame.quit()
