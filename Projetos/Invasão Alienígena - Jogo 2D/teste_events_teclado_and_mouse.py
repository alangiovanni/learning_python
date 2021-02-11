import pygame
import sys

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    # Inicia o laço principal do game
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Deixa a tela mais recente visivel
        pygame.display.flip()

run_game()