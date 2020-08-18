class Dog():
    """Uma classe que modela o cachorro"""
    # __init__ é como se fosse o construtor da classe. Este é quem faz a instanciação;
    def __init__(self, name, age):
        """Inicializa os atributos name e age"""
        self.name = name
        self.age = age
    
    # Função na classe é um método
    def sit(self):
        """Simula um cachorro sentando em resposta ao comando"""
        print(self.name.title() + " is now sitting.")
    
    def rool_over(self):
        """Simula um cachorro rolando em resposta ao comando"""
        print(self.name.title() + " rolled over!")

class Car():
    """Uma classe que modela o carro"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def get_descriptive_name(self):
        """Devolve um descritivo do nome, formatado de modo elegante"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a kilometragem do carro"""
        print("This car has " + str(self.odometer) + " kilometers on it.")
    
    def update_odometer(self, km):
        """Define um novo valor de leitura do hodômetro com o valor especificado"""
        if km >= self.odometer:
            self.odometer = km
        else:
            print("You can't rool back an odometer!")
    
    def increment_odometer(self, km):
        """Soma o valor do hodômetro com o valor especificado"""
        if km > 0:
            self.odometer += km
        else:
            print("You can't lower the odometer.")
## INSTANCIAÇÃO DAS CLASSES ACIMA

############## DOGS
my_dog = Dog('penny', 2) # instanciando um cachorro
# Acessando os atributos
print("My Dog's name is " + my_dog.name.title() + ".")
print("My Dog is " + str(my_dog.age) + " years old.")
# Chamando os métodos
my_dog.sit()
my_dog.rool_over()

print() #espaço em branco no console

your_dog = Dog('amora', 3) # instanciando um cachorro
# Acessando os atributos
print("Your Dogs's name is " + your_dog.name.title() + ".")
print("Your Dog is " + str(your_dog.age) + " years old.")
# Chamando os métodos
your_dog.sit()
your_dog.rool_over()

############## CAR
print()
my_new_car = Car('audi', 'a4', 2018)
print("Meu carro novo: " + my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Alterando o atributo por método
my_new_car.update_odometer(1000)
my_new_car.read_odometer()

## alterando o atributo diretamente
# my_new_car.odometer = 2000
# my_new_car.read_odometer()

# Tentando fazer um roolback no hodômetro
my_new_car.update_odometer(900)
my_new_car.read_odometer()

# Incrementando
my_new_car.increment_odometer(500)
my_new_car.read_odometer()

# Tentando decrementar
my_new_car.increment_odometer(-500)
my_new_car.read_odometer()