# 9.10 - Importando Restaurante
from modulo.mod_restaurant import Restaurant
new_restaurant = Restaurant('dogão063', 'brasileira')
# Chamada de um método
# new_restaurant.describe_restaurant()

# 9.13 - Rescrevendo o programa com OrderedDict
from collections import OrderedDict
favorite_languages = OrderedDict() # Dessa forma instancio um dicionário mantendo o controle da ordem de inserção
# favorite_languages = {} # Instanciando um dicionário sem controle de ordem de inserção.
# Linguages favoritas - Dicionário
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'

# Percorrendo um dicionário adequadamente
for key, value in favorite_languages.items():
    print(key + ": " + value)

# 9.14 - Dados
from random import randint
class Die():
    def __init__(self):
        # Atributos
        self.sides = 6
    
    # Métodos
    def roll_dies(self):
        number = randint(1, self.sides)
        print(str(number))

dado = Die()

for qtde in range(1,11):
    dado.roll_dies()