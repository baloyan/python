import random

# !/usr/bin/python3

"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
SAMPLE = range(1, 91)
lst = list(SAMPLE)


def get_barrel(x):
    random.shuffle(x)
    yield x.pop(0)


class Card:
    def __init__(self, name):
        self.numbers = random.sample(SAMPLE, 15)
        self.name = name
        self.list1 = self.numbers[:5]
        self.list2 = self.numbers[5:10]
        self.list3 = self.numbers[10:]

        def build_line(lst):
            res = ' '
            lst_cur = sorted(lst)
            for i in range(4):
                rand_place = random.randint(0, 9)
                lst_cur.insert(rand_place, " ")
            return lst_cur

        self.line1 = build_line(self.list1)
        self.line2 = build_line(self.list2)
        self.line3 = build_line(self.list3)
        self.lines = (self.line1, self.line2, self.line3)
        self.draw_card(self.lines)

    def draw_card(self, lines):
        print("---", "Карточка " + self.name + "а", "---")
        for line in lines:
            draw = ''
            for i in line:
                draw += str(i) + ' '
            print(draw)
        print("--------------------------")

    def check_turn(self, turn):
        for line in self.lines:
            if turn in line:
                place = line.index(turn)
                line[place] = '-'
                print(turn, "Совпало!!!!!!!")
        self.draw_card(self.lines)


class Player:
    def __init__(self, name):
        self.name = name

    def make_turn(self):
        self.turn = next(get_barrel(lst))
        print(self.name, 'вытянул ', self.turn)
        c2.check_turn(self.turn)

    '''
    def cross_or_cont(self):
        des = input("Введите З чтобы зачеркнуть или П чтобы продолжить")
        if des == 'З':
            if self.turn in self.numbers:
                pass
    '''


player1 = "Игрок"
player2 = "Компьютер"
c1 = Card(player1)
c2 = Card(player2)
p1 = Player(player1)
p2 = Player(player2)
p1.make_turn()
c1.check_turn(p1.turn)
p2.make_turn()
c2.check_turn(p2.turn)