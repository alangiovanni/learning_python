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

    def read_odometer(self):
        """Exibe uma frase que mostra a kilometragem do carro"""
        print("This car has " + str(self.odometer) + " kilometers on it.")
    
    def update_odometer(self, km):
        """Define um novo valor de leitura do hodômetro com o valor especificado"""
        if km >= self.odometer:
            self.odometer = km
        else:
            print("You can't rool back an odometer!")
    
    def increment_odometer(self, km):
        """Soma o valor do hodômetro com o valor especificado"""
        if km > 0:
            self.odometer += km
        else:
            print("You can't lower the odometer.")

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

my_tesla = EletricCar('tesla', 'model s', 2017)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()