from mod_car2 import Car

class Battery():
    """Módulo da Classe que modela a bateria do carro elétrico"""
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

class EletricCar(Car):
    """Classe herdada de Car, mostra aspectos específicos do Carro elétrico"""
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe PAI"""
        super().__init__(make, model, year)
        # abaixo definimos os atributos específicos dessa sub-classe
        self.battery = Battery() # Esse atributo é um objeto da classe Battery
        
    # Métodos da sub-classe aqui abaixo