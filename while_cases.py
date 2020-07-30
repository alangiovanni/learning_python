# 7.1 - Locação de Automóveis
#car_choise = input("Qual carro você gostaria de alugar? ")
#print("Deixe me ver se encontro um " + car_choise.title() + " para você!")

# 7.2 - Lugares em um restaurante
#qtde_pessoa = int(input("Quantas pessoas estão no seu grupo? "))
#if qtde_pessoa > 8:
#    message="Por favor aguarde!"
#else:
#    message="Encontramos uma mesa para você!"
#print(message)

# 7.3 - Múltiplo de 10
#number = int(input("Informe um número: "))
#if number % 10 == 0:
#    message = "O número informado É múltiplo de 10"
#else:
#    message = "O número informado NÃO é múltiplo de 10"
#print(message)

# 7.4 - Ingredientes para uma pizza
# Para este exercício fiz um outro .py nomeado como software_pedido_pizza.py

# 7.5 - Ingressos para o cinema
active = True
while active:
    age = input("Quantos anos você tem? ")
    
    # Se o usuário digitar QUIT eu saio do laço
    if age == 'quit':
        break
    
    # Converto a resposta em INT.
    age = int(age)

    if age < 3:
        message = "Ingresso Gratuíto"
    elif age < 12:
        message = "Ingresso custa R$ 10,00"
    else:
        message = "Ingresso custa R$ 15,00"
    
    print(message)