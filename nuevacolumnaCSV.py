import csv

file_path = 'products.csv'
updated_file_path = 'products_updated.csv'

#leer el archivo para copiar al nuevo csv
with open(file_path,mode='r') as file:
    csv_reader = csv.DictReader(file)
    #obtener los nombres de las columnas existentes.
    fieldNames = csv_reader.fieldnames + ['total_value']

    with open(updated_file_path, mode = 'w', newline='') as updated_file:
        csv_writter = csv.DictWriter(updated_file, fieldnames= fieldNames)
        csv_writter.writeheader() #Escribir los encabezados de información.
        
        for row in csv_reader: 
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writter.writerow(row)
            
 


