squares = [x ** 2 for x in range(1,11)]
#print("Los cuadrados son: ", squares)

celcius = [0,10,20,30,40,50]
fahrenheit = [(9/5 * t) +32 for t in celcius]
#print("temperatura en Fahrenheit: ", fahrenheit)

#Numeros pares
evens = [x for x in range(1,21) if x % 2 == 0]
print("Números pares: ", evens)
unevens = [x for x in range (1,21) if x % 2 != 0]
print("Números impares: ", unevens)