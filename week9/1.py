import pygame
import math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
done = False
display = pygame.display.set_mode((700, 500))


# pygame.draw.rect(display, BLACK, (10, 10, 800, 600))
def draw_verticals():
    x = 50
    while x <= 650:
        if x != 350:
            pygame.draw.line(display, BLACK, (x, 30), (x, 470), 1)
        else:
            pygame.draw.line(display, BLACK, (x, 30), (x, 470), 3)
        x += 100


def draw_horizontals():
    y = 50
    while y <= 450:
        if y != 250:
            pygame.draw.line(display, BLACK, (30, y), (670, y), 1)
        else:
            pygame.draw.line(display, BLACK, (30, y), (670, y), 3)
        y += 50


def draw_something1():
    x = 50
    small = 5
    large = 10
    mid = 15
    while x < 650:
        delta = 0
        for i in range(8):
            if i % 2 == 0:
                if i != 4:
                    pygame.draw.line(display, BLACK, (x + delta, 30), (x + delta, 30 + large), 1)
                else:
                    pygame.draw.line(display, BLACK, (x + delta, 30), (x + delta, 30 + mid), 1)
            else:
                pygame.draw.line(display, BLACK, (x + delta, 30), (x + delta, 30 + small), 1)
            delta += 12.5
        x += 100


def draw_something2():
    y = 50
    small = 5
    large = 10
    while y < 450:
        delta = 0
        for i in range(4):
            if i % 2 == 0:
                pygame.draw.line(display, BLACK, (30, y + delta), (30 + small, y + delta), 1)
            else:
                pygame.draw.line(display, BLACK, (30, y + delta), (30 + large, y + delta), 1)
            delta += 12.5
        y += 50


def draw_something3():
    x = 50
    small = 5
    large = 10
    mid = 15
    while x < 650:
        delta = 0
        for i in range(8):
            if i % 2 == 0:
                if i != 4:
                    pygame.draw.line(display, BLACK, (x + delta, 470), (x + delta, 470 - large), 1)
                else:
                    pygame.draw.line(display, BLACK, (x + delta, 470), (x + delta, 470 - mid), 1)
            else:
                pygame.draw.line(display, BLACK, (x + delta, 470), (x + delta, 470 - small), 1)
            delta += 12.5
        x += 100


def draw_something4():
    y = 50
    small = 5
    large = 10
    while y < 450:
        delta = 0
        for i in range(4):
            if i % 2 == 0:
                pygame.draw.line(display, BLACK, (670, y + delta), (670 - small, y + delta), 1)
            else:
                pygame.draw.line(display, BLACK, (670, y + delta), (670 - large, y + delta), 1)
            delta += 12.5
        y += 50


def draw_cos():
    x = -3 * math.pi
    real_x = 50
    # float(real_x)
    dx = math.pi / 100
    real_dx = 100 / 100
    points_cos = []
    while real_x <= 650:
        pair = (real_x, 250 - 200 * math.cos(x))
        points_cos.append(pair)
        real_x += real_dx
        x += dx
    pygame.draw.aalines(display, BLUE, False, points_cos)


# pygame.draw.line()
# pygame.draw.lines()
def draw_sin():
    real_x = 50
    x = -3 * math.pi
    real_dx = 100 / 100
    dx = math.pi / 100
    points_sin = []
    while real_x <= 650:
        pair = (real_x, 250 - math.sin(x) * 200)
        points_sin.append(pair)
        real_x += real_dx
        x += dx
    pygame.draw.aalines(display, RED, False, points_sin)


# def insert_txt1():
#     y =
f_of_x = []


def get_fx():
    fx = -1
    while fx <= 1.00:
        font = pygame.font.SysFont(str(fx), 20)
        f_of_x.append(font.render(str(fx), True, BLACK))
        fx += 0.25


def fill_fx():
    get_fx()
    y = 450
    for text in f_of_x:
        display.blit(text, (0, y - 5))
        y -= 50


X = []


def get_x():
    x = -3
    cnt = 0
    while x <= 3:
        if cnt % 2 == 0:
            font = pygame.font.SysFont(f'{str(x)}pi', 20)
            X.append(font.render(f'{str(x)}pi', True, BLACK))
        else:
            font = pygame.font.SysFont(f'{str(int(x * 2))}/2pi', 20)
            X.append(font.render(f'{str(int(x * 2))}/2pi', True, BLACK))
        cnt += 1
        x += 0.5


def fill_x():
    get_x()
    x = 50
    for value in X:
        display.blit(value, (x - 5, 480))
        x += 50


def draw_cos_dashed():
    for x in range(50, 651, 3):
        cos_y1 = 200 * math.cos((x - 50) / 100 * math.pi)
        cos_y2 = 200 * math.cos((x - 49) / 100 * math.pi)
        pygame.draw.aalines(display, BLUE, False, [(x, 250 + cos_y1), ((x + 1), 250 + cos_y2)])


display.fill(WHITE)
pygame.draw.rect(display, BLACK, (30, 30, 640, 440), 2)
draw_horizontals()
draw_verticals()
draw_something1()
draw_something2()
draw_something3()
draw_something4()
# draw_cos()
draw_sin()
draw_cos_dashed()
fill_fx()
fill_x()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()
