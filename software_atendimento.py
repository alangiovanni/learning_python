# Bibliotecas
import os

def get_infor_atendentes(atendentes):
    """Função executada no começo do software apenas para buscar o número de atendentes disponíveis para atendimento da fila"""
    qtde_atendentes = input("Favor informe a quantidade de atendentes em seu estabelecimento: ")
    # Converte em int
    qtde_atendentes = int(qtde_atendentes)
    for id in range(1, qtde_atendentes+1):
        first_name = input("\nFavor informar o primeiro nome do " + str(id) + "º atendente: ")
        atendente = {'id': id, 'nome': first_name, 'disponibilidade': 'livre', 'em_atendimento': ''}
        atendentes.append(atendente)

def status_atendentes(atendentes):
    """Printa na Tela os Status dos atendentes atuais"""
    print('\n== STATUS DOS ATENDENTES ==')
    for atendente in atendentes:
        if atendente['em_atendimento']: 
            print(str(atendente['id']) + ' - ' + atendente['nome'] + ' - ' + atendente['disponibilidade'] + ' - ' + atendente['em_atendimento'])
        else:
            print(str(atendente['id']) + ' - ' + atendente['nome'] + ' - ' + atendente['disponibilidade'])

def status_fila(fila):
    """Printa na tela a fila atual"""
    count=1
    print('\n== FILA ==')
    if fila:
        for pessoa in fila:
            if count == 1:
                print(pessoa, end='')
            else:
                print(", " + pessoa, end='')
            count += 1
        #Limpar o print após usar o end
        print()
    else:
        print('[VAZIA]')

def exibe_menu_principal():
    """Opções do Menu Principal do Software"""
    print('\n== MENU PRINCIPAL DO SOFTWARE ==')
    print('1 - Realizar Atendimento')
    print('2 - Finalizar Atendimento')
    print('3 - Pegar uma ficha para atendimento')
    print('0 - SAIR')
    opcao = input('\nFavor informe o número da opção desejada: ')
    opcao = int(opcao)
    return opcao

def ler_opcao(opcao, atendentes, fila):
    if opcao == 1:
        realizar_atendimento(atendentes, fila)
    elif opcao == 2:
        finalizar_atendimento(atendentes, fila)
    elif opcao == 3:
        inserir_fila(fila)

def realizar_atendimento(atendentes, fila):
    """Coloca o próximo da fila em atendimento no primeiro caixa disponível"""
    if fila:
        encontrou_atendente = False

        for atendente in atendentes:
            if atendente['disponibilidade'] == 'livre':
                encontrou_atendente = True
                proximo_atendimento = fila.pop(0)
                atendente['disponibilidade'] = 'ocupado'
                atendente['em_atendimento'] = proximo_atendimento
                break
        if encontrou_atendente == False:
            input("Todos os atendentes estão ocupados. Enter para voltar ao menu...")
    else:
        input("Fila VAZIA! Enter para voltar ao menu...")

def finalizar_atendimento(atendentes, fila):
    """Finaliza um atendimento de qualquer atendente através do ID informado"""
    encontrou_atendente = False
    id_caixa = input('Favor digitar o ID do caixa a ser liberado: ')
    id_caixa = int(id_caixa)

    for atendente in atendentes:
        if atendente['id'] == id_caixa:
            encontrou_atendente = True
            atendente['disponibilidade'] = 'livre'
            atendente['em_atendimento'] = ''
            break

    if encontrou_atendente == False:
        input("ID não encontrado. Enter para voltar ao menu...")

def inserir_fila(fila):
    """Insere uma pessoa na fila"""
    pessoa = input("Favor digite o nome da pessoa para adicionar a fila: ")
    fila.append(pessoa)

def main():
    """Função Principal do Programa"""
    # lista de atendentes
    atendentes = []
    # Pessoas na fila para atendimento
    fila = []
    # Populo a lista de atendentes
    get_infor_atendentes(atendentes)
    
    # Populo manualmente, simulando um software que fica distribuindo ficha, a fila;
    fila = ['Marx', 'Marileide', 'Marcone', 'Antony', 'Neemias']

    active = True
    while active:
        # Limpa a tela. Linux or Windows
        os.system('cls' if os.name == 'nt' else 'clear')
        status_atendentes(atendentes)
        status_fila(fila)
        opcao = exibe_menu_principal()

        # No menu o usuário apertou 0, SAIR.
        if opcao == 0:
            active = False
        else:
            ler_opcao(opcao, atendentes, fila)

# Start da Mágica
main()