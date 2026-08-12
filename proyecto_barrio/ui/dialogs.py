"""Sistema de diálogos e interacción de Proyecto Barrio."""

import pygame


class DialogManager:
    """Gestiona la interfaz de interacción con NPCs."""

    def __init__(self):
        """Inicializa el gestor de diálogos."""
        self.options = [
            "Hablar",
            "Ayudar",
            "Robar",
            "Pegar",
            "Cancelar",
        ]

        self.selected = 0

    def reset(self):
        """Reinicia la selección del menú."""
        self.selected = 0

    def move_selection(self, direction):
        """Mueve la selección del menú."""
        self.selected += direction

        if self.selected < 0:
            self.selected = len(self.options) - 1

        if self.selected >= len(self.options):
            self.selected = 0

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
                option,
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
