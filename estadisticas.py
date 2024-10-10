#importo la librería de estadísticas de venta
import statistics
import csv

#leer los datos del archivo csv, ventas mensuales.
monthly_sales = {}
print(monthly_sales)
with open ('monthly_sales.csv',mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

#guardo en la variable sales en formato de lista los valores del diccionario monthly_sales
sales = list(monthly_sales.values()) 
#print(sales)       

#hallar la media
mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

#hallar la mediana.
median_sales = statistics.median(sales)
print(f"La mediana de las ventas es: {median_sales}")

#hallar la moda 
mode_sales = statistics.mode(sales)
print(f"La moda de las ventas es: {mode_sales}")

#Hallar la desviación estandar.
standar_deviation_sales = statistics.stdev(sales)
print(f"La desviación estándar es: {standar_deviation_sales}")

#Hallar la varianza
varinace_sales = statistics.variance(sales)
print(f"La varianza es: {varinace_sales} ")

#Hallar un maximo de ventas:
max_sales = max(sales)
print(f"El máximo de ventas: {max_sales}")

#Hallar un minimo de ventas:
min_sales = min(sales)
print(f"El mínimo de ventas: {min_sales} ")

#Hallar el máximo de ventas 
max_sales = max(sales)
print(f"El máximo de ventas: {max_sales}")

#Rango de las ventas
range_sales = max_sales - min_sales
print(f"El rango de ventas es: {range_sales}")


