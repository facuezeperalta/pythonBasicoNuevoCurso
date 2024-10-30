class Employee:
    name: str
    age: int
    salary: float
    def __init__(self, name:str, age: int, salary: float): #constructor
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:
        return f"Hola me llamo {self.name} y tengo {self.age} años."
    
    def report_salary(self) -> str:
        return f"Hola me llamo {self.name}, tengo {self.age} y gano {self.salary} por mes."

empleado = Employee('Carlos', 20, 3500.00)

print(empleado.introduce())
print(empleado.report_salary())
        
    
