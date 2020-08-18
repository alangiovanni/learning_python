car = 'subaru'
if car == 'subaru':
    print(car == 'subaru')
    print(car == 'audi')

car = 'Subaru'
if car == 'subaru'.title():
    print(car)

number = 10
if number < 11 and number > 5:
    print(number)

lista=['arroz', 'macarrão', 'feijão']

if 'arroz' in lista:
    print("Arroz está na lista")

if 'carro' not in lista:
    print("Carro não está na lista")

age=4
if age >= 18:
    print("Você pode votar!")
else:
    print("Você não pode votar")

if age < 4:
    print("Entrada Gratuita")
elif age < 18:
    print("Entrada de 5 Doláres")
else:
    print("Entrada de 10 Doláres")

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