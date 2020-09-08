# Para este exercício só pode ter a classe Car aqui. Favor consultar o my_cars_2.py
"""Módulo da classe que modela o carro"""
class Car():
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