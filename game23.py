#Write a program to create a Pygame window with two circles, one solid and another hollow circle with border width 3. Keep the background colour as - white RGB(255, 255, 255) and the colour of the rectangle as green (0, 255, 0). Try changing the values of centre and radius to see how the position and size of the balls change.



# import pygame
# pygame.init()

# window = pygame.display.set_mode((400,400))

# window.fill((255,255,255))

# BLACK = (0,0,0)

# pygame.draw.circle(window,BLACK,(300,300),50)
# pygame.draw.circle(window,BLACK,(100,100),50,3)
# pygame.draw.rect(window, (0,125,255),pygame.Rect(30,200,60,70))

# pygame.display.update()

# running = True

# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# pygame.quit()



#Write a program that detects when keys are pressed and changes the color of a sprite when it touches the screen boundaries.

import pygame
def main():
    pygame.init()
    screen_width, screen_height = 500 , 500
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption('color changing sprite')

    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
         'blue': pygame.Color('blue'),
          'white': pygame.Color('white'),
           'yellow': pygame.Color('yellow')


    }
    current_color = colors['white']

    x,y = 30,30
    sprite_width, sprite_height = 60,60

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -=3
        if pressed[pygame.K_RIGHT]: x +=3
        if pressed[pygame.K_UP]: y -=3
        if pressed[pygame.K_DOWN]: y +=3

        x = min(max(0,x),screen_width - sprite_width)
        y = min(max(0,y),screen_width - sprite_height)

        if x == 0: current_color = colors['blue']
        elif x == screen_width - sprite_width: current_color = colors['yellow']
        elif y == 0: current_color = colors['red']
        elif y == screen_height - sprite_height:
            current_color = colors['green']
        else:
            current_color = colors['white']

        screen.fill((0,0,0))
        pygame.draw.rect(screen, current_color,(x,y, sprite_width, sprite_height))

        pygame.display.flip()
        clock.tick(90)

    pygame.quit()

if __name__ == "__main__":
    main()
