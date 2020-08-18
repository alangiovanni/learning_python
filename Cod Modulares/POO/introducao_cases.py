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

# 9.5 - Tentativas de Login
class User():
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password
        self.login_attemps = 0
    
    def describe_profile(self):
        print("Nome do usuário: " + self.name.title())
        print("Login: " + self.login)
        print("Password: " + self.password)
        print("Logins realizados na plataforma: " + str(self.login_attemps))
    
    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0

# Instanciando um novo perfil do usuário
print()
new_user = User('alan targino', 'alan.targino', '123qweasd')

new_user.increment_login_attemps() # +1 Login
new_user.increment_login_attemps() # +1 Login
new_user.increment_login_attemps() # +1 Login
# new_user.reset_login_attemps() # Reseta os logins
new_user.describe_profile()