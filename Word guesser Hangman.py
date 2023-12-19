from random import *


def rand_word(word_list):
    word = choice(word_list)
    return word


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    word = word.lower()
    ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    word_completion = ['_' for _ in range(len(word))]
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    while True:
        maybe_word = ''.join(word_completion)

        if tries == 0:
            print(display_hangman(tries))
            break
        else:
            print(display_hangman(tries))
            print('Попробуйте угадать!')
            print(''.join(word_completion))
            attempt = input().lower()
            cnt = 0

            for i in attempt:
                if i in ru:
                    cnt += 1

            if len(attempt) == cnt and len(attempt) > 1 and attempt not in guessed_words:
                if attempt == word:
                    tries -= 1
                    guessed = True
                    break
                else:
                    tries -= 1
                    guessed_words.append(attempt)
                    print('Увы, это не то слово...')
                    continue
            elif len(attempt) == cnt and len(attempt) == 1 and attempt not in guessed_letters:
                if attempt in word:
                    tries -= 1
                    guessed_letters.append(attempt)
                    count = 0

                    for i in word:
                        if attempt == i:
                            word_completion[count] = attempt
                            count += 1
                        else:
                            count += 1

                    if maybe_word == word:
                        guessed = True
                        break

                else:
                    tries -= 1
                    guessed_letters.append(attempt)
                    print('Увы, этой буквы нет в слове...')
                    continue
            elif attempt in guessed_words:
                print('Это слово уже было...')
                continue
            elif attempt in guessed_letters:
                print('Эта буква уже была...')
                continue
            else:
                print('Только буква или слово...')
                continue

    return guessed, (6 - tries)


def win_or_not(guessed, tries, word):
    if guessed:
        print(f'''Поздравляем, вы угадали слово {word}! Вы победили!')
        Количество попыток - {tries}''')
    else:
        print(f'Сожалею, вы не угадали... Загаданное слово - {word}')


def game_exit():
    while True:
        print('Хотите сыграть еще разок? Y/N')
        another_game = input().lower()
        if another_game != 'y' and another_game != 'n':
            print('Такого ответа я не знаю...')
            continue
        else:
            break
    return another_game


def start():
    word_list = ['Ладонь', 'Пылесос', 'Король', 'Полдник', 'Зеркало', 'Табурет', 'Красота', 'Волк', 'Переход',
                 'Аквапарк', 'Желание', 'Конфета', 'Учитель', 'Опушка', 'Песок', 'Снежинка', 'Силач', 'Корабль',
                 'Куртка', 'Сказка', 'Пирог', 'Звезда', 'Сахар', 'Пряник', 'Лимон', 'Берег', 'Горка', 'Пирамида',
                 'Дружба', 'Рыба', 'Телевизор', 'Покрывало', 'Секрет', 'Тесто', 'Лужа', 'Музыка', 'Невидимка',
                 'Трещина', 'Кладовка', 'Мультик', 'Экран', 'Магазин', 'Занавеска', 'Свинья', 'Дедушка', 'Камень',
                 'Свисток', 'Молния', 'Игрушка', 'Доброта', 'Картошка', 'Строитель', 'Раковина', 'Краб', 'Дерево',
                 'Стекло', 'Подушка', 'Минута', 'Замок', 'Разговор', 'Правда', 'Прогулка', 'Бульдозер', 'Подоконник',
                 'Сердце', 'Балкон', 'Сосулька', 'Кошка', 'Картинка', 'Штаны', 'Прихожая', 'Вечер', 'Стакан', 'Яма',
                 'Водопад', 'Ветер', 'Колесо', 'Ложка', 'Железо', 'Палка', 'Картон', 'Пластилин', 'Скатерть',
                 'Грибок', 'Книга', 'Батон', 'Корова', 'Земля', 'Остров', 'Загадка', 'Машина', 'Масло', 'Волна',
                 'Голова', 'Зарядка', 'Птица', 'Пятно', 'Ведро', 'Дождь', 'Шапка']

    print('Давайте играть в угадайку слов!')

    while True:
        word = rand_word(word_list)
        print(word)

        guessed, tries = play(word)

        win_or_not(guessed, tries, word)

        another_game = game_exit()
        if another_game == 'y':
            continue
        else:
            break


start()
