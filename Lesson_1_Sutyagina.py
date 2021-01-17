# 1. Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

from math import factorial
# все крести
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


print(combinations(13, 4))
print(combinations(52, 4))

P = combinations(13, 4)/combinations(52, 4)
print(P)
print()

# один туз
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


print(combinations(48, 4))
print(combinations(52, 4))

P = 1 - combinations(48, 4)/combinations(52, 4)
print(P)
print()

# 2.На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно.
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

print(combinations(10, 3))

m = 1
P = m/combinations(10, 3)
print(P)
print()

# 3. В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

print(combinations(9, 3))
print(combinations(15, 3))


P = (combinations(9, 3)/combinations(15, 3))
print(P)
print()

# 4.В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

print(combinations(100, 2))

P = combinations(98, 2)/combinations(100, 2)
print(P)