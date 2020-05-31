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

# Outro For, aparentemente mais adequado
print("\nGlossário")
for key, value in glossario.items():
    print(key)
    print("\t" + value)