# Импорт библиотек
import random

# Функция для запроса числа на ввод; автоматическая проверка является ли введенное значение числом.
def request_num(instruction):
    while True:
        num = input(instruction)

        if not num.isdigit():
            print('Ошибка: введенное значение не является числом.')
            return int(input('\n Введите новое число:  '))
        else:
            num = int(num)
            break
        
    return num

# Функция для создания списка допустимых символов для генерации паролей
def generate_char_list(incl_digits = False, incl_lwr = False, incl_uppr = False, incl_symb = False, incl_unclear = True):

# Создание списков со значениями по категориям: цифры, буквы нижнего регистра, буквы верхнего регистра, знаки препинания
    numbers = [chr(i) for i in range(48, 58)]
    lwr_letters = [chr(i) for i in range(97, 123)]
    uppr_letters = [chr(i) for i in range(65, 91)]

    symbols = [chr(i) for i in range (33, 48)] + \
    [chr(i) for i in range (58, 65)] + \
    [chr(i) for i in range (91, 97)] + \
    [chr(i) for i in range (123, 127)]

# Ввод допустимых символов для дальнейшей генерации пароля. Удаление "ненужных" символов
    chars = []
    if incl_digits:
        chars.extend(numbers)
    if incl_lwr:
        chars.extend(lwr_letters)
    if incl_uppr:
        chars.extend(uppr_letters)
    if incl_symb:
        chars.extend(symbols)

    if not incl_unclear:
        to_remove = ['1', '0', 'i', 'l', 'o', 'L', 'O']
        chars = [element for element in chars if element not in to_remove]

    return chars

# Функция для генерации паролей по заданным параметрам
def gen_password(gen_amount, psw_len, incl_digits = False, incl_lwr = False, icnl_uppr = False, incl_symb = False, incl_unclear = True):
    chars = generate_char_list(incl_digits, incl_lwr, incl_uppr, incl_symb, incl_unclear)

    for i in range(gen_amount):
        print(f'Пароль №{i + 1}:  ', ''.join(random.choice(chars) for _ in range(psw_len)))

gen_amount = request_num('Введите количество паролей (целое число), которые Вы хотите получить в результате генерации:  ')
psw_len = request_num('Введите длину генерируемых паролей (целое число):  ')

incl_digits = bool(input('Нажмите на любую клавишу + Enter, если пароли должны содержать ЦИФРЫ. В противном случае нажмите Enter:  '))
incl_lwr = bool(input('Нажмите на любую клавишу + Enter, если пароли должны содержать БУКВЫ НИЖНЕГО РЕГИСТРА. В противном случае нажмите Enter:  '))
incl_uppr = bool(input('Нажмите на любую клавишу + Enter, если пароли должны содержать БУКВЫ ВЕРХНЕГО РЕГИСТРА. В противном случае нажмите Enter:  '))
incl_symb = bool(input('Нажмите на любую клавишу + Enter, если пароли должны содержать СИМВОЛЫ ПУНКТУАЦИИ. В противном случае нажмите Enter:  '))

# Подразумеваются следующие символы: il1Lo0O
incl_unclear = bool(input('Нажмите на любую клавишу + Enter, если пароли должны содержать ПУТАЮЩИЕСЯ СИМВОЛЫ. В противном случае нажмите Enter:  '))

print()
gen_password(gen_amount, psw_len, incl_digits, incl_lwr, incl_uppr, incl_symb, incl_unclear)