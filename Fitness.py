from datetime import timedelta as td

FORMAT = '%H:%M:%S'
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.
TRANSFER_COEFF = 1000  # Коэффициент перевода значения расстояния из метров в километры

package = ('9:36:02', 15305)  # p
time = package[0]  # t
steps = package[1]  # st
storage_data = {}  # Словарь для хранения полученных данных.

h,m,s = time.split(':')
current_time = int(td(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())  # ct


def get_step_day(st):
    for step in storage_data.values():
        st += step
    return st


print(f'Общее кол-во шагов: {get_step_day(steps)}')


def check_correct_data(p):
    if len(p) != 2 or p[0] is None or p[1] is None:
        return False
    return True


def check_correct_time(p):
    for time_check in storage_data.keys():
        if time_check >= p[0] and storage_data != {}:
            return False
    return True


def accept_package(p):
    if check_correct_data(p) is False and check_correct_time(p) is False:
        exit()
    else:
        storage_data[p[0]] = p[1]  # Словарь для хранения полученных данных.
        return storage_data


accept_package(package)
storage_data = accept_package(package)
print(f'Содержание словаря: {storage_data}')


def get_distance(st):
    d = round(st * STEP_M / TRANSFER_COEFF, 2)
    return d


dist = get_distance(steps)


def get_achievement(d):
    if d >= 6.5:
        a = 'Отличный результат! Цель достигнута.'
    elif d >= 3.9:
        a = 'Неплохо! День был продуктивным.'
    elif d >= 2:
        a = 'Маловато, но завтра наверстаем!'
    else:
        a = 'Лежать тоже полезно. Главное — участие, а не победа!'
    return a


achievement = get_achievement(dist)  # a


def get_spent_calories(d, ct):
    mean_speed = d / (ct / 3600)
    minutes = ct / 60
    inner_cals = (K_1 * WEIGHT + (mean_speed ** 2 / HEIGHT) * K_2 * WEIGHT) * minutes
    return inner_cals


cals = get_spent_calories(dist, current_time)  # c


def show_message(t, st, d, c, a):
    print(f'''
    Время: {t}.
    Количество шагов за сегодня: {st}.
    Дистанция составила {d} км.
    Вы сожгли {int(c)} ккал.
    {a}''')


show_message(time, steps, dist, cals, achievement)
