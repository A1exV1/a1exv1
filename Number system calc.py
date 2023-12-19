def questions():
    systems = [2, 8, 10, 16]
    let_16 = 'abcdef'
    rome = 'ivxlcdm'

    while True:
        print('''Из какой системы необходимо перевести число?
        Я умею переводить числа из следующих систем:
        - Десятеричная (10)
        - Двоичная (2)
        - Восьмеричная (8)
        - Шестнадцатеричная (16)
        - Римская (R)
        Напиши только число или R:''')
        from_sys = input().lower()

        if from_sys.isdigit():
            from_sys = int(from_sys)
            if from_sys in systems:
                break
            else:
                print('Прошу повторить ввод...')
                continue
        elif from_sys == 'r':
            break
        else:
            print('Прошу повторить ввод...')
            continue

    while True:
        print('''В какую систему необходимо перевести число?
        Напиши только число 2/8/10/16 или R:''')
        to_sys = input().lower()

        if to_sys.isdigit():
            to_sys = int(to_sys)
            if to_sys in systems and to_sys != from_sys:
                break
            elif to_sys == from_sys:
                print('Переводить в ту же систему бессмысленно...')
                continue
            else:
                print('Прошу повторить ввод...')
                continue
        elif to_sys == 'r':
            if to_sys != from_sys:
                break
            else:
                print('Переводить в ту же систему бессмысленно...')
                continue
        else:
            print('Прошу повторить ввод...')
            continue

    while True:
        print('Прошу ввести число для перевода:')
        numb = input().lower()

        if numb.isdigit():
            if from_sys != 'r':
                break
            else:
                print('Только римские цифры...')
                continue
        elif numb.isalpha():
            if from_sys == 'r':
                leng = len(numb)
                cnt = 0
                for i in numb:
                    if i in rome:
                        cnt += 1
                    else:
                        pass

                if cnt == leng:
                    break
                else:
                    print('Только римские цифры...')
                    continue
            else:
                print('Только арабские цифры...')
                continue
        elif numb.isalnum() and from_sys == 16:
            leng = len(numb)
            cnt = 0
            for i in numb:
                if i.isdigit():
                    cnt += 1
                elif i in let_16:
                    cnt += 1
                else:
                    pass

            if cnt == leng:
                break
            else:
                print('Только буквы от A до F...')
                continue
        else:
            print('Прошу повторить ввод...')
            continue

    return from_sys, to_sys, numb


def calc_from_10(to_sys, numb):
    numb = int(numb)

    if to_sys == 2:
        out = str(bin(numb))
        return out[2:]
    elif to_sys == 8:
        out = str(oct(numb))
        return out[2:]
    else:
        out = str(hex(numb))
        return out[2:].upper()


def calc_to_10(from_sys, numb):
    cnt = 0
    out = 0
    bmun = numb[::-1]

    if from_sys == 2 or from_sys == 8:
        for i in bmun:
            out += int(i) * (from_sys ** cnt)
            cnt += 1
        return out
    else:
        for i in bmun:
            if i.isdigit():
                out += int(i) * (from_sys ** cnt)
                cnt += 1
            else:
                if i == 'a':
                    out += 10 * (from_sys ** cnt)
                elif i == 'b':
                    out += 11 * (from_sys ** cnt)
                elif i == 'c':
                    out += 12 * (from_sys ** cnt)
                elif i == 'd':
                    out += 13 * (from_sys ** cnt)
                elif i == 'e':
                    out += 14 * (from_sys ** cnt)
                else:
                    out += 15 * (from_sys ** cnt)
                cnt += 1
        return out


def calc_to_r_from_10(numb):
    leng = len(numb)
    numb_int = int(numb)
    out = ''

    if (numb_int // 1000) != 0:
        out += 'M' * int(numb_int / 1000)

    if (numb_int // 100) != 0:
        point = (numb_int % 1000) // 100
        print(point)
        if point == 9:
            out += 'CM'
        elif 5 <= point <= 8:
            out += 'D' + ('C' * (point - 5))
        elif point == 4:
            out += 'CD'
        else:
            out += 'C' * point

    if (numb_int // 10) != 0:
        point = (numb_int % 100) // 10
        print(point)
        if point == 9:
            out += 'XC'
        elif 5 <= point <= 8:
            out += 'L' + ('X' * (point - 5))
        elif point == 4:
            out += 'XL'
        elif 2 <= point <= 3:
            out += 'X' * point

        if 19 <= (numb_int % 100) <= 10:
            point = numb_int % 100
            if point == 19:
                out += 'XIX'
            elif 15 <= point <= 18:
                out += 'XV' + ('I' * (point - 5))
            elif point == 14:
                out += 'XIV'
            elif 10 <= point <= 13:
                out += 'X' * point

    point = numb_int % 10
    if point == 9:
        out += 'IX'
    elif 5 <= point <= 8:
        out += 'V' + ('I' * (point - 5))
    elif point == 4:
        out += 'IV'
    elif 1 <= point <= 3:
        out += 'I' * point

    return out


def calc_from_r_to_10(numb):
    lst = []
    cnt = 0
    out = 0

    for i in numb:
        if i == 'i':
            lst.append(1)
        elif i == 'v':
            lst.append(5)
        elif i == 'x':
            lst.append(10)
        elif i == 'l':
            lst.append(50)
        elif i == 'c':
            lst.append(100)
        elif i == 'd':
            lst.append(500)
        else:
            lst.append(1000)

    for p in range(len(lst)):
        if (cnt == (len(lst) - 1)) and (lst[p] <= lst[p - 1]):
            out += lst[p]
        elif (cnt == (len(lst) - 1)) and (lst[p] > lst[p - 1]):
            out += (lst[p] - lst[p - 1])
        elif lst[p] < lst[p + 1]:
            pass
        elif (cnt != 0) and (lst[p] > lst[p - 1]):
            out += (lst[p] - lst[p - 1])
        elif lst[p] == lst[p + 1]:
            out += lst[p]

        cnt += 1

    return out


def calc(from_sys, to_sys, numb):
    if from_sys == 10 and to_sys != 'r':
        out = calc_from_10(to_sys, numb)
    elif to_sys == 10 and from_sys != 'r':
        out = calc_to_10(from_sys, numb)
    elif (from_sys == 2 or from_sys == 8 or from_sys == 16) and (to_sys == 2 or to_sys == 8 or to_sys == 16):
        first = calc_to_10(from_sys, numb)
        out = calc_from_10(to_sys, str(first))
    elif from_sys == 'r' and to_sys == 10:
        out = calc_from_r_to_10(numb)
    elif to_sys == 'r' and from_sys == 10:
        out = calc_to_r_from_10(numb)
    elif from_sys == 'r':
        first = calc_from_r_to_10(numb)
        out = calc_from_10(to_sys, str(first))
    else:
        first = calc_to_10(from_sys, numb)
        out = calc_to_r_from_10(str(first))

    return out


def numb_exit():
    while True:
        print('Переведем другое число? Y/N')
        another_numb = input().lower()
        if another_numb != 'y' and another_numb != 'n':
            print('Такого ответа я не знаю...')
            continue
        else:
            break
    return another_numb


def start():
    print('Приветствую! Это калькулятор систем счисления.')

    while True:
        from_sys, to_sys, numb = questions()

        out = calc(from_sys, to_sys, numb)
        print(out)

        another_numb = numb_exit()
        if another_numb == 'y':
            continue
        else:
            break


start()
