#clase padre o Superclase.
class Vehicle:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehículo {self.brand}. Ha sido vendido.")
        else:
            print(f"El vehículo {self.brand}. NO esta disponible.")
    
    def check_available(self):
        return self.is_available
    
    def get_price(self): #siempre que queremos mostrar el precios o alguna cosa de un objeeto usamos el get
        return self.price

    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")
    
    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")


class Car(Vehicle):
    #polimorfísmo?
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} esta en marcha."
        else:
            return f"El coche con la marca {self.brand} no está disponible."
    def stop_engine(self):          
        if  self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche de la marca {self.brand} no está disponible."

class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta  {self.brand} esta en marcha."
        else:   
            return f"La bicicleta con la marca {self.brand} no está disponible."
    
    def stop_engine(self):          
        if  self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta de la marca {self.brand} no está disponible."

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El camión {self.brand} esta en marcha."
        else:   
            return f"El camión con la marca {self.brand} no está disponible."
    
    def stop_engine(self):          
        if  self.is_available:
            return f"El camión {self.brand} se ha detenido"
        else:
            return f"El camión de la marca {self.brand} no está disponible."

class Costumer:  
    def __init__(self, name):
        self.name = name
        self.purcharsedVehicle = []
    
    def buy_vehicle(self, vehicle:Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purcharsedVehicle.append(vehicle)
        else:
            print(f"Lo siento, el vechiculo {vehicle.brand} no está disponible.")
    
    def inquire_vehicle (self,vehicle:Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "NO Disponible"
        print(f"El vehículo, {vehicle.brand} está {availablity}, \nEl precio:{vehicle.get_price}")
    


class DealerShip():
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self,vehicle:Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand}  ha sido añadido al inventario.")
    
    def register_costumer(self, customer: Costumer):
        self.customers.append(customer)
        print(f"El {customer.name} ha sido añadido.")
    
    def show_available_vehicles(self):
        print("Los vehículos disponibles en la tienda: ")
        for vehicle in self.inventory:
            if  vehicle.check_available:
                print(f"{vehicle.brand} por ${vehicle.get_price()}")


car1=  Car("Ford","Focus",250000)
bike1 = Bike("Volta","Viggo",300)
truck1 = Truck("Scania","FH-2020",900000)

custumer1 = Costumer("Facu")

Shop = DealerShip()

Shop.add_vehicles(car1)
Shop.add_vehicles(bike1)
Shop.add_vehicles(truck1)

#MOstrar los vehículos disponibles
Shop.show_available_vehicles()

#Cliente consulta.
custumer1.buy_vehicle(bike1l)
