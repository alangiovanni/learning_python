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

