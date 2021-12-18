# Menu
def perguntar(possiveis_opcoes):
    # Possíveis opções
    possiveis_opcoes.append("I")
    possiveis_opcoes.append("P")
    possiveis_opcoes.append("E")
    possiveis_opcoes.append("L")
    
    # IMPORTANTE - Sempre que adicionar uma nova opção também deve ser adicionado a execução na função "executar_opcao"

    # Menu com as opções
    opcao=input("O que deseja realizar? \n\
" + 
            "<I> - Para Inserir um usuário \n\
"+ 
            "<P> - Para Pesquisar um usuário \n\
"+ 
            "<E> - Para Excluir um usuário \n\
"+
            "<L> - Para Listar um usuário \n\
" +
                   "Digite: ").upper()
    return opcao

def inserir(dicionario):
    chave=input("Digite o login: ").upper()
    dicionario[chave]=[input("Digite o nome: ").upper(),
                    input("Digite a última data de acesso: "),
                    input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)

def executar_opcao(dicionario, opcao):
    if opcao == "I":
        inserir(dicionario)
    elif opcao=="P":
        pesquisar(dicionario,input("Qual login deseja pesquisar? ").upper())
    elif opcao == "E":
        excluir(dicionario,input("Qual login deseja excluir? ").upper())
    elif opcao == "L":
        listar(dicionario)
    else:
        # Opção inválida
        return False
    # Retorno padrão se a opção existir
    return True

def main():
    # Cria um dicionário vazio para os usuários
    usuarios={}
    # Possiveis Opções do Menu - Vazio, preenchido dentro da função menu()
    possiveis_opcoes = []
    # Flag para o While
    opcao_valida = True

    while opcao_valida:
        # Abre um menu de opções
        opcao = perguntar(possiveis_opcoes)
        # Executa a opção selecionada
        opcao_valida = executar_opcao(usuarios, opcao)

# Start da Mágica
main()