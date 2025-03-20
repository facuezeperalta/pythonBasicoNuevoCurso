class Person:
    def __init__(self, name,age, is_working):
        self.name= name
        self.age = age
        self.is_working = is_working
    
    def get_data_person(self):
        return[
            {
                'name': self.name,
                'age': self.age,
                'isWorking': self.is_working
            }
        ]
    
