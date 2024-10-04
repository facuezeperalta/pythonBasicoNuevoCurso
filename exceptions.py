try:
    divisor = int(input("ingresa un numero divisor: "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e:
    print("El divisor no puede ser 0")
    print("Nombre del error: ", e)
except ValueError:
    print("Debes ingresar un número!")
   



#Arbol de excepciones:
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)