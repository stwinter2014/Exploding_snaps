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
class Cardback_3 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cardback_2.png").convert()
        self.rect = self.image.get_rect()
class Cardback_4 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cardback_2.png").convert()
        self.rect = self.image.get_rect()

class Card_1 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_1.png").convert()
        self.rect = self.image.get_rect()
class Card_2 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_2.png").convert()
        self.rect = self.image.get_rect()
class Card_3 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_3.png").convert()
        self.rect = self.image.get_rect()
class Card_4 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_4.png").convert()
        self.rect = self.image.get_rect()
class Card_5 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_5.png").convert()
        self.rect = self.image.get_rect()
class Card_6 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_6.png").convert()
        self.rect = self.image.get_rect()
class Card_7 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_7.png").convert()
        self.rect = self.image.get_rect()
class Card_8 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_8.png").convert()
        self.rect = self.image.get_rect()
class Card_9 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_9.png").convert()
        self.rect = self.image.get_rect()
class Card_10 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_10.png").convert()
        self.rect = self.image.get_rect()
