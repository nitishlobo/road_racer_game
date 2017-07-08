import time
import random
import pygame
import colours

def text_objects(text, font):
    '''Return an invisible surface and rectangle that contains the text.

    Keyword arguments:
    text -- text in the rectangular surface.
    font -- font of the text.'''
    text_surface = font.render(text, True, colours.BLACK)
    return text_surface, text_surface.get_rect()

def display_message(text):
    '''Display a large message to the center of the game display.

    Keyword arguments:
    text -- text to display to the screen.'''
    #Font type and size of message.
    large_font = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_font)
    text_rect.center = ((display_width/2), (display_height/2))

    #Update game window and display new text.
    game_display.blit(text_surf, text_rect)
    pygame.display.update()

def update_car_position(x, y):
    '''Display car icon on screen using top left as origin.

    Keyword arguments:
    x -- x co-ordinate from left of the window.
    y -- y co-ordinate from top of the window.'''
    game_display.blit(carImg, (x, y))

def generate_obstacle(x_position, y_position, width, height, colour):
    '''Draw an obstacle on the screen.

    Keyword arguments:
    x_position -- x co-ordinate of obstacle from left of the window.
    y_position -- y co-ordinate of obstacle from top of the window.
    width -- width of the obstacle.
    height -- height of the obstacle.
    colour -- colour of the obstacle.'''
    pygame.draw.rect(game_display, colour, [x_position, y_position, width, height])

def update_score_counter(score):
    '''Display how many obstacles were dodged on the top left corner of the game.

    Keyword arguments:
    score -- total number of obstacles dodged.'''
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(score), True, colours.BLACK)
    game_display.blit(text,(0,0))

def crash():
    '''Display a crash message.'''
    display_message('You crashed!')
    #Delay before restarting the game
    time.sleep(2)
    game_loop()

def game_loop():
    #Start position of the car.
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    #Configure obstacle
    ob_x = random.randrange(0, display_width)
    ob_y = -600
    ob_speed = 7
    ob_width = 100
    ob_height = 100
    score = 0

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

        #Generate obstacles
        generate_obstacle(ob_x, ob_y, ob_width, ob_height, colours.BLUE)
        ob_y += ob_speed
        update_score_counter(score)
        #Regenerate a new obstacle once the previous obstacle has passed the screen.
        if ob_y > display_height:
            score += 1
            ob_y = -ob_height
            ob_x = random.randrange(0,display_width)
            #Increase difficulty of the game.
            ob_speed += 1
            ob_width += (score * 1.2)

        update_car_position(x, y)
        #Determine whether car has hit obstacle.
        if y < ob_y + ob_height:
            if ((x > ob_x) and (x < ob_x + ob_width)) or ((x + car_width > ob_x) and (x + car_width < ob_x + ob_width)):
                crash()

        #Exit game when car hits edges of the game window.
        if (x > (display_width - car_width)) or x < 0:
            crash()

        pygame.display.update()
        clock.tick(120)

pygame.init()

#Set clock rate.
clock = pygame.time.Clock()

#Define car width in pixels and load car icon.
car_width = 50
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
