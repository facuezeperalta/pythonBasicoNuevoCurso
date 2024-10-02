""" def greeting(name):
    print(f"hola, {name}")


greeting("facu") """

def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    while True:
        print("Selecciones una operación: ")
        print("1. Suma")
        print("2. Resta")
        print("3. Division")
        print("4. Multiplicacion")
        print("0. Exit")

        option = int(input("Ingrese una opción (1,2,3,4,0): "))

        if option == 0:
          print("Saliendo de la calculadora")
        
        if option in [1,2,3,4]:
            num1 = float("Ingresa un número: ")
            num2 = float("Ingresa el segundo numero: ")
            


