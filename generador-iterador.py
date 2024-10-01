""" #ejemplo iterador.

#crear un lista.
my_list = [1,2,3,4]

#obtener iterador
my_iter = iter(my_list)

#usar el iterador:

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

 """
#iterar en cadenas 
#creamos la cadena
mytext = "Hola mundo"
#creamos objeto iterador.

iter_text = iter(mytext)

#iteramos la cadena.
for char in iter_text:
    print(char)


#creamos un iterador para los números impares

limit = 10

odd_numbers = iter(range(1,limit+1,2))

for num in odd_numbers:
    print(num)

