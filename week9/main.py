import pygame
import math

red = (255, 0, 0)
B = (0, 0, 0)
points = []
size = width, height = (840, 600)
screen = pygame.display.set_mode(size)  # объект на котором мы работаем
screen.fill((255, 255, 255))  # white

pygame.draw.rect(screen, B, (60, 20, 760, 520), 2)  # экран, цвет, (x, y, w, h)
pygame.draw.line(screen, B, [440, 20], [440, 540], 2)
pygame.draw.line(screen, B, [60, 280], [820, 280], 2)

for i in range(80, 801, 120):
    pygame.draw.line(screen, B, [i, 20], [i, 540], 1)

for i in range(40, 521, 60):
    pygame.draw.line(screen, B, [60, i], [820, i], 1)

for i in range(95, 786, 30):
    pygame.draw.line(screen, B, [i, 20], [i, 25], 1)
    pygame.draw.line(screen, B, [i, 540], [i, 535], 1)

for i in range(110, 771, 60):
    pygame.draw.line(screen, B, [i, 20], [i, 30], 1)
    pygame.draw.line(screen, B, [i, 540], [i, 530], 1)

for i in range(140, 741, 120):
    pygame.draw.line(screen, B, [i, 20], [i, 35], 1)
    pygame.draw.line(screen, B, [i, 540], [i, 525], 1)

for i in range(55, 506, 30):
    pygame.draw.line(screen, B, [60, i], [65, i], 1)
    pygame.draw.line(screen, B, [815, i], [820, i], 1)

for i in range(70, 491, 60):
    pygame.draw.line(screen, B, [60, i], [70, i], 1)
    pygame.draw.line(screen, B, [810, i], [820, i], 1)

points = []
n = 6
A = 180
for x in range(80, 801):
    # if x >= 80 and x <= 800:
    y = float(math.sin(abs(80 - x) * (math.pi / 120)) * 240 + 280)
    # if y >= 40 and y <= 760:
    points.append([x, y])
pygame.draw.aalines(screen, red, False, points, 3)


# def draw_cos_line():
x = 0
y1 = 0
y2 = 0
for x in range(80, 801, 3):
    y1 = 240 * math.cos((x - 80) / 120 * math.pi)
    y2 = 240 * math.cos((x - 79) / 120 * math.pi)
    pygame.draw.aalines(screen, (0, 0, 255), False, [(x, 280 + y1), ((x + 1), 280 + y2)])
# draw_cos_line()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()
