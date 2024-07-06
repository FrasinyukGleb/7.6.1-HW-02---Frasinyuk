# Игра в крестики-нолики

print('Приветствую! Перед Вами игра в крестики-нолики для двух игроков.\n'
      'Правила игры: игроки ходят по очереди, выставляя на игровом поле символы Х или О\n'
      'Цель игры: первым выставить 3 своих символа в ряд по вертикали, горизонтали или диагонали.\n'
      'Игрок должен ввести сначала номер строки, затем номер столбца,\n'
      'куда он хочет поставить свой символ.')

game_table = [[' ', '1', '2', '3'],
              ['1', '-', '-', '-'],
              ['2', '-', '-', '-'],
              ['3', '-', '-', '-']]


def print_table(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end='  ')
        print()


def win_check(table):
    for y in range(4):
        if table[y][1] == table[y][2] == table[y][3] and table[y][1] == 'X':
            result = 'Игрок_1 победил! Игра окончена!'
            return result
        elif table[y][1] == table[y][2] == table[y][3] and table[y][1] == 'O':
            result = 'Игрок_2 победил! Игра окончена!'
            return result
    for x in range(4):
        if table[x][1] == table[x][2] == table[x][3] and table[x][1] == 'X':
            result = 'Игрок_1 победил! Игра окончена!'
            return result
        elif table[x][1] == table[x][2] == table[x][3] and table[x][1] == 'X':
            result = 'Игрок_2 победил! Игра окончена!'
            return result
    if table[1][1] == table[2][2] == table[3][3] and table[1][1] == 'X':
        result = 'Игрок_1 победил! Игра окончена!'
        return result
    elif table[1][1] == table[2][2] == table[3][3] and table[1][1] == 'O':
        result = 'Игрок_2 победил! Игра окончена!'
        return result
    elif table[1][3] == table[2][2] == table[3][1] and table[2][2] == 'X':
        result = 'Игрок_1 победил! Игра окончена!'
        return result
    elif table[1][3] == table[2][2] == table[3][1] and table[2][2] == 'O':
        result = 'Игрок_2 победил! Игра окончена!'
        return result
    else:
        return False


def p1_turns(table):
    while True:
        i = input('Игрок_1, выберите строку: ')
        j = input('Игрок_1, выберите столбец: ')
        if not i.isdigit() or not j.isdigit():
            print('Введено неверное значение! Введите число от 1 до 3.')
        else:
            i = int(i)
            j = int(j)
            if i < 1 or i > 3 or j < 1 or j > 3:
                print('Такой ячейки не существует! Попробуйте другую.')
            elif table[i][j] in 'XO':
                print('Ячейка занята! Выберите другую.')
            else:
                table[i][j] = 'X'
                print_table(table)
                win_check(table)
                break


def p2_turns(table):
    while True:
        i = input('Игрок_2, выберите строку: ')
        j = input('Игрок_2, выберите столбец: ')
        if not i.isdigit() or not j.isdigit():
            print('Введено неверное значение! Введите число от 1 до 3.')
        else:
            i = int(i)
            j = int(j)
            if i < 1 or i > 3 or j < 1 or j > 3:
                print('Такой ячейки не существует! Попробуйте другую.')
            elif table[i][j] in 'XO':
                print('Ячейка занята! Выберите другую.')
            else:
                table[i][j] = 'O'
                print_table(table)
                win_check(table)
                break


def game_start(table):
    print_table(table)
    turn_count = 0
    while turn_count < 9:
        p1_turns(table)
        turn_count += 1
        if win_check(table):
            print(win_check(table))
            break
        if turn_count == 9:
            print('Ничья! Игра окончена!')
            break
        p2_turns(table)
        turn_count += 1
        if win_check(table):
            print(win_check(table))
            break


def game():
    while True:
        new_game = input('\nХотите сыграть? y/n: ')
        if new_game == 'y':
            game_start(game_table)
            break
        elif new_game == 'n':
            print('До свидания!')
            break
        else:
            print('Ошибка! Введено некорректное значение!')


game()
