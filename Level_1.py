import pygame
import random
import Sprite_init
import Shuffle
def Level_1():
    pygame.init()
    size = [1200, 900]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snap")
    done = False
    clock = pygame.time.Clock()


    
    black = (0,0,0)
    white = (255, 255, 255)
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    counter_4 = 0
    counter_5 = 0
    counter_6 = 0
    counter_7 = 0
    counter_8 = 0
    counter_9 = 0
    counter_10 = 0
    background = pygame.image.load('background1.jpg').convert()
    cardback_1 = pygame.image.load('cardback_1.png').convert()
    
    cardb_red_list = pygame.sprite.Group()
    cardb_green_list = pygame.sprite.Group()
    cardb_lblue_list = pygame.sprite.Group()
    cardb_dblue_list = pygame.sprite.Group()
    card_1_list = pygame.sprite.Group()
    card_2_list = pygame.sprite.Group()
    card_3_list = pygame.sprite.Group()
    card_4_list = pygame.sprite.Group()
    card_5_list = pygame.sprite.Group()
    card_6_list = pygame.sprite.Group()
    card_7_list = pygame.sprite.Group()
    card_8_list = pygame.sprite.Group()
    card_9_list = pygame.sprite.Group()
    card_10_list = pygame.sprite.Group()
    
    for i in range (2):
        cardback_red = Sprite_init.Cardback_1()
        cardb_red_list.add(cardback_red)
    for i in range (4):
        cardback_green = Sprite_init.Cardback_2()
        cardb_green_list.add(cardback_green)
    for i in range (6):
        cardback_lblue = Sprite_init.Cardback_2()
        cardb_lblue_list.add(cardback_lblue)
    for i in range (8):
        cardback_dblue = Sprite_init.Cardback_2()
        cardb_dblue_list.add(cardback_dblue)
    Shuffle.Shuffle (card_1_list, card_2_list, card_3_list, card_4_list, card_5_list,
                card_6_list, card_7_list, card_8_list, card_9_list, card_10_list)
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.blit(background, [0,0])
        card_1_list.draw(screen)
        card_2_list.draw(screen)
        card_3_list.draw(screen)
        card_4_list.draw(screen)
        card_5_list.draw(screen)
        card_6_list.draw(screen)
        card_7_list.draw(screen)
        card_8_list.draw(screen)
        card_9_list.draw(screen)
        card_10_list.draw(screen)
        """
        cardb_red_list.draw(screen)
        cardb_green_list.draw(screen)
        cardb_lblue_list.draw(screen)
        cardb_dblue_list.draw(screen)
        """
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
Level_1()
