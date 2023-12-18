from random import *


def right_number():
    global nright
    while True:
        try:
            nright = int(input())
        except ValueError:
            print('Нам нужно именно число...')
            continue
        else:
            if is_right_valid(nright):
                break
            else:
                print('Нам нужно именно число...')


def is_right_valid(n):
    if n > 0:
        return True
    return False


def in_game():
    cnt = 0
    while True:
        print('Какое число я загадал?')
        try:
            num = int(input())
        except ValueError:
            print(f'А может быть все-таки введем целое число от 1 до {nright}?')
            continue

        if is_num_valid(num):
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
            print('Вы угадали, поздравляем!')
            print(f'Количество попыток - {cnt}')
            break


def is_num_valid(n):
    if 1 <= n <= nright:
        return True
    return False


def game_exit():
    global another_game
    while True:
        print('Хотите сыграть еще разок? Y/N')
        another_game = input()
        if another_game.lower() != 'y' and another_game.lower() != 'n':
            continue
        else:
            break


while True:
    print('Добро пожаловать в числовую угадайку!')
    print('До какого числа будем играть?')

    nright = 0
    right_number()

    rand_numb = randint(1, nright)

    in_game()

    another_game = ''
    game_exit()

    if another_game.lower() == 'y':
        continue
    else:
        break
