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
all_ingredientes = ['tomate', 'queijo mussarela', '4 queijos', 'presunto', 'azeitona', 'bacon', 'milho', 'ervilha', 'catupiry', 'camarao']
my_ingredientes = []

while True:
    print("\nIngredientes Disponíveis para sua pizza!")
    count=0
    for ingrediente in all_ingredientes:
        message=str(count) + " - " + ingrediente
        print(message.title())
        count += 1
    
    print("\n" + 'Você pode finalizar o pedido digitando "quit" a qualquer momento!')
    print("Ingredientes selecionados até o momento: " + str(my_ingredientes))
    ingrediente_choise = input("\nPor favor digite o número referente ao ingrediente que deseja: ")
    if ingrediente_choise == 'quit':
        print("\nPedido realizado com sucesso! Abaixo segue os ingredientes da sua pizza: ")
        for ingrediente in my_ingredientes:
            print("-> " + ingrediente)
        break
    
    # Se chegou aqui o teste deu falso então o usuário não informou quit e sim um ingrediente. Converte em número a escolha
    ingrediente_choise = int(ingrediente_choise)
    # Coloca no fim da lista o ingrediente selecionado
    my_ingredientes.append(all_ingredientes[ingrediente_choise])
    # Retira o Ingrediente da lista de disponíveis
    all_ingredientes.remove(all_ingredientes[ingrediente_choise])