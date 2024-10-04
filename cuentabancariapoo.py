#creamos la cuenta bancaria
class BankAccount:
    #constructor del objeto.
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    #Método para depositar dinero en la cuenta
    def deposit(self,depositAmount):
        if self.is_active:
            self.balance += depositAmount
            print(f"Se ha depositado ${depositAmount} en la cuenta de {self.account_holder}. Saldo actual: ${self.balance}")
        else:
            print("No se ha podido realizar el depósito, cuenta inactiva")
    
    def withdraw (self, withdrawAmount):
        if self.is_active:
            if withdrawAmount <= self.balance:
                self.balance -= withdrawAmount
                print(f"Se ha retirado ${withdrawAmount}. El saldo actual de la cuenta es: ${self.balance}")
            else:
                print(f"El saldo de la cuenta es insuficiente para realizar una extracción. Saldo actual ${self.balance}")
        else:
            print("La cuenta se encuentra inactiva, no es posible realizar extracciones.")
    
    def deactivateAccount(self):
        self.is_active = False
        print("La cuenta ha sido desactivada correctamente.")
    
    def activateAccount(self):
        self.is_active = True
        print("La cuenta ha sido activada correctamente.")

    

account1 = BankAccount("Facu",500)
account2 = BankAccount("Eze",1000)

account1.deposit(500)
account2.deactivateAccount()
account2.deposit(1500)
account2.activateAccount()
account2.deposit(10)



