 #función que suma dos numeros.
def add(a,b):
    return a+b

#función que resta dos numeros.
def substract(a,b): 
    return a-b

#funcion que multiplica dos numeros.
def multiply(a,b):
    return a*b

#funcion que divide dos numeros.
def divide(a,b):
    if b == 0:
        raise ValueError('No se puede dividir por 0')
    return a / b


if __name__ == "__main__":
    print('Operaciones: ')
    res_1= add(3,4)
    print(f'Suma: {res_1}')
    res_2 = substract(10,5)
    print(f'Resta: {res_2}')
    res_3 = divide(10,2)
    print(f'División: {res_3}')




