def check_acces(func):
    def wrapper(employee): #recibo el empleado.
        #comprobamos el rol de la persona que tiene que eliminar y DEBE ser admin.
        if employee.get('role') == 'admin': #comparo el rol
            return func(employee) #devuelvo el empleado.
        else: 
            print(f'ACCESO DENEGADO: No es administrador, solo los admins puedne acceder') #en el caso de que no se cumple la condición mostramos el mensaje.
    return wrapper
        
@check_acces
def delete_employee(employee):
    print(f'el empleado {employee['name']} ha sido eliminado.')

admin = {'name' : 'Carlos', 'role' : 'admin',}
employee1 = {'name' : 'Roberto', 'role' : 'employee'}

delete_employee(admin)
delete_employee(employee1)


