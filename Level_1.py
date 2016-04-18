import pygame
import random
import Sprite_init
import Shuffle
import time
def Level_1():
    pygame.init()
    size = [1200, 900]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snap")
    done = False
    clock = pygame.time.Clock()
    black = (0,0,0)
    white = (255, 255, 255)
    score = 0
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
    final_count = 0
    shake = [False, False, False, False, False, False, False, False, False, False]
    timer_sh = [0,0,0,0,0,0,0,0,0,0]
    shake_l = [False, False, False, False, False, False, False, False, False, False]
    timer_l = [0,0,0,0,0,0,0,0,0,0]
    move = [False, False, False, False, False, False, False, False, False, False]
    move_l = [False, False, False, False, False, False, False, False, False, False]
    tim = [0,0,0,0,0,0,0,0,0,0]
    tim_l = [0,0,0,0,0,0,0,0,0,0]
    left = [10,10,10,10,10,10,10,10,10,10]
    left_l = [10,10,10,10,10,10,10,10,10,10]
    freedom = True
    fr_count = 0
    step_x = 0
    step_y = 0
    compare = False
    couple = 0
    number = 0
    ness_pos_x = 0
    ness_pos_x = 0
    all_ch = 0
    font = pygame.font.Font(None, 100)
    font.set_italic(1)
    font1 = pygame.font.Font(None, 100)
    font.set_italic(1)
    click_sound = pygame.mixer.Sound("click.wav")
    explode_sound = pygame.mixer.Sound("explode.wav")
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
    card_win_list = pygame.sprite.Group()
    pointer = Sprite_init.Pointer()
    pointer_list.add(pointer)
    pause_x = (size[0]*2//3 - cardback_1.get_width()*5)//6
    pause_y = (size[1] - cardback_1.get_height()*4)//5
    pointer_move_x = [pause_x, pause_x*2 + cardback_1.get_width(), pause_x*3 + cardback_1.get_width()*2,
                      pause_x*4 + cardback_1.get_width()*3, pause_x*5 + cardback_1.get_width()*4]
    pointer_move_y = [pause_y, pause_y*2 + cardback_1.get_height(), pause_y*3 + cardback_1.get_height()*2,
                      pause_y*4 + cardback_1.get_height()*3]
    win_place = [(size[0] - size[0]*1//3) + (size[0] - size[0]*2//3 - cardback_1.get_width())//2, size[1] - cardback_1.get_height() - 30]
    Shuffle.Shuffle (card_1_list, card_2_list, card_3_list, card_4_list, card_5_list,
                card_6_list, card_7_list, card_8_list, card_9_list, card_10_list,
                     cardb_red_list, cardb_green_list, cardb_lblue_list, cardb_dblue_list)
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and freedom == True:
                    if step_x > 0:
                        step_x -= 1
                        click_sound.play()
                    else:
                        step_x = 4
                        click_sound.play()
                if event.key == pygame.K_RIGHT and freedom == True:
                    if step_x < 4:
                        step_x += 1
                        click_sound.play()
                    else:
                        step_x = 0
                        click_sound.play()
                if event.key == pygame.K_UP and freedom == True:
                    if step_y > 0:
                        step_y -= 1
                        click_sound.play()
                    else:
                        step_y = 3
                        click_sound.play()
                if event.key == pygame.K_DOWN and freedom == True:
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
        for i in range(0, len(shake)):
            if shake[i] == False:
                fr_count += 1
        for j in range(0, len(shake_l)):
            if shake_l[i] == False:
                fr_count += 1
        if fr_count == 20:
            freedom = True
            fr_count = 0
        else:
            freedom = False
            fr_count = 0
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
                    compare = False
            elif couple == 1:
                if ness_pos_x == position_x and ness_pos_y == position_y:
                    compare = False
                else:
                    for card_1 in card_1_list:
                        if card_1.rect.x == position_x and card_1.rect.y == position_y and all_ch == 1:
                            for cardback_lb in cardb_lblue_list:
                                if cardback_lb.rect.x == position_x and cardback_lb.rect.y == position_y:
                                    cardb_lblue_list.remove(cardback_lb)
                            all_ch = 2
                            print ('da1')
                            if number == 1:
                                score += 10
                                for card_1 in card_1_list:
                                    if card_1.rect.x == position_x and card_1.rect.y == position_y:
                                        card_1_list.remove(card_1)
                                    if card_1.rect.x == ness_pos_x and card_1.rect.y == ness_pos_y:
                                        card_1_list.remove(card_1)
                                        card_1_w = Sprite_init.Card_1()
                                        card_win_list.add(card_1_w)
                                        card_1_w.rect.x = win_place[0]
                                        card_1_w.rect.y = win_place[1]
                            elif number == 2:
                                shake[0] = True
                                shake_l[1] = True
                            elif number == 3:
                                shake[0] = True
                                shake_l[2] = True
                            elif number == 4:
                                shake[0] = True
                                shake_l[3] = True
                            elif number == 5:
                                shake[0] = True
                                shake_l[4] = True
                            elif number == 6:
                                shake[0] = True
                                shake_l[5] = True
                            elif number == 7:
                                shake[0] = True
                                shake_l[6] = True
                            elif number == 8:
                                shake[0] = True
                                shake_l[7] = True
                            elif number == 9:
                                shake[0] = True
                                shake_l[8] = True
                            elif number == 10:
                                shake[0] = True
                                shake_l[9] = True
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
                                score += 10
                                for card_2 in card_2_list:
                                    if card_2.rect.x == position_x and card_2.rect.y == position_y:
                                        card_2_list.remove(card_2)
                                    if card_2.rect.x == ness_pos_x and card_2.rect.y == ness_pos_y:
                                        card_2_list.remove(card_2)
                                        card_2_w = Sprite_init.Card_2()
                                        card_win_list.add(card_2_w)
                                        card_2_w.rect.x = win_place[0]
                                        card_2_w.rect.y = win_place[1]
                            elif number == 1:
                                shake[1] = True
                                shake_l[0] = True
                            elif number == 3:
                                shake[1] = True
                                shake_l[2] = True
                            elif number == 4:
                                shake[1] = True
                                shake_l[3] = True
                            elif number == 5:
                                shake[1] = True
                                shake_l[4] = True
                            elif number == 6:
                                shake[1] = True
                                shake_l[5] = True
                            elif number == 7:
                                shake[1] = True
                                shake_l[6] = True
                            elif number == 8:
                                shake[1] = True
                                shake_l[7] = True
                            elif number == 9:
                                shake[1] = True
                                shake_l[8] = True
                            elif number == 10:
                                shake[1] = True
                                shake_l[9] = True
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
                                score += 10
                                for card_3 in card_3_list:
                                    if card_3.rect.x == position_x and card_3.rect.y == position_y:
                                        card_3_list.remove(card_3)
                                    if card_3.rect.x == ness_pos_x and card_3.rect.y == ness_pos_y:
                                        card_3_list.remove(card_3)
                                        card_3_w = Sprite_init.Card_3()
                                        card_win_list.add(card_3_w)
                                        card_3_w.rect.x = win_place[0]
                                        card_3_w.rect.y = win_place[1]
                            elif number == 1:
                                shake[2] = True
                                shake_l[0] = True
                            elif number == 2:
                                shake[2] = True
                                shake_l[1] = True
                            elif number == 4:
                                shake[2] = True
                                shake_l[3] = True
                            elif number == 5:
                                shake[2] = True
                                shake_l[4] = True
                            elif number == 6:
                                shake[2] = True
                                shake_l[5] = True
                            elif number == 7:
                                shake[2] = True
                                shake_l[6] = True
                            elif number == 8:
                                shake[2] = True
                                shake_l[7] = True
                            elif number == 9:
                                shake[2] = True
                                shake_l[8] = True
                            elif number == 10:
                                shake[2] = True
                                shake_l[9] = True
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
                                score += 10
                                for card_4 in card_4_list:
                                    if card_4.rect.x == position_x and card_4.rect.y == position_y:
                                        card_4_list.remove(card_4)
                                    if card_4.rect.x == ness_pos_x and card_4.rect.y == ness_pos_y:
                                        card_4_list.remove(card_4)
                                        card_4_w = Sprite_init.Card_4()
                                        card_win_list.add(card_4_w)
                                        card_4_w.rect.x = win_place[0]
                                        card_4_w.rect.y = win_place[1]
                            elif number == 1:
                                shake[3] = True
                                shake_l[0] = True
                            elif number == 2:
                                shake[3] = True
                                shake_l[1] = True
                            elif number == 3:
                                shake[3] = True
                                shake_l[2] = True
                            elif number == 5:
                                shake[3] = True
                                shake_l[4] = True
                            elif number == 6:
                                shake[3] = True
                                shake_l[5] = True
                            elif number == 7:
                                shake[3] = True
                                shake_l[6] = True
                            elif number == 8:
                                shake[3] = True
                                shake_l[7] = True
                            elif number == 9:
                                shake[3] = True
                                shake_l[8] = True
                            elif number == 10:
                                shake[3] = True
                                shake_l[9] = True
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
                                score += 10
                                for card_5 in card_5_list:
                                    if card_5.rect.x == position_x and card_5.rect.y == position_y:
                                        card_5_list.remove(card_5)
                                    if card_5.rect.x == ness_pos_x and card_5.rect.y == ness_pos_y:
                                        card_5_list.remove(card_5)
                                        card_5_w = Sprite_init.Card_5()
                                        card_win_list.add(card_5_w)
                                        card_5_w.rect.x = win_place[0]
                                        card_5_w.rect.y = win_place[1]
                            elif number == 1:
                                shake[4] = True
                                shake_l[0] = True
                            elif number == 2:
                                shake[4] = True
                                shake_l[1] = True
                            elif number == 3:
                                shake[4] = True
                                shake_l[2] = True
                            elif number == 4:
                                shake[4] = True
                                shake_l[3] = True
                            elif number == 6:
                                shake[4] = True
                                shake_l[5] = True
                            elif number == 7:
                                shake[4] = True
                                shake_l[6] = True
                            elif number == 8:
                                shake[4] = True
                                shake_l[7] = True
                            elif number == 9:
                                shake[4] = True
                                shake_l[8] = True
                            elif number == 10:
                                shake[4] = True
                                shake_l[9] = True
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
                                score += 10
                                for card_6 in card_6_list:
                                    if card_6.rect.x == position_x and card_6.rect.y == position_y:
                                        card_6_list.remove(card_6)
                                    if card_6.rect.x == ness_pos_x and card_6.rect.y == ness_pos_y:
                                        card_6_list.remove(card_6)
                                        card_6_w = Sprite_init.Card_6()
                                        card_win_list.add(card_6_w)
                                        card_6_w.rect.x = win_place[0]
                                        card_6_w.rect.y = win_place[1]
                            elif number == 1:
                                shake[5] = True
                                shake_l[0] = True
                            elif number == 2:
                                shake[5] = True
                                shake_l[1] = True
                            elif number == 3:
                                shake[5] = True
                                shake_l[2] = True
                            elif number == 4:
                                shake[5] = True
                                shake_l[3] = True
                            elif number == 5:
                                shake[5] = True
                                shake_l[4] = True
                            elif number == 7:
                                shake[5] = True
                                shake_l[6] = True
                            elif number == 8:
                                shake[5] = True
                                shake_l[7] = True
                            elif number == 9:
                                shake[5] = True
                                shake_l[8] = True
                            elif number == 10:
                                shake[5] = True
                                shake_l[9] = True
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
                                score += 10
                                for card_7 in card_7_list:
                                    if card_7.rect.x == position_x and card_7.rect.y == position_y:
                                        card_7_list.remove(card_7)
                                    if card_7.rect.x == ness_pos_x and card_7.rect.y == ness_pos_y:
                                        card_7_list.remove(card_7)
                                        card_7_w = Sprite_init.Card_7()
                                        card_win_list.add(card_7_w)
                                        card_7_w.rect.x = win_place[0]
                                        card_7_w.rect.y = win_place[1]
                            elif number == 1:
                                shake[6] = True
                                shake_l[0] = True
                            elif number == 2:
                                shake[6] = True
                                shake_l[1] = True
                            elif number == 3:
                                shake[6] = True
                                shake_l[2] = True
                            elif number == 4:
                                shake[6] = True
                                shake_l[3] = True
                            elif number == 5:
                                shake[6] = True
                                shake_l[4] = True
                            elif number == 6:
                                shake[6] = True
                                shake_l[5] = True
                            elif number == 8:
                                shake[6] = True
                                shake_l[7] = True
                            elif number == 9:
                                shake[6] = True
                                shake_l[8] = True
                            elif number == 10:
                                shake[6] = True
                                shake_l[9] = True
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
                                score += 10
                                for card_8 in card_8_list:
                                    if card_8.rect.x == position_x and card_8.rect.y == position_y:
                                        card_8_list.remove(card_8)
                                    if card_8.rect.x == ness_pos_x and card_8.rect.y == ness_pos_y:
                                        card_8_list.remove(card_8)
                                        card_8_w = Sprite_init.Card_8()
                                        card_win_list.add(card_8_w)
                                        card_8_w.rect.x = win_place[0]
                                        card_8_w.rect.y = win_place[1]
                            elif number == 1:
                                shake[7] = True
                                shake_l[0] = True
                            elif number == 2:
                                shake[7] = True
                                shake_l[1] = True
                            elif number == 3:
                                shake[7] = True
                                shake_l[2] = True
                            elif number == 4:
                                shake[7] = True
                                shake_l[3] = True
                            elif number == 5:
                                shake[7] = True
                                shake_l[4] = True
                            elif number == 6:
                                shake[7] = True
                                shake_l[5] = True
                            elif number == 7:
                                shake[7] = True
                                shake_l[6] = True
                            elif number == 9:
                                shake[7] = True
                                shake_l[8] = True
                            elif number == 10:
                                shake[7] = True
                                shake_l[9] = True
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
                                score += 10
                                for card_9 in card_9_list:
                                    if card_9.rect.x == position_x and card_9.rect.y == position_y:
                                        card_9_list.remove(card_9)
                                    if card_9.rect.x == ness_pos_x and card_9.rect.y == ness_pos_y:
                                        card_9_list.remove(card_9)
                                        card_9_w = Sprite_init.Card_9()
                                        card_win_list.add(card_9_w)
                                        card_9_w.rect.x = win_place[0]
                                        card_9_w.rect.y = win_place[1]
                            elif number == 1:
                                shake[8] = True
                                shake_l[0] = True
                            elif number == 2:
                                shake[8] = True
                                shake_l[1] = True
                            elif number == 3:
                                shake[8] = True
                                shake_l[2] = True
                            elif number == 4:
                                shake[8] = True
                                shake_l[3] = True
                            elif number == 5:
                                shake[8] = True
                                shake_l[4] = True
                            elif number == 6:
                                shake[8] = True
                                shake_l[5] = True
                            elif number == 7:
                                shake[8] = True
                                shake_l[6] = True
                            elif number == 8:
                                shake[8] = True
                                shake_l[7] = True
                            elif number == 10:
                                shake[8] = True
                                shake_l[9] = True
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
                                score += 10
                                for card_10 in card_10_list:
                                    if card_10.rect.x == position_x and card_10.rect.y == position_y:
                                        card_10_list.remove(card_10)
                                    if card_10.rect.x == ness_pos_x and card_10.rect.y == ness_pos_y:
                                        card_10_list.remove(card_10)
                                        card_10_w = Sprite_init.Card_10()
                                        card_win_list.add(card_10_w)
                                        card_10_w.rect.x = win_place[0]
                                        card_10_w.rect.y = win_place[1]
                            elif number == 1:
                                shake[9] = True
                                shake_l[0] = True
                            elif number == 2:
                                shake[9] = True
                                shake_l[1] = True
                            elif number == 3:
                                shake[9] = True
                                shake_l[2] = True
                            elif number == 4:
                                shake[9] = True
                                shake_l[3] = True
                            elif number == 5:
                                shake[9] = True
                                shake_l[4] = True
                            elif number == 6:
                                shake[9] = True
                                shake_l[5] = True
                            elif number == 7:
                                shake[9] = True
                                shake_l[6] = True
                            elif number == 8:
                                shake[9] = True
                                shake_l[7] = True
                            elif number == 9:
                                shake[9] = True
                                shake_l[8] = True
                            couple = 0
                            compare = False
                    if all_ch == 1:
                        compare = False
        if shake[0] == True:
            timer_sh[0] +=1
            if timer_sh[0] == 60:
                explode_sound.play()
                cardback_lb = Sprite_init.Cardback_3()
                cardb_lblue_list.add(cardback_lb)
                cardback_lb.rect.x = position_x
                cardback_lb.rect.y = position_y
                timer_sh[0] = 0
                shake[0] = False
        if shake[1] == True:
            timer_sh[1] +=1
            if timer_sh[1] == 60:
                explode_sound.play()
                cardback_lb = Sprite_init.Cardback_3()
                cardb_lblue_list.add(cardback_lb)
                cardback_lb.rect.x = position_x
                cardback_lb.rect.y = position_y
                timer_sh[1] = 0
                shake[1] = False
        if shake[2] == True:
            timer_sh[2] +=1
            if timer_sh[2] == 60:
                explode_sound.play()
                cardback_db = Sprite_init.Cardback_4()
                cardb_dblue_list.add(cardback_db)
                cardback_db.rect.x = position_x
                cardback_db.rect.y = position_y
                timer_sh[2] = 0
                shake[2] = False
        if shake[3] == True:
            timer_sh[3] +=1
            if timer_sh[3] == 60:
                explode_sound.play()
                cardback_db = Sprite_init.Cardback_4()
                cardb_dblue_list.add(cardback_db)
                cardback_db.rect.x = position_x
                cardback_db.rect.y = position_y
                timer_sh[3] = 0
                shake[3] = False
        if shake[4] == True:
            timer_sh[4] +=1
            if timer_sh[4] == 60:
                explode_sound.play()
                cardback_r = Sprite_init.Cardback_1()
                cardb_red_list.add(cardback_r)
                cardback_r.rect.x = position_x
                cardback_r.rect.y = position_y
                timer_sh[4] = 0
                move[4] = True
                shake[4] = False
        if shake[5] == True:
            timer_sh[5] +=1
            if timer_sh[5] == 60:
                explode_sound.play()
                cardback_g = Sprite_init.Cardback_2()
                cardb_green_list.add(cardback_g)
                cardback_g.rect.x = position_x
                cardback_g.rect.y = position_y
                timer_sh[5] = 0
                shake[5] = False
        if shake[6] == True:
            timer_sh[6] +=1
            if timer_sh[6] == 60:
                explode_sound.play()
                cardback_db = Sprite_init.Cardback_4()
                cardb_dblue_list.add(cardback_db)
                cardback_db.rect.x = position_x
                cardback_db.rect.y = position_y
                timer_sh[6] = 0
                shake[6] = False
        if shake[7] == True:
            timer_sh[7] +=1
            if timer_sh[7] == 60:
                explode_sound.play()
                cardback_lb = Sprite_init.Cardback_3()
                cardb_lblue_list.add(cardback_lb)
                cardback_lb.rect.x = position_x
                cardback_lb.rect.y = position_y
                timer_sh[7] = 0
                shake[7] = False
        if shake[8] == True:
            timer_sh[8] +=1
            if timer_sh[8] == 60:
                explode_sound.play()
                cardback_g = Sprite_init.Cardback_2()
                cardb_green_list.add(cardback_g)
                cardback_g.rect.x = position_x
                cardback_g.rect.y = position_y
                timer_sh[8] = 0
                shake[8] = False
        if shake[9] == True:
            timer_sh[9] +=1
            if timer_sh[9] == 60:
                explode_sound.play()
                cardback_db = Sprite_init.Cardback_4()
                cardb_dblue_list.add(cardback_db)
                cardback_db.rect.x = position_x
                cardback_db.rect.y = position_y
                timer_sh[9] = 0
                shake[9] = False
        if shake_l[0] == True:
            timer_l[0] += 1
            if timer_l[0] == 60:
                cardback_lb = Sprite_init.Cardback_3()
                cardb_lblue_list.add(cardback_lb)
                cardback_lb.rect.x = ness_pos_x
                cardback_lb.rect.y = ness_pos_y
                timer_l[0] = 0
                shake_l[0] = False
        if shake_l[1] == True:
            timer_l[1] += 1
            if timer_l[1] == 60:
                cardback_lb = Sprite_init.Cardback_3()
                cardb_lblue_list.add(cardback_lb)
                cardback_lb.rect.x = ness_pos_x
                cardback_lb.rect.y = ness_pos_y
                timer_l[1] = 0
                shake_l[1] = False
        if shake_l[2] == True:
            timer_l[2] += 1
            if timer_l[2] == 60:
                cardback_db = Sprite_init.Cardback_4()
                cardb_dblue_list.add(cardback_db)
                cardback_db.rect.x = ness_pos_x
                cardback_db.rect.y = ness_pos_y
                timer_l[2] = 0
                shake_l[2] = False
        if shake_l[3] == True:
            timer_l[3] += 1
            if timer_l[3] == 60:
                cardback_db = Sprite_init.Cardback_4()
                cardb_dblue_list.add(cardback_db)
                cardback_db.rect.x = ness_pos_x
                cardback_db.rect.y = ness_pos_y
                timer_l[3] = 0
                shake_l[3] = False
        if shake_l[4] == True:
            timer_l[4] += 1
            if timer_l[4] == 60:
                cardback_r = Sprite_init.Cardback_1()
                cardb_red_list.add(cardback_r)
                cardback_r.rect.x = ness_pos_x
                cardback_r.rect.y = ness_pos_y
                timer_l[4] = 0
                shake_l[4] = False
        if shake_l[5] == True:
            timer_l[5] += 1
            if timer_l[5] == 60:
                cardback_g = Sprite_init.Cardback_2()
                cardb_green_list.add(cardback_g)
                cardback_g.rect.x = ness_pos_x
                cardback_g.rect.y = ness_pos_y
                timer_l[5] = 0
                shake_l[5] = False
        if shake_l[6] == True:
            timer_l[6] += 1
            if timer_l[6] == 60:
                cardback_db = Sprite_init.Cardback_4()
                cardb_dblue_list.add(cardback_db)
                cardback_db.rect.x = ness_pos_x
                cardback_db.rect.y = ness_pos_y
                timer_l[6] = 0
                shake_l[6] = False
        if shake_l[7] == True:
            timer_l[7] += 1
            if timer_l[7] == 60:
                cardback_lb = Sprite_init.Cardback_3()
                cardb_lblue_list.add(cardback_lb)
                cardback_lb.rect.x = ness_pos_x
                cardback_lb.rect.y = ness_pos_y
                timer_l[7] = 0
                shake_l[7] = False
        if shake_l[8] == True:
            timer_l[8] += 1
            if timer_l[8] == 60:
                cardback_g = Sprite_init.Cardback_2()
                cardb_green_list.add(cardback_g)
                cardback_g.rect.x = ness_pos_x
                cardback_g.rect.y = ness_pos_y
                timer_l[8] = 0
                shake_l[8] = False
        if shake_l[9] == True:
            timer_l[9] += 1
            if timer_l[9] == 60:
                cardback_db = Sprite_init.Cardback_4()
                cardb_dblue_list.add(cardback_db)
                cardback_db.rect.x = ness_pos_x
                cardback_db.rect.y = ness_pos_y
                timer_l[9] = 0
                shake_l[9] = False
        text = font.render("Score: ", True, white)
        text1 = font.render(str(score), True, white)
        screen.blit(text, [win_place[0], 400])
        screen.blit(text1, [win_place[0]+70, 500])
        if move[4] == True:
            print('move rabotaet')
            text_5 = font.render(str(left[4]), True, white)
            screen.blit(text_5, [win_place[0], 700])
            tim[4] += 1
            if tim[4]% 60 == 0:
                left[4] -= 1
            if tim[4] == 600:
                cardb_red_list.remove(cardback_r)
                tim[4] = 0
                left[4] = 10
                move[4] = False






            
        for card_1 in card_1_list:
            final_count += 1
        for card_2 in card_2_list:
            final_count += 1
        for card_3 in card_3_list:
            final_count += 1
        for card_4 in card_4_list:
            final_count += 1
        for card_5 in card_5_list:
            final_count += 1
        for card_6 in card_6_list:
            final_count += 1
        for card_7 in card_7_list:
            final_count += 1
        for card_8 in card_8_list:
            final_count +=1
        for card_9 in card_9_list:
            final_count +=1
        for card_10 in card_10_list:
            final_count += 1
        if final_count < 2:
            done = True
        else:
            final_count = 0
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
        cardb_red_list.draw(screen)
        cardb_green_list.draw(screen)
        cardb_lblue_list.draw(screen)
        cardb_dblue_list.draw(screen)
        card_win_list.draw(screen)
        pointer_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    
Level_1()
