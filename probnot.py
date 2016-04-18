import pygame
pygame.init()
size = [900, 900]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snap")
done = False
clock = pygame.time.Clock()
black = (0,0,0)
white = (255, 255, 255)
card_1_list = pygame.sprite.Group()
background = pygame.image.load('background1.jpg').convert()
class Card_1 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_1.png").convert()
        self.rect = self.image.get_rect()
    def moving(self, rect_x):
            self.rect.x += 5
card_1 = Card_1()
card_1.rect.x = 350
card_1.rect.y = 350
card_1_list.add(card_1)
move = False
moveZ = False
time = [11,11,30]
timer = 0
time_f = 0
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                move = True
    if move == True:
        time_f += 1
        if timer <= time[0]:
            card_1.rect.x += 1
        elif timer > time[1] and timer < time[2]:
            card_1.rect.x -= 1
        else:
            print('nol')
            timer = 0
            card_1.rect.x = 350
            card_1.rect.y = 350
        timer += 1
        if time_f%60 == 0:
            print('da')
            time[0] -= 3
            time[1] -= 3
            time[2] -= 3
            print(time)
            print(time_f)
            print(timer)
        if time_f == 600:
            card_1.rect.x = 350
            card_1.rect.y = 350
            move = False
            timer = 0
            time = [11,11,30]
            card_1_list.remove(card_1)
            time_f = 0
    screen.blit(background, [0,0])
    card_1_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
