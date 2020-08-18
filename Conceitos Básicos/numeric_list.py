for value in range(1,101):
    print(value)

# Convertendo um range de número em uma lista
numbers = list(range(1,11))
print(numbers)

# Lista de números pares
numbers = list(range(2,101,2))
print(numbers)

# Quadrados perfeitos
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print("Lista de Quadrado perfeito em 4 linhas: " + str(squares))

# List Comprehensions
squares = [value**2 for value in range(1,11)]
print("Lista de Quadrado perfeito em 1 FUCKING linha: " + str(squares))

print("Valor mínimo dos quadrados: " + str(min(squares)))
print("Valor máximo dos quadrados: " + str(max(squares)))
print("Soma dos quadrados: " + str(sum(squares)))
