# Coletando dados do usuário
#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

#name = input("What is your name? ")
#print("Hello " + name.title() + "!")

#String multilinha
#prompt = "If you tell us who you are, we can personalize the messsage you see."
#prompt += "\nWhat is your first name? "
#name = input(prompt)
#print("Hello " + name.title() + "!")

#prompt = "\nWe need to know your age to make sure you can vote."
#prompt += "\nHow old are you? "
# Recebendo a idade e convertendo em int
#age = int(input(prompt))

#if age >= 18:
#    message = "Gz! You can vote!"
#else:
#    message = "Putz! You can't vote."
#print(message)

# Resto da divisão
#number = input("\nInforme um número: ")
#number = int(number)

#if number % 2 == 0:
#    message = "O número informado é PAR"
#else:
#    message = "O número informado é iMPAR"
#print(message)

# While
# Printa números até que a condição seja falsa
#current_number = 1
#while current_number <= 10:
#    print(current_number)
#    current_number += 1

# Repete tudo que o usuário digitar até que ele digite quit
#message = ""
#prompt = "Tell me something, and i will repeat it back to you: "
#while message != 'quit':
#    message = input(prompt)
#    if message == 'quit':
#        print("OK! See you.")
#    else:
#        print(message)

# Mesmo While do anterior, porém mais elegante com uso de FLAG
#message = ""
#prompt = "Tell me something, and i will repeat it back to you: "
#active = True
#while active:
#    message = input(prompt)
#    if message == 'quit':
#        print("OK! See you.")
        # Sai do laço
#        active = False
        # Também sai do laço e anula a necessidade de usar uma flag;
        # break
#    else:
#        print(message)

# Uso do continue em um laço
# Print apenas números impares de um intervalo de números
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        # Número é par, prossiga ao próximo loop;
        continue
    # Printa o número
    print(current_number)