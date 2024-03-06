class NumberCalc:
    def __init__(self, from_sys: str, to_sys: str, numb: str):
        self.from_sys = from_sys if from_sys == 'R' else int(from_sys)
        self.to_sys = to_sys if to_sys == 'R' else int(to_sys)
        self.numb = numb

    def run(self):
        self.numb = self.to_int() if self.from_sys in [2, 8, 16] \
            else self.roman_to_int() if self.from_sys == 'R' else self.numb
        self.numb = self.int_to_roman() if self.to_sys == 'R' \
            else self.from_int() if self.to_sys in [2, 8, 16] else self.numb
        return self.numb

    def from_int(self):
        return [f'{self.numb:b}', f'{self.numb:o}', f'{self.numb:X}'][[2, 8, 16].index(self.to_sys)]

    def to_int(self):
        return int(self.numb, base=self.from_sys)

    def int_to_roman(self):
        int_dct, out = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                        500: 'D', 900: 'CM', 1000: 'M'}, ''

        for n in reversed(int_dct.keys()):
            while n <= self.numb:
                out += int_dct[n]
                self.numb -= n
        return out

    def roman_to_int(self):
        roman_dct, out = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}, 0

        for i in range(len(self.numb) - 1, -1, -1):
            num = roman_dct[self.numb[i]]
            out = out - num if 3 * num < out else out + num
        return out


class Run:
    def __init__(self):
        print('Приветствую! Это калькулятор систем счисления.')

        while True:
            self.from_sys = self.get_from_sys()
            self.to_sys = self.get_to_sys()
            self.numb = self.get_numb()

            calc = NumberCalc(self.from_sys, self.to_sys, self.numb)
            print(calc.run())

            if self.exit() == 'N':
                print('До свидания!')
                break

    def get_from_sys(self):
        while True:
            print('''Из какой системы необходимо перевести число?
            Я умею переводить числа из следующих систем:
            - Десятеричная (10)
            - Двоичная (2)
            - Восьмеричная (8)
            - Шестнадцатеричная (16)
            - Римская (R)
            Напишите только число или R:''')
            self.from_sys = input().upper()

            if self.from_sys == 'R' or (self.from_sys.isdigit() and self.from_sys in ['2', '8', '10', '16']):
                return self.from_sys
            print('Неверный ввод...')

    def get_to_sys(self):
        while True:
            print('''В какую систему необходимо перевести число?
            Напишите только число 2/8/10/16 или R:''')
            self.to_sys = input().upper()

            if self.to_sys != self.from_sys and ((self.to_sys.isdigit() and self.to_sys in ['2', '8', '10', '16'])
                                                 or self.to_sys == 'R'):
                return self.to_sys
            print('Неверный ввод...')

    def get_numb(self):
        while True:
            print('Прошу ввести число для перевода:')
            self.numb = input().upper()

            if (self.from_sys == 'R' and all(i in 'IVXLCDM' for i in self.numb)) or \
                    (self.from_sys == '2' and all(i in '01' for i in self.numb)) or \
                    (self.from_sys == '8' and all(i in '01234567' for i in self.numb)) or \
                    (self.from_sys == '10' and all(i.isdigit() for i in self.numb)) or \
                    (self.from_sys == '16' and all(i in '0123456789ABCDEF' for i in self.numb)):
                return self.numb
            print('Неверный ввод...')

    @staticmethod
    def exit():
        while True:
            print('Переведем другое число? Y/N')
            another = input().upper()

            if another in ['Y', 'N']:
                return another
            print('Такого ответа я не знаю...')


if __name__ == '__main__':
    Run()
