# 10.1 - Aprendendo Python
python_work = 'c:/Users/alan1/Documentos/GIT/learning_python/Cod Modulares/Persistencia de dados/python_work'
filename = python_work + '/learning_python.txt'

# Lendo todo o arquivo de uma vez e repetindo 3 vezes
with open(filename) as file_object:
    contents = file_object.read()
    for i in range(1,4): # Iteração começando de 1.
        print('\n' + str(i) + 'ª iteração') 
        print(contents)

# 10.2 - Aprendendo C (Uso do Replace)
python_work = 'c:/Users/alan1/Documentos/GIT/learning_python/Cod Modulares/Persistencia de dados/python_work'
filename = python_work + '/learning_python.txt'

print('\nUso do Replace')
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        line = line.replace('Python', 'Java')
        print(line.strip())