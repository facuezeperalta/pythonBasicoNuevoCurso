#importo la librerá de python 
import csv

""" #leer el archivo.
with open('products.csv','r') as file:
    #imprimir lo que tiene el csv
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
 """
#Mostrar información por columnas:
with open('products.csv','r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precios: {row['price']}, Categoria: {row['category']}")

