"""Entidad principal del jugador de Proyecto Barrio."""

import pygame


class Player:
    """Representa al personaje controlado por el jugador."""

    def __init__(self, x, y):
        """Inicializa el jugador en una posición determinada."""
        self.position = pygame.Vector2(x, y)

        self.width = 40
        self.height = 40

        self.walk_speed = 200
        self.run_speed = 350

        self.rect = pygame.Rect(
            round(self.position.x),
            round(self.position.y),
            self.width,
            self.height,
        )

    def update(self, delta_time, screen_width, screen_height, collision_manager=None):
        """Actualiza el movimiento del jugador."""
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_w]:
            direction.y -= 1

        if keys[pygame.K_s]:
            direction.y += 1

        if keys[pygame.K_a]:
            direction.x -= 1

        if keys[pygame.K_d]:
            direction.x += 1

        if direction.length_squared() == 0:
            return

        direction = direction.normalize()

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            speed = self.run_speed
        else:
            speed = self.walk_speed

        movement = direction * speed * delta_time

        if collision_manager is not None:
            collision_manager.move_with_collisions(
                self.rect,
                movement,
            )

            self.rect.x = max(
                0,
                min(self.rect.x, screen_width - self.width),
            )

            self.rect.y = max(
                0,
                min(self.rect.y, screen_height - self.height),
            )

            self.position.update(
                self.rect.x,
                self.rect.y,
            )

        else:
            self.position += movement

            self.position.x = max(
                0,
                min(self.position.x, screen_width - self.width),
            )

            self.position.y = max(
                0,
                min(self.position.y, screen_height - self.height),
            )

            self.rect.topleft = (
                round(self.position.x),
                round(self.position.y),
            )

    def get_nearby_npc(self, npcs, interaction_distance=70):
        """Devuelve el NPC más cercano dentro del rango de interacción."""
        closest_npc = None
        closest_distance = float("inf")

        for npc in npcs:
            distance = self.position.distance_to(npc.position)

            if distance <= interaction_distance and distance < closest_distance:
                closest_npc = npc
                closest_distance = distance

        return closest_npc

    def draw(self, screen):
        """Dibuja temporalmente al jugador en pantalla."""
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (
                round(self.position.x),
                round(self.position.y),
                self.width,
                self.height,
            ),
        )
