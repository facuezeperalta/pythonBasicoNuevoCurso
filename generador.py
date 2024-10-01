def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

def fibonacci(limit):
    a, b = 0, 1
    while  a < limit:
        yield a
        a, b = b, a+b

for number in fibonacci(10):
    print(number)