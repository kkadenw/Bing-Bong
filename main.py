import pygame
import random

# set up pygame modules
pygame.init()
pygame.font.init()

# Font settings
font = pygame.font.SysFont('Arial', 20)
font2 = pygame.font.SysFont('Arial', 50)
font3 = pygame.font.SysFont('Arial', 30)


pygame.display.set_caption("TROLL CASINO!")
size = (1274, 980)
screen = pygame.display.set_mode(size)

# Load images
g_character = pygame.image.load("Gorilla Character.png")
p_character = pygame.image.load("Panda Character.png")
sg_character = pygame.image.load("S Gorilla Character.png")
bg = pygame.image.load("CASINO.jpg")
coin = pygame.image.load("coin.png")
bac_table = pygame.image.load("baccarat table.png")
characterp_background = pygame.image.load("CharacterP Background.jpg")


# Render text
space_rendered = font.render("Press SPACE to Enter The Casino!", True, (255, 255, 255))
character_pick_front = font2.render("Press 1 2 3 To select your character!", True, (255, 255, 255))
game_inst = font3.render("PLACE YOUR BETS ON EITHER PLAYER(5) OR BANK(6)", True, (255, 255, 255))
coin_amt = font.render("$1,000", True, (0, 0, 0))
character1 = font2.render("1", True, (255, 255, 255))
character2 = font2.render("2", True, (255, 255, 255))
character3 = font2.render("3", True, (255, 255, 255))
player_bet = font2.render("PLAYER", True, (0, 0, 0))
bank_bet = font2.render("BANKER", True, (0, 0, 0))
enter_bet_amt = font2.render("Enter your bet amount:", True, (255, 255, 255))

# Game variables
run = True
clock = pygame.time.Clock()
start_screen = True
character_pick = False
which_character = None
game_begin = False
bet_placed = False
bet_amount_selected = False
bet = None
bet_amount = ""
total_amount = 1000  

while run:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if not start_screen and not character_pick and game_begin and not bet_placed and not bet_amount_selected:
                if event.key == pygame.K_5:
                    bet = 'Player'
                    bet_placed = True
                elif event.key == pygame.K_6:
                    bet = 'Banker'
                    bet_placed = True
            elif not start_screen and not character_pick and game_begin and bet_placed and not bet_amount_selected:
                if event.key == pygame.K_RETURN:
                    if bet_amount.isdigit() and 0 < int(bet_amount) <= total_amount:
                        total_amount -= int(bet_amount)
                        bet_amount_selected = True
                    else:
                        bet_amount = ""
                elif event.key == pygame.K_BACKSPACE:
                    bet_amount = bet_amount[:-1]
                else:
                    bet_amount += event.unicode

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and start_screen:
        character_pick = True
        start_screen = False

    if character_pick:
        if keys[pygame.K_1]:
            which_character = 'Gorilla'
            character_pick = False
            game_begin = True
        elif keys[pygame.K_2]:
            which_character = 'Panda'
            character_pick = False
            game_begin = True
        elif keys[pygame.K_3]:
            which_character = 'Super Gorilla'
            character_pick = False
            game_begin = True

    # Drawing logic
    screen.fill((0, 0, 0))  # Clear the screen with black

    if start_screen:
        screen.blit(bg, (0, 0))
        screen.blit(space_rendered, (525, 200))
    elif character_pick:
        screen.blit(characterp_background, (0, 0))
        screen.blit(g_character, (50, 300))
        screen.blit(p_character, (500, 300))
        screen.blit(sg_character, (900, 300))
        screen.blit(character_pick_front, (330, 100))
        screen.blit(character1, (75, 400))
        screen.blit(character2, (500, 400))
        screen.blit(character3, (925, 400))
    elif game_begin:
        screen.blit(characterp_background, (0, 0))
        screen.blit(bac_table, (350, 350))
        if which_character == 'Gorilla':
            screen.blit(g_character, (15, 40))
        elif which_character == 'Panda':
            screen.blit(p_character, (15, 40))
        elif which_character == 'Super Gorilla':
            screen.blit(sg_character, (15, 40))
        screen.blit(coin, (15, 900))
        screen.blit(coin_amt, (125, 930))
        if not bet_placed:
            screen.blit(game_inst, (350, 200))
            screen.blit(player_bet, (300, 700))
            screen.blit(bank_bet, (800, 700))
        elif not bet_amount_selected:
            screen.blit(enter_bet_amt, (300, 200))
            bet_input = font2.render(bet_amount, True, (255, 255, 255))
            screen.blit(bet_input, (550, 300))
        else:
            bet_text = font2.render(f"Bet Placed on: {bet}", True, (255, 255, 255))
            screen.blit(bet_text, (400, 100))
            bet_amt_text = font2.render(f"Bet Amount: ${bet_amount}", True, (255, 255, 255))
            screen.blit(bet_amt_text, (400, 200))
            total_amt_text = font.render(f"Total Amount: ${total_amount}", True, (255, 255, 255))
            screen.blit(total_amt_text, (20, 20))


    pygame.display.update()
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
