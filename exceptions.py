try:
    divisor = int(input("ingresa un numero divisor: "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError:
    print("El divisor no puede ser 0")
except ValueError:
    print("Debes ingresar un número!")
   
