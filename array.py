# Declarando uma nova lista/array
nomes = ['Antony', 'Neemias', 'Rodrigo', 'Marx']

# Printando um a um cada elemento
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])

# Editar a posição 3 do array
nomes[3] = 'Cayo'

# Inserção de um novo elemento no FINAL da lista
nomes.append('Marx')
print(nomes)

# Declarando uma nova lista/array
sobrenomes = []
sobrenomes.append('Batista')
sobrenomes.append('Adriel')
sobrenomes.append('Otniel')
sobrenomes.append('Menezes')
sobrenomes.append('Wendell')

# Printando as listas
print(nomes)
print(sobrenomes)

# Inserção de um novo item no INÍCIO da lista
nomes.insert(0, 'Alan')
sobrenomes.insert(0, 'Giovanni')

# Printando as listas
print(nomes)
print(sobrenomes)

# POP
print("\nMétodo POP")
# Numa estrutura de Pilha, retira o último a entrar.
popped_nome = nomes.pop() # Aqui retiro o elemento do nomes e atribuo ao popped_nomes quem saiu.
print(nomes)
print(popped_nome)

# Retirando o primeiro item da lista
popped_sobrenome = sobrenomes.pop(0)
print(sobrenomes)
print(popped_sobrenome)

# REMOVE
print("\nMétodo Remove")
nomes.remove('Alan')
sobrenomes.remove('Wendell')
print(nomes)
print(sobrenomes)