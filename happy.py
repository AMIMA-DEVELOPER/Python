import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Catch")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 32)

bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (70, 70))

coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (40, 40))

player = player_img.get_rect(midbottom=(WIDTH // 2, HEIGHT - 20))
coin = coin_img.get_rect(midtop=(random.randint(20, WIDTH - 20), -50))

score = 0
speed = 6

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 8
    if keys[pygame.K_RIGHT]:
        player.x += 8

    player.x = max(0, min(WIDTH - player.width, player.x))

    coin.y += speed

    if coin.colliderect(player):
        score += 1
        speed += 0.3
        coin.x = random.randint(20, WIDTH - 60)
        coin.y = -50

    if coin.y > HEIGHT:
        coin.x = random.randint(20, WIDTH - 60)
        coin.y = -50

    screen.blit(bg, (0, 0))
    screen.blit(player_img, player)
    screen.blit(coin_img, coin)

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (20, 20))

    pygame.display.flip()

pygame.quit()