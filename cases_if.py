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