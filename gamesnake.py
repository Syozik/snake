import pygame
import sys
import random
import pygame_menu

pygame.init()

bg = pygame.image.load("snake3.jpg")
# bg2 = pygame.image.load("chuma1.jpg")
pygame.mixer.music.load("phonk3.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0)

COLOR = (20, 255, 255)
WHITE = (255, 255, 255)
DARK = (0,0,0)
BLUE = (204, 255, 255)
RED = (224, 0, 0)
FON = (155,200,100)
SNAKE_COLOR = (102,102,102)
KOL_BLOCK = 20
MARGA = 70
SIZE_BLOCK = 20
SPEED = 1
speed_otstup = 280
diff = 'easy'
welcome = 'Welcome!'
easy = 'Еasy'
medium = 'Medium'
hard = 'Hard'
Total = 'Total'
Speed = 'Speed'
welcome = 'Welcome'
name = 'Name: '
default = 'SJ'
play = 'Play'
Easy = 'Easy'
Medium = 'Medium'
Hard = 'Hard'
music_on = 'Music: ON'
music_off = 'Music: OFF'
English = 'English'
Russian = 'Russian'
Ukrainian = 'Ukrainian'
Exit = 'Exit'
language = 'english'

size = [SIZE_BLOCK*KOL_BLOCK + 2*SIZE_BLOCK+KOL_BLOCK, SIZE_BLOCK*KOL_BLOCK + 2*SIZE_BLOCK + KOL_BLOCK + MARGA]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
surface = pygame.display.set_mode(size)
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 28)


class SnakeBlock:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0<=self.x<SIZE_BLOCK and 0<=self.y<SIZE_BLOCK

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK+column*SIZE_BLOCK + column+1, MARGA + SIZE_BLOCK + row*SIZE_BLOCK + row + 1, SIZE_BLOCK, SIZE_BLOCK])


def start_music():
    pygame.mixer.music.set_volume(0.5)
def pause_music():
    pygame.mixer.music.set_volume(0)

def start_the_game():
    
    def get_empty_block():
        x = random.randint(0, KOL_BLOCK - 1)
        y = random.randint(0, KOL_BLOCK - 1)
        empty_block = SnakeBlock(x,y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, KOL_BLOCK - 1)
            empty_block.y = random.randint(0, KOL_BLOCK)    
        return empty_block
    
    snake_blocks = [SnakeBlock(9,8), SnakeBlock(9,9), SnakeBlock(9,10)]
    apple = get_empty_block()
    d_row = buf_row = 0
    d_col = buf_col = 1
    total = 0
    speed = SPEED
    running = True
    while running == True:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.exit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w and d_col!=0:
                    buf_row = -1
                    buf_col = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s and d_col!=0:
                    buf_row = 1
                    buf_col = 0
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and d_row!=0:
                    buf_row = 0
                    buf_col = -1
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and d_row!=0:
                    buf_row = 0
                    buf_col = 1
                if event.key == pygame.K_p:
                    pause_music()
                if event.key == pygame.K_o:
                    start_music()
                    
        screen.fill(COLOR)
        pygame.draw.rect(screen, FON, [0, 0, size[0], MARGA])
        
        text_total = courier.render(f"{Total}: {total}", 10, DARK)
        text_speed = courier.render(f'{Speed}: {speed}', 10, DARK)
        
        screen.blit(text_total,(SIZE_BLOCK, SIZE_BLOCK))
        screen.blit(text_speed, (SIZE_BLOCK+speed_otstup, SIZE_BLOCK))

        for row in range (KOL_BLOCK):
            for column in range(KOL_BLOCK):
                if(row+column)%2==0:
                    color = BLUE
                else:
                    color = WHITE
                draw_block(color,row,column)

        head = snake_blocks[-1]
        if not head.is_inside():
            # print("You lose")
            break

        draw_block(RED, apple.x, apple.y)
        for block in snake_blocks:            
            draw_block(SNAKE_COLOR, block.x, block.y)
        
        if apple == head:
            total += 1
            snake_blocks.append(apple)
            apple = get_empty_block()
        speed = total // 5 + SPEED
        
        d_row = buf_row
        d_col = buf_col
        new_head = SnakeBlock(head.x + d_row, head.y + d_col)
        
        if new_head in snake_blocks:
            break

        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        pygame.display.flip()
        timer.tick(3+speed)

def easy_diff():
    global SPEED, diff
    SPEED = 1
    diff = 'easy'
    menu()
def medium_diff():
    global SPEED, diff
    SPEED = 5
    diff = 'medium'
    menu()
def hard_diff():
    global SPEED, diff
    SPEED = 10
    diff = 'hard'
    menu()
def language_english():
    global language, Total, Speed, welcome, name, default, play, music_on, music_off, English, Russian, Ukrainian, Exit, speed_otstup, easy, medium, hard
    language = 'english'
    easy = 'Easy'
    medium = 'Medium'
    hard = 'Hard'
    Total = 'Total'
    Speed = 'Speed'
    welcome = 'Welcome!'
    name = 'Name: '
    default = 'SJ'
    play = 'Play'
    music_on = 'Music: ON'
    music_off = 'Music: OFF'
    English = 'English'
    Russian = 'Russian'
    Ukrainian = 'Ukrainian'
    Exit = 'Exit'
    speed_otstup = 280
    menu()
    
def language_russian():
    global language, Total, Speed, welcome, name, default, play, music_on, music_off, English, Russian, Ukrainian, Exit, speed_otstup, easy, medium, hard
    easy = 'Легко'
    medium = 'Нормально'
    hard = 'Сложно'
    language = 'russian'
    Total = 'Очки'
    Speed = 'Скорость'
    welcome = 'Добро пожаловать!'
    name = 'Имя: '
    default = 'SJ'
    play = 'Играть'
    Easy = 'Легко'
    Medium = 'Нормально'
    Hard = 'Тяжело'
    music_on = 'Mузыка: вкл.'
    music_off = 'Mузыка: выкл.'
    English = 'Английский'
    Russian = 'Русский'
    Ukrainian = 'Украинский'
    Exit = 'Выход'
    speed_otstup = 230
    menu()

    
def language_ukrainian():
    global language, Total, Speed, welcome, name, default, play, music_on, music_off, English, Russian, Ukrainian, Exit, speed_otstup, easy, medium, hard
    language = 'ukrainian'
    easy = 'Легко'
    medium = 'Помірно'
    hard = 'Складно'
    Total= 'Очки'
    Speed = 'Швидкість'
    welcome = 'Ласкаво просимо!'
    name = 'Ім\'я: '
    play = 'Грати'
    music_on = 'Музика: ввімк.'
    music_off = 'Музика: ввимк.'
    English = 'Англійська'
    Russian = 'Російська'
    Ukrainian = 'Українська'
    Exit = 'Вихід'
    speed_otstup = 200
    menu()


main_theme = pygame_menu.themes.THEME_DARK.copy()
main_theme.set_background_color_opacity(0.75)

def menu():

    menu = pygame_menu.Menu(400,450, f'{diff}', theme=main_theme)
     # menu.add_text_input(f'{name}', default = 'default')
    # menu.add_selector('Складність:',[('Hard', 1), ('Easy', 2)], onchange = set_difficulty)
    menu.add_button(f'{play}', start_the_game)
    if diff == 'easy':
        menu.add_button(f'{medium}', medium_diff)
        menu.add_button(f'{hard}', hard_diff)
    if diff =='medium':
        menu.add_button(f'{easy}', easy_diff)
        menu.add_button(f'{hard}', hard_diff)
    if diff == 'hard':
        menu.add_button(f'{easy}', easy_diff)
        menu.add_button(f'{medium}', medium_diff)

    menu.add_button(f'{music_on}', start_music)
    menu.add_button(f'{music_off}', pause_music)
    if (language == 'english'):
        menu.add_button(f'{Ukrainian}', language_ukrainian)
        menu.add_button(f'{Russian}', language_russian)
    elif language == 'russian':
        menu.add_button(f'{English}', language_english)
        menu.add_button(f'{Ukrainian}', language_ukrainian)
    elif language == 'ukrainian':
        menu.add_button(f'{English}', language_english)
        menu.add_button(f'{Russian}', language_russian)
    
    menu.add_button(f'{Exit}',pygame_menu.events.EXIT)
    while True:
            
            screen.blit(bg, (0,0))

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                
            if menu.is_enabled():
                menu.update(events)
                menu.draw(screen)
            
            pygame.display.update()
menu()

