from functools import reduce


def fib():
    a, b = 1, 0
    while True:
        yield a
        a, b = b, a + b


my_list = range(0, 11, 5)

#
# fib_generator = fib(10)
#
# i = 0
# while i != 5:
#     i = i + 1
#     print(next(fib_generator))


my_gen = sum(x ** 2 for x in my_list)

print(my_gen)

squares = [k * k for k in range(1, 5)]
print(squares)


def factor_of(num):
    return [k for k in range(1, num + 1) if num % k == 0]


def factorial(num):
    return reduce(lambda x, y: x * y, range(1, num + 1))


