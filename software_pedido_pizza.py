# Bibliotecas
import os

# Todos os ingredientes disponíveis na loja
all_ingredientes = ['tomate', 'queijo mussarela', '4 queijos', 'presunto', 'azeitona', 'bacon', 'milho', 'ervilha', 'catupiry', 'camarao']
# Ingredientes selecionados pelo o usuário
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
            print("-> " + ingrediente.title())
        break
    
    # Se chegou aqui o teste deu falso então o usuário não informou quit e sim um ingrediente. Converte em número a escolha
    ingrediente_choise = int(ingrediente_choise)
    # Coloca no fim da lista o ingrediente selecionado
    my_ingredientes.append(all_ingredientes[ingrediente_choise])
    # Retira o Ingrediente da lista de disponíveis
    all_ingredientes.remove(all_ingredientes[ingrediente_choise])

    # Limpa a tela. Linux or Windows
    os.system('cls' if os.name == 'nt' else 'clear')