import pygame
import sys

pygame.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

# Background image
background = pygame.image.load("download.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# ONE character image
player = pygame.image.load("downlaod1.png").convert_alpha()
player = pygame.transform.scale(player, (80, 100))

player_x = 400
player_y = 400

# Background movement
bg_x = 0
bg_speed = 2

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Move background
    bg_x -= bg_speed

    if bg_x <= -WIDTH:
        bg_x = 0

    # Draw background twice
    screen.blit(background, (bg_x, 0))
    screen.blit(background, (bg_x + WIDTH, 0))

    # Character movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= 5

    if keys[pygame.K_RIGHT]:
        player_x += 5

    if keys[pygame.K_UP]:
        player_y -= 5

    if keys[pygame.K_DOWN]:
        player_y += 5

    # Draw character
    screen.blit(player, (player_x, player_y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()