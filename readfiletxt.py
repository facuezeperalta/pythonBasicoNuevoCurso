#Leer un archivo linea por linea. con strip para eliminar espacios y saltos de línea
""" with open('caperucita.txt','r') as file:
    for lineas in file:
        print(lineas) #.strip() borra salto de lineas. """

""" #leer todas las líneas pero en una lista.
with open('caperucita.txt','r') as file:
    lines = file.readlines()
    print(lines) """

""" #añadir texto al final del archivo
with open('caperucita.txt','a') as file:
    file.write('\n \n El fin? ') """

""" #sobreescribir el texto.
with open('caperucita.txt','w') as file:
    file.write("\n \n esto fue con write.") #Al usar este método sobreescribimos todo lo que estaba en el archivo quedando solo la línea.
    #cuidado con este método.
 """
#contar la cantidad de líneas que tiene el archivo
with open('caperucita.txt','r') as file:
    lines = file.readlines()
    print(lines)
    print("------")
    print("cantidad de lineas del archivo: ", len(lines))