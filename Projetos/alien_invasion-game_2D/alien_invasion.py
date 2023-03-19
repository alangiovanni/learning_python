import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    
    # Configurações
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.title_game)

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)

    # Inicia o laço principal do game
    while True:
        # Observa eventos do teclado e do mouse
        gf.check_events(ship)
        # Atualiza a posição da nave
        ship.update()
        # Atualiza a tela
        gf.update_screen(ai_settings, screen, ship)

run_game()