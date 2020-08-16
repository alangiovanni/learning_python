# 8.3 Camisetas
def make_shirt(shirt_size, shirt_msg):
    print("\nNova Camisa!!")
    print("O tamanho da camiseta é " + shirt_size.upper() + ".\nA mensagem da camisa é " + shirt_msg + ".")

def make_shirt_default(shirt_size='G', shirt_msg='Eu amo Python'):
    print("\nNova Camisa!!")
    print("O tamanho da camiseta é " + shirt_size.upper() + ".\nA mensagem da camisa é " + shirt_msg + ".")
# Tipos de Argumento
make_shirt('m', "Argumento Posicional") # Posicional
make_shirt(shirt_msg="Argumento Nomeado", shirt_size='p') # Nomeado

# 8.4 - Criando camisetas com informações default
make_shirt_default()
make_shirt_default(shirt_msg='Essa é default Modificada')
make_shirt_default('M')

# Criando Trigger Zabbix
def create_trigger(name_trigger, formula, key, delay='30s', unit='', description=''):
    """Cria uma requisição para a API zabbix create.trigger"""
    trigger = {'name': name_trigger, 'form': formula, 'key': key, 'delay': delay}
    if unit:
        trigger['unit'] = unit
    elif description:
        trigger['description'] = description
    
    return trigger

# chamada a trigger
retorno_trigger = create_trigger('Indisponibilidade VPN', 'item.last()=1', 'key-qualquer', description='Trigger de indisponibilidade da VPN')
print(retorno_trigger)

# 8.12 - Sanduiches
def make_sanduiche(*toppings):
    """Faz um sanduiche"""
    print("\nO seu sanduiche possui os seguintes ingredientes: ")
    for topping in toppings:
        print(topping)

# Criando sanduiches
make_sanduiche('queijo', 'presunto')
make_sanduiche('queijo', 'presunto', 'bacon')
make_sanduiche('queijo', 'presunto', 'bacon', 'ovos')

# 8.13 - Perfil do Usuário
def build_profile(first_name, last_name, **user_info):
    """Constrói um dicionário contendo tudo que se sabe sobre um usuário"""
    print('\nBuildando um perfil de usuário')
    profile = {}
    profile['first_name'] = first_name.title()
    profile['last_name'] = last_name.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Chamada da função para criar um perfil de usuário
user_profile = build_profile('alan', 'targino', location='brazil', field='IT', company='Conductor')
print(user_profile)


