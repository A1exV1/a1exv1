def questions():
    while True:
        print(f'Зашифровать или дешифровать? E/D')
        dest = input().lower()
        if dest != 'e' and dest != 'd':
            print('Такого ответа я не знаю...')
            continue
        else:
            break

    while True:
        print(f'На каком языке? Ru/En')
        lang = input().lower()
        if lang != 'ru' and lang != 'en':
            print('Такого ответа я не знаю...')
            continue
        else:
            break

    while True:
        print('Какой шаг сдвига? Ru до 31/En до 25')
        step = input()

        if step.isdigit():
            step = int(step)
            if lang == 'ru' and 0 < step < 32:
                break
            elif lang == 'en' and 0 < step < 26:
                break
            else:
                print('Должен быть больше 0...')
                continue
        else:
            print('Нам нужно именно число...')
            continue

    print('Какую фразу необходимо обработать?')
    words = input()

    return dest, step, words


def code(dest, step, words):
    en_lower = 'abcdefghijklmnopqrstuvwxyz'
    en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ru_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    ru_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    coded = ''

    if dest == 'e':
        for i in words:
            if i in en_lower:
                char = en_lower[(en_lower.index(i) + step) % len(en_lower)]
                coded += char
            elif i in en_upper:
                char = en_upper[(en_upper.index(i) + step) % len(en_upper)]
                coded += char
            elif i in ru_lower:
                char = ru_lower[(ru_lower.index(i) + step) % len(ru_lower)]
                coded += char
            elif i in ru_upper:
                char = ru_upper[(ru_upper.index(i) + step) % len(ru_upper)]
                coded += char
            else:
                coded += i
    else:
        for i in words:
            if i in en_lower:
                char = en_lower[(en_lower.index(i) - step) % len(en_lower)]
                coded += char
            elif i in en_upper:
                char = en_upper[(en_upper.index(i) - step) % len(en_upper)]
                coded += char
            elif i in ru_lower:
                char = ru_lower[(ru_lower.index(i) - step) % len(ru_lower)]
                coded += char
            elif i in ru_upper:
                char = ru_upper[(ru_upper.index(i) - step) % len(ru_upper)]
                coded += char
            else:
                coded += i

    print(coded)


def cipher_exit():
    while True:
        print('Будут еще шифры? Y/N')
        another_cipher = input().lower()
        if another_cipher != 'y' and another_cipher != 'n':
            print('Такого ответа я не знаю...')
            continue
        else:
            break
    return another_cipher


def start():
    print('Приветствую! Сейчас мы будем работать с Шифром Цезаря.')

    while True:
        dest, step, words = questions()

        code(dest, step, words)

        another_cipher = cipher_exit()
        if another_cipher == 'y':
            continue
        else:
            break


start()
