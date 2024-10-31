def log_transaction(func):
    def wrapper():
        print('1 - Log de la transacción...')
        func()
        print('3 - Log terminado...')
    return wrapper




@log_transaction #usamos el decorador.
def process_payment():
    print('Procesando pago...')


process_payment()