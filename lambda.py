add = lambda a,b : a+b

print(add(10,4))

multy = lambda a,b : a*b

print(multy(2,4))

#Cuadrado de cada numero

numbers = range(11)
squared_numbers = list(map(lambda x : x**2,numbers))
print("Cuadrados: ",squared_numbers)

#pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("Numeros pares: ",even_numbers)