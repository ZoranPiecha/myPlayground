import pygame, random
import time
import keyboard
from random import randint

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 115, 115)
green = (211, 255, 206)
blue = (50, 153, 213)
purple = (102, 0, 102)
grey = (162, 196, 201)
color1 = (150, 50, 80)
color2 = (150, 250, 180)
color3 = (150, 150, 180)

dis_width = 1200
dis_height = 800

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game modified by Zoran')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15
snake_block2 = 10
snake_speed2 = 15

projectile_block = 8
projectile_speed = 30

font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 30)


def your_score(score):
    value = score_font.render("P1 Score: " + str(score), True, color1)
    dis.blit(value, [10, 0])


def your_score2(score2):
    value = score_font.render("P2 Score: " + str(score2), True, color2)
    dis.blit(value, [10, 40])


computer = color1
#computer2 = color2


def our_snake(computer, snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, computer, [x[0], x[1], snake_block, snake_block])


'''def our_snake2(computer2, snake_block2, snake_list2):
   for x in snake_list2:
        pygame.draw.rect(dis, computer2, [x[0], x[1], snake_block2, snake_block2])'''


def our_projectile(projectile_colour, projectile_block, projectile_list):
    for x in projectile_list:
        pygame.draw.rect(dis, projectile_colour, [x[0], x[1], projectile_block, projectile_block])


def message(msg, color):
    mesg = font_style.render(msg, True, purple)
    dis.blit(mesg, [dis_width / 3, dis_height / 7])


def game_loop():
    re = 0
    game_over = False
    col_bool = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2
 #   xp2 = dis_width / 3
#   yp2 = dis_height / 3

#   x2 = dis_width / 2
 #   y2 = dis_height / 2

    x1_change = 0
    y1_change = 0
 #   xp2_change = 0
#   yp2_change = 0

  #  x2_change = 0
  #  y2_change = 0

    snake_list = []
 #  snake_list2 = []

    projectile_list = []

    snake_colour = [black]
    projectile_colour = [black]
    length_of_snake = 1
   # length_of_snake2 = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    foodx2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    foodx3 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody3 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    foodx4 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody4 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:

            dis.fill(blue)
            message(f"You've Lost! Press C-Play Again or Q-Quit", red)
            your_score(length_of_snake - 1)
            #your_score2(length_of_snake2 - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_SPACE:
                    y2_change = projectile_block
                    x2_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        #xp2 += xp2_change
       # yp2 += yp2_change

       #x2 += x2_change
        #y2 += y2_change

        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, yellow, [foodx2, foody2, snake_block, snake_block])
        pygame.draw.rect(dis, purple, [foodx3, foody3, snake_block, snake_block])
        pygame.draw.rect(dis, green, [foodx4, foody4, snake_block, snake_block])
        snake_head = []
        #snake2_head = []

        projectile_head = []
        snake_head.append(x1)
        snake_head.append(y1)

        #snake2_head.append(xp2)
        #snake2_head.append(yp2)

        snake_list.append(snake_head)
        #snake_list2.append(snake2_head)

        #projectile_head.append(x2)
        #projectile_head.append(y2)

        projectile_list.append(projectile_head)
        computer = snake_colour[randint(0, 0)]
        #computer2 = snake_colour[randint(0, 0)]

# print(snake_colour)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        '''if len (snake_list2) > length_of_snake2:
            del snake_list2[0]'''

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = False

#        our_projectile(blue, bullet_block, projectile_list)
        our_snake(computer, snake_block, snake_list)
        your_score(length_of_snake - 1)

        '''for x in snake_list2[:-1]:
            if x == snake2_head:
                game_close = False'''

#        our_projectile(blue, bullet_block, projectile_list)
       #our_snake2(computer2, snake_block2, snake_list2)
       # your_score2(length_of_snake2 - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            # or xp2 == foodx and yp2 == foody:
            if snake_colour[0] == red:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                length_of_snake += 3
            else:
                snake_colour.append(red)
                snake_colour.pop(0)
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                length_of_snake += 1

        if x1 == foodx2 and y1 == foody2:
                #or xp2 == foodx and yp2 == foody:
            if snake_colour[0] == yellow:
                foodx2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                length_of_snake += 3
            else:
                snake_colour.append(yellow)
                snake_colour.pop(0)
                foodx2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                length_of_snake += 1

        if x1 == foodx3 and y1 == foody3:
            # or xp2 == foodx and yp2 == foody:
            if snake_colour[0] == purple:
                foodx3 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody3 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                length_of_snake += 3
            else:
                snake_colour.append(purple)
                snake_colour.pop(0)
                foodx3 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody3 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                length_of_snake += 1

        if x1 == foodx4 and y1 == foody4:
            #or xp2 == foodx and yp2 == foody:
            if snake_colour[0] == green:
                foodx4 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody4 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                length_of_snake += 3
            else:
                snake_colour.append(green)
                snake_colour.pop(0)
                foodx4 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody4 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
