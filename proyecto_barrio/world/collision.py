"""Sistema de colisiones del mundo de Proyecto Barrio."""

import pygame


class CollisionManager:
    """Gestiona las colisiones entre entidades y obstáculos."""

    def __init__(self, obstacles):
        """Inicializa el gestor con una lista de obstáculos."""
        self.obstacles = obstacles

    def get_collision_rects(self):
        """Devuelve los rectángulos de colisión de los obstáculos."""
        return [obstacle.rect for obstacle in self.obstacles]

    def move_with_collisions(self, rect, movement):
        """Mueve un rectángulo evitando atravesar obstáculos."""
        collision_rects = self.get_collision_rects()

        rect.x += round(movement.x)

        for obstacle_rect in collision_rects:
            if rect.colliderect(obstacle_rect):
                if movement.x > 0:
                    rect.right = obstacle_rect.left
                elif movement.x < 0:
                    rect.left = obstacle_rect.right

        rect.y += round(movement.y)

        for obstacle_rect in collision_rects:
            if rect.colliderect(obstacle_rect):
                if movement.y > 0:
                    rect.bottom = obstacle_rect.top
                elif movement.y < 0:
                    rect.top = obstacle_rect.bottom
