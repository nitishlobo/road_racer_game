import pygame
import colours

def update_car_position(x, y):
    '''Display car icon on screen using top left as origin.

    Keyword arguments:
    x -- x co-ordinate from left of the window.
    y -- y co-ordinate from top of the window'''
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_loop():
    #Start position of the car.
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            #Exit main while loop.
            if event.type == pygame.QUIT:
                gameExit = True

            #Keyboard control of main image.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        #Update x-co-ordinate of the car
        x += x_change
        #Display white background on game window.
        gameDisplay.fill(colours.WHITE)
        update_car_position(x, y)

        #Exit game when car hits edges of the game window.
        if x > display_width - car_width or x <0:
            gameExit = True

        pygame.display.update()
        clock.tick(60)

pygame.init()
#Set clock rate.
clock = pygame.time.Clock()
#Define car width in pixels and load car icon.
car_width = 64
carImg = pygame.image.load('car_64_pixels.png')
#Set game window size & title.
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Road Racer')
#Begin game
game_loop()

pygame.quit()
quit()
