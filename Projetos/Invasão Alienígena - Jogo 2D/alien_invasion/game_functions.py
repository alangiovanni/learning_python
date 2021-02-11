import sys
import pygame

def check_events(ship):
    """Responde a eventos gerados pelo usuário através do mouse e/ou teclado"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Eventos do usuário por meio do teclado
        check_keydown_events(event, ship)
        check_keyup_events(event, ship)

def check_keydown_events(event, ship):
    """Responde a pressionamentos de teclas"""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            # mova a espaçonave para a DIREITA
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # mova a espaçonave para a ESQUERDA
            ship.moving_left = True
        elif event.key == pygame.K_UP:
            # mova a espaçonave para CIMA
            ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # mova a espaçonave para BAIXO
            ship.moving_down = True

def check_keyup_events(event, ship):
    """Responde a solturas de teclas"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            # Interrompa a ação de mover a espaçonave para a DIREITA
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Interrompa a ação de mover a espaçonave para a ESQUERDA
            ship.moving_left = False
        elif event.key == pygame.K_UP:
            # Interrompa a ação de mover a espaçonave para CIMA
            ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            # Interrompa a ação de mover a espaçonave para BAIXO
            ship.moving_down = False

def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e alterna para a nova tela"""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visivel
    pygame.display.flip()