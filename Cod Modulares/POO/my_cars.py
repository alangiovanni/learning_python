from modulo.mod_car import Car, EletricCar # Importando algumas classes
# from modulo.mod_car import * # Importando todas as classes [Não Recomendado]

# Carro instanciado através de uma classe modulada;
my_new_car = Car('renault', 'sandero', 2017)
print(my_new_car.get_descriptive_name())

#Linha em branco
print("")

# Carro instanciado através de uma classe modulada;
my_tesla = EletricCar('tesla', 'model s', 2017)
print(my_tesla.get_descriptive_name())