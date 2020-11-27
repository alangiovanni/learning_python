filename = 'c:/Users/alan1/Documentos/GIT/learning_python/Cod Modulares/Persistencia de dados/python_work/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("Iniciando o arquivo em modo escrita")
    file_object.write("Write sem quebra de linha!")
    file_object.write("\nWrite com quebra de linha no inicio e final!\n")

with open(filename, 'a') as file_object:
    file_object.write("\nIniciando o arquivo em modo append")
    file_object.write("\nWrite com quebra de linha no inicio e final!\n")