import pygame
import math
import random
import sys
import time
import pickle

pygame.init()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

done = False
sc_h = 600
sc_w = 800
screen = pygame.display.set_mode((sc_w, sc_h))

snake_speed = 10


class Walls:
    def __init__(self):
        self.wall = []
        self.wall.append([0, 0, sc_w, 20])
        self.wall.append([0, 0, 20, sc_w])
        self.wall.append([0, sc_h - 20, sc_w, 20])
        self.wall.append([sc_w - 20, 0, 20, sc_h])

    def draw(self):
        for w in self.wall:
            pygame.draw.rect(screen, BLACK, w)

    def add_wall(self, head):
        x = random.randint(20, 780)
        y = random.randint(20, 580)
        if math.sqrt((x - head[0]) ** 2 + (y - head[0]) ** 2) >= 20:
            self.wall.append([x, y, 20, 20])


head_im = pygame.image.load("head.png")
body_im = pygame.image.load("body.png")


class Snake:
    def __init__(self, sn_x, sn_y):
        # super(Snake, self).__init__()
        self.hx = sn_x
        self.hy = sn_y
        self.snake = []
        self.snake.append([self.hx, self.hy])
        self.directory = [snake_speed, 0]
        self.rect = pygame.Rect((self.hx, self.hy, 10, 10))

    def move(self):
        keys = pygame.key.get_pressed()
        i = len(self.snake)
        if keys[pygame.K_UP] and self.directory != [0, snake_speed]:
            self.directory = [0, -snake_speed]
        if keys[pygame.K_DOWN] and self.directory != [0, -snake_speed]:
            self.directory = [0, snake_speed]
        if keys[pygame.K_RIGHT] and self.directory != [-snake_speed, 0]:
            self.directory = [snake_speed, 0]
        if keys[pygame.K_LEFT] and self.directory != [snake_speed, 0]:
            self.directory = [-snake_speed, 0]
        n = len(self.snake)
        i = 0
        # pygame.draw.rect(screen, BLUE, (self.snake[0][0], self.snake[0][1], 10, 10))
        screen.blit(head_im, self.snake[0])
        self.rect.center = temp = [self.snake[0][0] + self.directory[0], self.snake[0][1] + self.directory[1]]
        while i <= n - 1:
            # pygame.draw.rect(screen, BLUE, (self.snake[i][0], self.snake[i][1], 10, 10))
            screen.blit(body_im, self.snake[i])
            temp1 = self.snake[i]
            self.snake[i] = temp
            temp = temp1
            i += 1
        ok = self.snake[0][0] > 790 or self.snake[0][0] < 10 or self.snake[0][1] > 590 or self.snake[0][1] < 10
        ko = False
        for i in range(1, len(self.snake)):
            ko |= self.snake[0] == self.snake[i]
        if ok or ko:
            return False
        return True

    def add_block(self):
        n = len(self.snake)
        x = self.snake[n - 1][0]
        y = self.snake[n - 1][1]
        if n == 1:
            if self.directory == [snake_speed, 0]:
                self.snake.append([x - 10, y])
            if self.directory == [-snake_speed, 0]:
                self.snake.append([x + 10, y])
            if self.directory == [0, snake_speed]:
                self.snake.append([x, y - 10])
            if self.directory == [0, -snake_speed]:
                self.snake.append([x, y + 10])
        else:
            x1, y1 = self.snake[n - 2][0], self.snake[n - 2][1]
            if x == x1:
                if y < y1:
                    self.snake.append([x, y - 10])
                else:
                    self.snake.append([x, y + 10])
            if y == y1:
                if x < x1:
                    self.snake.append([x - 10, y])
                else:
                    self.snake.append([x + 10, y])

        # print(len(self.snake))


class Snake2():
    def __init__(self, sn_x, sn_y):
        # super(Snake, self).__init__()
        self.hx = sn_x
        self.hy = sn_y
        self.snake = []
        self.snake.append([self.hx, self.hy])
        self.directory = [snake_speed, 0]
        self.rect = pygame.Rect((self.hx, self.hy, 10, 10))

    def move(self):
        keys = pygame.key.get_pressed()
        i = len(self.snake)
        if keys[pygame.K_w] and self.directory != [0, snake_speed]:
            self.directory = [0, -snake_speed]
        if keys[pygame.K_s] and self.directory != [0, -snake_speed]:
            self.directory = [0, snake_speed]
        if keys[pygame.K_d] and self.directory != [-snake_speed, 0]:
            self.directory = [snake_speed, 0]
        if keys[pygame.K_a] and self.directory != [snake_speed, 0]:
            self.directory = [-snake_speed, 0]
        n = len(self.snake)
        i = 0
        pygame.draw.rect(screen, BLUE, (self.snake[0][0], self.snake[0][1], 10, 10))
        self.rect.center = temp = [self.snake[0][0] + self.directory[0], self.snake[0][1] + self.directory[1]]
        while i <= n - 1:
            pygame.draw.rect(screen, BLUE, (self.snake[i][0], self.snake[i][1], 10, 10))
            temp1 = self.snake[i]
            self.snake[i] = temp
            temp = temp1
            i += 1
        ok = self.snake[0][0] > 790 or self.snake[0][0] < 10 or self.snake[0][1] > 590 or self.snake[0][1] < 10
        ko = False
        for i in range(1, len(self.snake)):
            ko |= self.snake[0] == self.snake[i]
        if ok or ko:
            return False
        return True

    def add_block(self):
        n = len(self.snake)
        x = self.snake[n - 1][0]
        y = self.snake[n - 1][1]
        if n == 1:
            if self.directory == [snake_speed, 0]:
                self.snake.append([x - 10, y])
            if self.directory == [-snake_speed, 0]:
                self.snake.append([x + 10, y])
            if self.directory == [0, snake_speed]:
                self.snake.append([x, y - 10])
            if self.directory == [0, -snake_speed]:
                self.snake.append([x, y + 10])
        else:
            x1, y1 = self.snake[n - 2][0], self.snake[n - 2][1]
            if x == x1:
                if y < y1:
                    self.snake.append([x, y - 10])
                else:
                    self.snake.append([x, y + 10])
            if y == y1:
                if x < x1:
                    self.snake.append([x - 10, y])
                else:
                    self.snake.append([x + 10, y])


class Eda:
    def __init__(self):
        self.x = random.randint(30, 770)
        self.y = random.randint(30, 570)

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), 5)

    def spawn(self):
        self.x = random.randint(30, 770)
        self.y = random.randint(30, 570)
        pygame.draw.circle(screen, RED, (self.x, self.y), 5)


def collision(x1, y1, x2, y2, r):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) < 2 * r


def collision2(x1, y1, stena):
    xx1 = stena[0]
    yy1 = stena[1]
    xx2 = xx1 + stena[2]
    yy2 = yy1 + stena[3]
    return (xx1 < x1 < xx2) and (yy1 < y1 < yy2)


walls = Walls()
snake1 = Snake(30, 30)
snake2 = Snake2(100, 100)
game_over = pygame.font.SysFont("game over", 100)
cnt = 0
eda1 = Eda()
FPS = 10
score = 0
im = pygame.image.load("fon.png")
FILE_NAME = 'snakes_saved.data'


def run_game():
    global done, cnt, FPS, score
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    with open(FILE_NAME, 'bw') as f:
                        pickle.dump(snake1, f)
                    done = True
                # pygame.quit()

        # screen.fill(WHITE)
        screen.blit(im, (0, 0))
        SCORE = pygame.font.SysFont("score", 30)
        SCORE_IM = SCORE.render(str(score), True, BLACK)
        walls.draw()
        eda1.draw()
        screen.blit(SCORE_IM, (0, 0))
        if not snake1.move():
            txt = game_over.render("GAME OVER", True, RED)
            screen.fill(WHITE)
            screen.blit(txt, (10, 10))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            quit()
        # if not snake2.move():
        #     txt = game_over.render("GAME OVER", True, RED)
        #     screen.fill(WHITE)
        #     screen.blit(txt, (10, 10))
        #     pygame.display.update()
        #     time.sleep(2)
        #     pygame.quit()
        #     quit()
        for wall in walls.wall:
            if collision2(snake1.rect.centerx, snake1.rect.centery, wall):
                txt = game_over.render("GAME OVER", True, RED)
                screen.fill(WHITE)
                screen.blit(txt, (10, 10))
                pygame.display.update()
                time.sleep(2)
                pygame.quit()
                quit()
        # if collision(snake2.rect.centerx, snake2.rect.centery, eda1.x, eda1.y, 5):
        #     eda1.spawn()
        #     score += 1
        #     ok = False
        #     for wall in walls.wall:
        #         ok |= collision2(eda1.x, eda1.y, wall)
        #     while ok:
        #         eda1.spawn()
        #         for wall in walls.wall:
        #             ok |= collision2(eda1.x, eda1.y, wall)
        #     cnt += 1
        #     snake2.add_block()
        if collision(snake1.rect.centerx, snake1.rect.centery, eda1.x, eda1.y, 5):
            eda1.spawn()
            ok = False
            for wall in walls.wall:
                ok |= collision2(eda1.x, eda1.y, wall)
            while ok:
                eda1.spawn()
                for wall in walls.wall:
                    ok |= collision2(eda1.x, eda1.y, wall)
            cnt += 1
            snake1.add_block()
            if cnt == 5:
                FPS += 2
            if cnt == 10:
                walls.add_wall(snake1.snake[0])
                cnt = 0

        pygame.display.update()
        # cnt += 1
        clock.tick(FPS)


start_w = pygame.font.SysFont("start", 50)
start = False
screen.fill(WHITE)
text = start_w.render("Press SPACE to load saved game", False, RED)
text1 = start_w.render("Press any other key to start new game", False, RED)
screen.blit(text, (150, 200))
screen.blit(text1, (150, 300))
ok = False
snakes = []
while not ok:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok = True
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_SPACE:
            start = True
            ok = True
            if event.key == pygame.K_SPACE:
                try:
                    with open(FILE_NAME, 'br') as f:
                        snake1 = pickle.load(f)
                except Exception as e:
                    print(e)
            else:
                pass
        pygame.display.update()
if start:
    run_game()
pygame.quit()
quit()
