dimensoes = (100, 50)
# Tentando alterar uma tupla
# dimensoes[0]=200 # Vai dar erro
print("Tupla Original: ")
for dimensao in dimensoes:
    print(dimensao)

# Não dá pra alterar a Tupla, mas podemos sobscrever toda ela
dimensoes = (400, 300)
print("Tupla Modificada: ")
for dimensao in dimensoes:
    print(dimensao)