#
#   Урок №4. Функции и работа с ними
#

# Пример простой функции
def sum_ab(a, b):
    return a + b


# еще пример
def hwh(n):
    if n > 100:
        return "n больше 100"
    else:
        return "n меньше 100"


# Мы можем их использовать где и сколько захотим
print("3 + 4 = ", sum_ab(3, 4))
print("542 + 929 = ", sum_ab(542, 929))
hwh(4)
hwh(120)


#
# Факториал числа это умножение всех чисел
#  от 1 до самого числа
#  Например: 5! = 1*2*3*4*5 = 120
#

def func_fact_while(n):
    res = 1
    while n > 1:
        res = res * n
        n = n - 1
    return res


def func_fact(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res


# Мы можем возвращать функцию из функции
# Это называется 'Рекурсией'
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

ы
print(fact(6))
