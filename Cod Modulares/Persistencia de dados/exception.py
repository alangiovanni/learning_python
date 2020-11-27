while True:
    first_number = input('Digite um número: [q para sair] ')
    
    if first_number == 'q':
        break

    second_number = input('Digite outro número: ')

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("ERROR: Nenhum número é divisível por 0.")
    else:
        print("Resultado da divisão: " + str(answer))