"""Entidades físicas del mundo de Proyecto Barrio."""

import pygame

class Building:
    """Representa un edificio dentro del mundo."""

    def __init__(self, x, y, width, height, building_type):
        """Inicializa un edificio."""
        self.position = pygame.Vector2(x, y)

        self.width = width
        self.height = height

        self.building_type = building_type

        self.rect = pygame.Rect(
            round(self.position.x),
            round(self.position.y),
            self.width,
            self.height,
        )

        self.color = self._get_color()

    def _get_color(self):
        """Obtiene el color temporal según el tipo de edificio."""
        colors = {
            "house": (180, 150, 110),
            "shop": (180, 180, 120),
            "restaurant": (170, 100, 80),
            "service": (120, 150, 180),
        }

        return colors.get(self.building_type, (150, 150, 150))

    def draw(self, screen):
        """Dibuja temporalmente el edificio."""
        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
        )
