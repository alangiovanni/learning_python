python_work = 'c:/Users/alan1/Documentos/GIT/learning_python/Cod Modulares/Persistencia de dados/python_work'

# Lendo todo o arquivo de uma vez
with open(python_work + '/pi_digits.txt') as file_object:
    print("\nLendo todo o arquivo de uma vez")
    contents = file_object.read()
    print(contents)

# Lendo o arquivo linha a linha
with open(python_work + '/pi_digits.txt') as file_object:
    print("\nLendo Linha a linha")
    for line in file_object:
        print(line.rstrip()) #rstrip() é a função que retira o espaços a direita da string

# Construindo uma string sem espaços utilizando o exemplo do arquivo com o valor de pi em várias linhas
with open(python_work + '/pi_digits.txt') as file_object:
    print("\nConstruindo uma string com o valor de Pi.")
    lines = file_object.readlines()
    
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()

    print('Valor de PI: ' + pi_string)
    print('tamanho: ' + str(len(pi_string)))

# Construindo uma string sem espaços utilizando o exemplo do arquivo com o valor de pi em várias linhas - MILHÕES DE DÍGITOS
python_work = 'c:/Users/alan1/Documentos/GIT/Curso Intensivo Python/chapter_10'
filename = python_work + '/pi_million_digits.txt'

with open(filename) as file_object:
    print("\nConstruindo uma string com o valor de Pi. (MILHÕES DE DIGITOS)")
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print('Valor de PI: ' + pi_string[:52] + '...')
print('Tamanho: ' + str(len(pi_string)))

# Meu aniversário está contido no primeiro milhão de digitos de PI?
# python_work = 'c:/Users/alan1/Documentos/GIT/Curso Intensivo Python/chapter_10'
# filename = python_work + '/pi_million_digits.txt'

with open(filename) as file_object:
    print("\nMeu aniversário está contido no primeiro milhão de digitos de PI? (MILHÕES DE DIGITOS)")
    lines = file_object.readlines()

    for line in lines:
        pi_string += line.strip()

    birthday = input('Enter your birthday, in the form mmddyy: ')
    if birthday in pi_string:
        print('Your birthday appears in the first million digits of pi!')
    else:
        print('Your birthday DOES NOT appear in the first million digits of pi.')
