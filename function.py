def greet_user(username): # Def informa ao Python que temos uma função, username é o parâmetro;
    """Exibe uma saudação simples""" # Este é um comentário para documentação. Isto é uma docstring
    print("Hello " + username.title() + "!") # Única linha de código dessa função

# Vários argumentos
def describe_pet(animal_type, pet_name):
    """Exibe informações sobre o animal de estimação"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Uso do return
def format_name(first_name, last_name, middle_name=''):
    """Devolve um nome completo formatado de modo elegante"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    
    return full_name.title()

# Return um dicionário
def build_person(first_name, last_name, age=''):
    """Devolve um dicionário com informações sobre uma pessoa"""
    person = {'first': first_name, 'last': last_name}
    
    # Se for passado a idade
    if age:
        person['age'] = age
    
    return person

# Aceitando vários argumentos sem saber ao certo a quantidade
# um único asterisco no paramêtro faz Python criar uma tupla vazia e coloca todos os argumentos recebidos.
def make_pizza(*toppings):
    """Exibe uma lista de ingredientes pedidos na pizza"""
    # print(toppings) #aqui mostra o formato da Tupla
    print("\nFazendo uma pizza com os seguintes ingredientes: ")
    for topping in toppings:
        print(topping)

def make_pizza_combo(qtde_pizza, size, *toppings):
    """Exibe uma lista de ingredientes pedidos na pizza, a quantidade e o tamanho"""
    print('\nFoi escolhido ' + str(qtde_pizza) + ' pizzas de tamanho ' + size + '.')
    print("Segue os ingredientes: ")
    for topping in toppings:
        print(topping)

# asterisco duplo cria um dicionário vazio e coloca todos os argumentos que será recebido ali
def build_profile(first_name, last_name, **user_info):
    """Constrói um dicionário contendo tudo que se sabe sobre um usuário"""
    print('\nBuildando um perfil de usuário')
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Chamadas das funções acima
greet_user('jesse') # Chamada da função com passagem de argumento
describe_pet('dog', 'penny') # Vários argumentos
describe_pet(pet_name='jurema', animal_type='cat') # Argumentos NOMEADOS, posso alterar a ordem
print("Meu nome: " + format_name('alan', 'targino')) # Uso do return
print("Meu nome: " + format_name('alan', 'targino', 'giovanni')) # Uso do return, o Giovanni é um termo opcional;

# Dicionário
pessoa=build_person('Alan', 'Targino')
print(pessoa)

# Quando a função não tem a quantidade de paramêtros definido
make_pizza('Cream Cheese')
make_pizza('peperoni', 'cheddar', 'bacon')
make_pizza_combo(2, 'Grande', 'peperoni', 'cheddar', 'bacon')

# Criando um dicionário com várias informações de um usuário
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

user_profile = build_profile('alan', 'targino', location='paraiba', field='ti', company='conductor')
print(user_profile)