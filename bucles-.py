""" numbers = [1,2,3,4,5,6,7,8,9]

for i in numbers:
    print("Nº:",i)

for i in range (25,50):
    print(i) """

frutas = ["manzana","pera","uva","naranja","tomate"]

for fruta in frutas:
    print(fruta)
    if fruta == "naranja":
        print("Naranja encontrada.")


x = 0

while x < 5:
    if(x == 3):
        break
    print(x)
    x+=1