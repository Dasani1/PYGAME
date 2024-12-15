import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
# initialize pygame
pygame.init()
screen_size = (700, 500)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
 

class object1:
    def __init__(self,mass,speed,pos,colour):
        self.hitbox1 = pygame.Rect(pos,300,50,50)
        self.xcoord1 = pos
        self.speed1 = speed
        self.border1 = 0
        self.border2 = 650
        self.mass1 = mass 
        self.collisions = 0
        self.colour = colour
    def draw(self):
        pygame.draw.rect(screen, self.colour, self.hitbox1)

    def move(self):
        if self.xcoord1 <= self.border1 or self.xcoord1 >= self.border2:
            self.collisions += 1
            self.speed1 *= -1
            # print(self.speed1, "hello")
        self.xcoord1 += self.speed1
        self.hitbox1 = pygame.Rect(self.xcoord1,300,50,50)

    def math(self,speed2,mass2):
        consv = self.mass1 * self.speed1 + mass2*speed2 #m1*v1 + m2*v2
        var1 = self.mass1**2 + (self.mass1*mass2) #v1^2
        var2 = 2*(-self.mass1*consv) #v1
        self.speed1 = ((var1 * self.speed1) + var2)/-var1 #Synthetic division

        return (-self.mass1*self.speed1+consv)/mass2 #Original formula, also returns the second speed
        # print(self.speed1, self.speed2)

    def collide(self,block2):
        confirm = pygame.Rect.colliderect(self.hitbox1,block2)
        if confirm:
            self.collisions +=1
            return confirm
    def getBox(self):
        return self.hitbox1
    def getSpeed(self):
        return self.speed1
    def getMass(self):
        return self.mass1
    def getCollisions(self):
        return self.collisions
    def setSpeed(self,speed):
        self.speed1 = speed
    

class Text:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.location = (400,100)
        self.title = (220,50)
    def display(self,collisions1,collisions2):
        text1 = self.font.render(f"Collisions: {collisions1 + collisions2}", True,WHITE,BLACK)
        text2 = self.font.render("TEC Simulator", True, WHITE, BLACK)
        screen.blit(text2,self.title)
        screen.blit(text1,self.location)

        
# clock is used to set a max fps
clock = pygame.time.Clock()

block = object1(1,0,200,RED) #Mass, Speed, Position, Colour
block2 = object1(100,-1,600,WHITE)
text = Text()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    screen.fill(BLACK)
     
    if block.collide(block2.getBox()):
        block2.setSpeed(block.math(block2.getSpeed(),block2.getMass()))
    block.move()
    block2.move()
    text.display(block.getCollisions(), block2.getCollisions())
    block.draw()
    block2.draw()

    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()