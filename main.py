class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')


class Student(Human):
    #  метод ask_question() принимает параметр self:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, question):
        # напечатайте на экран вопрос в нужном формате
        print(f'{self.name}, {question}')
        # запросите ответ на вопрос у someone
        self.answer_question(question)
        print()  # этот print выводит разделительную пустую строку


class Curator(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print("Держись, всё получится. Хочешь видео с котиками?")
        else:
            super().answer_question(question)

# объявите и реализуйте классы CodeReviewer и Mentor
