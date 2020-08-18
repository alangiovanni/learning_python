# Criando um dicionário com duas chaves
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# Adicionando novas chaves ao dicionário
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Movendo Alienígena
alien_0['speed'] = 'slow'
print("Original x-position: " + str(alien_0['x_position']))

# Move o alienígena para a direita
# Determina a que distância deve mover com base na sua velocidade
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Passou do Slow e do Medium. Este deve ser o fast (The Flash)
    x_increment = 3
# A nova posição do alien
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("Novo x-position: " + str(alien_0['x_position']))
# Apagando uma chave-valor do dicionário - Permanentemente
del alien_0['points']
print(alien_0)

# Um dicionário novo criado com o intuíto de armazenar o resultado de uma pesquisa
# Linguages favoritas
favorite_languages = {
    'alan': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python', # Colocar vírgula sempre no fim de cada linha, mesmo quando estiver terminado, é uma boa prática.
}
print(favorite_languages)

# Percorrendo um dicionário adequadamente
for key, value in favorite_languages.items():
    print(key + ": " + value)

# Percorrendo um dicionário retornando apenas as keys
for key in favorite_languages.keys(): # Código mais fácil de ler
    print(key)

#for key in favorite_languages: # Mesma coisa do For acima
#    print(key)

# Percorrendo um dicionário retornando apenas os values
for value in favorite_languages.values():
    print(value)

# Comparando uma lista com um dicionário; Caso encontrei a key na lista de amigos eu printo
friends = ['alan', 'edward']
for name in favorite_languages.keys():
    if name in friends:
        print("Olá " + name + ", sua linguagem favorita é: " + favorite_languages[name].title() + "!")

print(favorite_languages.keys())

# Uso da função set para retornar itens únicos e uso do método values para retornar apenas os valores do dicionário.
print("Uso da função set abaixo")
for language in set(favorite_languages.values()): 
    print(language.title())