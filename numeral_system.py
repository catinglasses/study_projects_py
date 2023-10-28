def convert_to_decimal(num, radix):
    cnv_num = 0
    numeric_storage = [] 
    hex_storage = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    for char in num:
        if char in hex_storage:
            char_num = hex_storage[char]
            numeric_storage.append(char_num)
        else:
            numeric_storage.append(int(char))

    rvrs = list(reversed(numeric_storage))
    for i in range(len(num)):
        cnv_num += rvrs[i] * radix ** i

    return cnv_num

def convert_from_decimal(num, radix):
    cnv_num = ''
    while int(num) != 0:
        cnv_num += str(int(num) % radix)
        num = int(num) // radix

    return cnv_num[::-1]

def convert_dif_numsys(num, radix0, radix1):
    if radix1 == 10:
        return convert_to_decimal(num, radix0)
    else:
        if radix0 == 10:
            return convert_from_decimal(num, radix1)
        else:
            decimal = convert_to_decimal(num, radix0)
            return convert_from_decimal (decimal, radix1)

amount = int(input('Введите сколько чисел Вы хотите перевести в иную систему счисления:  '))

for i in range(amount):
    num = input('Укажите ЧИСЛО, которое Вы хотите перевести в другую систему счисления:  ')
    radix0 = int(input('Укажите ОСНОВАНИЕ системы счисления введеного Вами РАНЕЕ числа:  '))
    radix1 = int(input('Укажите ОСНОВАНИЕ системы счисления, в которую Вы хотите ПЕРЕВЕСТИ число:  '))

    print(f'Число {num} в системе счисления {radix0} - это {convert_dif_numsys(num, radix0, radix1)} в системе счисления {radix1}.', '\n')