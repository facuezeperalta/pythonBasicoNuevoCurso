x= 100 #variable global.
def local_function():
    x = 10 #variable local.
    print(f"El valor de la variable es: {x}")


local_function()

def show_global():
    print(f"el valor de la variable global es: {x}")


show_global()
