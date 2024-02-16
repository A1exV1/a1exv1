class NumberCalc:
    def __call__(self, from_sys, to_sys, numb):
        if from_sys in ['2', '8', '16']:
            numb = NumberCalc.to_int(int(from_sys), numb)
        elif from_sys == 'R':
            numb = NumberCalc.roman_to_int(numb)

        if to_sys == 'R':
            return NumberCalc.int_to_roman(int(numb))
        elif to_sys in ['2', '8', '16']:
            return NumberCalc.from_int(int(to_sys), int(numb))
        return numb

    @staticmethod
    def from_int(to_sys, numb):
        if to_sys == 8:
            return str(oct(numb))[2:]
        elif to_sys == 16:
            return str(hex(numb))[2:].upper()
        return str(bin(numb))[2:]

    @staticmethod
    def to_int(from_sys, numb):
        return int(numb, base=from_sys)

    @staticmethod
    def int_to_roman(numb):
        dct, out = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                    500: 'D', 900: 'CM', 1000: 'M'}, ''

        for n in (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1):
            while n <= numb:
                out += dct[n]
                numb -= n
        return out

    @staticmethod
    def roman_to_int(numb):
        dct, out = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}, 0

        for i in range(len(numb) - 1, -1, -1):
            num = dct[numb[i]]
            if 3 * num < out:
                out -= num
            else:
                out += num
        return out


class Program:
    _from_sys = None

    def __call__(self):
        print('Приветствую! Это калькулятор систем счисления.')

        while True:
            from_sys = Program.from_sys()
            to_sys = Program.to_sys()
            numb = Program.numb()

            calc = NumberCalc()
            print(calc(from_sys, to_sys, numb))

            if Program.exit() == 'N':
                print('До свидания!')
                break

    @staticmethod
    def from_sys():
        while True:
            print('''Из какой системы необходимо перевести число?
            Я умею переводить числа из следующих систем:
            - Десятеричная (10)
            - Двоичная (2)
            - Восьмеричная (8)
            - Шестнадцатеричная (16)
            - Римская (R)
            Напишите только число или R:''')
            from_sys = input().upper()

            if from_sys == 'R' or (from_sys.isdigit() and from_sys in ['2', '8', '10', '16']):
                Program._from_sys = from_sys
                return from_sys
            print('Неверный ввод...')

    @staticmethod
    def to_sys():
        while True:
            print('''В какую систему необходимо перевести число?
            Напишите только число 2/8/10/16 или R:''')
            to_sys = input().upper()

            if to_sys != Program._from_sys and ((to_sys.isdigit() and to_sys in ['2', '8', '10', '16'])
                                                or to_sys == 'R'):
                return to_sys
            print('Неверный ввод...')

    @staticmethod
    def numb():
        while True:
            print('Прошу ввести число для перевода:')
            numb = input().upper()

            if Program._from_sys == 'R' and all(i in 'IVXLCDM' for i in numb):
                return numb
            elif Program._from_sys == '2' and all(i in '01' for i in numb):
                return numb
            elif Program._from_sys == '8' and all(i in '01234567' for i in numb):
                return numb
            elif Program._from_sys == '10' and all(i.isdigit() for i in numb):
                return numb
            elif Program._from_sys == '16' and all(i in '0123456789ABCDEF' for i in numb):
                return numb
            print('Неверный ввод...')

    @staticmethod
    def exit():
        while True:
            print('Переведем другое число? Y/N')
            another_numb = input().upper()
            if another_numb == 'Y' or another_numb == 'N':
                return another_numb
            print('Такого ответа я не знаю...')


start = Program()
start()
