# 3.4 Lista de Convidados
lista_convidados = ['Weslley', 'Milena', 'Roberto']

message = lista_convidados[0].title() + ", venha a um jantar em minha casa!"
print(message)

message = lista_convidados[1].title() + ", venha a um jantar em minha casa!"
print(message)

message = lista_convidados[2].title() + ", venha a um jantar em minha casa!"
print(message)

# 3.5 Alterando a Lista de Convidados
message = lista_convidados[2].title() + " não poderá vir ao jantar. :(\n"
print(message)

lista_convidados[2]='Gilson'
message = lista_convidados[0].title() + ", venha a um jantar em minha casa!"
print(message)

message = lista_convidados[1].title() + ", venha a um jantar em minha casa!"
print(message)

message = lista_convidados[2].title() + ", venha a um jantar em minha casa!"
print(message)

# 3.6 Mais convidados
print("\nNovos Convidados!")
lista_convidados.insert(0, 'Antony') # Insere no início
lista_convidados.insert(2, 'Jontis') # Insere no meio
lista_convidados.append('Ananda') # Insere no fim

message = lista_convidados[0].title() + ", venha a um jantar em minha casa!"
print(message)

message = lista_convidados[1].title() + ", venha a um jantar em minha casa!"
print(message)

message = lista_convidados[2].title() + ", venha a um jantar em minha casa!"
print(message)
message = lista_convidados[3].title() + ", venha a um jantar em minha casa!"
print(message)

message = lista_convidados[4].title() + ", venha a um jantar em minha casa!"
print(message)

message = lista_convidados[5].title() + ", venha a um jantar em minha casa!"
print(message)

# 3.7 Reduzindo a lista de convidados
message = "\nPrezados, é com grande pesar que informo que apenas duas pessoas poderá vir ao jantar."
print(message)

# -1
popped_convidado = lista_convidados.pop()
message = popped_convidado + ", lamento mas acabei de desconvidar você."
print(message)

# -2
popped_convidado = lista_convidados.pop()
message = popped_convidado + ", lamento mas acabei de desconvidar você."
print(message)

# -3
popped_convidado = lista_convidados.pop()
message = popped_convidado + ", lamento mas acabei de desconvidar você."
print(message)

# -4
popped_convidado = lista_convidados.pop()
message = popped_convidado + ", lamento mas acabei de desconvidar você."
print(message)

# Lista atual
del lista_convidados[0]
del lista_convidados[0]
print(lista_convidados)