class Caesar:
    _ru, _en = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'abcdefghijklmnopqrstuvwxyz'

    @staticmethod
    def cipher(dest, lang, step, words):
        coded, lang = '', [Caesar._ru, Caesar._en][['RU', 'EN'].index(lang)]
        for letter in words:
            upper, letter = letter.isupper(), letter.lower()
            letter = lang[(lang.index(letter) + [step, -step][['E', 'D'].index(dest)]) % len(lang)] if letter in lang\
                else letter
            coded += [letter, letter.upper()][upper]
        return coded


class Program:
    def __call__(self, *args, **kwargs):
        print('Приветствую! Сейчас мы будем работать с Шифром Цезаря.')

        while True:
            dest = Program.get('Зашифровать или дешифровать? E/D', ['E', 'D'])
            lang = Program.get('На каком языке? RU/EN', ['RU', 'EN'])
            choice = {'RU': 32, 'EN': 25}
            step = Program.get(f'Какой шаг сдвига? 1-{choice[lang]}', choice[lang])

            print('Какую фразу необходимо обработать?')
            words = input()

            print(f'''Послание:
{Caesar.cipher(dest, lang, step, words)} (ROT{step})''')

            if Program.exit() == 'N':
                print('До свидания!')
                break

    @classmethod
    def get(cls, phrase:str, choice:[list,int]):
        while True:
            print(phrase)
            out = input().upper()
            if isinstance(choice, list) and out in choice:
                return out
            elif isinstance(choice, int) and out.isdigit() and 1 <= int(out) <= choice:
                return int(out)
            print('Такого ответа я не знаю...')

    @classmethod
    def exit(cls):
        while True:
            print('Будут ещё шифры? Y/N')
            another = input().upper()
            if another in ['Y', 'N']:
                return another
            print('Такого ответа я не знаю...')


start = Program()
start()
