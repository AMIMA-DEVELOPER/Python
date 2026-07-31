import pygame
import math

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

SEGMENTS = 40
LENGTH = 15

points = [(WIDTH // 2, HEIGHT // 2) for _ in range(SEGMENTS)]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mx, my = pygame.mouse.get_pos()

    points[0] = (mx, my)

    for i in range(1, SEGMENTS):
        px, py = points[i - 1]
        x, y = points[i]

        dx = x - px
        dy = y - py

        dist = math.hypot(dx, dy)

        if dist != 0:
            dx /= dist
            dy /= dist

        points[i] = (
            px + dx * LENGTH,
            py + dy * LENGTH
        )

    screen.fill((20, 20, 20))

    for i in range(SEGMENTS - 1):
        pygame.draw.line(screen, (220, 220, 220), points[i], points[i + 1], 1)

        angle = math.atan2(
            points[i + 1][1] - points[i][1],
            points[i + 1][0] - points[i][0]
        )

        px, py = points[i]

        size = 6

        left = (
            px + math.cos(angle + math.pi / 2) * size,
            py + math.sin(angle + math.pi / 2) * size,
        )

        right = (
            px + math.cos(angle - math.pi / 2) * size,
            py + math.sin(angle - math.pi / 2) * size,
        )

        pygame.draw.line(screen, (180, 180, 180), (px, py), left, 1)
        pygame.draw.line(screen, (180, 180, 180), (px, py), right, 1)

        pygame.draw.circle(screen, (230, 230, 230), (int(px), int(py)), 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()