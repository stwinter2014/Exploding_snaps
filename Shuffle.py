import pygame
import random
import Sprite_init
pygame.init()
size = [1200, 900]
screen = pygame.display.set_mode(size)
cardback_1 = pygame.image.load('cardback_1.png').convert()
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

def Shuffle (card_1_list, card_2_list, card_3_list, card_4_list, card_5_list,
                card_6_list, card_7_list, card_8_list, card_9_list, card_10_list):
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
    rand_coll = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    rand = random.choice(rand_coll)
    if rand == '0':
        if counter_1 < 2:
            card_1 = Sprite_init.Card_1()
            card_1_list.add(card_1)
            card_1.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
            card_1.rect.y = (size[1]-cardback_1.get_height()*4)/5
            nesses_rect_x = card_1.rect.x
            nesses_rect_y = card_1.rect.y
            counter_1 += 1
        if counter_1 == 2:
            rand_coll.remove('0')
    if rand == '1':
        if counter_2 < 2:
            card_2 = Sprite_init.Card_2()
            card_2_list.add(card_2)
            card_2.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
            card_2.rect.y = (size[1]-cardback_1.get_height()*4)/5
            nesses_rect_x = card_2.rect.x
            nesses_rect_y = card_2.rect.y
            counter_2 += 1
        if counter_2 == 2:
            rand_coll.remove('1')
    if rand == '2':
        if counter_3 < 2:
            card_3 = Sprite_init.Card_3()
            card_3_list.add(card_3)
            card_3.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
            card_3.rect.y = (size[1]-cardback_1.get_height()*4)/5
            nesses_rect_x = card_3.rect.x
            nesses_rect_y = card_3.rect.y
            counter_3 += 1
        if counter_3 == 2:
            rand_coll.remove('2')
    if rand == '3':
        if counter_4 < 2:
            card_4 = Sprite_init.Card_4()
            card_4_list.add(card_4)
            card_4.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
            card_4.rect.y = (size[1]-cardback_1.get_height()*4)/5
            nesses_rect_x = card_4.rect.x
            nesses_rect_y = card_4.rect.y
            counter_4 += 1
        if counter_4 == 2:
            rand_coll.remove('3')
    if rand == '4':
        if counter_5 < 2:
            card_5 = Sprite_init.Card_5()
            card_5_list.add(card_5)
            card_5.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
            card_5.rect.y = (size[1]-cardback_1.get_height()*4)/5
            nesses_rect_x = card_5.rect.x
            nesses_rect_y = card_5.rect.y
            counter_5 += 1
        if counter_5 == 2:
            rand_coll.remove('4')
    if rand == '5':
        if counter_6 < 2:
            card_6 = Sprite_init.Card_6()
            card_6_list.add(card_6)
            card_6.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
            card_6.rect.y = (size[1]-cardback_1.get_height()*4)/5
            nesses_rect_x = card_6.rect.x
            nesses_rect_y = card_6.rect.y
            counter_6 += 1
        if counter_6 == 2:
            rand_coll.remove('5')
    if rand == '6':
        if counter_7 < 2:
            card_7 = Sprite_init.Card_7()
            card_7_list.add(card_7)
            card_7.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
            card_7.rect.y = (size[1]-cardback_1.get_height()*4)/5
            nesses_rect_x = card_7.rect.x
            nesses_rect_y = card_7.rect.y
            counter_7 += 1
        if counter_7 == 2:
            rand_coll.remove('6')
    if rand == '7':
        if counter_8 < 2:
            card_8 = Sprite_init.Card_8()
            card_8_list.add(card_8)
            card_8.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
            card_8.rect.y = (size[1]-cardback_1.get_height()*4)/5
            nesses_rect_x = card_8.rect.x
            nesses_rect_y = card_8.rect.y
            counter_8 += 1
        if counter_8 == 2:
            rand_coll.remove('7')
    if rand == '8':
        if counter_9 < 2:
            card_9 = Sprite_init.Card_9()
            card_9_list.add(card_9)
            card_9.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
            card_9.rect.y = (size[1]-cardback_1.get_height()*4)/5
            nesses_rect_x = card_9.rect.x
            nesses_rect_y = card_9.rect.y
            counter_9 += 1
        if counter_9 == 2:
            rand_coll.remove('8')
    if rand == '9':
        if counter_10 < 2:
            card_10 = Sprite_init.Card_10()
            card_10_list.add(card_10)
            card_10.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
            card_10.rect.y = (size[1]-cardback_1.get_height()*4)/5
            nesses_rect_x = card_10.rect.x
            nesses_rect_y = card_10.rect.y
            counter_10 += 1
        if counter_10 == 2:
            rand_coll.remove('9')
    rand = ""
    for i in range (4):
        rand = random.choice(rand_coll)
        if rand == '0':
            if counter_1 < 2:
                card_1 = Sprite_init.Card_1()
                card_1_list.add(card_1)
                card_1.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_1.rect.y = (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_1.rect.x
                nesses_rect_y = card_1.rect.y
                counter_1 += 1
            if counter_1 == 2:
                rand_coll.remove('0')
        if rand == '1':
            if counter_2 < 2:
                card_2 = Sprite_init.Card_2()
                card_2_list.add(card_2)
                card_2.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_2.rect.y = (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_2.rect.x
                nesses_rect_y = card_2.rect.y
                counter_2 += 1
            if counter_2 == 2:
                rand_coll.remove('1')
        if rand == '2':
            if counter_3 < 2:
                card_3 = Sprite_init.Card_3()
                card_3_list.add(card_3)
                card_3.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_3.rect.y = (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_3.rect.x
                nesses_rect_y = card_3.rect.y
                counter_3 += 1
            if counter_3 == 2:
                rand_coll.remove('2')
        if rand == '3':
            if counter_4 < 2:
                card_4 = Sprite_init.Card_4()
                card_4_list.add(card_4)
                card_4.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_4.rect.y = (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_4.rect.x
                nesses_rect_y = card_4.rect.y
                counter_4 += 1
            if counter_4 == 2:
                rand_coll.remove('3')
        if rand == '4':
            if counter_5 < 2:
                card_5 = Sprite_init.Card_5()
                card_5_list.add(card_5)
                card_5.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_5.rect.y = (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_5.rect.x
                nesses_rect_y = card_5.rect.y
                counter_5 += 1
            if counter_5 == 2:
                rand_coll.remove('4')
        if rand == '5':
            if counter_6 < 2:
                card_6 = Sprite_init.Card_6()
                card_6_list.add(card_6)
                card_6.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_6.rect.y = (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_6.rect.x
                nesses_rect_y = card_6.rect.y
                counter_6 += 1
            if counter_6 == 2:
                rand_coll.remove('5')
        if rand == '6':
            if counter_7 < 2:
                card_7 = Sprite_init.Card_7()
                card_7_list.add(card_7)
                card_7.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_7.rect.y = (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_7.rect.x
                nesses_rect_y = card_7.rect.y
                counter_7 += 1
            if counter_7 == 2:
                rand_coll.remove('6')
        if rand == '7':
            if counter_8 < 2:
                card_8 = Sprite_init.Card_8()
                card_8_list.add(card_8)
                card_8.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_8.rect.y = (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_8.rect.x
                nesses_rect_y = card_8.rect.y
                counter_8 += 1
            if counter_8 == 2:
                rand_coll.remove('7')
        if rand == '8':
            if counter_9 < 2:
                card_9 = Sprite_init.Card_9()
                card_9_list.add(card_9)
                card_9.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_9.rect.y = (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_9.rect.x
                nesses_rect_y = card_9.rect.y
                counter_9 += 1
            if counter_9 == 2:
                rand_coll.remove('8')
        if rand == '9':
            if counter_10 < 2:
                card_10 = Sprite_init.Card_10()
                card_10_list.add(card_10)
                card_10.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_10.rect.y = (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_10.rect.x
                nesses_rect_y = card_10.rect.y
                counter_10 += 1
            if counter_10 == 2:
                rand_coll.remove('9')
        rand = ''
    for j in range (3):
        rand = random.choice(rand_coll)
        if rand == '0':
            if counter_1 < 2:
                card_1 = Sprite_init.Card_1()
                card_1_list.add(card_1)
                card_1.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_1.rect.y = nesses_rect_y + cardback_1.get_height() + (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_1.rect.x
                nesses_rect_y = card_1.rect.y
                counter_1 += 1
            if counter_1 == 2:
                rand_coll.remove('0')
        if rand == '1':
            if counter_2 < 2:
                card_2 = Sprite_init.Card_2()
                card_2_list.add(card_2)
                card_2.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_2.rect.y = nesses_rect_y + cardback_1.get_height() + (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_2.rect.x
                nesses_rect_y = card_2.rect.y
                counter_2 += 1
            if counter_2 == 2:
                rand_coll.remove('1')
        if rand == '2':
            if counter_3 < 2:
                card_3 = Sprite_init.Card_3()
                card_3_list.add(card_3)
                card_3.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_3.rect.y = nesses_rect_y + cardback_1.get_height() + (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_3.rect.x
                nesses_rect_y = card_3.rect.y
                counter_3 += 1
            if counter_3 == 2:
                rand_coll.remove('2')
        if rand == '3':
            if counter_4 < 2:
                card_4 = Sprite_init.Card_4()
                card_4_list.add(card_4)
                card_4.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_4.rect.y = nesses_rect_y + cardback_1.get_height() + (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_4.rect.x
                nesses_rect_y = card_4.rect.y
                counter_4 += 1
            if counter_4 == 2:
                rand_coll.remove('3')
        if rand == '4':
            if counter_5 < 2:
                card_5 = Sprite_init.Card_5()
                card_5_list.add(card_5)
                card_5.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_5.rect.y = nesses_rect_y + cardback_1.get_height() + (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_5.rect.x
                nesses_rect_y = card_5.rect.y
                counter_5 += 1
            if counter_5 == 2:
                rand_coll.remove('4')
        if rand == '5':
            if counter_6 < 2:
                card_6 = Sprite_init.Card_6()
                card_6_list.add(card_6)
                card_6.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_6.rect.y = nesses_rect_y + cardback_1.get_height() + (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_6.rect.x
                nesses_rect_y = card_6.rect.y
                counter_6 += 1
            if counter_6 == 2:
                rand_coll.remove('5')
        if rand == '6':
            if counter_7 < 2:
                card_7 = Sprite_init.Card_7()
                card_7_list.add(card_7)
                card_7.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_7.rect.y = nesses_rect_y + cardback_1.get_height() + (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_7.rect.x
                nesses_rect_y = card_7.rect.y
                counter_7 += 1
            if counter_7 == 2:
                rand_coll.remove('6')
        if rand == '7':
            if counter_8 < 2:
                card_8 = Sprite_init.Card_8()
                card_8_list.add(card_8)
                card_8.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_8.rect.y = nesses_rect_y + cardback_1.get_height() + (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_8.rect.x
                nesses_rect_y = card_8.rect.y
                counter_8 += 1
            if counter_8 == 2:
                rand_coll.remove('7')
        if rand == '8':
            if counter_9 < 2:
                card_9 = Sprite_init.Card_9()
                card_9_list.add(card_9)
                card_9.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_9.rect.y = nesses_rect_y + cardback_1.get_height() + (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_9.rect.x
                nesses_rect_y = card_9.rect.y
                counter_9 += 1
            if counter_9 == 2:
                rand_coll.remove('8')
        if rand == '9':
            if counter_10 < 2:
                card_10 = Sprite_init.Card_10()
                card_10_list.add(card_10)
                card_10.rect.x = ((size[0])*2/3 - cardback_1.get_width()*5)/6
                card_10.rect.y = nesses_rect_y + cardback_1.get_height() + (size[1]-cardback_1.get_height()*4)/5
                nesses_rect_x = card_10.rect.x
                nesses_rect_y = card_10.rect.y
                counter_10 += 1
            if counter_10 == 2:
                rand_coll.remove('9')
        rand = ""
        for k in range (4):
            rand = random.choice(rand_coll)
            if rand == '0':
                if counter_1 < 2:
                    card_1 = Sprite_init.Card_1()
                    card_1_list.add(card_1)
                    card_1.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                    card_1.rect.y = nesses_rect_y
                    nesses_rect_x = card_1.rect.x
                    nesses_rect_y = card_1.rect.y
                    counter_1 += 1
                if counter_1 == 2:
                    rand_coll.remove('0')
            if rand == '1':
                if counter_2 < 2:
                    card_2 = Sprite_init.Card_2()
                    card_2_list.add(card_2)
                    card_2.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                    card_2.rect.y = nesses_rect_y
                    nesses_rect_x = card_2.rect.x
                    nesses_rect_y = card_2.rect.y
                    counter_2 += 1
                if counter_2 == 2:
                    rand_coll.remove('1')
            if rand == '2':
                if counter_3 < 2:
                    card_3 = Sprite_init.Card_3()
                    card_3_list.add(card_3)
                    card_3.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                    card_3.rect.y = nesses_rect_y
                    nesses_rect_x = card_3.rect.x
                    nesses_rect_y = card_3.rect.y
                    counter_3 += 1
                if counter_3 == 2:
                    rand_coll.remove('2')
            if rand == '3':
                if counter_4 < 2:
                    card_4 = Sprite_init.Card_4()
                    card_4_list.add(card_4)
                    card_4.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                    card_4.rect.y = nesses_rect_y
                    nesses_rect_x = card_4.rect.x
                    nesses_rect_y = card_4.rect.y
                    counter_4 += 1
                if counter_4 == 2:
                    rand_coll.remove('3')
            if rand == '4':
                if counter_5 < 2:
                    card_5 = Sprite_init.Card_5()
                    card_5_list.add(card_5)
                    card_5.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                    card_5.rect.y = nesses_rect_y
                    nesses_rect_x = card_5.rect.x
                    nesses_rect_y = card_5.rect.y
                    counter_5 += 1
                if counter_5 == 2:
                    rand_coll.remove('4')
            if rand == '5':
                if counter_6 < 2:
                    card_6 = Sprite_init.Card_6()
                    card_6_list.add(card_6)
                    card_6.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                    card_6.rect.y = nesses_rect_y
                    nesses_rect_x = card_6.rect.x
                    nesses_rect_y = card_6.rect.y
                    counter_6 += 1
                if counter_6 == 2:
                    rand_coll.remove('5')
            if rand == '6':
                if counter_7 < 2:
                    card_7 = Sprite_init.Card_7()
                    card_7_list.add(card_7)
                    card_7.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                    card_7.rect.y = nesses_rect_y
                    nesses_rect_x = card_7.rect.x
                    nesses_rect_y = card_7.rect.y
                    counter_7 += 1
                if counter_7 == 2:
                    rand_coll.remove('6')
            if rand == '7':
                if counter_8 < 2:
                    card_8 = Sprite_init.Card_8()
                    card_8_list.add(card_8)
                    card_8.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                    card_8.rect.y = nesses_rect_y
                    nesses_rect_x = card_8.rect.x
                    nesses_rect_y = card_8.rect.y
                    counter_8 += 1
                if counter_8 == 2:
                    rand_coll.remove('7')
            if rand == '8':
                if counter_9 < 2:
                    card_9 = Sprite_init.Card_9()
                    card_9_list.add(card_9)
                    card_9.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                    card_9.rect.y = nesses_rect_y
                    nesses_rect_x = card_9.rect.x
                    nesses_rect_y = card_9.rect.y
                    counter_9 += 1
                if counter_9 == 2:
                    rand_coll.remove('8')
            if rand == '9':
                if counter_10 < 2:
                    card_10 = Sprite_init.Card_10()
                    card_10_list.add(card_10)
                    card_10.rect.x = nesses_rect_x + cardback_1.get_width() + ((size[0])*2/3 - cardback_1.get_width()*5)/6
                    card_10.rect.y = nesses_rect_y
                    nesses_rect_x = card_10.rect.x
                    nesses_rect_y = card_10.rect.y
                    counter_10 += 1
                if counter_10 == 2:
                    rand_coll.remove('9')
            rand = ''
