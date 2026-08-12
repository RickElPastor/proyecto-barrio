"""Entidades NPC de Proyecto Barrio."""

import pygame


class NPC:
    """Representa a un personaje no controlado por el jugador."""

    def __init__(self, x, y, name, role="civil"):
        """Inicializa un NPC en una posición determinada."""
        self.position = pygame.Vector2(x, y)

        self.width = 36
        self.height = 36

        self.name = name
        self.role = role

        self.dialogue = [
            f"Qué onda, soy {self.name}.",
            "¿Qué tal tu día?",
        ]

        self.rect = pygame.Rect(
            round(self.position.x),
            round(self.position.y),
            self.width,
            self.height,
        )

        self.color = (70, 140, 220)

    def draw_interaction_indicator(self, screen):
        """Dibuja un indicador temporal de interacción sobre el NPC."""
        font = pygame.font.Font(None, 24)

        text = font.render("E", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.rect.centerx, self.rect.top - 12))

        screen.blit(text, text_rect)

    def draw(self, screen):
        """Dibuja temporalmente al NPC en pantalla."""
        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
        )
