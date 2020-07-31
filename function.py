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

# Chamadas das funções acima
greet_user('jesse') # Chamada da função com passagem de argumento
describe_pet('dog', 'penny') # Vários argumentos
describe_pet(pet_name='jurema', animal_type='cat') # Argumentos NOMEADOS, posso alterar a ordem
print("Meu nome: " + format_name('alan', 'targino')) # Uso do return
print("Meu nome: " + format_name('alan', 'targino', 'giovanni')) # Uso do return, o Giovanni é um termo opcional;