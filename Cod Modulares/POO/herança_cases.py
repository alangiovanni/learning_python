# 9.6 - Sorveteria
class Restaurant():
    """Classe que modela um restaurante"""
    def __init__(self, restaurant_name, cuisine_type):
        """Construtor da classe"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("Nome do estabelecimento é " + self.restaurant_name.title() + ".")
        print("O tipo de culinária é " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        print("O estabelecimento " + self.restaurant_name.title() + " está ABERTO!")

class IceStreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos da classe PAI"""
        super().__init__(restaurant_name, cuisine_type)
        # abaixo definimos os atributos específicos dessa sub-classe
        # Uma lista de sabores da sorveteria
        self.flavors = ['morango', 'chocolate', 'coco', 'flocos', 'amendoim', 'sonho de valsa']
    
    def print_flavors(self):
        print('\nSabores disponíveis de sorvete: ')
        for flavor in self.flavors:
            print(flavor)

print('\n9.6 - Sorveteria')
new_sorveteria = IceStreamStand('glacial', 'sorveteria')
new_sorveteria.describe_restaurant()
new_sorveteria.open_restaurant()
new_sorveteria.print_flavors()

#9.7 - Admin
class User():
    """Modela um usuário do sistema"""
    def __init__(self, name, login, password):
        """Construtor do Perfil"""
        self.name = name
        self.login = login
        self.password = password
        self.login_attemps = 0
    
    def describe_profile(self):
        """Printa a descrição do Usuário"""
        print("Nome do usuário: " + self.name.title())
        print("Login: " + self.login)
        print("Password: " + self.password)
        print("Logins realizados na plataforma: " + str(self.login_attemps))

class Admin(User):
    def __init__(self, name, login, password):
        """Inicializa os atributos da classe PAI"""
        super().__init__(name, login, password)
        # abaixo definimos os atributos específicos dessa sub-classe
        self.privileges=['can add post', 'can delete', 'can ban user']
    def show_privileges(self):
        print('\nPrivileges: ')
        for privilege in self.privileges:
            print(privilege)

print('\n9.7 - Admin')
new_admin = Admin('alan', 'alan.targino', '123qweasd')
new_admin.describe_profile()
new_admin.show_privileges()

# 9.9 - Upgrade Battery
class Car():
    """Uma classe que modela o carro"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def get_descriptive_name(self):
        """Devolve um descritivo do nome, formatado de modo elegante"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

class EletricCar(Car):
    """Classe herdada de Car, mostra aspectos específicos do Carro elétrico"""
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe PAI"""
        super().__init__(make, model, year)
        # abaixo definimos os atributos específicos dessa sub-classe
        self.battery = Battery() # Esse atributo é um objeto da classe Battery
    
    # Métodos da sub-classe aqui abaixo

class Battery():
    """Classe que modela a bateria do carro elétrico"""
    def __init__(self, battery_size=70):
        """Construtor"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidada da bateria"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com o nível de carga da bateria atual"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range) + " kilometers on a full charge"
        print(message)
    
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
            print("Battery Upgraded!")
        else:
            print("Nothing to be done...")
print('\n9.9 - Upgrade Battery Eletric Car')
my_tesla = EletricCar('tesla', 'model s', 2017)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()