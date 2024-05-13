import pygame

class Button():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.image = pygame.image.load("Start Button.png")
		self.image_size = self.image.get_size()
		self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
		self.delta = .1

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action