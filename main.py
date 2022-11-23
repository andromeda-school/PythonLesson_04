
# 2 3 5 7 11 13 17 19
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# 5! = 1 * 2 * 3 * 4 * 5 = 120
def fact2(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    print(f"{n}! = {res}")

# 43(10) => 101011(2)
def binary(n):
    tmp_n = n
    result = ""
    while n > 0:
        # print(f"{n} (Остаток: {n%2})")
        result = str(n%2) + result
        n = n // 2
    print(f"{tmp_n}(10) => {result}(2)")


def fact(n):
    if n == 1:
        return n
    else:
        print(f"Тронули {n}!")
        return n * fact(n-1)

fact(5)
# fact(365)

# binary(32442)

# for num in range(2, 1000001):
#     if is_prime(num):
#         print(f"Простое число: {num}")





