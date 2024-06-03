import pygame
import random


# set up pygame modules
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 20)
font2 = pygame.font.SysFont('Arial', 50)
pygame.display.set_caption("TROLL CASINO!")
button_rect = pygame.Rect(125, 125, 150, 50)
space_pressed = False
# set up variables for the display

size = (1274, 980)
screen = pygame.display.set_mode(size)
r = 50
g = 0
b = 100

g_character = pygame.image.load("Gorilla Character.png")
p_character = pygame.image.load("Panda Character.png")
sg_character = pygame.image.load("S Gorilla Character.png")
pk_table = pygame.image.load("PokerTable.png")
bg = pygame.image.load("CASINO.jpg")
characterp_background = pygame.image.load("CharacterP Background.jpg")
space_rendered = font.render("Press SPACE to Enter The Casino!", True, (255, 255, 255))
character_pick_front = font2.render("Press 1 2 3 To select your character!", True, (255, 255, 255))
character1 = font2.render("1", True,(255,255, 255))
character2 = font2.render("2", True,(255,255, 255))
character3 = font2.render("3", True,(255,255, 255))


lst = []
# render the text for later

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
start_screen = True
character_pick = False
character_pick2 = False
character_picked_1 = False
character_picked_2 = False
character_picked_3 = False
while run:
    # --- Main event loop
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        character_pick = True
        start_screen = False
    if keys[pygame.K_1]:
        character_picked_1 = True
        character_pick2 = True
        character_pick = False
    if keys[pygame.K_2]:
        character_picked_2 = True
        character_pick2 = True
        character_pick = False
    if keys[pygame.K_3]:
        character_picked_3 = True
        character_pick2 = True
        character_pick = False


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
            pos = pygame.mouse.get_pos()

        if start_screen == True:
            screen.blit(bg, (0, 0))
            screen.blit(space_rendered, (525, 200))
            pygame.display.update()
        if character_pick == True:
            screen.blit(characterp_background, (0, 0))
            screen.blit(g_character, (50, 300))
            screen.blit(p_character, (500, 300))
            screen.blit(sg_character,( 900,300))
            screen.blit(character_pick_front, (330, 100))
            screen.blit(character1, (75, 400))
            screen.blit(character2, (500, 400))
            screen.blit(character3, (925 , 400))
            pygame.display.update()
        if character_pick2 == True and character_picked_1 == True:
            screen.blit(characterp_background, (0, 0))
            screen.blit(pk_table, (300,350))
            screen.blit(g_character, (15, 40))
            pygame.display.update()
        if character_pick2 == True and character_picked_2 == True:
            screen.blit(characterp_background, (0, 0))
            screen.blit(pk_table, (300, 350))
            screen.blit(p_character, ( 15, 40))
            pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

