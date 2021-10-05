import  time
import pygame
import random
pygame.init()

widht = 600
height = 500
size = (widht,height)
display = pygame.display.set_mode(size)
pygame.display.set_caption('snake game')

green = (9, 232, 17)
black = (0,0,0)
yellow = (232 , 224 , 72)
font = pygame.font.SysFont('None', 35)


segment_size = 15
head_x = 100 // segment_size * segment_size
head_y = 100 // segment_size * segment_size


def get_random_point():
    x = random.randint(0,widht-segment_size ) // segment_size*segment_size
    y = random.randint(0,height-segment_size ) // segment_size*segment_size
    return x, y
food_x,food_y  =get_random_point()

snake = []
snake_lenght = 1

def show_snake(snake):
    for x in snake:
        pygame.draw.rect(display, green, [x[0],x[1], segment_size, segment_size])

def show_score(score):
    value = font.render('Очки '+ str(score),True,green)
    display.blit(value, [0,0])

v_x = 0
v_y = 0
speed_snake = 14


clock = pygame.time.Clock()

while True:

    if head_x < 0 or head_x > widht-segment_size or head_y < 0  or head_y > height - segment_size:
        message = font.render('Fuck', True, green)
        display.blit(message, [widht/2, height/2])
        pygame.display.flip()

        time.sleep(2)

        pygame.quit()
        quit()



    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                v_y= segment_size
                v_x = 0
            elif event.key == pygame.K_UP:
                v_y= -segment_size
                v_x = 0
            elif event.key == pygame.K_LEFT:
                v_y = 0
                v_x= -segment_size
            elif event.key == pygame.K_RIGHT:
                v_y = 0
                v_x= segment_size
    head_x += v_x
    head_y += v_y


    display.fill(black)

    pygame.draw.rect(display,yellow , [food_x ,food_y ,segment_size,segment_size])

    snake.append((head_x, head_y))
    if len(snake) > snake_lenght:
        del snake[0]

    show_snake(snake)
    show_score(snake_lenght - 1)

    if head_x == food_x and head_y == food_y:
        food_x,food_y  =get_random_point()
        snake_lenght += 1

    pygame.display.flip()
    clock.tick(speed_snake)
