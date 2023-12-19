from random import *


def is_right_valid(nright):
    if nright > 0:
        return True
    return False


def right_number():
    while True:
        nright = input()
        if nright.isdigit():
            nright = int(nright)
        else:
            print('Нам нужно именно число...')
            continue

        if is_right_valid(nright):
            break
        else:
            print('Нам нужно число больше 0...')
            continue
    return nright


def rand_number(nright):
    rand_numb = randint(1, nright)
    return rand_numb


def is_num_valid(num, nright):
    if 1 <= num <= nright:
        return True
    return False


def in_game(nright, rand_numb):
    cnt = 0

    while True:
        print('Какое число я загадал?')
        num = input()
        if num.isdigit():
            num = int(num)
        else:
            print(f'А может быть все-таки введем целое число от 1 до {nright}?')
            continue

        if is_num_valid(num, nright):
            pass
        else:
            print(f'А может быть все-таки введем целое число от 1 до {nright}?')
            continue

        if num < rand_numb:
            cnt += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num > rand_numb:
            cnt += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            break

    return cnt


def game_exit():
    while True:
        print('Хотите сыграть еще разок? Y/N')
        another_game = input().lower()
        if another_game != 'y' and another_game != 'n':
            print('Такого ответа я не знаю...')
            continue
        else:
            break
    return another_game


def start():
    while True:
        print('Добро пожаловать в числовую угадайку!')
        print('До какого числа будем играть?')

        nright = right_number()
        rand_numb = rand_number(nright)

        cnt = in_game(nright, rand_numb)
        print('Вы угадали, поздравляем!')
        print(f'Количество попыток - {cnt}')

        another_game = game_exit()
        if another_game == 'y':
            continue
        else:
            break


start()
