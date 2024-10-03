def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

facotorial_5 = factorial(5)
print(facotorial_5)
factorial_30 = factorial(30)
print(factorial_30)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print("--------")
number_zero = 0
numbero_one = 1
number = 3
print(fibonacci(number_zero))
print(fibonacci(numbero_one))
print(fibonacci(number))
