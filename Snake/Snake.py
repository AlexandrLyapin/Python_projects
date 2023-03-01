import pygame
import time
import random
 
pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)    #вводим все цвета
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 1200    #размеры окошка
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

snake_block = 10  # размер змейки
record_e = '0'
record_m = '0'
record_h = '0'
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("Helvetica", 50)


def Your_score(score):
    value = score_font.render("Размер: " + str(score), True, yellow)
    dis.blit(value, [0, 540])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block]) #функция создания змейки


def message(msg, color):
    mesg = font_style.render(msg, True, color)  #первая функция для вывода текста на экран
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
    
def message1(msg, color, w, h):
    mesg = font_style.render(msg, True, color) #вторая функция для вывода текста на экран
    dis.blit(mesg, [w, h])


def gameLoop():
    global record_e
    global record_m
    global record_h
    ind = 0
    series = 0
    game_open = True
    game_open1 = True
    snake_speed = 1
    lastbutton = 'I'
    while game_open == True:
        dis.fill(black)
        message1("Выберите режим:", white, 470, 200)
        message1("'E' - лёгкий, 'M' - средний, 'H' - сложный", white, 350, 250) #выбираем слоность игры
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    snake_speed = 15
                    game_open = False
                    k = 0
                if event.key == pygame.K_m:
                    snake_speed = 25
                    game_open = False
                    k = 1
                if event.key == pygame.K_h:
                    snake_speed = 35
                    game_open = False
                    k = 2
                    
    while game_open1 == True:
        dis.fill(black)
        message1("Выберите цвет змейки:", white, 420, 200)
        message1("G - зелёная", green, 500, 250)
        message1("B - голубая", blue, 500, 300)     #Выбираем цвет змейки
        message1("Y - жёлтая", yellow, 500, 350)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    def our_snake(snake_block, snake_list):
                        for x in snake_list:
                            pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
                    game_open1 = False
                if event.key == pygame.K_b:
                    def our_snake(snake_block, snake_list):
                        for x in snake_list:
                            pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])
                    game_open1 = False
                if event.key == pygame.K_y:
                    def our_snake(snake_block, snake_list):
                        for x in snake_list:
                            pygame.draw.rect(dis, yellow, [x[0], x[1], snake_block, snake_block])
                    game_open1 = False

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #создание координат яблок
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    bonusx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #создание координат яблок
    bonusy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0     
    

    while not game_over:
        while game_close == True:
                    dis.fill(black)
                    message1("'W' - начать заново, 'Q' - закончить игру", white, 310, 250) #то, что будет происходить в конце игры
                    message1("Рекорд в лёгком: ", yellow, 20, 20)
                    message1(record_e, yellow, 270, 22)
                    message1("Рекорд в среднем: ", yellow, 20, 55)
                    message1(record_m, yellow, 290, 57)
                    message1("Рекорд в тяжёлом: ", yellow, 20, 90)
                    message1(record_h, yellow, 290, 92)                 
                    message1("Счёт в этой игре: ", yellow, 20, 125)
                    message1(str(Length_of_snake - 1), yellow, 270, 127)
                    Your_score(Length_of_snake - 1)
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_w:
                                gameLoop()                            
                            if event.key == pygame.K_q:
                                game_over = True
                                game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if lastbutton != 'D':
                        lastbutton = 'A'
                        x1_change = -snake_block
                        y1_change = 0
                elif event.key == pygame.K_d:
                    if lastbutton != 'A':
                        lastbutton = 'D'
                        x1_change = snake_block   #действия для каждой клавиши
                        y1_change = 0
                elif event.key == pygame.K_w:
                    if lastbutton != 'S':
                        lastbutton = 'W'
                        y1_change = -snake_block
                        x1_change = 0
                elif event.key == pygame.K_s:
                    if lastbutton != 'W':
                        lastbutton = 'S'
                        y1_change = snake_block
                        x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #если выходим за пределы поля, то гг
            game_close = True
        x1 += x1_change
        y1 += y1_change #изменение положения змейки
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        if series >= 5 and ind == 0:
            pygame.draw.rect(dis, blue, [bonusx, bonusy, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True        

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            series += 1
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  #То, что происходит после съедания яблока
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            if ind == 0:
                Length_of_snake += 1
            if ind == 1 and series == 6:
                Length_of_snake += 5
                series = 0
            ind = 0
            if series == 6:
                series = 0
            if k == 0:
                if int(record_e) <  Length_of_snake - 1:
                    record_e = str(Length_of_snake - 1)                
                snake_speed += 2
            if k == 1:
                if int(record_m) <  Length_of_snake - 1:
                    record_m = str(Length_of_snake - 1)                
                snake_speed += 3
            if k == 2:
                if int(record_h) <  Length_of_snake - 1:
                    record_h = str(Length_of_snake - 1)                
                snake_speed += 4

        if x1 == bonusx and y1 == bonusy:
            bonusx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #создание координат яблок
            bonusy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0     
            ind = 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()
gameLoop()