from random import *


def gamer_name():
    print('Как имя твое?')
    gamer = input()
    return gamer


def is_question(question):
    if question.endswith('?'):
        return True
    else:
        return False


def in_game(answers):
    while True:
        print('Какой у тебя вопрос ко мне?')
        question = input()

        if is_question(question):
            break
        else:
            print('Это не вопрос!')
            continue

    rand = choice(answers)
    return rand


def game_exit():
    while True:
        print('У тебя есть еще вопросы? Y/N')
        another_question = input().lower()
        if another_question != 'y' and another_question != 'n':
            print('Такого ответа я не знаю...')
            continue
        else:
            break
    return another_question


def start():
    answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
               'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
               'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
               'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
               'Перспективы не очень хорошие', 'Весьма сомнительно']

    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')

    gamer = gamer_name()
    print(f'Привет, {gamer}!')

    while True:
        rand = in_game(answers)
        print(f'Мой ответ: {rand}')

        another_question = game_exit()
        if another_question == 'y':
            continue
        else:
            break


start()
