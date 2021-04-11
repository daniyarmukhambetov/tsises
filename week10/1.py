import pygame, sys
from pygame.locals import *
import random, time
import math

pygame.init()
sc_w = 400
sc_h = 600
sc = pygame.display.set_mode((sc_w, sc_h))

done = False

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

cnt2 = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.surface.Surface((40, 80))
        self.rect = self.surf.get_rect(center=(200, 560))

    def move(self):
        sc.blit(self.image, self.rect)
        keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if keys[pygame.K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 600:
            if keys[pygame.K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 400:
            if keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)


espeed = random.randint(2, 5) + 2.5


# def find_valid(x, y, speed):
#     a = random.random()
#     print(a)
#     res = []
#     xx = [60, 210, 360]
#     if a % 2 == 0:
#         speed0 = speed - random.randrange(1, speed + 1)
#         if speed0 <= 0:
#             speed0 = speed / 2
#         x0 = x
#         y0 = random.randrange(-200, -100)
#         res.append(x0)
#         res.append(y0)
#         res.append(speed)
#     if a % 2 == 1:
#         speed0 = speed + random.randrange(-speed + 1, 2 * speed + 1)
#         if speed0 <= 0:
#             speed0 = speed / 2
#         x0 = xx[random.randint(1, 2)]
#         y0 = random.randrange(-200, -100)
#         res.append(x0)
#         res.append(y0)
#         res.append(speed)
#     return res


cnt = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.surface.Surface((40, 80))
        self.rect = self.surf.get_rect(center=(x, y))
        self.speed = speed

    def move(self):
        global cnt
        sc.blit(self.image, self.rect)
        if self.rect.top > 600:
            cnt += 1
            # a = find_valid(x, y, speed)
            # a = []
            # self.speed = 3
            xx = [60, 210, 360]
            x = xx[random.randint(0, 2)]
            y = random.randint(-200, -100)
            self.speed = random.randint(3, 7)
            self.rect.center = (x, y)
        else:
            self.rect.move_ip(0, self.speed)


class Line:
    def __init__(self, y):
        self.x = y
        self.y = [-200, 0, 200, 400]
        self.speed = 2

    def move(self):
        for i in range(4):
            pygame.draw.rect(sc, WHITE, (self.x, self.y[i], 20, 100))
            if self.y[i] == 600:
                self.y[i] = -200
            else:
                self.y[i] += self.speed


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()
        self.image = pygame.image.load("coin.png")
        self.surf = pygame.surface.Surface((30, 30))
        self.rect = self.surf.get_rect(center=(random.randint(30, 370), -10))

    def move(self):
        sc.blit(self.image, self.rect)
        if self.rect.top >= 600:
            xx = [60, 210, 260]
            self.rect.center = (random.randint(30, 370), -10)
        else:
            self.rect.move_ip(0, 2)

    def change(self):
        self.rect.center = (random.randint(30, 370), -10)


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
p = Player()
L1 = Line(120)
L2 = Line(260)
e1 = Enemy(60, -50, 5)
all_sprites.add(p)
all_sprites.add(e1)
enemies = pygame.sprite.Group()
enemies.add(e1)
coin = Coin()
coins.add(coin)
# e2 = Enemy(210, -50, 4)
score = pygame.font.SysFont("lalala", 20)
total = pygame.font.SysFont("alala", 30)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    sc.fill((155, 155, 155))
    L1.move()
    L2.move()
    coin.move()
    p.move()
    e1.move()
    if (abs(p.rect.top - coin.rect.bottom) <= 5 or abs(coin.rect.top - p.rect.bottom) <= 5) and (
            abs(-p.rect.right + coin.rect.left <= 0) or abs(-coin.rect.right - p.rect.left) <= 5):
        coin.rect.center = (random.randint(30, 370), random.randint(-200, -30))
        cnt2 += 1
    sc.blit(total.render(str(cnt2), True, RED), (370, 10))

    if pygame.sprite.spritecollideany(p, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        sc.fill(RED)
        sc.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    sc.blit(score.render(str(cnt), True, BLACK), (10, 10))
    pygame.display.update()
    clock.tick(60)
