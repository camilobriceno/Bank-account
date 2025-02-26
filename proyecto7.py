import random

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def mostrar_cuenta(self):
        print(f"""      
              Name: {self.nombre} 
              Last name: {self.apellido}
              Bank account: {self.numero_cuenta} 
              Balance: {self.balance}€
            """)

    def depositar(self):
        valor_deposito = int(input("Enter the value to be deposited into your account: "))
        self.balance += valor_deposito
        print(f"******** You have entered {valor_deposito}€ ********")
        print(f"Your balance is {self.balance}€")
        return valor_deposito

    def retirar(self):
        valor_retirar = int(input("Amount of money to withdraw: "))
        if self.balance >= valor_retirar:
            self.balance -= valor_retirar
            print(f"******** Withdraw {valor_retirar}€ ******** OK!!!!")
            print(f"Current balance: {self.balance}€")
        else:
            print("You don't have enough funds")


def crear_cliente():
    nombre = input("Enter your name: ")
    apellido = input("Enter your last name: ")
    numero_cuenta = random.randint(100000, 600000)
    balance = 0
    username = Cliente(nombre, apellido, numero_cuenta, balance)
    print("Account created successfully!")
    return username


menu_banco = """
    MENU PRINCIPAL
    
    [0] - Deposit money
    [1] - Withdraw money
    [2] - Exit menu
"""

def inicio():
    print("**** WELCOME TO BANCO CENTRAL****")
    usuario_actual = crear_cliente()

    opc_usuario = input("Press enter to continue...")
    while True and opc_usuario != 2:
        print(menu_banco)
        opc_usuario = int(input("Choose your option: "))
        if opc_usuario !=2:
            match opc_usuario:
                case 0:
                    #print("usuario deposita dinero")
                    usuario_actual.depositar()
                    input("Press enter to return menu")
                case 1:
                    usuario_actual.retirar()
                    input("Press enter to return menu")
                case 2:
                    #print("salir del menu")
                    break
                case default:
                    print("Wrong option, try again")
                    input("Press enter to return menu")

inicio()