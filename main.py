import pygame
import random
from button import start
pygame.init()

r = 50
g = 0
b = 100

#window dimensions
window_width = 1274
window_height = 980
window_size = ( window_width, window_height)
bg_display = pygame.display.set_mode(window_size)
bg_image = pygame.image.load('CASINO.jpg')
st_button = pygame.image.load('Start button.png')

# MAIN LOOP
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bg_display.blit(bg_image,(0,0))
    st_button.blit(st_button, (40, 60))
    screen.blit(st_button)
    pygame.display.update()

pygame.quit()
