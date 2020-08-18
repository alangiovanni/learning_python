# 6.7 - Pessoas
# Pessoa 1
pessoa_0 = {
    'first': 'alan',
    'last': 'targino',
    'age': 24,
}
pessoa_1 = {
    'first': 'thalita',
    'last': 'menezes',
    'age': 21,
}

people = [pessoa_0, pessoa_1]

for pessoa in people:
    for key, value in pessoa.items():
        print(str(key) + ": " + str(value))
    print("\n")

# 6.8 - Animais de estimação
penny = {
    'tipo': 'cachorro',
    'raça': 'shitzu',
    'dono': 'thalita',
}
amora = {
    'tipo': 'cachorro',
    'raça': 'shitzu',
    'dono': 'jailson',
}
jade = {
    'tipo': 'gato',
    'raça': 'desconhecida',
    'dono': 'simone',
}

pets = [penny, amora, jade]

for pet in pets:
    for key, value in pet.items():
        print(str(key) + ": " + str(value))
    print("\n")