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
    step_x = 0
    step_y = 0
    compare = False
    couple = 0
    number = 0
    ness_pos_x = 0
    ness_pos_x = 0
    all_ch = 0
    click_sound = pygame.mixer.Sound("click.wav")
    background = pygame.image.load('background1.jpg').convert()
    cardback_1 = pygame.image.load('cardback_1.png').convert()
    pointer_list = pygame.sprite.Group()
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
    
    pointer = Sprite_init.Pointer()
    pointer_list.add(pointer)
    pause_x = (size[0]*2//3 - cardback_1.get_width()*5)//6
    pause_y = (size[1] - cardback_1.get_height()*4)//5
    pointer_move_x = [pause_x, pause_x*2 + cardback_1.get_width(), pause_x*3 + cardback_1.get_width()*2,
                      pause_x*4 + cardback_1.get_width()*3, pause_x*5 + cardback_1.get_width()*4]
    pointer_move_y = [pause_y, pause_y*2 + cardback_1.get_height(), pause_y*3 + cardback_1.get_height()*2,
                      pause_y*4 + cardback_1.get_height()*3]
    Shuffle.Shuffle (card_1_list, card_2_list, card_3_list, card_4_list, card_5_list,
                card_6_list, card_7_list, card_8_list, card_9_list, card_10_list,
                     cardb_red_list, cardb_green_list, cardb_lblue_list, cardb_dblue_list)
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if step_x > 0:
                        step_x -= 1
                        click_sound.play()
                    else:
                        step_x = 4
                        click_sound.play()
                if event.key == pygame.K_RIGHT:
                    if step_x < 4:
                        step_x += 1
                        click_sound.play()
                    else:
                        step_x = 0
                        click_sound.play()
                if event.key == pygame.K_UP:
                    if step_y > 0:
                        step_y -= 1
                        click_sound.play()
                    else:
                        step_y = 3
                        click_sound.play()
                if event.key == pygame.K_DOWN:
                    if step_y < 3:
                        step_y += 1
                        click_sound.play()
                    else:
                        step_y = 0
                        click_sound.play()
                if event.key == pygame.K_SPACE:
                    compare = True
                    if couple == 0:
                        all_ch = 0
        screen.blit(background, [0,0])
        pointer.rect.x = pointer_move_x[step_x]
        pointer.rect.y = pointer_move_y[step_y]
        if compare == True:
            position_x = pointer.rect.x
            position_y = pointer.rect.y
            if couple == 0:
                for card_1 in card_1_list:
                    if card_1.rect.x == position_x and card_1.rect.y == position_y and all_ch == 0:
                        for cardback_lb in cardb_lblue_list:
                            if cardback_lb.rect.x == position_x and cardback_lb.rect.y == position_y:
                                cardb_lblue_list.remove(cardback_lb)
                        all_ch = 1
                        print ('da1')
                        number = 1
                        ness_pos_x = position_x
                        ness_pos_y = position_y
                        couple += 1
                        compare = False
                for card_2 in card_2_list:
                    if card_2.rect.x == position_x and card_2.rect.y == position_y and all_ch == 0:
                        for cardback_lb in cardb_lblue_list:
                            if cardback_lb.rect.x == position_x and cardback_lb.rect.y == position_y:
                                cardb_lblue_list.remove(cardback_lb)
                        all_ch = 1
                        print ('da2')
                        number = 2
                        ness_pos_x = position_x
                        ness_pos_y = position_y
                        couple += 1
                        compare = False
                for card_3 in card_3_list:
                    if card_3.rect.x == position_x and card_3.rect.y == position_y and all_ch == 0:
                        for cardback_db in cardb_dblue_list:
                            if cardback_db.rect.x == position_x and cardback_db.rect.y == position_y:
                                cardb_dblue_list.remove(cardback_db)
                        all_ch = 1
                        print ('da3')
                        number = 3
                        ness_pos_x = position_x
                        ness_pos_y = position_y
                        couple += 1
                        compare = False
                for card_4 in card_4_list:
                    if card_4.rect.x == position_x and card_4.rect.y == position_y and all_ch == 0:
                        for cardback_db in cardb_dblue_list:
                            if cardback_db.rect.x == position_x and cardback_db.rect.y == position_y:
                                cardb_dblue_list.remove(cardback_db)
                        all_ch = 1
                        print ('da4')
                        number = 4
                        ness_pos_x = position_x
                        ness_pos_y = position_y
                        couple += 1
                        compare = False
                for card_5 in card_5_list:
                    if card_5.rect.x == position_x and card_5.rect.y == position_y and all_ch == 0:
                        for cardback_r in cardb_red_list:
                            if cardback_r.rect.x == position_x and cardback_r.rect.y == position_y:
                                cardb_red_list.remove(cardback_r)
                        all_ch = 1
                        print ('da5')
                        number = 5
                        ness_pos_x = position_x
                        ness_pos_y = position_y
                        couple += 1
                        compare = False
                for card_6 in card_6_list:
                    if card_6.rect.x == position_x and card_6.rect.y == position_y and all_ch == 0:
                        for cardback_g in cardb_green_list:
                            if cardback_g.rect.x == position_x and cardback_g.rect.y == position_y:
                                cardb_green_list.remove(cardback_g)
                        all_ch = 1
                        print ('da6')
                        number = 6
                        ness_pos_x = position_x
                        ness_pos_y = position_y
                        couple += 1
                        compare = False
                for card_7 in card_7_list:
                    if card_7.rect.x == position_x and card_7.rect.y == position_y and all_ch == 0:
                        for cardback_db in cardb_dblue_list:
                            if cardback_db.rect.x == position_x and cardback_db.rect.y == position_y:
                                cardb_dblue_list.remove(cardback_db)
                        all_ch = 1
                        print ('da7')
                        number = 7
                        ness_pos_x = position_x
                        ness_pos_y = position_y
                        couple += 1
                        compare = False
                for card_8 in card_8_list:
                    if card_8.rect.x == position_x and card_8.rect.y == position_y and all_ch == 0:
                        for cardback_lb in cardb_lblue_list:
                            if cardback_lb.rect.x == position_x and cardback_lb.rect.y == position_y:
                                cardb_lblue_list.remove(cardback_lb)
                        all_ch = 1
                        print ('da8')
                        number = 8
                        ness_pos_x = position_x
                        ness_pos_y = position_y
                        couple += 1
                        compare = False
                for card_9 in card_9_list:
                    if card_9.rect.x == position_x and card_9.rect.y == position_y and all_ch == 0:
                        for cardback_g in cardb_green_list:
                            if cardback_g.rect.x == position_x and cardback_g.rect.y == position_y:
                                cardb_green_list.remove(cardback_g)
                        all_ch = 1
                        print ('da9')
                        number = 9
                        ness_pos_x = position_x
                        ness_pos_y = position_y
                        couple += 1
                        compare = False
                for card_10 in card_10_list:
                    if card_10.rect.x == position_x and card_10.rect.y == position_y and all_ch == 0:
                        for cardback_db in cardb_dblue_list:
                            if cardback_db.rect.x == position_x and cardback_db.rect.y == position_y:
                                cardb_dblue_list.remove(cardback_db)
                        all_ch = 1
                        print ('da10')
                        number = 10
                        ness_pos_x = position_x
                        ness_pos_y = position_y
                        couple += 1
                        compare = False
                if all_ch == 0:
                    print("strsssssssssssssssssssssss")
                    compare = False
            elif couple == 1:
                for card_1 in card_1_list:
                    if card_1.rect.x == position_x and card_1.rect.y == position_y and all_ch == 1:
                        for cardback_lb in cardb_lblue_list:
                            if cardback_lb.rect.x == position_x and cardback_lb.rect.y == position_y:
                                cardb_lblue_list.remove(cardback_lb)
                        all_ch = 2
                        print ('da1')
                        if number == 1:
                            for card_1 in card_1_list:
                                if card_1.rect.x == position_x and card_1.rect.y == position_y:
                                    card_1_list.remove(card_1)
                                if card_1.rect.x == ness_pos_x and card_1.rect.y == ness_pos_y:
                                    card_1_list.remove(card_1)
                        couple = 0
                        compare = False
                for card_2 in card_2_list:
                    if card_2.rect.x == position_x and card_2.rect.y == position_y and all_ch == 1:
                        for cardback_lb in cardb_lblue_list:
                            if cardback_lb.rect.x == position_x and cardback_lb.rect.y == position_y:
                                cardb_lblue_list.remove(cardback_lb)
                        all_ch = 2
                        print ('da2')
                        if number == 2:
                            for card_2 in card_2_list:
                                if card_2.rect.x == position_x and card_2.rect.y == position_y:
                                    card_2_list.remove(card_2)
                                if card_2.rect.x == ness_pos_x and card_2.rect.y == ness_pos_y:
                                    card_2_list.remove(card_2)
                        couple = 0
                        compare = False
                for card_3 in card_3_list:
                    if card_3.rect.x == position_x and card_3.rect.y == position_y and all_ch == 1:
                        for cardback_db in cardb_dblue_list:
                            if cardback_db.rect.x == position_x and cardback_db.rect.y == position_y:
                                cardb_dblue_list.remove(cardback_db)
                        all_ch = 2
                        print ('da3')
                        if number == 3:
                            for card_3 in card_3_list:
                                if card_3.rect.x == position_x and card_3.rect.y == position_y:
                                    card_3_list.remove(card_3)
                                if card_3.rect.x == ness_pos_x and card_3.rect.y == ness_pos_y:
                                    card_3_list.remove(card_3)
                        couple = 0
                        compare = False
                for card_4 in card_4_list:
                    if card_4.rect.x == position_x and card_4.rect.y == position_y and all_ch == 1:
                        for cardback_db in cardb_dblue_list:
                            if cardback_db.rect.x == position_x and cardback_db.rect.y == position_y:
                                cardb_dblue_list.remove(cardback_db)
                        all_ch = 2
                        print('da4')
                        if number == 4:
                            for card_4 in card_4_list:
                                if card_4.rect.x == position_x and card_4.rect.y == position_y:
                                    card_4_list.remove(card_4)
                                if card_4.rect.x == ness_pos_x and card_4.rect.y == ness_pos_y:
                                    card_4_list.remove(card_4)
                        couple = 0
                        compare = False
                for card_5 in card_5_list:
                    if card_5.rect.x == position_x and card_5.rect.y == position_y and all_ch == 1:
                        for cardback_r in cardb_red_list:
                            if cardback_r.rect.x == position_x and cardback_r.rect.y == position_y:
                                cardb_red_list.remove(cardback_r)
                        all_ch = 2
                        print('da5')
                        if number == 5:
                            for card_5 in card_5_list:
                                if card_5.rect.x == position_x and card_5.rect.y == position_y:
                                    card_5_list.remove(card_5)
                                if card_5.rect.x == ness_pos_x and card_5.rect.y == ness_pos_y:
                                    card_5_list.remove(card_5)
                        couple = 0
                        compare = False
                for card_6 in card_6_list:
                    if card_6.rect.x == position_x and card_6.rect.y == position_y and all_ch == 1:
                        for cardback_g in cardb_green_list:
                            if cardback_g.rect.x == position_x and cardback_g.rect.y == position_y:
                                cardb_green_list.remove(cardback_g)
                        all_ch = 2
                        print('da6')
                        if number == 6:
                            for card_6 in card_6_list:
                                if card_6.rect.x == position_x and card_6.rect.y == position_y:
                                    card_6_list.remove(card_6)
                                if card_6.rect.x == ness_pos_x and card_6.rect.y == ness_pos_y:
                                    card_6_list.remove(card_6)
                        couple = 0
                        compare = False
                for card_7 in card_7_list:
                    if card_7.rect.x == position_x and card_7.rect.y == position_y and all_ch == 1:
                        for cardback_db in cardb_dblue_list:
                            if cardback_db.rect.x == position_x and cardback_db.rect.y == position_y:
                                cardb_dblue_list.remove(cardback_db)
                        all_ch = 2
                        print ('da7')
                        if number == 7:
                            for card_7 in card_7_list:
                                if card_7.rect.x == position_x and card_7.rect.y == position_y:
                                    card_7_list.remove(card_7)
                                if card_7.rect.x == ness_pos_x and card_7.rect.y == ness_pos_y:
                                    card_7_list.remove(card_7)
                        couple = 0
                        compare = False
                for card_8 in card_8_list:
                    if card_8.rect.x == position_x and card_8.rect.y == position_y and all_ch == 1:
                        for cardback_lb in cardb_lblue_list:
                            if cardback_lb.rect.x == position_x and cardback_lb.rect.y == position_y:
                                cardb_lblue_list.remove(cardback_lb)
                        all_ch = 2
                        print ('da8')
                        if number == 8:
                            for card_8 in card_8_list:
                                if card_8.rect.x == position_x and card_8.rect.y == position_y:
                                    card_8_list.remove(card_8)
                                if card_8.rect.x == ness_pos_x and card_8.rect.y == ness_pos_y:
                                    card_8_list.remove(card_8)
                        couple = 0
                        compare = False
                for card_9 in card_9_list:
                    if card_9.rect.x == position_x and card_9.rect.y == position_y and all_ch == 1:
                        for cardback_g in cardb_green_list:
                            if cardback_g.rect.x == position_x and cardback_g.rect.y == position_y:
                                cardb_green_list.remove(cardback_g)
                        all_ch = 2
                        print ('da9')
                        if number == 9:
                            for card_9 in card_9_list:
                                if card_9.rect.x == position_x and card_9.rect.y == position_y:
                                    card_9_list.remove(card_9)
                                if card_9.rect.x == ness_pos_x and card_9.rect.y == ness_pos_y:
                                    card_9_list.remove(card_9)
                        couple = 0
                        compare = False
                for card_10 in card_10_list:
                    if card_10.rect.x == position_x and card_10.rect.y == position_y and all_ch == 1:
                        for cardback_db in cardb_dblue_list:
                            if cardback_db.rect.x == position_x and cardback_db.rect.y == position_y:
                                cardb_dblue_list.remove(cardback_db)
                        all_ch = 2
                        print ('da10')
                        if number == 10:
                            for card_10 in card_10_list:
                                if card_10.rect.x == position_x and card_10.rect.y == position_y:
                                    card_10_list.remove(card_10)
                                if card_10.rect.x == ness_pos_x and card_10.rect.y == ness_pos_y:
                                    card_10_list.remove(card_10)
                        couple = 0
                        compare = False
                if all_ch == 1:
                    compare = False
                    print('waaaaaaaaaaaaaaaaw')

        cardb_red_list.draw(screen)
        cardb_green_list.draw(screen)
        cardb_lblue_list.draw(screen)
        cardb_dblue_list.draw(screen)
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
        pointer_list.draw(screen)
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
Level_1()
