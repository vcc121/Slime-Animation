import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 684))

class Slime(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # set up the image
        self.image = pygame.image.load("slime_front.png")
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (72, 72))

        #create the corresponding rect
        self.rect = self.image.get_rect()
        self.rect.centerx = 512
        self.rect.centery = 342
        
        #create the ability to move
        self.dx = 5
        self.dy = 5
        
    def update(self):
        #falling
        
        self.rect.centery += self.dy
        #movement with keys, jump to stay up (like flappy bird!)
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.centerx -= self.dx
            
        if keys[pygame.K_d]:
            self.rect.centerx += self.dx
            
        if keys[pygame.K_SPACE]:
            self.rect.centery -= self.dy*4
            
               
        # check bounds
        if self.rect.right > screen.get_width():
            self.rect.left = 0
        if self.rect.bottom > screen.get_height():
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.right = screen.get_width()
        if self.rect.top < 0:
            self.rect.bottom = screen.get_height()
            

def main():
    
    #display
    pygame.display.set_caption("Slime!")
    
    background = pygame.image.load("field background.jpg")
    screen.blit(background, (0, 0))
    
    slime = Slime()
    allSprites = pygame.sprite.Group(slime)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while(keepGoing):
        clock.tick(30)
        
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        # clear and redraw sprites
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
    pygame.quit()   