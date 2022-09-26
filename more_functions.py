
#
#   Создадим программу перевода в двоичную систему
#    И добавим функцию в функцию
#

def func_binary(num):
    result = ""
    while num >= 2:
        calc2 = num % 2
        result += str(calc2)       # result = result + calc2
        print("Отчет : num = ", num)
        print("      : result = ", result)
        num = num // 2

    result += str(num)
    return result[::-1]


def func_profi_binary(num):
    result = ""
    while num > 0:
        result = str(num%2) + result
        num //= 2
    return result

def cipher_binary(bi_res):
    # какой-нибудь алгоритм шифрования
    return bi_res[:len(bi_res) // 2]  # выводит только половину результата


#
#   Попробуем наши функции в деле
#    26 = bin(11010)
#

num = int(input("Введите число: "))
bi_res = func_profi_binary(num)
print(bi_res)

print("\nРЕЗУЛЬТАТ деления : ", func_binary(num))

# Мы передаем функции шифрования другую функцию.
# В итоге получается, что они работают вместе.
print("\nРЕЗУЛЬТАТ шифр: ", cipher_binary(func_binary(num)))




