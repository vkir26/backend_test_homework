import time

import datetime as dt


# Объявите класс Quest с методами и свойствами.
class Quest:
    def __init__(self, name, goal, description):
        # Свойства:
        self.name = name
        self.goal = goal
        self.description = description
        # Допишите два свойства класса.
        self.start_time = None
        self.end_time = None

    # Напишите методы приема и сдачи квеста.
    # В метод accept_quest() в свойство start_time запишите текущее время.
    # Метод должен вернуть фразу 'Начало "{название_квеста}" положено.'
    def accept_quest(self):
        if self.end_time:
            print(self.end_time)
            return 'С этим испытанием вы уже справились.'

        self.start_time = dt.datetime.now()
        return f'Начало "{self.name}" положено.'

    # В метод pass_quest() в свойство end_time тоже запишите текущее время.
    # Также в этом методе объявите переменную completion_time
    # и посчитайте в ней разницу между временем завершения и начала квеста. Метод
    # Метод должен вернуть фразу 'Квест "{название_квеста}" окончен.
    # Время выполнения квеста: {разница_между_завершением_и_началом_квеста}'
    def pass_quest(self):
        if self.start_time is None:
            return 'Нельзя завершить то, что не имеет начала!'

        self.end_time = dt.datetime.now()
        completion_time = self.end_time - self.start_time
        return (f'Квест "{self.name}" окончен. '
                f'Время выполнения квеста: {completion_time}')

    # Напишите код метода __str__.
    def __str__(self):
        s = ''
        if self.end_time:
            s = ' Квест завершён.'
        elif self.start_time:
            s = ' Квест выполняется.'
        return f'Цель квеста {self.name} - {self.goal}{s}'


quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

new_quest = Quest(quest_name, quest_goal, quest_description)

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())

# Печатаем объект класса Quest:
print(new_quest)