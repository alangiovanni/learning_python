class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena"""
    def __init__(self):
        """Inicializa as configurações do game"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.title_game = "Alien Invasion by Alan"

        # Configurações da Espaçonave
        self.ship_speed_factor = 1.5