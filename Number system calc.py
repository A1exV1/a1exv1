class NumberCalc:
    def __call__(self, from_sys, to_sys, numb, *args, **kwargs):
        numb = NumberCalc.to_int(int(from_sys), numb) if from_sys in ['2', '8', '16'] else \
            NumberCalc.roman_to_int(numb) if from_sys == 'R' else numb

        return NumberCalc.int_to_roman(int(numb)) if to_sys == 'R' \
            else NumberCalc.from_int(int(to_sys), int(numb)) if to_sys in ['2', '8', '16'] else numb

    @classmethod
    def from_int(cls, to_sys, numb):
        return [f'{numb:b}', f'{numb:o}', f'{numb:X}'][[2, 8, 16].index(to_sys)]

    @classmethod
    def to_int(cls, from_sys, numb):
        return int(numb, base=from_sys)

    @classmethod
    def int_to_roman(cls, numb):
        dct, out = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                    500: 'D', 900: 'CM', 1000: 'M'}, ''

        for n in reversed(dct.keys()):
            while n <= numb:
                out += dct[n]
                numb -= n
        return out

    @classmethod
    def roman_to_int(cls, numb):
        dct, out = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}, 0

        for i in range(len(numb) - 1, -1, -1):
            num = dct[numb[i]]
            out = out - num if 3 * num < out else out + num
        return out


class Program:
    _from_sys = None

    def __call__(self, *args, **kwargs):
        print('Приветствую! Это калькулятор систем счисления.')

        while True:
            from_sys = Program.get_from_sys()
            to_sys = Program.get_to_sys()
            numb = Program.get_numb()

            calc = NumberCalc()
            print(calc(from_sys, to_sys, numb))

            if Program.exit() == 'N':
                print('До свидания!')
                break

    @classmethod
    def get_from_sys(cls):
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

    @classmethod
    def get_to_sys(cls):
        while True:
            print('''В какую систему необходимо перевести число?
            Напишите только число 2/8/10/16 или R:''')
            to_sys = input().upper()

            if to_sys != Program._from_sys and ((to_sys.isdigit() and to_sys in ['2', '8', '10', '16']) or
                                                to_sys == 'R'):
                return to_sys
            print('Неверный ввод...')

    @classmethod
    def get_numb(cls):
        while True:
            print('Прошу ввести число для перевода:')
            numb = input().upper()

            if (Program._from_sys == 'R' and all(i in 'IVXLCDM' for i in numb)) or \
                    (Program._from_sys == '2' and all(i in '01' for i in numb)) or \
                    (Program._from_sys == '8' and all(i in '01234567' for i in numb)) or \
                    (Program._from_sys == '10' and all(i.isdigit() for i in numb)) or \
                    (Program._from_sys == '16' and all(i in '0123456789ABCDEF' for i in numb)):
                return numb
            print('Неверный ввод...')

    @classmethod
    def exit(cls):
        while True:
            print('Переведем другое число? Y/N')
            another = input().upper()
            if another in ['Y', 'N']:
                return another
            print('Такого ответа я не знаю...')


start = Program()
start()
