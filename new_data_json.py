import json

file_path = 'products.json'

new_product = {
    "name" : "Wireless Chargar",
    "Price": 75,
    "quantity" : 30,
    "brand": "Ugreen",
    "category" : "Accessories",
    "entry_date": "2024-10-07"
}

with open(file_path,mode='r') as file:
    products = json.load(file)

#agrego el prodcuto a la variable product
products.append(new_product)

with open(file_path, mode = 'w') as file:
    json.dump(products,file, indent=4)
