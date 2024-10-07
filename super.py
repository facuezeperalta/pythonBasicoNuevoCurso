class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
<<<<<<< HEAD
    def greet(self):
        print("Hola soy una persona!")

class Student(Person): 
    def __init__(self,name,age,student_id):
        super().__init__(name,age) #hago referencia a los atributos de la clase padre.
        self.student_id = student_id
     
    def greet(self):
        super().greet()
        print(f"Hola! mi id de estudiante es {self.student_id}")    
    

studen1 = Student("Ana",20,"S123")   

studen1.greet()

=======
    def greet():
        print("Hola soy una persona!")

class Student: 
     def __init__(self,name,age,student_id):
         super().__init__(name,age) #hago referencia a los atributos de la clase padre.
         self.student_id = student_id
>>>>>>> 315c547d9c80d5c990252c4ce593f85586613f53

