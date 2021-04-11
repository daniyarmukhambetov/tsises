import pygame
import random
import math

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
colors = (
    (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255))


class Ball:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        # self.speed = speed
        self.dx = 3
        self.dy = -3
        self.color = colors[random.randint(1, 7)]

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if (self.r <= self.x <= screen_width - self.r) and (self.r <= self.y <= screen_height - self.r):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        if self.x > screen_width - self.r or self.x < self.r:
            if self.dx > 0:
                self.dx = -(3 + random.randrange(0, 5) / 10)
            else:self.dx = (3 + random.randrange(0, 5) / 10)
            self.color = colors[random.randint(1, 7)]
        if self.y > screen_height - self.r or self.y < self.r:
            if self.dy > 0:
                self.dy = -(3 + random.randrange(0, 5) / 10)
            else:
                self.dy = (3 + random.randrange(0, 5) / 10)
            self.color = colors[random.randint(1, 7)]
        # elif (self.x > 800 or self.x < self.r) and


clock = pygame.time.Clock()
done = False
balls = []
for i in range(10):
    balls.append(Ball(random.randrange(30, 770), random.randrange(30, 570), 30))
# ball1 = Ball(screen_width // 4, screen_height // 3, 30)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0, 0, 0))
    # ball1.move()
    for ball in balls:
        ball.move()
    pygame.display.update()
    clock.tick(100)
