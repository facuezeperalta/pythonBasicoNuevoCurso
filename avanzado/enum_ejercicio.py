from enum import Enum

class Order_status(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3

def check_order_status(status: Order_status):
    #Comprueba el estado del pedido y devuelve un mensaje.
    if status == Order_status.PENDING:
        return 'Order is still PENDING.'
    elif status == Order_status.SHIPPED:
        return 'Order has been SHIPPED.'
    elif status == Order_status.DELIVERED:
        return 'Order has been DELIVERED'
    elif status == 1:
        return 'Order is still PENDING.'
    elif status == 2:
        return 'Order Has been SHIPPED'
    elif status == 3:
        return 'Order has been DELIVERED'
    

print(check_order_status(Order_status.DELIVERED))
print(check_order_status(Order_status.SHIPPED))
print(check_order_status(Order_status.PENDING))
print('---Con números---')
print(check_order_status(1))
print(check_order_status(2))
print(check_order_status(3))
