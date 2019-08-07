# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        Быки и коровы
# Purpose:     Игра
#
# Author:      kirpichnikov_aa
#
# Created:     11.12.2017
# Copyright:   (c) kirpichnikov_aa 2017
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import random


def main():
    ##while len (comp_guess) != 4:
    ##number_1 = random.randint(0,9)
    ##if number_1 not in comp_guess:
    ##comp_guess.append(number_1)
    a1 = random.randint(1, 9)
    a2 = random.randint(0, 9)
    while a1 == a2:
        a2 = random.randint(0, 9)
    a3 = random.randint(0, 9)
    while a1 == a3 or a2 == a3:
        a3 = random.randint(0, 9)
    a4 = random.randint(0, 9)
    while a1 == a4 or a2 == a4 or a3 == a4:
        a4 = random.randint(0, 9)

    ish1 = a1 * 1000 + a2 * 100 + a3 * 10 + a4
    ish = [a1, a2, a3, a4]

    for i in range(15):
        byk, kor = 0, 0
        while True:
            try:
                inp = raw_input(u'Быки и коровы. Версия 1.0\nВведите ваше число без повторяющихся цифр:')
            except:  # EOFError, KeyboardInterrupt:
                a = -1  # отмена ввода
                print(u'Жаль, что Вы уходите...')
                break
            a = ''
            for j in range(len(inp)):
                if a.find(inp[j]) == -1 and inp[j] != ' ':
                    a += inp[j]
            if isinstance(a, basestring) and a.isdigit() and len(a) == 4:
                a = int(a)
                break
            else:
                print(u'Введите 4-значное число без повторяющихся цифр!')

        if a == -1:  # отмена ввода
            break  # выход из цикла for
        if a == ish1:
            print(u'Да ладно! Вы угадали!!! %d' % ish1)
            break
        elif i == 14:
            print(u'Попробуйте ещё разок, вдруг повезёт ;-)')
            break
        inp = [a // 1000, (a // 100) % 10, (a // 10) % 10, a % 10]
        for w, e in zip(ish, inp):
            if w == e:
                byk += 1
        for w, e in zip(inp, range(4)):
            if (w in ish) and (w != ish[e]):
                kor += 1
        print(u'Ваше число %d: у вас %d коров и %d быков' % (a, kor, byk))
        print(u'У Вас осталось %d попыток' % (14 - i))


if __name__ == '__main__':
    main()
