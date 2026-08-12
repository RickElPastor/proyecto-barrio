"""Mapa principal del mundo de Proyecto Barrio."""

import pygame

from proyecto_barrio.world.buildings import Building
from proyecto_barrio.world.locations import Location
from proyecto_barrio.world.npcs import NPC


class GameMap:
    """Representa el mundo del juego."""

    def __init__(self, width, height):
        """Inicializa el mapa con sus dimensiones."""
        self.width = width
        self.height = height

        self.ground_color = (70, 120, 70)
        self.road_color = (70, 70, 70)

        self.roads = [
            pygame.Rect(0, 270, width, 80),
            pygame.Rect(270, 0, 80, height),
        ]

        self.buildings = [
            Building(100, 100, 140, 120, "house"),
            Building(430, 100, 140, 120, "house"),
            Building(750, 100, 180, 120, "shop"),
            Building(100, 400, 140, 120, "house"),
            Building(430, 400, 180, 120, "restaurant"),
        ]

        self.npcs = [
            NPC(200, 260, "Carlos"),
            NPC(650, 260, "María"),
            NPC(700, 500, "Luis"),
        ]

        self.locations = [
            Location(
                "Zona residencial",
                "residential",
                0,
                0,
                width,
                270,
            ),
            Location(
                "Centro",
                "center",
                0,
                270,
                width,
                180,
            ),
            Location(
                "Zona comercial",
                "commercial",
                0,
                450,
                width,
                height - 450,
            ),
        ]

    def get_npcs(self):
        """Devuelve los NPC del mapa."""
        return self.npcs

    def get_collision_obstacles(self):
        """Devuelve los edificios que actúan como obstáculos."""
        return self.buildings

    def draw(self, screen):
        """Dibuja el terreno, las calles y los edificios."""
        screen.fill(self.ground_color)

        for road in self.roads:
            pygame.draw.rect(
                screen,
                self.road_color,
                road,
            )

        for building in self.buildings:
            building.draw(screen)

        for npc in self.npcs:
            npc.draw(screen)
