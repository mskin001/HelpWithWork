import pygame
import time
import random

# window Size
window_x = 720
window_y = 480

# define colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

# initialize pygame
pygame.init()

# initialize game window
pygame.display.set_caption("Snek Go Munch")
game_window = pygame.display.set_mode((window_x,window_y))

# FPS controller
fps = pygame.time.Clock()

# define snake default position and speed
snake_pos = [100,50]
snake_speed = 15

# define default snake body
snake_body = [[100,50],
              [90,50],
              [80,50],
              [70,50]]

# food position
food_pos = [random.randrange(1,(window_x//10))*10,
            random.randrange(1,(window_y//10))*10]
food_spawn = True

# set default snake direction
direction = "RIGHT"
change_to = direction

score = 0

def show_score(choice, color, font, size):
    # create font object score_font
    score_font = pygame.font.SysFont(font,size)

    # create a display surface object score_surface
    score_surface = score_font.render("Score: " + str(score), True, color)

    # create a rectangular object fo the text surface
    score_rect = score_surface.get_rect()

    # display text
    game_window.blit(score_surface, score_rect)

def game_over():
    # create font object my_font
    my_font = pygame.font.SysFont("times new roman", 50)

    # create a text surface on which text will be drawn
    game_over_surface = my_font.render("Your Score is: " + str(score), True, red)

    # create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    # bilt will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 5 seconds we will quit the program
    time.sleep(3)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()

while True:
    # handle key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # if two keys pressed simultaneously we don't want snake
    # to move into two directions simultaneously
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    
    # move the snake
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    # snake body growing mechanism if fruit and snake collide
    # then the score will be imcremented by 10
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (window_x//10))*10,
                    random.randrange(1,(window_y//10))*10]
        snake_speed += 1
    
    food_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window,green,pygame.Rect(pos[0],pos[1],10,10))
    
    pygame.draw.rect(game_window,white,pygame.Rect(food_pos[0],food_pos[1],10,10))

    # game over condition
    if snake_pos[0] < 0 or snake_pos[0] > window_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > window_y-10:
        game_over()
    
    # touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    
    # display score continuously
    show_score(1,white,"times new roman", 20)

    #refresh game screen
    pygame.display.update()

    # fps/refresh rate
    fps.tick(snake_speed)