# 6.1 - Pessoas
pessoa = {
    'first_name': 'alan',
    'last_name': 'targino',
    'age': 24,
    'city': 'joão pessoa',
}
print(pessoa)

# 6.2 - Números Favoritos
numbers = {
    'alan': 18,
    'thalita': 18,
    'mariselia': 30,
    'benedito': 40,
}
print(numbers)

# 6.3 - Glossário
glossario = {
    'for': 'Estrutura de laço de repetição',
    'if-else': 'Estrutura para tomada de decisão',
    'tupla': 'Estrutura que guarda valores imutáveis',
    'pep 8': 'Guia de Estilo na linguagem, refere-se a boas práticas durante a codificação',
    'dicionario': 'Estrutura chave-valor, similar a JSON',
}

print("\nGlossário")
for palavra in glossario:
    print(palavra + ": " + str(glossario[palavra]) + "\n")

# 6.4 - Glossário 2
# Adicionando novos termos ao glossário (dicionário)
glossario['list']='Lista é uma cadeira de informações acessadas por índices'
glossario['list comprehesions']='É uma forma de resumir ainda mais o código em Python, é possível criar um for e armazenar o resultado em uma variável utilizando apenas uma linha'

# Outro For mais adequado - Deve mostrar os novos termos adicionados
print("\nGlossário")
for key, value in glossario.items():
    print(key)
    print("\t" + value)

# 6.5 - Rios
rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'são francisco': 'brasil',
}

for rio, pais in rios.items():
    message="O rio " + str(rio).title() + " corre pelo " + str(pais).title() + "."
    print(message)

for rio in rios.keys():
    message="Rio: " + str(rio).title()
    print(message)

for pais in set(rios.values()):
    message="País: " + str(pais).title()
    print(message)

# 6.6 - Enquete
favorite_languages = {
    'alan': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python', # Colocar vírgula sempre no fim de cada linha, mesmo quando estiver terminado, é uma boa prática.
}

list_pessoas = ['alan', 'antony', 'thalita', 'edward']

for pessoa in list_pessoas:
    if pessoa in favorite_languages.keys():
        message="Obrigado por responder, " + pessoa
    else:
        message="Olá " + pessoa + ", vamos responder seu questionário agora?"
    print(message)
