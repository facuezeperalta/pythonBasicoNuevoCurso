""" construyo el decorador """
def log_transaction(func):
    def wrapper():
        print('1- Log de la transacción...')
        """ llamo a la función que tengo como parámetro """
        func() 
        print('3- Log terminado...')
    return wrapper
        


""" hacemos uso del decorador """
@log_transaction 

def process_payment():
    print('2- Procesando pago...')

process_payment()