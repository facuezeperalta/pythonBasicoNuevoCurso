"""
1- Recibirá una lista de diccionarios. Cada diccinoario tendrá las claves: 'Nombre', 'edad' y 'Sueldo'
2- Debe devolver una lista de empleados que ganen mas  de cierto valor.
"""
empleados = [
   
    {
        "nombre": "Facundo",
        "edad" : 29,
        "sueldo": 900
    },
    {
        "nombre" : "Roberto",
        "edad" : 30,
        "sueldo" : 1200
    },
    {
        "nombre" : "Juan",
        "edad" : 45,
        "sueldo" : 2000
    },
    {
        "nombre" : "Sofia",
        "edad" : 18,
        "sueldo" : 900
    }

]

def filtrar_empleados( empleados : list, limite_salario : float) -> list:
   lista_filtrada = [empleado for empleado in empleados if empleado['sueldo'] >= limite_salario]
   return lista_filtrada


print(filtrar_empleados(empleados,1000)) 



    