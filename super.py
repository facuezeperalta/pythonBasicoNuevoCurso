class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet():
        print("Hola soy una persona!")

class Student: 
     def __init__(self,name,age,student_id):
         super().__init__(name,age) #hago referencia a los atributos de la clase padre.
         self.student_id = student_id

