def calculate_average(numbers):
    """
    Calcula el promedio  de una lista de números
    Parámetros: Numbers (tipo lista): puede ser númoeros enteros o números flotantes
    retorna: float: y este es el promedio de números en la lista.
    """
    return sum(numbers) / len(numbers)

#Imprimimos el resultado de la función.
print(calculate_average([1,2,3,4,5]))

