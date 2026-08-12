"""Sistema de diálogos e interacción de Proyecto Barrio."""

import pygame


class DialogManager:
    """Gestiona la interfaz de interacción con NPCs."""

    def __init__(self):
        """Inicializa el gestor de diálogos."""
        self.options = [
            {
                "id": "talk",
                "label": "Hablar",
                "returns_to_menu": True,
            },
            {
                "id": "help",
                "label": "Ayudar",
                "returns_to_menu": True,
            },
            {
                "id": "steal",
                "label": "Robar",
                "returns_to_menu": False,
            },
            {
                "id": "attack",
                "label": "Pegar",
                "returns_to_menu": False,
            },
            {
                "id": "cancel",
                "label": "Cancelar",
                "returns_to_menu": False,
            },
        ]

        self.selected = 0

        self.active_dialogue = False
        self.dialogue_lines = []
        self.dialogue_index = 0

    def reset(self):
        """Reinicia la selección del menú."""
        self.selected = 0

    def start_dialogue(self, npc):
        """Inicia el diálogo con un NPC."""
        self.active_dialogue = True
        self.dialogue_lines = npc.dialogue
        self.dialogue_index = 0

    def advance_dialogue(self):
        """Avanza a la siguiente línea del diálogo."""
        if not self.active_dialogue:
            return

        self.dialogue_index += 1

        if self.dialogue_index >= len(self.dialogue_lines):
            self.active_dialogue = False
            self.dialogue_lines = []
            self.dialogue_index = 0

    def move_selection(self, direction):
        """Mueve la selección del menú."""
        self.selected += direction

        if self.selected < 0:
            self.selected = len(self.options) - 1

        if self.selected >= len(self.options):
            self.selected = 0

    def get_selected_action(self):
        """Devuelve la acción actualmente seleccionada."""
        return self.options[self.selected]

    def draw(self, screen, npc):
        """Dibuja el menú de interacción."""
        font = pygame.font.Font(None, 32)

        menu_rect = pygame.Rect(
            400,
            150,
            480,
            420,
        )

        pygame.draw.rect(
            screen,
            (20, 20, 20),
            menu_rect,
        )

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            menu_rect,
            2,
        )

        title = font.render(
            npc.name,
            True,
            (255, 255, 255),
        )

        screen.blit(
            title,
            (
                menu_rect.x + 30,
                menu_rect.y + 30,
            ),
        )

        for index, option in enumerate(self.options):
            option_y = menu_rect.y + 90 + index * 55

            if index == self.selected:
                pygame.draw.rect(
                    screen,
                    (60, 60, 60),
                    (
                        menu_rect.x + 20,
                        option_y - 5,
                        menu_rect.width - 40,
                        45,
                    ),
                )

            option_text = font.render(
                option["label"],
                True,
                (255, 255, 255),
            )

            screen.blit(
                option_text,
                (
                    menu_rect.x + 40,
                    option_y,
                ),
            )

    def draw_dialogue(self, screen, npc):
        """Dibuja el diálogo actual del NPC."""
        if not self.active_dialogue:
            return

        font = pygame.font.Font(None, 30)

        dialogue_rect = pygame.Rect(
            120,
            500,
            1040,
            150,
        )

        pygame.draw.rect(
            screen,
            (20, 20, 20),
            dialogue_rect,
        )

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            dialogue_rect,
            2,
        )

        name_text = font.render(
            npc.name,
            True,
            (255, 255, 255),
        )

        screen.blit(
            name_text,
            (
                dialogue_rect.x + 25,
                dialogue_rect.y + 20,
            ),
        )

        line = self.dialogue_lines[self.dialogue_index]

        dialogue_text = font.render(
            line,
            True,
            (255, 255, 255),
        )

        screen.blit(
            dialogue_text,
            (
                dialogue_rect.x + 25,
                dialogue_rect.y + 65,
            ),
        )

        continue_text = font.render(
            "ENTER para continuar",
            True,
            (180, 180, 180),
        )

        screen.blit(
            continue_text,
            (
                dialogue_rect.right - 250,
                dialogue_rect.bottom - 35,
            ),
        )
