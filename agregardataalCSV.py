import csv

#creo el producto
new_product = {
    'name' : 'Wireless charger',
    'price' : 100,
    'quantity': 100,
    'brand' : 'Ugreen',
    'category': 'Accessories',
    'entry_date': '2024-10-7'
}

with open('products.csv',  mode ='a', newline='') as file:
    csv_writter = csv.DictWriter(file,fieldnames=new_product.keys())
    csv_writter.writerow(new_product)
    file.write('\n')


