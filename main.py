import pygame
import random


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("TROLL CASINO!")
button_rect = pygame.Rect(125, 125, 150, 50)

# set up variables for the display
size = (1274, 980)
screen = pygame.display.set_mode(size)

bg = pygame.image.load("CASINO.jpg")
start = pygame.image.load("Start button.png")
start = pygame.transform.scale(start, (270, 90))

lst = []
# render the text for later

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
while run:
    # --- Main event loop


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if start.get_rect().collidepoint(x, y):
                    print('clicked on image')

    screen.blit(bg, (0, 0))
    screen.blit(start, (505,40))
    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

