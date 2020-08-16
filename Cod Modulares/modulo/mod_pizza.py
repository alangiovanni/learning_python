def make_pizza(qtde_pizza, size, *toppings):
    """Exibe uma lista de ingredientes pedidos na pizza, a quantidade e o tamanho"""
    print('\nFoi escolhido ' + str(qtde_pizza) + ' pizzas de tamanho ' + size + '.')
    print("Segue os ingredientes: ")
    for topping in toppings:
        print(topping)