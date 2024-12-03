#decorador que comprueba si un empleado tiene un rol específico
def check_acces(requiered_role):
    def decorator(func):
        def wrapper(employee):
            #comprobamos si el rol del empleado coincide con el rol requerido
            if employee.get('role') == requiered_role:
                    return func(employee)
            else:
                 print(f'ACCESO DENEGADO. Solo {requiered_role} pueden realizar esta acción.')
        return wrapper
    return decorator

#decorar 
def log_action(func):
     def wrapper(employee):
          print(f'Registrando acción para el empleado {employee['name']}') 
          return func(employee)
     return wrapper
          
     

@check_acces('admin')
@log_action
def delete_employee(employee):
    print(f'El empleado {employee['name']} ha sido eliminado.')



admin = {'name': 'facundo','role' : 'admin'}
employee1 = {'name':'roberto','role':'employee'}


delete_employee(admin)

