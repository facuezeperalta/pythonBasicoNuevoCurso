a = [1,2,3,4,5]
b = a
print(a)
print(b)

del a[0]
print(id(a))
print(id(b))

c= a[:] #copio todo el array entero.
print("-----")
print(id(c))

a.append(6)
print("-----")
print(a)
print(b)
print(c)

