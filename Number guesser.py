from random import *

while True:
    print('Добро пожаловать в числовую угадайку!')


    def is_valid_right(nr):
        if nr > 0:
            return True
        return False


    def is_valid(n):
        if 1 <= n <= nright:
            return True
        return False


    while True:
        print('До какого числа будем играть?')
        try:
            nright = int(input())
        except ValueError:
            print('Нам нужно именно число...')
            continue

        if is_valid_right(nright):
            break
        else:
            print('Нам нужно именно число...')
            continue

    x = randint(1, nright)
    cnt = 0

    while True:
        print('Какое число я загадал?')
        try:
            num = int(input())
        except ValueError:
            print(f'А может быть все-таки введем целое число от 1 до {nright}?')
            continue

        if is_valid(num):
            pass
        else:
            print(f'А может быть все-таки введем целое число от 1 до {nright}?')
            continue

        if num < x:
            cnt += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num > x:
            cnt += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print(f'Количество попыток - {cnt}')
            break

    while True:
        print('Хотите сыграть еще разок? Y/N')
        another_game = input()
        if another_game.lower() != 'y' and another_game.lower() != 'n':
            continue
        else:
            break

    if another_game.lower() == 'y':
        continue
    else:
        break
