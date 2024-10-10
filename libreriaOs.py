import os

#obtener el directorio actual
""" cwd = os.getcwd()
print(f"Direcctorio de trabajo actual: {cwd}") """

#Listar los archivos txt.
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Los archivos txt son: ",txt_files)

#cambiar el nombre de un archivo.
os.rename('caperucita.txt','Cuento - caperucita.txt')
print("Archivo renombrado correctamente.")

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Los archivos txt son: ",txt_files)



