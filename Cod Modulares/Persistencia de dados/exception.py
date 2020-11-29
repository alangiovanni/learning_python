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

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print('Arquivo ' + filename + ' não encontrado!')
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words;")

filename = 'c:/Users/alan1/Documentos/GIT/learning_python/Cod Modulares/Persistencia de dados/python_work/file_writer_cases.txt'
count_words(filename)
filename = 'teste.txt'
count_words(filename)

### Relembrando de um usuário nas próximas execuções
import json

def save_user(filename):
    with open(filename, 'w') as f_obj:
        usuario = input('Bem vindo ao primeiro start do programa. Qual o seu nome? ')
        json.dump(usuario, f_obj)
        print('Ok ' + usuario + ', eu vou me lembrar do seu nome na próxima execução deste programa.')

def get_user(filename):
    with open(filename) as f_obj:
        usuario = json.load(f_obj)
        return usuario

def greet_user(usuario, filename):
    print('Olá ' + usuario + ', seja bem vindo de volta!')
    print('Caso deseje reiniciar minha memória, basta deletar o arquivo: ' + filename)

def remember_user(filename):
    try:
        usuario = get_user(filename)

    except FileNotFoundError:
        save_user(filename)
    else:
        greet_user(usuario, filename)

def main():
    filename = 'c:/Users/alan1/Documentos/GIT/learning_python/Cod Modulares/Persistencia de dados/python_work/remember.txt'
    remember_user(filename)

# Start
main()