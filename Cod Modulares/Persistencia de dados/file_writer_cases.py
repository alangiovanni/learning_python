filename = 'c:/Users/alan1/Documentos/GIT/learning_python/Cod Modulares/Persistencia de dados/python_work/file_writer_cases.txt'

# 10.3 - Convidados
print('10.3 - Convidados')
nome = input('Digite o seu nome, caro usuário: ')

with open(filename, 'w') as file_object:
    file_object.write(nome)

# 10.4 - Lista de convidados
print('\n10.4 - Lista de Convidados')
with open(filename, 'a') as file_object:
        file_object.write("\n\nLista de Convidados:")
while True:
    nome = input('Digite o seu nome, caro convidado (quit, para sair): ')
    
    # Condição de parada do While
    if nome == 'quit':
        break

    print('Olá ' + nome + ' seja bem vindo(a)!')
    with open(filename, 'a') as file_object:
        file_object.write("\n" + nome)

# 10.5 - Enquete sobre Programação
print('\n10.5 - Enquete sobre Programação')
with open(filename, 'a') as file_object:
        file_object.write("\n\nEnquete sobre Programacao:")
while True:
    nome = input('Digite o seu nome para responder a enquete (quit, para sair): ')

    # Condição de parada do While
    if nome == 'quit':
        break

    linguagem = input('Olá ' + nome + '! Qual linguagem de programação você mais gosta? ')
    motivo = input('Porque? [Enter se não quiser responder] ')

    if motivo:
        # Criando um dicionário
        enquete = {'nome': nome, 'linguagem': linguagem, 'motivo': motivo}
        with open(filename, 'a') as file_object:
            file_object.write("\n" + str(enquete))