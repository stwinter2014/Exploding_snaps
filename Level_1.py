import pygame
import random
import Sprite_init
def Level_1():
    pygame.init()
    size = [1000, 750]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snap")
    done = False
    clock = pygame.time.Clock()


    
    black = (0,0,0)
    white = (255, 255, 255)
    cardback_list = pygame.sprite.Group()
    for i in range (1):
        cardback_red = Sprite_init.Cardback_1()
        cardback_red.rect.x = 150
        cardback_red.rect.y = 300
        cardback_list.add(cardback_red)
    for i in range (1):
        cardback_green = Sprite_init.Cardback_2()
        cardback_green.rect.x = 150
        cardback_green.rect.y = 600
        cardback_list.add(cardback_green)

    
    
    background = pygame.image.load('background1.jpg').convert()
    cardback_1 = pygame.image.load('cardback_1.png').convert()
    cardback_2 = pygame.image.load('cardback_2.png').convert()
    
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.blit(background, [0,0])
        cardback_list.draw(screen)
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
Level_1()
