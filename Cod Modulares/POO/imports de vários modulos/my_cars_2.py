# Importando um módulo para este módulo
from mod_car2 import Car # Import de um módulo
from mod_eletric_car import EletricCar # Import de outro módulo em outro arquivo

# Carro instanciado através de uma classe modulada;
my_tesla = EletricCar('tesla', 'model s', 2017)
print(my_tesla.get_descriptive_name())