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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Call the on_mouse_button_down() function
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")

    screen.blit(bg, (0, 0))
    screen.blit(start, (525,40))
    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

