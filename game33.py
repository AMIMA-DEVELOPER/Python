import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle and Text")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 36)

# Text
text = font.render("Welcome to Pygame!", True, BLACK)

# Rectangle
rect = pygame.Rect(300, 200, 200, 100)

# Game loop
running = True
while running:

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, rect)

    # Draw text
    screen.blit(text, (250, 100))

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()