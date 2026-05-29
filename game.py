# import pygame
# pygame.init()

# screen = pygame.display.set_mode((300,400))

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill(("Blue"))

#     pygame.display.flip()

# pygame.quit()

import pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('ADDING IMAGE AND BACKGROUND')

background_image = pygame.transform.scale(
    pygame.image.load('bg.jpg').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)
duck_image = pygame.transform.scale(
    pygame.image.load('img.jpg').convert_alpha(),(200,200)
)

duck_rect = duck_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-50))

text = pygame.font.Font(None, 36).render('Hello I am duck',True,pygame.Color('black'))

text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2+110))


def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        display_surface.blit(background_image,(0,0))
        display_surface.blit(duck_image, duck_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()

