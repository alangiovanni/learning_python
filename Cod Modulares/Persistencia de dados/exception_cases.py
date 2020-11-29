# 10.6 e 10.7- Adição
while True:
    first_number = input('Digite um número: [q para sair] ')
    if first_number == 'q':
        break

    try:
        first_number = int(first_number)
    except ValueError:
        print('Caro usuário, favor digite um número ou "q" para encerrar o programa.')
    else:
        try:
            second_number = int(input('Digite outro número: '))
            answer = first_number + second_number
            print("Resultado da divisão: " + str(answer))
        except ValueError:
            print('Caro usuário, favor digite outro número!')
        except ZeroDivisionError:
            print('Caro usuário, digite um número diferente de 0 para realizar a soma.')