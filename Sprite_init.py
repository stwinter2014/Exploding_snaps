import pygame

black = (0,0,0)
white = (255, 255, 255)

class Cardback_1 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cardback_1.png").convert()
        self.rect = self.image.get_rect()

class Cardback_2 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cardback_2.png").convert()
        self.rect = self.image.get_rect()
