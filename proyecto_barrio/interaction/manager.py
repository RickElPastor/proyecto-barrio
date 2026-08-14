"""Administrador central de interacciones de Proyecto Barrio."""

import pygame

from proyecto_barrio.interaction.state import InteractionState


class InteractionManager:
    """Controla el estado general de las interacciones."""

    def __init__(self, dialog_manager, action_manager):
        self.state = InteractionState.NONE
        self.npc = None

        self.dialog_manager = dialog_manager
        self.action_manager = action_manager

    @property
    def active(self):
        """Indica si existe una interacción activa."""
        return self.state != InteractionState.NONE

    @property
    def show_menu(self):
        """Indica si debe mostrarse el menú de interacción."""
        return self.state == InteractionState.MENU and self.npc is not None

    @property
    def show_dialogue(self):
        """Indica si existe un diálogo activo."""
        return self.state == InteractionState.DIALOGUE

    @property
    def show_message(self):
        """Indica si existe un mensaje activo."""
        return self.state == InteractionState.MESSAGE

    def open_menu(self, npc):
        """Abre el menú de interacción con un NPC."""
        self.npc = npc
        self.state = InteractionState.MENU

    def close(self):
        """Cierra completamente la interacción."""
        self.npc = None
        self.state = InteractionState.NONE
    
    def open_menu_state(self):
        """Cambia la interacción al estado de menú."""
        self.state = InteractionState.MENU

    def open_dialogue_state(self):
        """Cambia la interacción al estado de diálogo."""
        self.state = InteractionState.DIALOGUE

    def open_message_state(self):
        """Cambia la interacción al estado de mensaje."""
        self.state = InteractionState.MESSAGE

    def handle_event(self, event, game):
        """Procesa un evento de teclado relacionado con una interacción."""

        if self.state == InteractionState.MESSAGE:
            self._handle_message_event(event)

            return True

        if self.state == InteractionState.DIALOGUE:
            self._handle_dialogue_event(event)

            return True

        if self.state == InteractionState.MENU:
            self._handle_menu_event(event, game)

            return True

        if event.key == pygame.K_RETURN:
            nearby_npc = game.player.get_nearby_npc(game.npcs)

            if nearby_npc is not None:
                self.dialog_manager.reset()
                self.open_menu(nearby_npc)

                return True

        return False

    def _handle_message_event(self, event):
        """Procesa las entradas mientras se muestra un mensaje."""

        if event.key == pygame.K_RETURN:
            self.dialog_manager.close_message()
            self.dialog_manager.reset()
            self.open_menu_state()

        elif event.key == pygame.K_ESCAPE:
            self.dialog_manager.close_message()
            self.dialog_manager.reset()
            self.open_menu_state()

    def _handle_dialogue_event(self, event):
        """Procesa las entradas mientras existe un diálogo activo."""

        if event.key == pygame.K_RETURN:
            self.dialog_manager.advance_dialogue()

            if not self.dialog_manager.active_dialogue:
                self.dialog_manager.reset()
                self.open_menu_state()

        elif event.key == pygame.K_ESCAPE:
            self.dialog_manager.active_dialogue = False
            self.dialog_manager.dialogue_lines = []
            self.dialog_manager.dialogue_index = 0

            self.dialog_manager.reset()
            self.open_menu_state()

    def _handle_menu_event(self, event, game):
        """Procesa las entradas del menú de interacción."""

        if event.key in (pygame.K_UP, pygame.K_w):
            self.dialog_manager.move_selection(-1)

        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.dialog_manager.move_selection(1)

        elif event.key == pygame.K_ESCAPE:
            self.dialog_manager.reset()
            self.close()

        elif event.key == pygame.K_RETURN:
            action = self.dialog_manager.get_selected_action()

            result = self.action_manager.execute(
                action,
                self.npc,
            )

            if action["id"] == "talk":
                self.dialog_manager.start_dialogue(self.npc)
                self.open_dialogue_state()

            elif action["id"] == "help":
                if result is not None:
                    self.dialog_manager.show_message(result["message"])
                    self.open_message_state()

            elif action["id"] == "cancel":
                self.dialog_manager.reset()
                self.close()
