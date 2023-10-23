# Создание англ и рус алфавитов нижнего регистра
eng_ltrs = [chr(ord('a') + i) for i in range(26)]
rus_ltrs = [chr(ord('а') + i) for i in range(32)]

language_keys = {
    'language': ['английский', 'русский'],
    'max_rot': [25, 31],
    'ltrs': [eng_ltrs, rus_ltrs]
}

print('Здравствуйте! Вас приветствует алгоритм шифровки и дешифровки сообщений по алгоритму Цезаря.')
print()

# Функция шифрования 
def encryption(txt_in, ltrs, rot):
    txt_out = ''
    for char in txt_in:
        if char in ltrs:
            # Вносим в список зашифрованные символы, "избавляемся" от избыточного шага ( % len(ltrs) )
            txt_out += ltrs[(ltrs.index(char) + rot) % len(ltrs)]
        elif char.lower() in ltrs:
            txt_out += ltrs[(ltrs.index(char.lower()) + rot) % len(ltrs)].upper()
        else:
            txt_out += char
    return txt_out

# Функция дешифрования
def decryption(txt_in, ltrs, rot):
    txt_out = ''
    for char in txt_in:
        if char in ltrs:
            # Вносим в список дешифрованные символы, "избавляемся" от избыточного шага ( % len(ltrs) )
            txt_out += ltrs[(ltrs.index(char) - rot) % len(ltrs)]
        elif char.lower() in ltrs:
            txt_out += ltrs[(ltrs.index(char.lower()) - rot) % len(ltrs)].upper()
        else:
            txt_out += char
    return txt_out

def main():
    # False для encryption, True для decryption
    task = bool(input('Нажмите Enter, если хотите зашифровать текст. В противном случае введите любое значение.  '))
    language = int(bool(input('Нажмите Enter для выбора английского алфавита. В противном случае введите любое значение.  ')))

    if task:
        decrypt_menu(language)
    else:
        encrypt_menu(language)

def encrypt_menu(language):
    while True:
        rot = input(f'Введите любое ЦЕЛОЕ число от 1 до {language_keys["max_rot"][language]}. Оно будет означать шаг для шифрования.  ')
        if not rot.isdigit():
            print('Ошибка: введенное значение не является числом.')
            continue    
        else:
            rot = int(rot)
            break
    print()
    txt_input = input(f'Введите текст, который нужно зашифровать. Язык текста должен быть {language_keys["language"][language]}.  ')
    txt_output = encryption(txt_input, language_keys['ltrs'][language], rot)
    print('\n Результат шифрования текста:', txt_output, sep='\n')

def decrypt_menu(language):
    while True:
        rot = input(f'Введите любое ЦЕЛОЕ число от 1 до {language_keys["max_rot"][language]}. '
                    'Оно будет означать шаг для дешифрования. Если шаг неизвестен, нажмите Enter.  ')
        if rot == '':
            break
        elif not rot.isdigit():
            print('Ошибка: введенное значение не является числом.')
            continue
        else:
            break
    print()
    txt_input = input(f'Введите текст, который нужно дешифровать. Язык текста должен быть {language_keys["language"][language]}.  ')
    if rot.isdigit():
        txt_output = decryption(txt_input, language_keys['ltrs'][language], int(rot))
    else:
        for i in range(1, language_keys['max_rot'][language]):
            txt_output = decryption(txt_input, language_keys['ltrs'][language], i)
            print()
            print(f'Возможное закодированное сообщение:  {txt_output}')
            readable = input('Если Вы можете прочитать закодированное сообщение, нажмите Enter. В противном случае введите любое значение.   ')
            if readable == '':
                break
    print('\n Результат дешифрования текста:', txt_output, sep='\n')


main()

# TODO: дописать decrypt_menu в сторону дешифровки без наличия ключа дешифровки: сортировка значений на обработку (?). 
# TODO: Попробовать реализовать шифровку и дешифровку в оба направления, а не только вправо и влево соответственно.
