import json

# Leemos el archivo
with open('products.json', mode='r') as file:
    products = json.load(file)

# Mostrar el contenido del JSON
for product in products:
    print(product)
