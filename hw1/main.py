# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

''' Обычные задания '''

# Первое задание

bee = 2 # пчела за одну секонду пролетает два блока
ten = bee * 10 # узнаем сколько блоков пчела пролетит за 10 секунд

print ( ten ) # выводим переменную ten

# Второе задание

mincrafter = 2000  # підписників
doctor = 50  # підписників

print (doctor - mincrafter)

# Третье задание

doctorHto = 5 # получает 5 копейок за каждое просмотренное видео
doctorHto_1000_views = doctorHto * 100 # узнаем сколько получится копейок с 1000 просмотров

print (doctorHto_1000_views)

# Четвертое задание

kate_first_age = 10 # от скольки лет катя начала рисовать картины
kate_last_age = 15 # до скольки лет катя продолжала рисовать картины
picture = 5 * ( kate_first_age - kate_last_age )  # за каждый год катя нарисовала 5 картин

print ( picture )

''' Завдання з підвищеною складністю '''
# 1
firefox = 0.5 # новая вкладка в firefox занимает 0.5 гб
firefox_two = 0.75 # 2 новые вкладки в firefox занимают 0.75
firefox_three = 0.875  # 3 новые вкладки в firefox занимают 0.875

firefox_tabs_gb = firefox + ( firefox_two * 2 ) # узнаем сколько занимает ГБ 5 вкладок

gb = 2

# сверяем gb и firefox_tabs_gb если совпадает то выводим количество вкладок которое можно открыть
if firefox_tabs_gb == gb:
    print ("Мы можем открыть всего 5 вкладок")

# если нельзя открыть 5 вкладок
elif firefox_tabs_gb > gb:
    print("Мы не можем открыть 5 вкладок в FIREFOX")

# 2

print ("Не может открыть 200 вкладок")

# Домашнее задание