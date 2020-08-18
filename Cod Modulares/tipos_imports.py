import modulo.mod_pizza # Necessária usar a notação toda na hora de chamar a função make_pizza
from modulo.mod_pizza import make_pizza # Dessa forma se pode chamar a função pelo nome.
from modulo.mod_pizza import make_pizza as mp # Dessa forma se pode chamar a função pelo nome e atribuo um alias, onde make_pizzz, pode ser chamado por mp;
import modulo.mod_pizza as pizza # Aqui é definido um alias para todo o caminho do modulo

# Chamando a função do import completo
modulo.mod_pizza.make_pizza(2, 'Grande', 'peperoni', 'cheddar', 'bacon')

# Chamando a função pelo nome por causa do import específico
make_pizza(1, 'Pequena', 'chocolate', 'queijo')

# Chamando a função pelo alias
mp(3, 'Média', 'cheddar', 'tomate', 'carne')

# Chamando a função do import completo com o alias
pizza.make_pizza(2, 'Grande', 'peperoni', 'cheddar', 'bacon')