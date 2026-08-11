"""Núcleo principal del juego Proyecto Barrio."""

import pygame

from proyecto_barrio.config.settings import (
    FPS,
    FULLSCREEN,
    RESIZABLE,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)

class Game:
    """Controla el ciclo de vida principal del juego."""

    def __init__(self):
        """Inicializa Pygame y prepara la ventana del juego."""
        pygame.init()

        display_flags = 0

        if FULLSCREEN:
            display_flags |= pygame.FULLSCREEN

        if RESIZABLE:
            display_flags |= pygame.RESIZABLE

        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            display_flags,
        )

        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        """Procesa los eventos recibidos por Pygame."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Actualiza la lógica del juego."""
        pass

    def draw(self):
        """Dibuja el estado actual del juego."""
        self.screen.fill((30, 30, 30))
        pygame.display.flip()

    def run(self):
        """Ejecuta el Game Loop principal."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(FPS)

        pygame.quit()
