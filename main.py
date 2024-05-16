import pygame
import random


# set up pygame modules
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("TROLL CASINO!")
button_rect = pygame.Rect(125, 125, 150, 50)
space_pressed = False
# set up variables for the display

size = (1274, 980)
screen = pygame.display.set_mode(size)

bg = pygame.image.load("CASINO.jpg")
space_rendered = font.render("Press SPACE to Enter The Casino!", True, (255, 255, 255))

lst = []
# render the text for later

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
character_pick = False
while run:
    # --- Main event loop


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
            pos = pygame.mouse.get_pos()
            if event.type == pygame.K_SPACE:
                character_pick = True

    screen.blit(bg, (0, 0))
    screen.blit(space_rendered, (525, 200))
    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

