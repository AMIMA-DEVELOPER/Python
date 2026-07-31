import pygame

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dance Game")

sheet = pygame.image.load("sprite.png").convert_alpha()

cols = 5
rows = 4
fw = sheet.get_width() // cols
fh = sheet.get_height() // rows

frames = []
for y in range(rows):
    for x in range(cols):
        frame = pygame.Surface((fw, fh), pygame.SRCALPHA)
        frame.blit(sheet, (0, 0), (x * fw, y * fh, fw, fh))
        frames.append(pygame.transform.scale(frame, (140, 140)))

clock = pygame.time.Clock()
i = 0
score = 0
text = ""

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        i = (i + 1) % 5
        text = "GOOD!"
        score += 1

    elif keys[pygame.K_LEFT]:
        i = 5 + (i + 1) % 5
        text = "LEVEL UP!"
        score += 1

    elif keys[pygame.K_UP]:
        i = 10 +((i + 1) % 5)
        text = "WELL DONE!"
        score -= 1

    elif keys[pygame.K_DOWN]:
        i = 15 + ((i + 1) % 5)
        text = "AWESOME!"
        score += 1

    screen.fill((35, 35, 60))
    pygame.draw.rect(screen, (80, 80, 120), (0, 380, 800, 120))

    screen.blit(frames[i], (330, 170))

    f = pygame.font.SysFont("Arial", 32, True)
    screen.blit(f.render(text, True, (255, 255, 0)), (20, 20))
    screen.blit(f.render("Score: " + str(score), True, (255, 255, 255)), (20, 60))

    pygame.display.flip()
    clock.tick(8)

pygame.quit()