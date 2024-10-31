from collections import Counter

def count_products(products: list[str]) -> Counter:
    #Usamos counter para contar cuantos productos de cada tipo de han vendido.
    return Counter(products)

sales = ['Celular','GPU','CPU','GPU','Celular','GPU','Pasta termica']

result = count_products(sales)

print(result)

