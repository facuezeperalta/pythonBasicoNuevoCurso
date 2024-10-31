def check_access(func):
    def wrapper(employee):
        #comprobamos el rol de la persona que quiere eliminar.
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print(f'ACCESO DENEGADO {employee['name']}. SOLO LOS ADMINISTADORES PUEDEN ACCEDER. TU ROL ES: {employee['role']}')
    return wrapper




@check_access #llamo a la función para ser ejecutada antes de delete_employee
def delete_employee(employee):
    print(f'El empleado {employee['name']} ha sido eliminado.')


admin = {'name': 'Facu', 'role':'admin'}
empleado = {'name':'Roberto', 'role':'employee'}

delete_employee(admin)
delete_employee(empleado)