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
from proyecto_barrio.world.map import GameMap
from proyecto_barrio.world.collision import CollisionManager
from proyecto_barrio.ui.dialogs import DialogManager
from proyecto_barrio.interaction.actions import ActionManager


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

        self.game_map = GameMap(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
        )

        self.npcs = self.game_map.get_npcs()

        self.interaction_open = False
        self.interaction_npc = None

        self.dialog_manager = DialogManager()

        self.action_manager = ActionManager()

        self.collision_manager = CollisionManager(
            self.game_map.get_collision_obstacles()
        )

        self.player = Player(
            WINDOW_WIDTH // 2 - 20,
            WINDOW_HEIGHT // 2 - 20,
        )

    def handle_events(self):
        """Procesa los eventos recibidos por Pygame."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type != pygame.KEYDOWN:
                continue

            # =========================
            # DIÁLOGO ACTIVO
            # =========================
            if self.dialog_manager.active_dialogue:
                if event.key == pygame.K_RETURN:
                    self.dialog_manager.advance_dialogue()

                    if not self.dialog_manager.active_dialogue:
                        self.interaction_open = True
                        self.dialog_manager.reset()

                elif event.key == pygame.K_ESCAPE:
                    self.dialog_manager.active_dialogue = False
                    self.dialog_manager.dialogue_lines = []
                    self.dialog_manager.dialogue_index = 0

                continue

            # =========================
            # MENÚ DE INTERACCIÓN
            # =========================
            if self.interaction_open:
                if event.key in (pygame.K_UP, pygame.K_w):
                    self.dialog_manager.move_selection(-1)

                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.dialog_manager.move_selection(1)

                elif event.key == pygame.K_ESCAPE:
                    self.interaction_open = False
                    self.interaction_npc = None
                    self.dialog_manager.reset()

                elif event.key == pygame.K_RETURN:
                    action = self.dialog_manager.get_selected_action()

                    result = self.action_manager.execute(
                        action,
                        self,
                    )

                    if action["id"] == "talk":
                        self.interaction_open = False

                        self.dialog_manager.start_dialogue(self.interaction_npc)

                    elif action["id"] == "cancel":
                        self.interaction_open = False
                        self.interaction_npc = None
                        self.dialog_manager.reset()

                continue

            # =========================
            # JUEGO NORMAL
            # =========================
            if event.key == pygame.K_RETURN:
                nearby_npc = self.player.get_nearby_npc(self.npcs)

                if nearby_npc is not None:
                    self.interaction_open = True
                    self.interaction_npc = nearby_npc
                    self.dialog_manager.reset()

    def update(self, delta_time):
        """Actualiza la lógica del juego."""

        if not self.interaction_open:
            self.player.update(
                delta_time,
                WINDOW_WIDTH,
                WINDOW_HEIGHT,
                self.collision_manager,
            )

    def draw(self):
        """Dibuja el estado actual del juego."""
        self.game_map.draw(self.screen)
        self.player.draw(self.screen)

        nearby_npc = self.player.get_nearby_npc(self.npcs)

        if nearby_npc is not None:
            nearby_npc.draw_interaction_indicator(self.screen)

        if self.interaction_open and self.interaction_npc is not None:
            self.dialog_manager.draw(
                self.screen,
                self.interaction_npc,
            )

        if self.dialog_manager.active_dialogue:
            self.dialog_manager.draw_dialogue(
                self.screen,
                self.interaction_npc,
            )

        pygame.display.set_caption(f"Proyecto Barrio - FPS: {self.clock.get_fps():.1f}")

        pygame.display.flip()

    def run(self):
        """Ejecuta el Game Loop principal."""
        while self.running:
            self.handle_events()

            delta_time = self.clock.tick(FPS) / 1000.0

            self.update(delta_time)
            self.draw()

        pygame.quit()
