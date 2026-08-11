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

from proyecto_barrio.player.player import Player

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

        self.player = Player(
            WINDOW_WIDTH // 2 - 20,
            WINDOW_HEIGHT // 2 - 20,
        )

    def handle_events(self):
        """Procesa los eventos recibidos por Pygame."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, delta_time):
        """Actualiza la lógica del juego."""
        self.player.update(
            delta_time,
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
        )

    def draw(self):
        """Dibuja el estado actual del juego."""
        self.screen.fill((30, 30, 30))
        self.player.draw(self.screen)

        pygame.display.set_caption(
            f"Proyecto Barrio - FPS: {self.clock.get_fps():.1f}"
        )

        pygame.display.flip()

    def run(self):
        """Ejecuta el Game Loop principal."""
        while self.running:
            self.handle_events()

            delta_time = self.clock.tick(FPS) / 1000.0

            self.update(delta_time)
            self.draw()

        pygame.quit()
