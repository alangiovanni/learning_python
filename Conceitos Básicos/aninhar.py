# aninhando três dicionários de alienígenas em uma lista
alien_0 = {
    'color': 'green',
    'points': 5,
}
alien_1 = {
    'color': 'yellow',
    'points': 10,
}
alien_2 = {
    'color': 'red',
    'points': 15,
}

aliens = [alien_0, alien_1, alien_2]

print("\nExemplo de aninhar dicionário em lista")
for alien in aliens:
    print(alien)

# Criando uma frota de 30 alienígenas
# Frota vazia
aliens = []

# Cria 30 alienígenas verdes
for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }
    aliens.append(new_alien)

print("\nNúmero de Aliens Criados: " + str(len(aliens)))
for alien in aliens[:3]:
    print(alien)
print('...')

print("\nAlterando o Alien")
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

print("Exibindo os 5 primeiros: ")
for alien in aliens[:5]:
    print(alien)
print('...')