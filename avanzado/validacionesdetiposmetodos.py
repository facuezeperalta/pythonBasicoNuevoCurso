def divide (a: int, b: int):
    #validamos que ambos sean int
    if not isinstance(a,int) or not isinstance(b,int):
        print("Error: Ambos valores deben ser enteros o float")
        return None
    #verificamos que el divisor no sea 0
    if b == 0:
        print("Error: El divisor no puede ser 0")
    return a/b


