class Caesar:
    @staticmethod
    def cipher(dest, lang, step, words):
        ru, en = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'abcdefghijklmnopqrstuvwxyz'
        coded, lang = '', [ru, en][['RU', 'EN'].index(lang)]
        for letter in words:
            upper, letter = letter.isupper(), letter.lower()
            letter = lang[(lang.index(letter) + [step, -step][['E', 'D'].index(dest)]) % len(lang)] if letter in lang\
                else letter
            coded += [letter, letter.upper()][upper]
        return coded


class Run:
    def __init__(self):
        print('Приветствую! Сейчас мы будем работать с Шифром Цезаря.')

        while True:
            dest = self.get('Зашифровать или дешифровать? E/D', ['E', 'D'])
            lang = self.get('На каком языке? RU/EN', ['RU', 'EN'])
            choice = {'RU': 32, 'EN': 25}
            step = self.get(f'Какой шаг сдвига? 1-{choice[lang]}', choice[lang])

            print('Какую фразу необходимо обработать?')
            words = input()

            print(f'''Послание:
{Caesar.cipher(dest, lang, step, words)} (ROT{step})''')

            if self.exit() == 'N':
                print('До свидания!')
                break

    @staticmethod
    def get(phrase:str, choice:[list, int]):
        while True:
            print(phrase)
            out = input().upper()
            if isinstance(choice, list) and out in choice:
                return out
            elif isinstance(choice, int) and out.isdigit() and 1 <= int(out) <= choice:
                return int(out)
            print('Такого ответа я не знаю...')

    @staticmethod
    def exit():
        while True:
            print('Будут ещё шифры? Y/N')
            another = input().upper()

            if another in ['Y', 'N']:
                return another
            print('Такого ответа я не знаю...')


if __name__ == '__main__':
    Run()
