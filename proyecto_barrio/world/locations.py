"""Locaciones del mundo de Proyecto Barrio."""

import pygame


class Location:
    """Representa una locación o zona del mundo."""

    DEBUG_COLORS = {
        "residential": (90, 150, 90),
        "center": (150, 130, 80),
        "commercial": (90, 120, 160),
    }

    def __init__(self, name, location_type, x, y, width, height):
        """Inicializa una locación."""
        self.name = name
        self.location_type = location_type

        self.position = pygame.Vector2(x, y)

        self.width = width
        self.height = height

        self.rect = pygame.Rect(
            round(self.position.x),
            round(self.position.y),
            self.width,
            self.height,
        )

        self.debug_color = self.DEBUG_COLORS.get(
            self.location_type,
            (120, 120, 120),
        )

    def draw(self, screen):
        """Dibuja temporalmente el área de la locación."""
        pass
