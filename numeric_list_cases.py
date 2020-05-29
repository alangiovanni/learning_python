#for value in range(0,1000):
#    print(value)

numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

for value in range(1,20,2):
    print(value)

for value in range(3,30,3):
    print(value)

# Cubos perfeitos
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print("Lista de Cubos perfeito em 4 linhas: " + str(cubes))

# List Comprehensions
cubes = [value**3 for value in range(1,11)]
print("Lista de Cubos perfeito em 1 FUCKING linha: " + str(cubes))