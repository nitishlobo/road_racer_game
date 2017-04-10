import time
import pygame
import colours

def update_car_position(x, y):
    '''Display car icon on screen using top left as origin.

    Keyword arguments:
    x -- x co-ordinate from left of the window.
    y -- y co-ordinate from top of the window'''
    game_display.blit(carImg, (x, y))

def text_objects(text, font):
    text_surface = font.render(text, True, colours.BLACK)
    return text_surface, text_surface.get_rect()

def display_message(text):
    #Font type and size of message.
    large_font = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_font)
    text_rect.center = ((display_width/2), (display_height/2))
    #Update game window and display new text.
    game_display.blit(text_surf, text_rect)
    pygame.display.update()
    #Delay before restarting the game
    time.sleep(2)
    game_loop()

def crash():
    display_message('You crashed!')

def game_loop():
    #Start position of the car.
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            #Exit main while loop.
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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
        game_display.fill(colours.WHITE)
        update_car_position(x, y)

        #Exit game when car hits edges of the game window.
        if x > display_width - car_width or x <0:
            crash()

        pygame.display.update()
        clock.tick(120)

pygame.init()
#Set clock rate.
clock = pygame.time.Clock()
#Define car width in pixels and load car icon.
car_width = 64
carImg = pygame.image.load('car_64_pixels.png')
#Set game window size & title.
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Road Racer')
#Begin game
game_loop()

pygame.quit()
quit()
