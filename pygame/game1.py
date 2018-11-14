import pygame

pygame.init() #initialize pygame

gameDisplay = pygame.display.set_mode( (800, 600)) #sets size of display

pygame.display.set_caption('Dog Dodgin!') #set caption for game

clock = pygame.time.Clock()  #gameclock

crashed = False #starting the dog not running into anything

while not crashed: #while crash has not occurred

    for event in pygame.event.get(): #generates a list of events from the user
        if event.type == pygame.QUIT:
            crashed = True

        print(event) #we will see the events recorded by pygame

    pygame.display.update() #updates screen

    clock.tick(20) #setting frames per second

pygame.quit()
quit()

