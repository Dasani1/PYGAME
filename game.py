import pygame

get = [25,25]
Range = [200,200]

class Piece:
    def __init__(self):
        self.hitbox = pygame.Rect(get[0]-25,get[1]-25,50,50)
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.hitbox)

class Block:
    def __init__(self):
        self.hitbox = pygame.Rect(Range[0],Range[1],200,200)
    def draw(self):
        pygame.draw.rect(screen,RED,self.hitbox)
    
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
# initialize pygame
pygame.init()
screen_size = (600, 600)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
 
# clock is used to set a max fps
clock = pygame.time.Clock()
 
# create a demo surface, and draw a red line diagonally across it
surface_size = (25, 45)
test_surface = pygame.Surface(surface_size)
test_surface.fill(WHITE)
pygame.draw.aaline(test_surface, RED, (0, surface_size[1]), (surface_size[0], 0))
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Press = pygame.mouse.get_pressed()[0]
    if Press != True:
        Press = False
    Track = pygame.mouse.get_pos()
        
    #clear the screen
    screen.fill(BLACK)
    pawn = Piece()
    pawn.draw()
    grid = Block()
    grid.draw()

    #Sheesh that if statement
    if Press and Track[0] -25 <= get[0] and Track[0] + 25 >= get[0] and Track[1] - 25 <= get[1] and Track[1] + 25 >= get[1]: 
        get = pygame.mouse.get_pos()
        pawn.draw()
        print(get)

    if not Press and get[0] >= Range[0]-25  and get[0] <= 425 and get[1] >= Range[1]-25 and get[1] <= 425:
        get = [Range[0]*1.5,Range[1]*1.5]
        pawn.draw()

    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()