import random

class Lotto:
    def __init__(self, karta, rand_90, poz1, poz2):
        self.karta = karta
        self.rand_90 = rand_90
        self.poz1 = poz1
        self.poz2 = poz2

    def def_karta(self):
        znach = random.sample(range(1, 91), 15)
        return znach

    def def_rand_90(self):
        rand_90 = random.sample(range(1, 91), 90)
        return rand_90

    def do_replace_c(self, karta, i):
        print(f'выбран боченок:{self.rand_90[i]} (ход № {i + 1})')
        for j in range(len(karta)):
            if karta[j] == self.rand_90[i]:
                karta[j] = 'X'
        num_x = sum(1 for j in karta if j == 'X')
        return karta, num_x

    def def_karta_stroki(self, karta, poz):
        blank_karta = [[' ' for j in range(9)] for i in range(3)]
        split_list = [sorted(map(str, karta[:5])), sorted(map(str, karta[5:10])), sorted(map(str, karta[10:]))]

        for i in range(3):
            for j, val in enumerate(poz[i]):
                blank_karta[i][val] = split_list[i][j]
        return '\n'.join([' '.join(str(j) for j in row) for row in blank_karta])

    def def_poz(self):
        e = [sorted(random.sample(range(0, 9), 5)) for i in range(3)]
        return e

#-------Реализация ДЗ dunder методы
    def __str__(self):
        return self.def_karta_stroki(self.karta, self.poz1)

    # магический метод __eq__ для класса Lotto
    def __eq__(self, other):
        return self.karta == other.karta

    # магический метод __ne__ для класса Lotto
    def __ne__(self, other):
        return self.karta != other.karta

class C_to_c(Lotto):
    def __init__(self):
        karta = self.def_karta()
        rand_90 = self.def_rand_90()
        poz1 = self.def_poz()
        poz2 = self.def_poz()
        Lotto.__init__(self, karta, rand_90, poz1, poz2)
        self.karta_1 = self.def_karta()
        self.num_x1 = self.karta_1.count('X')
        self.karta_2 = self.def_karta()
        self.num_x2 = self.karta_2.count('X')

    def play_cc(self):
        for i in range(len(self.rand_90)):
            self.karta_1, self.num_x1 = self.do_replace_c(self.karta_1, i)
            self.karta_2, self.num_x2 = self.do_replace_c(self.karta_2, i)
            print(self)  #_____ Вывод актуальной карточки Лото после выбора боченка
            if self.num_x1 == 15 or self.num_x2 == 15:
                return f'Выиграл Комп # {1 if self.num_x1 == 15 else 2}'
        return 'Игра закончена'

#----Реализация ДЗ dunder методы
    def __str__(self):
        comp1_card = self.def_karta_stroki(self.karta_1, self.poz1)
        comp2_card = self.def_karta_stroki(self.karta_2, self.poz2)
        return f'Карта Компьютера #1:\n{comp1_card}\n\nКарта Компьютера #2:\n{comp2_card}'

class C_to_i(Lotto):
    def def_y_n(self, y_or_n):
        while True:
            if y_or_n == 'y' or y_or_n == 'n':
                return y_or_n
            else:
                print('Пожалуйста, введите "y" или "n".')
                y_or_n = self.def_y_n(input('Пожалуйста, введите "y" или "n: '))

    def __init__(self):
        karta = self.def_karta()
        rand_90 = self.def_rand_90()
        poz1 = self.def_poz()
        poz2 = self.def_poz()
        Lotto.__init__(self, karta, rand_90, poz1, poz2)
        self.karta_1 = self.def_karta()
        self.num_x1 = self.karta_1.count('X')
        self.karta_2 = self.def_karta()
        self.num_x2 = self.karta_2.count('X')
        self.y_or_n = self.def_y_n

    def play_ci(self):
        for i in range(len(self.rand_90)):
            self.karta_1, self.num_x1 = self.do_replace_c(self.karta_1, i)
            y_or_n = self.def_y_n(input(f'Число {self.rand_90[i]} присутствует в вашей карте? Нажмите (y/n): '))
            if y_or_n == 'y' and self.rand_90[i] in self.karta_2:
                self.karta_2, self.num_x2 = self.do_replace_c(self.karta_2, i)
                print(self)  #____ Вывод актуальной карточки Лото после выбора боченка
                if self.num_x1 == 15 or self.num_x2 == 15:
                    return f'Выиграл Игрок # {1 if self.num_x1 == 15 else 2}'
            elif y_or_n == 'n' and self.rand_90[i] not in self.karta_2:
                self.karta_2, self.num_x2 = self.do_replace_c(self.karta_2, i)
                print(self)  #____ Вывод актуальной карточки Лото после выбора боченка
            else:
                return 'Вы проиграли, завершение программы'

#-----
    def __str__(self):
        player_card = self.def_karta_stroki(self.karta_2, self.poz2)
        return f'Ваша карта:\n{player_card}'

while True:
    print('2. Игра Лотто Компьютер - Игрок')
    print('3. Игра Лотто Компьютер - Компьютер')
    print('4. Реализация методов __eq__  и __ne__ ')
    print('5. Выйте из игры')

    choice = input('Выберите пункт меню: ')
    if choice == '2':
        print('Вы выбрали игру Лотто Компьютер - Игрок')
        game = C_to_i()
        print(game)  # Вывод карты игрока до начала игры
        result = game.play_ci()
        print(result)  # Вывод результата игры
        print(game)  # Вывод карты игрока после игры

    if choice == '3':
        print('Вы выбрали игру Лотто Компьютер - Компьютер')
        game = C_to_c()
        print(game)  # Вывод карты компьютера до начала игры
        result = game.play_cc()
        print(result)  # Вывод результата игры
        print(game)  # Вывод карты компьютера после игры

    if choice == '4':
        print('Вы выбрали демонстрацию методов __eq__ и __ne__ ')
        # создаем два объекта класса C_to_i или C_to_c
        a = C_to_i()
        b = C_to_i()
        # сравниваем объекты
        print(a == b)  # False
        print(a != b)  # True
        # изменяем значения карт
        a.karta = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        b.karta = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # сравниваем объекты повторно
        print(a == b)  # True
        print(a != b)  # False

    elif choice == '5':
        print('Вы вышли из игры')
        break
    else:
        print('Вы выбрали неверный пункт меню')
