import pygame

pygame.init() #initialize pygame
display_width = 800 #coding as variables allows easier manipulation
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


gameDisplay = pygame.display.set_mode( (display_width, display_height)) #sets size of display

pygame.display.set_caption('Dog Dodgin!') #set caption for game

clock = pygame.time.Clock()  #gameclock

dogImg = pygame.image.load('hennessy.svg') #load an image

def car(x, y):
    #this function displays our image at some location x, y
    gameDisplay.blit(dogImg, (x, y))

x = (display_width * 0.4) #setting our initial position
y = (display_height * 0.8)


crashed = False #starting the dog not running into anything

while not crashed: #while crash has not occurred

    for event in pygame.event.get(): #generates a list of events from the user
        if event.type == pygame.QUIT: #also our "event loop"
            crashed = True

        print(event) #we will see the events recorded by pygame

    gameDisplay.fill(white) #fills the background and then redraw car
    car(x, y)
    pygame.display.update() #updates screen

    clock.tick(20) #setting frames per second

pygame.quit()
quit()

