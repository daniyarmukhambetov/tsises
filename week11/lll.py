# Paint
import pygame, random


# (x1, y1), (x2, y2)
# A = y2 - y1
# B = x1 - x2
# C = x2 * y1 - x1 * y2
# Ax + By + C = 0
# (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)

def drawLine(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)


def circle(screen, pos, radius, param, col):
    pygame.draw.circle(screen, col, pos, radius, param)


def draw_rect(screen, param, col, width=0):
    pygame.draw.rect(screen, col, param, width)


def draw_line(screen, pos1, pos2, col, width=1):
    pygame.draw.line(screen, col, pos1, pos2, width)


pp1 = [-1, -1]
pp2 = [-1, -1]


def up():
    global pp1, pp2
    pp1 = [-1, -1]
    pp2 = [-1, -1]


def main():
    global pp1, pp2
    screen = pygame.display.set_mode((800, 600))
    mode = 0
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 10

    # colors = {
    #     'red': (255, 0, 0),
    #     'blue': (0, 0, 255),
    #     'green': (0, 255, 0)
    # }
    colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0)]
    r = 0
    w = 10
    h = 10
    widd = 1
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if r == 0:
                if event.type == pygame.QUIT:
                    pygame.image.save(screen, 'screenshot.jpg')
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and ctrl_held:
                        return
                    if event.key == pygame.K_F4 and alt_held:
                        return
                    if event.key == pygame.K_r:
                        mode = 0
                    if event.key == pygame.K_b:
                        mode = 1
                    if event.key == pygame.K_g:
                        mode = 2
                    if event.key == pygame.K_UP:
                        radius += 1
                    if event.key == pygame.K_DOWN:
                        radius -= 1
                    if event.key == pygame.K_t:
                        r += 1
                        r %= 5
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #     if mode == 'random':
                    #         color = (random.randrange(256), random.randrange(256), random.randrange(256))
                    #     else:
                    color = colors[mode]
                    pygame.draw.circle(screen, color, event.pos, radius)
                    draw_on = True
                if event.type == pygame.MOUSEBUTTONUP:
                    draw_on = False
                    last_pos = (0, 0)
                if event.type == pygame.MOUSEMOTION:
                    if draw_on:
                        drawLine(screen, last_pos, event.pos, radius, color)
                        # pygame.draw.circle(screen, color, event.pos, radius)
                    last_pos = event.pos
            elif r == 1:
                param = 0
                if event.type == pygame.QUIT:
                    pygame.image.save(screen, 'screenshot.jpg')
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and ctrl_held:
                        return
                    if event.key == pygame.K_r:
                        mode = 0
                    if event.key == pygame.K_b:
                        mode = 1
                    if event.key == pygame.K_g:
                        mode = 2
                    if event.key == pygame.K_UP:
                        radius += 1
                    if event.key == pygame.K_DOWN:
                        radius -= 1
                    if event.key == pygame.K_t:
                        r += 1
                        r %= 5
                    if event.key == pygame.K_w:
                        param ^= 1
                # if event.type == pygame.KEYDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    circle(screen, pygame.mouse.get_pos(), radius, param, colors[mode])
            elif r == 2:
                wid = 0
                if event.type == pygame.QUIT:
                    pygame.image.save(screen, 'screenshot.jpg')
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and ctrl_held:
                        return
                    if event.key == pygame.K_F4 and alt_held:
                        return
                    if event.key == pygame.K_r:
                        mode = 0
                    if event.key == pygame.K_b:
                        mode = 1
                    if event.key == pygame.K_g:
                        mode = 2
                    if event.key == pygame.K_UP:
                        h += 5
                    if event.key == pygame.K_DOWN:
                        h -= 5
                    if event.key == pygame.K_LEFT:
                        w -= 5
                    if event.key == pygame.K_RIGHT:
                        w += 5
                    if event.key == pygame.K_m:
                        wid ^= 1
                    if event.key == pygame.K_t:
                        r += 1
                        r %= 5
                x, y = pygame.mouse.get_pos()
                param = [x, y, w, h]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    draw_rect(screen, param, colors[mode], wid)
            elif r == 3:
                if event.type == pygame.QUIT:
                    pygame.image.save(screen, 'screenshot.jpg')
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and ctrl_held:
                        return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        mode = 0
                    if event.key == pygame.K_b:
                        mode = 1
                    if event.key == pygame.K_g:
                        mode = 2
                    if event.key == pygame.K_s:
                        pp1 = pygame.mouse.get_pos()
                    if event.key == pygame.K_e:
                        pp2 = pygame.mouse.get_pos()
                    if event.key == pygame.K_UP:
                        widd += 1
                    if event.key == pygame.K_DOWN:
                        widd -= 1
                    if event.key == pygame.K_t:
                        r += 1
                        r %= 5
                    if pp1 != [-1, -1] and pp2 != [-1, -1]:
                        draw_line(screen, pp1, pp2, colors[mode], widd)
                        up()

            elif r == 4:
                if event.type == pygame.QUIT:
                    pygame.image.save(screen, 'screenshot.jpg')
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and ctrl_held:
                        return
                    if event.key == pygame.K_F4 and alt_held:
                        return
                    if event.key == pygame.K_UP:
                        radius += 1
                    if event.key == pygame.K_DOWN:
                        radius -= 1
                    if event.key == pygame.K_t:
                        r += 1
                        r %= 5
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #     if mode == 'random':
                    #         color = (random.randrange(256), random.randrange(256), random.randrange(256))
                    #     else:
                    color = (0, 0, 0)
                    pygame.draw.circle(screen, color, event.pos, radius)
                    draw_on = True
                if event.type == pygame.MOUSEBUTTONUP:
                    draw_on = False
                    last_pos = (0, 0)
                if event.type == pygame.MOUSEMOTION:
                    if draw_on:
                        drawLine(screen, last_pos, event.pos, radius, color)
                        # pygame.draw.circle(screen, color, event.pos, radius)
                    last_pos = event.pos

        pygame.display.flip()

    pygame.quit()


main()

# rect = pygame.Rect(10, 20, 30, 50)
# print(rect.bottom)
# print(rect.top)
# print(rect.left)
# print(rect.right)
# print(rect.bottomleft)
# print(rect.bottomright)
# print(rect.center)
