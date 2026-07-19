import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Square and Circle Sprites")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Square (player)
square_size = 50
square_x = 100
square_y = 100
speed = 5

# Circle
circle_x = 500
circle_y = 300
circle_radius = 25

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        square_x -= speed
    if keys[pygame.K_RIGHT]:
        square_x += speed
    if keys[pygame.K_UP]:
        square_y -= speed
    if keys[pygame.K_DOWN]:
        square_y += speed

    # Keep square inside the screen
    square_x = max(0, min(square_x, WIDTH - square_size))
    square_y = max(0, min(square_y, HEIGHT - square_size))

    # Draw
    screen.fill(WHITE)

    # Draw square
    pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size, square_size))

    # Draw circle
    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

    pygame.display.update()

pygame.quit()