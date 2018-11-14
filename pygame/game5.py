import pygame
import time

pygame.init() #initialize pygame
display_width = 800 #coding as variables allows easier manipulation
display_height = 600

image_width = 30
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


gameDisplay = pygame.display.set_mode( (display_width, display_height)) #sets size of display

pygame.display.set_caption('Dog Dodgin!') #set caption for game

clock = pygame.time.Clock()  #gameclock

dogImg = pygame.image.load('hennessy.png') #load an image

def car(x, y):
    #this function displays our image at some location x, y
    gameDisplay.blit(dogImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(20)

    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():
    x = (display_width * 0.4) #setting our initial position
    y = (display_height * 0.5)

    x_change = 0 #start with no change in x direction


    gameExit = False #starting the dog not running into anything

    while not gameExit: #while crash has not occurred

        for event in pygame.event.get(): #generates a list of events from the user
            if event.type == pygame.QUIT: #also our "event loop"
                crashed = True

            if event.type == pygame.KEYDOWN: #adding movement based on key presses
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = +5

            if event.type == pygame.KEYUP: #when you lift finger stop moving
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white) #fills the background and then redraw car
        car(x, y)

        if x > (display_width - image_width) or x < 0:
            crash()


        pygame.display.update() #updates screen
        clock.tick(2) #setting frames per second

game_loop()
pygame.quit()
quit()

