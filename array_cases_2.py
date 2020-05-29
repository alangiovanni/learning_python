# 4.10 - Fatias
itens=['espelho', 'elefante', 'maça', 'tv', 'salto', 'girafa', 'garfo', 'dvd', 'copo']

print("Os Três primeiros itens da minha lista são: ")
for item in itens[:3]:
    print(item)
print("Os três itens do meio da lista são:")
for item in itens[3:6]:
    print(item)
print("Os três últimos itens da lista são:")
for item in itens[-3:]:
    print(item)

# 4.11 - Minhas Pizzas, Suas pizzas
my_pizzas=['napolitano', 'chocoloate', 'doritos']
friend_pizzas=my_pizzas[:]

my_pizzas.append('bacon')
friend_pizzas.append('frango')

print("Minhas pizzas favoritas são: ")
for pizza in my_pizzas:
    print(pizza)

print("As pizzas favoritas do meu amigo são: ")
for pizza in friend_pizzas:
    print(pizza)