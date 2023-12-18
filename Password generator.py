from random import *


def questions():
    symbols = ['0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!#$%&*+-=?@^', 'il1Lo0O']
    chars = ''

    while True:
        print('Сколько паролей сгенерировать?')
        pwd_numb = input()

        if pwd_numb.isdigit():
            pwd_numb = int(pwd_numb)
            if pwd_numb > 0:
                break
            else:
                print('Их должно быть больше 0...')
                continue
        else:
            print('Нам нужно именно число...')
            continue

    while True:
        print('Какая длина одного пароля?')
        pwd_len = input()

        if pwd_len.isdigit():
            pwd_len = int(pwd_len)
            break
        else:
            print('Нам нужно именно число...')
            continue

    while True:
        for i in range(5):
            while True:
                print(f'Включать ли в пароль символы {symbols[i]}? Y/N')
                answer = input().lower()
                if answer == 'y':
                    chars += symbols[i]
                    break
                elif answer == 'n':
                    break
                else:
                    continue

        if chars != '':
            break
        else:
            print('У пароля должны быть символы!')
            continue

    return pwd_numb, pwd_len, chars


def generate_pwd(pwd_numb, pwd_len, chars):
    for i in range(1, pwd_numb+1):
        pwd = ''
        for p in range(pwd_len):
            pwd += choice(chars)
        print(pwd)


def pwd_exit():
    while True:
        print('Нужны еще пароли? Y/N')
        another_pwd = input().lower()
        if another_pwd != 'y' and another_pwd != 'n':
            continue
        else:
            break
    return another_pwd


def start():
    print('Приветствую! Сейчас мы сгенерируем пароль.')

    while True:
        pwd_numb, pwd_len, chars = questions()

        generate_pwd(pwd_numb, pwd_len, chars)

        another_pwd = pwd_exit()
        if another_pwd == 'y':
            continue
        else:
            break


start()
