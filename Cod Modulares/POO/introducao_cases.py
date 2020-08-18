class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Construtor"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("Nome do restaurante é " + self.restaurant_name.title() + ".")
        print("O tipo de culinária é " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        print("O restaurante " + self.restaurant_name + " está ABERTO!")

restaurante = Restaurant('mamamia', 'portuguesa')
restaurante.describe_restaurant()
restaurante.open_restaurant()
