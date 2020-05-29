# Cores de Alieníginas
alien_color = 'red'

if alien_color == 'green':
    pontos = 5
elif alien_color == 'red':
    pontos = -5
else:
    pontos = 0
print("Seus pontos: " + str(pontos))

# Estágios da Vida

age = 65
if age < 2:
    message='É um bb'
elif age < 4:
    message='É uma criança'
elif age < 13:
    message='É um garoto'
elif age < 20:
    message='É um adolescente'
elif age < 65:
    message='É um adulto'
else:
    message='É um idoso'
print(message)

# Testando o conteúdo da lista
ingredientes=[]
# ingredientes=['tomate', 'queijo', 'oregano']
if ingredientes:
    for ingrediente in ingredientes:
        print("Adicionando " + ingrediente + ".")
    print("A pizza esta pronta!")
else:
    print("Você realmente quer uma pizza com apenas massa?")