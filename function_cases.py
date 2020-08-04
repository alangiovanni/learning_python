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


