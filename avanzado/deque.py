from collections import deque

def manage_delivery_queue() -> deque:
    #crea una cola  para gestionar entregas de productos
    delivery_que = deque(['Order_1','Order_2','Order_3'])
    delivery_que.append('Order_4') #agrega una orden al final de la cola.
    delivery_que.appendleft('Order_0') #agrega una orden al comienzo de la lista.
    delivery_que.pop() #borra el último elemento.
    delivery_que.popleft() #borra el primer elemento de la izquierda.
    return delivery_que #devuelvo las ordenes.

print(manage_delivery_queue())