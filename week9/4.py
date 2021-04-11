import pygame
import math
pygame.init()
black = (0, 0, 0)
whilte = (255, 255, 255)
red =(255, 0, 0)
blue = (0, 0, 255)
size = h, w = (700, 500)
screen =pygame.display.set_mode(size)
screen.fill(whilte)
pygame.display.set_caption("ARU GAME")
done = False
cnt = 50
cnt1 = 50
for n1 in range(48):
    cnt +=12.5
    pygame.draw.line(screen, black, [0 + cnt, 30], [0 +cnt, 40], 1)
    pygame.draw.line(screen, black, [0 +cnt, 460], [0 +cnt, 470], 1)
for n3 in range(32):
    cnt1+=12.5
    pygame.draw.line(screen, black, [30, 0+cnt1], [40, 0+cnt1], 1)
    pygame.draw.line(screen, black, [660, 0+cnt1], [670, 0+cnt1], 1)
pygame.draw.line(screen, black, [30, 30], [670, 30], 5)
pygame.draw.line(screen, black, [30, 30], [30, 470], 5)
pygame.draw.line(screen, black, [30, 470], [670, 470], 5)
pygame.draw.line(screen, black, [670, 30], [670, 470], 5)
pygame.draw.line(screen, black, [350, 30], [350, 470], 5)
pygame.draw.line(screen, black, [30, 250], [670, 250], 5)
for i in range(50, 700,100):
    pygame.draw.line(screen, black, [0 + i, 30], [0+i, 470], 1)
    pygame.draw.line(screen, black, [0+ i +50, 30 ], [0 + i +50, 47], 1)
    pygame.draw.line(screen, black, [0 +i + 50,453], [0 + i +50, 470], 1)
for n in range(50,650,25):
    pygame.draw.line(screen, black, [0+ n, 30 ], [0 + n, 44], 1)
    pygame.draw.line(screen, black, [0+ n, 456 ], [0 + n, 470], 1)
for j in range(50, 500,50):
    pygame.draw.line(screen, black, [30, 0+j], [670, 0+j], 1)
for n2 in range(50,450,25):
    pygame.draw.line(screen,black, [30,0+n2],[44,0+n2],1)
    pygame.draw.line(screen, black, [656, 0+n2], [670, 0+n2],1)
def draw_cos():
    x = -3 * math.pi
    real_x = 50
    # float(real_x)
    dx = math.pi / 1000
    real_dx = 100 / 1000
    points_cos = []
    while real_x <= 650:
        pair = (real_x, 250 - 200 * math.cos(x))
        points_cos.append(pair)
        real_x += real_dx
        x += dx
    pygame.draw.aalines(screen, blue , False, points_cos)
def draw_sin():
    real_x = 50
    x = -3 * math.pi
    real_dx = 100 / 1000
    dx = math.pi / 1000
    points_sin = []
    while real_x <= 650:
        pair = (real_x, 250 - math.sin(x) * 200)
        points_sin.append(pair)
        real_x += real_dx
        x += dx
    pygame.draw.aalines(screen, red, False, points_sin)
draw_cos()
draw_sin()
n = -1.00
cnt4 =0
while n<=1:
    font = pygame.font.Font(None,20)
    text = font.render(str(n), True, black)
    screen.blit(text, (0, 40 + cnt4))
    cnt4 +=50
    n +=0.25
nn = -3
cnt5 =0
while nn<=3:
    if nn%1!=0.5:
        font = pygame.font.Font(None,20)
        text1 = font.render(str(nn) + "П",True, black)
        screen.blit(text1, (40 + cnt5, 480))
    elif nn%1==0.5:
        font = pygame.font.Font(None,15)
        text1 = font.render(str(int(nn*2)) +"/2" + "П",True, black)
        screen.blit(text1, (40 + cnt5, 480))
    cnt5 +=50
    nn +=0.5
while not done:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()